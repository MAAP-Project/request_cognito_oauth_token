import requests 
from request_cognito_oauth_token.models import Creds, CognitoClientDetails
import boto3
import json 
import fire

def get_cognito_service_details(secret_id: str) -> CognitoClientDetails:
        client = boto3.client("secretsmanager")
        try:
            response = client.get_secret_value(SecretId=secret_id)
        except client.exceptions.ResourceNotFoundException:
            raise Exception(
                f"Unable to find a secret for '{secret_id}'. "
                "\n\nHint: Check your stage and service id. Also, verify that the correct "
                "AWS_PROFILE is set on your environment."
            )
        return CognitoClientDetails(**json.loads(response["SecretString"]))


def oauth2_request(config: CognitoClientDetails) -> Creds:
    response = requests.post(
        f"{config.cognito_domain}/oauth2/token",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
        },
        auth=(config.client_id, config.client_secret),
        data={
            "grant_type": "client_credentials",
            # A space-separated list of scopes to request for the generated access token.
            "scope": config.scope,
        },
    )
    try:
        response.raise_for_status()
    except Exception:
        print(response.text)
        raise
    return Creds(**response.json())

def get_creds(secret_id: str) -> Creds:
    client_details = get_cognito_service_details(secret_id)
    return oauth2_request(client_details)

if __name__ == "__main__":

    fire.Fire(get_creds)