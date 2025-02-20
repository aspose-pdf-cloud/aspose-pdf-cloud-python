import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, Bookmarks, BookmarksResponse

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
    PDF_DOCUMENT_NAME = "sample.pdf"

class PdfBookmarks:
    """Class for managing PDF bookmarks using Aspose PDF Cloud API."""

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

    def show_bookmarks_array(self, bookmarks, prefix):
        for item in bookmarks.list:
            logging.info(f"{prefix} => level: '{item.level}' - action: '{item.action}' - title: '{item.title}'")
            if item.bookmarks and item.bookmarks.list and item.bookmarks.list.length > 0:
                self.show_bookmarks_array(bookmarks=item.bookmarks, prefix=prefix)

    def get_all_bookmarks(self):
        """Get all bookmarks for a specific PDF document."""    
        if not self._ensure_api_initialized():
            return

        try:
            response : BookmarksResponse = self.pdf_api.get_document_bookmarks( Config.PDF_DOCUMENT_NAME)
            if response.code == 200:
                self.show_bookmarks_array(response.bookmarks, "All")
            else:
                logging.error(f"Failed to get bookmarks for the document. Response code: {response.code}")
        except Exception as e:
            logging.error(f"Error while retrieving bookmarks array: {e}")

if __name__ == "__main__":
    pdf_bookmarks = PdfBookmarks()
    pdf_bookmarks.upload_document()
    pdf_bookmarks.get_all_bookmarks()