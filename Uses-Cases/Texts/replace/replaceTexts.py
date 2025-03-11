import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, TextReplace, TextReplaceListRequest

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\\Samples")
    PDF_DOCUMENT_NAME = "sample.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    PAGE_NUMBER = 2
    TEXT_SOURCE_FOR_REPLACE = "YOUR source text"
    TEXT_NEW_VALUE = "YOUR new text"

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class PdfTexts:
    """Class for managing PDF texts using Aspose PDF Cloud API."""

    def __init__(self, credentials_file: Path = Config.CREDENTIALS_FILE):
        self.pdf_api = None
        self._init_api(credentials_file)

    def _init_api(self, credentials_file: Path):
        """Initialize the API client."""
        try:
            with credentials_file.open("r", encoding="utf-8") as file:
                credentials = json.load(file)
                api_key, app_id = credentials.get("key"), credentials.get("id")
                if not api_key or not app_id:
                    raise ValueError("Error: Missing API keys in the credentials file.")
                self.pdf_api = PdfApi(ApiClient(api_key, app_id))
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            logging.error(f"Failed to load credentials: {e}")

    def _ensure_api_initialized(self):
        """Check if the API is initialized before making API calls."""
        if not self.pdf_api:
            logging.error("PDF API is not initialized. Operation aborted.")
            return False
        return True

    def upload_document(self):
        """Upload a PDF document to the Aspose Cloud server."""
        if not self._ensure_api_initialized():
            return

        file_path = Config.LOCAL_FOLDER / Config.PDF_DOCUMENT_NAME
        try:
            self.pdf_api.upload_file(Config.PDF_DOCUMENT_NAME, str(file_path))
            logging.info(f"File {Config.PDF_DOCUMENT_NAME} uploaded successfully.")
        except Exception as e:
            logging.error(f"Failed to upload file: {e}")

    def download_result(self):
        """ Download the processed PDF document from the Aspose Cloud server """
        if not self._ensure_api_initialized():
            return

        try:
            temp_file = self.pdf_api.download_file(Config.PDF_DOCUMENT_NAME)
            local_path = Config.LOCAL_FOLDER / Config.LOCAL_RESULT_DOCUMENT_NAME
            shutil.move(temp_file, str(local_path))
            logging.info(f"download_result(): File successfully downloaded: {local_path}")
        except Exception as e:
            logging.error(f"download_result(): Failed to download file: {e}")

    def replace_document_texts(self):
        """ Replace text in the PDF document """
        if not self.pdf_api:
            return

        text_replace_obj = TextReplace(old_value=Config.TEXT_SOURCE_FOR_REPLACE, new_value=Config.TEXT_NEW_VALUE, regex=False)

        text_replace_request = TextReplaceListRequest([text_replace_obj])

        response = self.pdf_api.post_document_text_replace(
            Config.PDF_DOCUMENT_NAME, text_replace_request
        )

        if response.code == 200:
            print(f"Text '{Config.TEXT_SOURCE_FOR_REPLACE}' replaced with '{Config.TEXT_NEW_VALUE}' - successfully.")
        else:
            print("Failed to replace text in document.")

    def replace_page_texts(self):
        """ Replace text on the page in PDF document """
        if not self.pdf_api:
            return

        text_replace_obj = TextReplace(old_value=Config.TEXT_NEW_VALUE, new_value=Config.TEXT_SOURCE_FOR_REPLACE, regex=False)

        text_replace_request = TextReplaceListRequest([text_replace_obj])

        response = self.pdf_api.post_page_text_replace(
            Config.PDF_DOCUMENT_NAME,
            Config.PAGE_NUMBER,
            text_replace_request
        )

        if response.code == 200:
            print(f"Text '{Config.TEXT_NEW_VALUE}' replaced with '{Config.TEXT_SOURCE_FOR_REPLACE}' - successfully.")
        else:
            print("Failed to replace text in document.")



if __name__ == "__main__":
    pdf_texts = PdfTexts()
    pdf_texts.upload_document()
    pdf_texts.replace_document_texts()
    pdf_texts.replace_page_texts()
    pdf_texts.download_result()
