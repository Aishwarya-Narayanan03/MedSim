from google.cloud import secretmanager
import os
from typing import Optional

def get_secret(secret_id: str, project_id: Optional[str] = None) -> str:
    """Fetches a secret from GCP Secret Manager.

    Args:
        secret_id (str): The ID of the secret to fetch.
        project_id (Optional[str], optional): The ID of the project. 
            If not provided, it will be fetched from the PROJECT_ID environment variable. Defaults to None.

    Returns:
        str: The secret value.

    Raises:
        Exception: If there is an error accessing the secret.
    """
    if not project_id:
        project_id = os.environ.get("PROJECT_ID")
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")