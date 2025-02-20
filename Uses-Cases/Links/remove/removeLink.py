import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, AsposeResponse

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
    PDF_DOCUMENT_NAME = "sample.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    PAGE_NUMBER = 2
    LINK_FIND_ID = "GI5UO32UN5KVESKBMN2GS33OHMZTEMJMGUYDQLBTGYYCYNJSGE"


class PdfLinks:
    """Class for managing PDF links using Aspose PDF Cloud API."""

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
        """Download the processed PDF document from the Aspose Cloud server."""
        if not self._ensure_api_initialized():
            return

        try:
            temp_file = self.pdf_api.download_file(Config.PDF_DOCUMENT_NAME)
            local_path = Config.LOCAL_FOLDER / Config.LOCAL_RESULT_DOCUMENT_NAME
            shutil.move(temp_file, str(local_path))
            logging.info(f"download_result(): File successfully downloaded: {local_path}")
        except Exception as e:
            logging.error(f"download_result(): Failed to download file: {e}")

    def show_links_array(self, links, prefix):
        for item in links:
            logging.info(f"{prefix} Link ID: '{item.id}' - Link Action: '{item.action}'")

    def get_all_links(self):
        """Get all hyperlink annotations for a specific PDF document."""
        if not self._ensure_api_initialized():
            return

        try:
            response = self.pdf_api.get_page_link_annotations( Config.PDF_DOCUMENT_NAME, Config.PAGE_NUMBER)
            if response.code == 200:
                self.show_links_array(response.links.list, "All: ")
            else:
                logging.error(f"Failed to add link to the page. Response code: {response.code}")
        except Exception as e:
            logging.error(f"Error while adding link: No links found - {e}")

    def remove_link_by_id(self):
        if not self.pdf_api:
            return

        response: AsposeResponse = self.pdf_api.delete_link_annotation(Config.PDF_DOCUMENT_NAME, Config.LINK_FIND_ID)

        if response.code == 200:
            logging.info("Link annotation with ID " + Config.LINK_FIND_ID + " has been removed.")
        else:
            logging.erro("Failed to remove link annotation with ID " + Config.LINK_FIND_ID)

if __name__ == "__main__":
    pdf_links = PdfLinks()
    pdf_links.upload_document()
    pdf_links.get_all_links()
    pdf_links.remove_link_by_id()
    pdf_links.download_result()
