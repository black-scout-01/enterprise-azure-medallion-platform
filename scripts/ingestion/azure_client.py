from azure.storage.filedatalake import DataLakeServiceClient

from config import *

def get_service_client():

    account_url = (
        f"https://{AZURE_STORAGE_ACCOUNT}.dfs.core.windows.net"
    )

    return DataLakeServiceClient(
        account_url=account_url,
        credential=AZURE_STORAGE_KEY
    )