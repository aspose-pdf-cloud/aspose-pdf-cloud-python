import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, TextHeader, HorizontalAlignment, TextHorizontalAlignment

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
    PDF_DOCUMENT_NAME = "sample.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    HEADER_VALUE = "New header Value"
    PAGE_NUMBER = 2

class pdfHederFooter:
    """Class for managing PDF headers and footers using Aspose PDF Cloud API."""
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
                    raise ValueError("init_api(): Error: Missing API keys in the credentials file.")
                self.pdf_api = PdfApi(ApiClient(api_key, app_id))
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            logging.error(f"init_api(): Failed to load credentials: {e}")

    def _ensure_api_initialized(self):
        """Check if the API is initialized before making API calls."""
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

    def append_text_header(self):
        """Append a new text header to the PDF document."""
        if not self._ensure_api_initialized():
            return

        new_header = TextHeader(
            background = True,
            horizontal_alignment = HorizontalAlignment.CENTER,
            text_alignment = TextHorizontalAlignment.CENTER,
            value = Config.HEADER_VALUE
        )

        try:
            response = self.pdf_api.post_document_text_header(
                Config.PDF_DOCUMENT_NAME, new_header
            )
            if response.code == 200:
                logging.info(f"append_text_header(): Header '{new_header.value}' added to the document '{Config.PDF_DOCUMENT_NAME}'.")
            else:
                logging.error(f"append_text_header(): Failed to add header '{new_header.value}' to the document '{Config.PDF_DOCUMENT_NAME}'. Response code: {response.code}")
        except Exception as e:
            logging.error(f"append_text_header(): Error while adding header: {e}")

    def append_text_header_page(self):
        """Append a new text footer to the page on PDF document."""
        if not self._ensure_api_initialized():
            return

        new_header = TextHeader(
            background = True,
            horizontal_alignment = HorizontalAlignment.LEFT,
            text_alignment = TextHorizontalAlignment.CENTER,
            value = Config.HEADER_VALUE
        )

        try:
            response = self.pdf_api.post_document_text_header(
                Config.PDF_DOCUMENT_NAME, new_header, start_page_number=Config.PAGE_NUMBER, end_page_number=Config.PAGE_NUMBER
            )
            if response.code == 200:
                logging.info(f"append_text_header_page(): Header '{new_header.value}' added to the page #{Config.PAGE_NUMBER}.")
            else:
                logging.error(f"append_text_header_page(): Failed to add header '{new_header.value}' to the document #{Config.PAGE_NUMBER}. Response code: {response.code}")
        except Exception as e:
            logging.error(f"append_text_header_page(): Error while adding header: {e}")


if __name__ == "__main__":
    pdf_header_footer = pdfHederFooter()
    pdf_header_footer.upload_document()
    pdf_header_footer.append_text_header()
    pdf_header_footer.append_text_header_page()
    pdf_header_footer.download_result()