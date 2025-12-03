import shutil
import json
import logging
import os
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

credentials_file = Path("Settings/credentials.json")
local_folder = Path(r"test_data")
pdf_document = "output_sample.pdf"

pdf_api = None

try:
    """ Load credentials and create PDF Rest API object """
    with credentials_file.open("r", encoding="utf-8") as file:
        credentials = json.load(file)
        api_key, app_id = credentials.get("client_secret"), credentials.get("client_id")
        if not api_key or not app_id:
            raise ValueError("init_api(): Error: Missing API keys in the credentials file.")
        pdf_api = PdfApi(ApiClient(api_key, app_id))

    if pdf_api:
        """ Create empty PDF document """
        pdf_response = pdf_api.put_create_document(pdf_document)
        if pdf_response.code == 200:
            logging.info(f"Document #{pdf_document} created.")

            """ Download empty PDF document to local folder """
            temp_file = pdf_api.download_file(pdf_document)
            local_path = local_folder / pdf_document
            shutil.move(temp_file, str(local_path))
            logging.info(f"download_result(): File successfully downloaded: {local_path}")
except Exception as err:

    logging.error(f"Failed to create empty Pdfdocument '{pdf_document}'!.")
    logging.error(f"Unexpected {err=}, {type(err)=}")
