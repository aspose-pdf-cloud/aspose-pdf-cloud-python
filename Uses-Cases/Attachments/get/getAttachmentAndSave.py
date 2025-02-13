import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, AttachmentsResponse, AttachmentResponse, Attachment

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
    PDF_DOCUMENT_NAME = "sample_file_with_attachment.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    ATTACHMENT_PATH = "/1"

class PdfAttachments:
    """Class for managing PDF attachments using Aspose PDF Cloud API."""
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

    def get_attachments(self):
        """Get attachments for the PDF document."""
        if not self._ensure_api_initialized():
            return

        try:
            response : AttachmentsResponse = self.pdf_api.get_document_attachments(Config.PDF_DOCUMENT_NAME)
            if response.code == 200:
                logging.info(f"get_attachmnets(): attachments '{response.attachments}' for the document '{Config.PDF_DOCUMENT_NAME}'.")
            else:
                logging.error(f"get_attachmnets(): Failed to get attachments to the document. Response code: {response.code}")
        except Exception as e:
            logging.error(f"get_attachmnets(): Error while adding attachment: {e}")

    def get_attachment_by_id(self):
        """Get attachment by Id for the PDF document and save it to local file."""
        if not self._ensure_api_initialized():
            return

        try:
            response : AttachmentResponse = self.pdf_api.get_document_attachment_by_index(Config.PDF_DOCUMENT_NAME, Config.ATTACHMENT_PATH)
            if response.code == 200:
                attachment: Attachment = response.attachment
                file_path = self.pdf_api.get_download_document_attachment_by_index(Config.PDF_DOCUMENT_NAME, Config.ATTACHMENT_PATH)
                local_path = Config.LOCAL_FOLDER / attachment.name
                shutil.copy(file_path, local_path)
                logging.info(f"get_attachmnets(): attachments '{file_path}' for the document '{Config.PDF_DOCUMENT_NAME}' successfuly saved.")
            else:
                logging.error(f"get_attachmnets(): Failed to get attachments to the document. Response code: {response.code}")
        except Exception as e:
            logging.error(f"get_attachmnets(): Error while get attachment: {e}")


if __name__ == "__main__":
    pdf_attachments = PdfAttachments()
    pdf_attachments.upload_document()
    pdf_attachments.get_attachments()
    pdf_attachments.get_attachment_by_id()