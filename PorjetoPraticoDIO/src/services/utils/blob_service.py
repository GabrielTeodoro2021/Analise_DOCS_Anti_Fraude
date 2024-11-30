import os
from azure.storage.blob import BlobServiceClient
import streamlit as st
from utils.Config import Config

def upload_blob(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        return blob_service_client.url
    except Exception as ex:
        st.error(f"Erro ao enviar arquivo {ex}")
        return None