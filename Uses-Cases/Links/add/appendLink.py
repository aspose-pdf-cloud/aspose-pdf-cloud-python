import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi
from asposepdfcloud.models import LinkAnnotation, Color, Link, Rectangle

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
    PDF_DOCUMENT_NAME = "sample.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    NEW_LINK_ACTION = "https://reference.aspose.cloud/pdf/"
    PAGE_NUMBER = 2
    LINK_RECT = Rectangle(llx=244.914, lly=488.622, urx=284.776, ury=498.588)


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
        """Upload a PDF document to the Aspose Cloud server."""
        if not self._ensure_api_initialized():
            return

        file_path = Config.LOCAL_FOLDER / Config.PDF_DOCUMENT_NAME
        try:
            self.pdf_api.upload_file(Config.PDF_DOCUMENT_NAME, str(file_path))
            logging.info(f"upload_document(): File {Config.PDF_DOCUMENT_NAME} uploaded successfully.")
        except Exception as e:
            logging.error(f"upload_document(): Failed to upload file: {e}")

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

    def append_link(self):
        """Append a new hyperlink annotation to a specific page in the PDF document."""
        if not self._ensure_api_initialized():
            return

        link_annotation = LinkAnnotation(
            links=[Link(href=Config.NEW_LINK_ACTION)],
            action_type="GoToURIAction",
            action=Config.NEW_LINK_ACTION,
            highlighting="Invert",
            color=Color(a=255, r=0, g=255, b=0),
            rect=Config.LINK_RECT,
        )

        try:
            response = self.pdf_api.post_page_link_annotations(
                Config.PDF_DOCUMENT_NAME, Config.PAGE_NUMBER, [link_annotation]
            )
            if response.code == 200:
                logging.info(f"append_link(): Link '{Config.NEW_LINK_ACTION}' added to page #{Config.PAGE_NUMBER}.")
            else:
                logging.error(f"append_link(): Failed to add link to the page. Response code: {response.code}")
        except Exception as e:
            logging.error(f"append_link(): Error while adding link: {e}")


if __name__ == "__main__":
    pdf_links = PdfLinks()
    pdf_links.upload_document()
    pdf_links.append_link()
    pdf_links.download_result()
