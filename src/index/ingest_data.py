from src.config.logging import logger
from src.config.setup import config
from typing import Dict, Any
import requests

def import_documents_to_gcp(data_store_id: str, input_uri: str, errors_uri: str) -> None:
    """
    Sends a POST request to GCP to import documents into a specified data store.

    Args:
        data_store_id (str): The ID of the data store where documents will be imported.
        input_uri (str): The URI of the input documents in GCS.
        errors_uri (str): The URI for logging errors during the import process.

    Raises:
        Exception: If the request to the GCP API fails.
    """
    # Configuration and Request Setup
    gcp_access_token = config.get("ACCESS_TOKEN")
    project_id = config.get("PROJECT_ID")

    url = f"https://discoveryengine.googleapis.com/v1/projects/{project_id}/locations/global/collections/default_collection/dataStores/{data_store_id}/branches/0/documents:import"

    headers = {
        "Authorization": f"Bearer {gcp_access_token}",
        "Content-Type": "application/json"
    }

    data = {
        "gcsSource": {
            "inputUris": [input_uri],
            "dataSchema": "document",
        },
        "reconciliationMode": "INCREMENTAL",
        "errorConfig": {
            "gcsPrefix": errors_uri
        }
    }

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

# Example Usage
if __name__ == '__main__':
    data_store_id = 'moodys-demo4-doc-search'
    input_uri = 'gs://moodys-doc-search/metadata.jsonl'
    errors_uri = 'gs://moodys-doc-search-errors/'

    try:
        import_documents_to_gcp(data_store_id, input_uri, errors_uri)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
