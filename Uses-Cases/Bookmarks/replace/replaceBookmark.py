import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, Bookmark, BookmarksResponse, BookmarkResponse

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\\Samples")
    PDF_DOCUMENT_NAME = "sample.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    NEW_BOOKMARK_TITLE = "• Increased performance." #"• Productivity improvement"
    BOOKMARK_PATH = "/5"
    NEW_BOOKMARK_PAGE_NUMBER = 3

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class PdfBookmarks:
    """Class for managing PDF bookmarkss using Aspose PDF Cloud API."""

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

    def upload_document(self):
        """Upload a PDF document to the Aspose Cloud server."""
        if self.pdf_api:
            file_path = Config.LOCAL_FOLDER / Config.PDF_DOCUMENT_NAME
            try:
                self.pdf_api.upload_file(Config.PDF_DOCUMENT_NAME, str(file_path))
                logging.info(f"File {Config.PDF_DOCUMENT_NAME} uploaded successfully.")
            except Exception as e:
                logging.error(f"Failed to upload file: {e}")

    def download_result(self):
        """Download the processed PDF document from the Aspose Cloud server."""
        if self.pdf_api:
            try:
                temp_file = self.pdf_api.download_file(Config.PDF_DOCUMENT_NAME)
                local_path = Config.LOCAL_FOLDER / Config.LOCAL_RESULT_DOCUMENT_NAME
                shutil.move(temp_file, str(local_path))
                logging.info(f"download_result(): File successfully downloaded: {local_path}")
            except Exception as e:
                logging.error(f"download_result(): Failed to download file: {e}")

    def show_bookmarks_array(self, bookmarks, prefix):
        for item in bookmarks.list:
            logging.info(f"{prefix} => level: '{item.level}' - action: '{item.action}' - title: '{item.title}'")
            if item.bookmarks and item.bookmarks.list and item.bookmarks.list.length > 0:
                self.show_bookmarks_array(bookmarks=item.bookmarks, prefix=prefix)

    def get_all_bookmarks(self):
        """Get all bookmarks for a specific PDF document."""    
        if self.pdf_api:
            try:
                response : BookmarksResponse = self.pdf_api.get_document_bookmarks( Config.PDF_DOCUMENT_NAME)
                if response.code == 200:
                    self.show_bookmarks_array(response.bookmarks, "All")
                else:
                    logging.error(f"Failed to get bookmarks for the document. Response code: {response.code}")
            except Exception as e:
                logging.error(f"Error while retrieving bookmarks array: {e}")

    def get_bookmark(self):
        """Get bookmark for a specific PDF document using bookmark path."""    
        if self.pdf_api:
            try:
                response : BookmarkResponse = self.pdf_api.get_bookmark( Config.PDF_DOCUMENT_NAME, Config.BOOKMARK_PATH)
                if response.code == 200:
                    logging.info(f"Found bookmark => level: '{response.bookmark.level}' - action: '{response.bookmark.action}' - title: '{response.bookmark.title}'")
                    return response.bookmark
                else:
                    logging.error(f"Failed to find bookmark for the document. Response code: {response.code}")
                    return None
            except Exception as e:
                logging.error(f"Error while find bookmark: {e}")

    def replace_bookmark(self):
        if self.pdf_api:
            _bookmark: BookmarkResponse = self.get_bookmark()

            if not _bookmark:
                return

            _bookmark.title = Config.NEW_BOOKMARK_TITLE

            response: BookmarkResponse = self.pdf_api.put_bookmark(
                Config.PDF_DOCUMENT_NAME,
                Config.BOOKMARK_PATH,
                bookmark=_bookmark,
            )

            if response.code == 200:
                print("Bookmark replaced successfully.")
            else:
                print("Failed to replace Bookmark.")


if __name__ == "__main__":
    pdf_bookmarks = PdfBookmarks()
    pdf_bookmarks.upload_document()
    pdf_bookmarks.get_all_bookmarks()
    pdf_bookmarks.replace_bookmark()
    pdf_bookmarks.download_result()
