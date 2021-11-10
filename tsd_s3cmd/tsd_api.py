from typing import Literal
from tsdapiclient.authapi import get_jwt_tsd_auth
from tsdapiclient.tacl import get_api_key, get_user_credentials

S3_TOKEN_TYPE = Literal["s3import", "s3export"]

def authenticate(environment: str, project: str, token_type: S3_TOKEN_TYPE):
    api_key = get_api_key(env=environment, pnum=project)
    user_name, password, otp = get_user_credentials()
    get_jwt_tsd_auth(
        env=environment,
        pnum=project,
        api_key=api_key,
        user_name=user_name,
        password=password,
        otp=otp,
        token_type=token_type
    )