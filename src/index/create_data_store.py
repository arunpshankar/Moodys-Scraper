
from src.config.logging import logger
from src.config.setup import config
from typing import Dict, Any 
import requests


def import_documents_to_gcp(url: str, headers: Dict[str, str], data: Dict[str, Any]) -> None:
    """
    Sends a POST request to GCP to import documents.

    Args:
        url (str): The GCP API endpoint URL.
        headers (Dict[str, str]): Headers for the request, including authorization.
        data (Dict[str, Any]): The data to be sent in the request.

    Raises:
        Exception: If the request to the GCP API fails.
    """
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.exceptions.HTTPError as err:
        logger.error(f"HTTP error occurred: {err}")
        raise
    except Exception as err:
        logger.error(f"Error occurred during GCP documents import: {err}")
        raise
    else:
        logger.info("Request successful")
        logger.info(response.json())

# Configuration and Request Setup
gcp_access_token = config.get("ACCESS_TOKEN")
project_id = config.get("PROJECT_ID")

url = f"https://discoveryengine.googleapis.com/v1/projects/{project_id}/locations/global/collections/default_collection/dataStores/{data_store_id}/branches/0/documents:import"

headers = {
    "Authorization": f"Bearer {gcp_access_token}",
    "Content-Type": "application/json"
}

input_gcs_uri = 'gs://moodys-doc-search/metadata.jsonl'
gcs_doc_search_errors_uri = 'gs://moodys-doc-search-errors/'

data = {
    "gcsSource": {
        "inputUris": ["gs://moodys-doc-search/metadata.jsonl"],
        "dataSchema": "document",
    },
    "reconciliationMode": "INCREMENTAL",
    "errorConfig": {
        "gcsPrefix": ""
    }
}

# Perform the Request
import_documents_to_gcp(url, headers, data)
