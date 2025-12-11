import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, Stamp, AsposeResponse

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"settings/credentials.json")
    LOCAL_FOLDER = Path(r"test_data")
    PDF_DOCUMENT_NAME = "PageNumberStamp.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    PAGE_NUMBER = 2
    STAMP_ID = "GE5TAOZQ"

class PdfStamps:
    """ Class for managing PDF stamps using Aspose PDF Cloud API. """
    def __init__(self, credentials_file: Path = Config.CREDENTIALS_FILE):
        self.pdf_api = None
        self._init_api(credentials_file)

    def _init_api(self, credentials_file: Path):
        """ Initialize the API client. """
        try:
            with credentials_file.open("r", encoding="utf-8") as file:
                credentials = json.load(file)
                api_key, app_id = credentials.get("client_secret"), credentials.get("client_id")
                if not api_key or not app_id:
                    raise ValueError("init_api(): Error: Missing API keys in the credentials file.")
                self.pdf_api = PdfApi(ApiClient(api_key, app_id))
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            logging.error(f"init_api(): Failed to load credentials: {e}")

    def upload_document(self):
        """ Upload a PDF document to the Aspose Cloud server. """
        if self.pdf_api:
            file_path = Config.LOCAL_FOLDER / Config.PDF_DOCUMENT_NAME
            try:
                self.pdf_api.upload_file(Config.PDF_DOCUMENT_NAME, str(file_path))
                logging.info(f"upload_document(): File {Config.PDF_DOCUMENT_NAME} uploaded successfully.")
            except Exception as e:
                logging.error(f"upload_document(): Failed to upload file: {e}")

    def download_result(self):
        """ Download the processed PDF document from the Aspose Cloud server. """
        if self.pdf_api:
            try:
                file_path = self.pdf_api.download_file(Config.PDF_DOCUMENT_NAME)
                local_path = Config.LOCAL_FOLDER / Config.LOCAL_RESULT_DOCUMENT_NAME
                shutil.move(file_path, str(local_path))
                logging.info(f"download_result(): File successfully downloaded: {local_path}")
            except Exception as e:
                logging.error(f"download_result(): Failed to download file: {e}")

    def delete_page_stamps(self):
        """ Remove stamp in a specific page of the PDF document. """
        if self.pdf_api:
            response: AsposeResponse = self.pdf_api.delete_page_stamps(Config.PDF_DOCUMENT_NAME, Config.PAGE_NUMBER)
            
            if response.code == 200 :
                logging.info(f"Stamps on page #{Config.PAGE_NUMBER} was deleted for the document '{Config.PDF_DOCUMENT_NAME}'.")
            else:
                logging.error(f"Failed to remove stamps on page #{Config.PAGE_NUMBER} for the document '{Config.PDF_DOCUMENT_NAME}'.")

    def delete_stamp_by_id(self):
        """ Remove stamp by Id in the PDF document. """
        if self.pdf_api:
            try:
                response: AsposeResponse = self.pdf_api.delete_stamp(Config.PDF_DOCUMENT_NAME, Config.STAMP_ID)
                
                if response.code == 200 :
                    logging.info(f"Stamps with Id '{Config.STAMP_ID}' was deleted for the document '{Config.PDF_DOCUMENT_NAME}'.")
                else:
                    logging.error(f"Failed to remove stamp with Id '{Config.STAMP_ID}' for the document '{Config.PDF_DOCUMENT_NAME}'.")
            except Exception as e:
                logging.error(f"delete_stamp_by_id(): Failed to download file: {e}")

if __name__ == "__main__":
    pdf_stamps = PdfStamps()
    pdf_stamps.upload_document()
    pdf_stamps.delete_stamp_by_id()
    pdf_stamps.delete_page_stamps()
    pdf_stamps.download_result()
