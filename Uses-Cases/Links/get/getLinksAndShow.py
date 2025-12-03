import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"settings/credentials.json")
    LOCAL_FOLDER = Path(r"test_data")
    PDF_DOCUMENT_NAME = "PdfWithLinks.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    PAGE_NUMBER = 1
    LINK_FIND_ID = "GE5UYYLVNZRWQQLDORUW63R3HA4CYNRZGQWDCMZQFQ3TAOI"


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
                api_key, app_id = credentials.get("client_secret"), credentials.get("client_id")
                if not api_key or not app_id:
                    raise ValueError("Error: Missing API keys in the credentials file.")
                self.pdf_api = PdfApi(ApiClient(api_key, app_id))
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            logging.error(f"Failed to load credentials: {e}")

    def upload_document(self):
        """Upload a PDF document to the Aspose Cloud server."""
        if self.pdf_api:
            file_path = Config.LOCAL_FOLDER / Config.PDF_DOCUMENT_NAME
            try:
                self.pdf_api.upload_file(Config.PDF_DOCUMENT_NAME, str(file_path))
                logging.info(f"File {Config.PDF_DOCUMENT_NAME} uploaded successfully.")
            except Exception as e:
                logging.error(f"Failed to upload file: {e}")

    def show_links_array(self, links, prefix):
        for item in links:
            logging.info(f"{prefix} Link ID: '{item.id}' - Link Action: '{item.action}'")

    def get_all_links(self):
        """Get all hyperlink annotations for a specific PDF document."""
        if self.pdf_api:
            try:
                response = self.pdf_api.get_page_link_annotations( Config.PDF_DOCUMENT_NAME, Config.PAGE_NUMBER)
                if response.code == 200:
                    self.show_links_array(response.links.list, "All: ")
                else:
                    logging.error(f"Failed to add link to the page. Response code: {response.code}")
            except Exception as e:
                logging.error(f"Error while adding link: {e}")

    def get_link_by_id(self, link_id: str):
        """Get hyperlink annotation using the specific Id in PDF document."""
        if self.pdf_api:
            try:
                result_link = self.pdf_api.get_link_annotation(Config.PDF_DOCUMENT_NAME, link_id)
                if result_link.code == 200:
                    self.show_links_array([result_link.link], "Find: ")
            except Exception as e:
                logging.error(f"Error while adding link: {e}")

if __name__ == "__main__":
    pdf_links = PdfLinks()
    pdf_links.upload_document()
    pdf_links.get_all_links()
    pdf_links.get_link_by_id(Config.LINK_FIND_ID)
