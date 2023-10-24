import pydantic

class CognitoClientDetails(pydantic.BaseModel):
    cognito_domain: str
    client_id: str
    client_secret: str = pydantic.Field(repr=False)
    scope: str
    
class Creds(pydantic.BaseModel):
    access_token: str
    expires_in: int
    token_type: str
