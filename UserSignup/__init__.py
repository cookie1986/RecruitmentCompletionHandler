import logging
from dotenv import load_dotenv
import os

import azure.functions as func

# get api key from the receiver side (local only)
load_dotenv()
RECEIVER_API = os.environ.get('RECEIVER-API-KEY')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # authorisation
    SENDER_API = req.headers.get('SENDER-API-KEY')
    logging.info(f'Access attempted with API Key: {SENDER_API}')
    if RECEIVER_API != SENDER_API:
        return func.HttpResponse("Invalid API Key", status_code=401)

    # process the incoming request
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        print(name)
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        print("cant find the name")
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
