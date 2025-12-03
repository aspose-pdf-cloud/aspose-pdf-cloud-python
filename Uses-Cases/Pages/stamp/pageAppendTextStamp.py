import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, Stamp, AsposeResponse, HorizontalAlignment, StampType

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"settings/credentials.json")
    LOCAL_FOLDER = Path(r"test_data")
    PDF_DOCUMENT_NAME = "sample.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    PAGE_NUMBER = 2
    STAMP_TEXT = "NEW TEXT STAMP"

class PdfPages:
    """ Class for managing PDF pages using Aspose PDF Cloud API. """
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
                temp_file = self.pdf_api.download_file(Config.PDF_DOCUMENT_NAME)
                local_path = Config.LOCAL_FOLDER / Config.LOCAL_RESULT_DOCUMENT_NAME
                shutil.move(temp_file, str(local_path))
                logging.info(f"download_result(): File successfully downloaded: {local_path}")
            except Exception as e:
                logging.error(f"download_result(): Failed to download file: {e}")

    def add_page_text_stamp(self):
        """ Adds a text stamp to a specific page in a PDF document. """
        if self.pdf_api:
            page_stamp: Stamp = Stamp(
                type = StampType.TEXT,
                background = True,
                horizontal_alignment = HorizontalAlignment.CENTER,
                text_alignment = HorizontalAlignment.CENTER,
                value = Config.STAMP_TEXT,
                page_index = Config.PAGE_NUMBER,
            )

            response: AsposeResponse = self.pdf_api.put_page_add_stamp(Config.PDF_DOCUMENT_NAME, Config.PAGE_NUMBER, page_stamp)

            if response.code == 200:
                logging.info(f"Text stamp '{Config.STAMP_TEXT}' added to page #{Config.PAGE_NUMBER}.")
            else:
                logging.error(f"Failed to add text stamp '{Config.STAMP_TEXT}' to page #{Config.PAGE_NUMBER}.")

if __name__ == "__main__":
    pdf_pages = PdfPages()
    pdf_pages.upload_document()
    pdf_pages.add_page_text_stamp()
    pdf_pages.download_result()
