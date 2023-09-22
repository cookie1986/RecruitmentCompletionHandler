import logging
from dotenv import load_dotenv
load_dotenv()

import os

import azure.functions as func

# get api key from the receiver side (local only)
RECEIVER_API = os.environ.get('RECEIVER-API-KEY')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('UserSignup HTTP trigger function processed an incoming request.')

    # authorisation
    SENDER_API = req.headers.get('SENDER-API-KEY')
    if RECEIVER_API != SENDER_API:
        logging.info(f'Access attempted with an incorrect API Key: {SENDER_API}')
        return func.HttpResponse("Invalid API Key", status_code=401)

    # if API key is approved, process the incoming request
    email = req.params.get('email')
    if not email:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            email = req_body.get('email')
    
    # if email is in payload
    if email:
        logging.info(f'User with email {email} has completed signup')
        return func.HttpResponse(f"Hello, {email}. This HTTP triggered function executed successfully.")
    else:
        logging.info(f'Incoming request did not include email in payload.')
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )