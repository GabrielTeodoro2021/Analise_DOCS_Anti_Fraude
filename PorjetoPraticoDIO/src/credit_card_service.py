from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from utils.Config import Config


def analize_credit_card(card_url):
    try:
        credential = AzureKeyCredential(Config.KEY)
        return result
    except Exception as ex:
        return None