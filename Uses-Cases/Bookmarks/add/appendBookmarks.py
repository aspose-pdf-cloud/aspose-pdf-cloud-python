import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, Color, Bookmark

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
    PDF_DOCUMENT_NAME = "sample.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    NEW_BOOKMARK_TITLE = "• Increased performance.." #"• Productivity improvement"
    PARENT_BOOKMARK_FOR_APPEND = ""                 #The parent bookmark path. Specify an empty string when adding a bookmark to the root.
    NEW_BOOKMARK_PAGE_NUMBER = 3
    BOOKMARK_PAGE_POSITION_X = 89
    BOOKMARK_PAGE_POSITION_Y = 564
    

class PdfBookmarks:
    """Class for managing PDF bokkmarks using Aspose PDF Cloud API."""
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

    def upload_document(self):
        """Upload a PDF document to the Aspose Cloud server."""
        if self.pdf_api:
            file_path = Config.LOCAL_FOLDER / Config.PDF_DOCUMENT_NAME
            try:
                self.pdf_api.upload_file(Config.PDF_DOCUMENT_NAME, str(file_path))
                logging.info(f"upload_document(): File {Config.PDF_DOCUMENT_NAME} uploaded successfully.")
            except Exception as e:
                logging.error(f"upload_document(): Failed to upload file: {e}")

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

    def append_bookmark_link(self):
        """Append a new bookmark link to a specific page in the PDF document."""
        if self.pdf_api:
            newBookmark = Bookmark(
                title = Config.NEW_BOOKMARK_TITLE,
                italic = True,
                bold = True,
                color = Color(a=255,r=0,g=255,b=0),
                level = 1,
                page_display_left = Config.BOOKMARK_PAGE_POSITION_X,
                page_display_top = Config.BOOKMARK_PAGE_POSITION_Y,
                page_display_zoom = 2,
                page_number = Config.NEW_BOOKMARK_PAGE_NUMBER
            )

            try:
                response = self.pdf_api.post_bookmark(
                    Config.PDF_DOCUMENT_NAME, Config.PARENT_BOOKMARK_FOR_APPEND, [newBookmark]
                )
                if response.code == 200:
                    logging.info(f"append_bookmark_link(): Bookmark '{response.bookmarks.list[0].action}'->'{Config.NEW_BOOKMARK_TITLE}' added to page #{Config.NEW_BOOKMARK_PAGE_NUMBER}.")
                else:
                    logging.error(f"append_bookmark_link(): Failed to add bookmark '{Config.NEW_BOOKMARK_TITLE}' to the page #{Config.NEW_BOOKMARK_PAGE_NUMBER}. Response code: {response.code}")
            except Exception as e:
                logging.error(f"append_bookmark_link(): Error while adding bookmark: {e}")


if __name__ == "__main__":
    pdf_bookmarks = PdfBookmarks()
    pdf_bookmarks.upload_document()
    pdf_bookmarks.append_bookmark_link()
    pdf_bookmarks.download_result()
