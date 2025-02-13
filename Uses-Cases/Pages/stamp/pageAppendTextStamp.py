import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, Stamp, AsposeResponse

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
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
                api_key, app_id = credentials.get("key"), credentials.get("id")
                if not api_key or not app_id:
                    raise ValueError("init_api(): Error: Missing API keys in the credentials file.")
                self.pdf_api = PdfApi(ApiClient(api_key, app_id))
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            logging.error(f"init_api(): Failed to load credentials: {e}")

    def _ensure_api_initialized(self):
        """ Check if the API is initialized before making API calls. """
        if not self.pdf_api:
            logging.error("ensure_api_initialized(): PDF API is not initialized. Operation aborted.")
            return False
        return True

    def upload_document(self):
        """ Upload a PDF document to the Aspose Cloud server. """
        if not self._ensure_api_initialized():
            return

        file_path = Config.LOCAL_FOLDER / Config.PDF_DOCUMENT_NAME
        try:
            self.pdf_api.upload_file(Config.PDF_DOCUMENT_NAME, str(file_path))
            logging.info(f"upload_document(): File {Config.PDF_DOCUMENT_NAME} uploaded successfully.")
        except Exception as e:
            logging.error(f"upload_document(): Failed to upload file: {e}")

    def download_result(self):
        """ Download the processed PDF document from the Aspose Cloud server. """
        if not self._ensure_api_initialized():
            return

        try:
            file_path = self.pdf_api.download_file(Config.PDF_DOCUMENT_NAME)
            local_path = Config.LOCAL_FOLDER / Config.LOCAL_RESULT_DOCUMENT_NAME
            shutil.move(file_path, str(local_path))
            logging.info(f"download_result(): File successfully downloaded: {local_path}")
        except Exception as e:
            logging.error(f"download_result(): Failed to download file: {e}")

    def add_page_text_stamp(self):
        """ Adds a text stamp to a specific page in a PDF document. """

        page_stamp: Stamp = Stamp(
            type="Text",
            background=True,
            horizontal_alignment="Center",
            text_alignment="Center",
            value=Config.STAMP_TEXT,
            page_index=Config.PAGE_NUMBER,
        )

        response: AsposeResponse = self.pdf_api.put_page_add_stamp(Config.PDF_DOCUMENT_NAME, Config.PAGE_NUMBER, page_stamp)

        if response.code == 200:
            logging.info(f"Text stamp '{Config.STAMP_TEXT}' added to page #{Config.PAGE_NUMBER}.")
        else:
            logging.error(f"Failed to add text stamp '{Config.STAMP_TEXT}' to page #{Config.PAGE_NUMBER}.")
        return

if __name__ == "__main__":
    pdf_pages = PdfPages()
    pdf_pages.upload_document()
    pdf_pages.add_page_text_stamp()
    pdf_pages.download_result()
