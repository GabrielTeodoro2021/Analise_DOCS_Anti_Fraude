import streamlit as st
from azure.storage.blob import BlobServiceClient
from services.credit_card_services import detect_credit_card_info

def configure_interface():
    st.title("Upload de Arquivo DIO - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    fileName = uploaded_file.name
    #Enviar para o blob storage
    blob_url = upload_blob(uploaded_file, fileName)
    if blob_url:
        st.write(f"Arquivo{fileName} enviado com sucesso para o Azure Blob Storage")
        credit_card_info = ""

    else:
        st.write(f"Erro ao enviar o arquivo {fileName} para o Azure Blob Storage")

    def show_image_and_validation(blob_url, credit_card_info):

        if credit_card_info and credit_card_info["card_name"]:
            st.markdown(f"<h1 style='color:green;'>Cartão Válido</h1>", unsafe_allow_html_True)
            st.write(f"Nome do Titular: {credit_card_info['card_name']}")
            st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
            st.write(f"Data de Validade: {credit_card_info['expiry_date']}")

        else:
            st.markdown(f"<h1 style='color:red;'>Cartão Inválido</h1>", unsafe_allow_html_True)
            st.write("Esse não é um cartão válido!")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", use_column_width=True)


    if __name__ == "__main__":
        configure_interface()