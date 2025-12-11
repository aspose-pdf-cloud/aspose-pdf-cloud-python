import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, AttachmentInfo

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"settings/credentials.json")
    LOCAL_FOLDER = Path(r"test_data")
    PDF_DOCUMENT_NAME = "PdfWithEmbeddedFiles.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    NEW_ATTACHMENT_FILE = "sample.pdf"
    NEW_ATTACHMENT_MIME = "application/pdf"
    PAGE_NUMBER = 2

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
                api_key, app_id = credentials.get("client_secret"), credentials.get("client_id")
                if not api_key or not app_id:
                    raise ValueError("init_api(): Error: Missing API keys in the credentials file.")
                self.pdf_api = PdfApi(ApiClient(api_key, app_id))
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            logging.error(f"init_api(): Failed to load credentials: {e}")

    def upload_file(self, fileName: str):
        """ Upload a local fileName to the Aspose Cloud server. """
        if self.pdf_api:
            file_path = Config.LOCAL_FOLDER / fileName
            try:
                self.pdf_api.upload_file(fileName, str(file_path))
                logging.info(f"upload_file(): File '{fileName}' uploaded successfully.")
            except Exception as e:
                logging.error(f"upload_document(): Failed to upload file: {e}")

    def upload_document(self):
        """ Upload a PDF document to the Aspose Cloud server. """
        self.upload_file(Config.PDF_DOCUMENT_NAME)

    def download_result(self):
        """ Download the processed PDF document from the Aspose Cloud server. """
        if self.pdf_api:
            try:
                temp_file = self.pdf_api.download_file(Config.PDF_DOCUMENT_NAME)
                local_path = Config.LOCAL_FOLDER / Config.LOCAL_RESULT_DOCUMENT_NAME
                shutil.move(temp_file, str(local_path))
                logging.info(f"download_result(): File successfully downloaded: {local_path}")
            except Exception as e:
                logging.error(f"download_result(): Failed to download file: {e}")

    def append_attachmnet(self):
        """Append a new attachment to the PDF document."""
        if self.pdf_api:
            new_attachment = AttachmentInfo(
                path = Config.NEW_ATTACHMENT_FILE,
                description = 'This is a sample attachment',
                mime_type = Config.NEW_ATTACHMENT_MIME,
                name = Config.NEW_ATTACHMENT_FILE
            )

            try:
                response = self.pdf_api.post_add_document_attachment(Config.PDF_DOCUMENT_NAME, new_attachment)
                if response.code == 200:
                    logging.info(f"append_attachment(): attachment '{Config.NEW_ATTACHMENT_FILE}' added to the document '{Config.PDF_DOCUMENT_NAME}'.")
                else:
                    logging.error(f"append_attachment(): Failed to add attachment to the document. Response code: {response.code}")
            except Exception as e:
                logging.error(f"append_attachment(): Error while adding attachment: {e}")


if __name__ == "__main__":
    pdf_attachments = PdfAttachments()
    pdf_attachments.upload_document()
    pdf_attachments.upload_file(Config.NEW_ATTACHMENT_FILE)
    pdf_attachments.append_attachmnet()
    pdf_attachments.download_result()
