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
    PDF_DOCUMENT_NAME = "adbe.x509.rsa_sha1.valid.pdf"


class PdfSignatures:
    """Class for managing PDF signatures using Aspose PDF Cloud API."""
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

    def upload_document(self):
        """Upload a PDF document to the Aspose Cloud server."""
        if self.pdf_api:
            file_path = Config.LOCAL_FOLDER / Config.PDF_DOCUMENT_NAME
            try:
                self.pdf_api.upload_file(Config.PDF_DOCUMENT_NAME, str(file_path))
                logging.info(f"File {Config.PDF_DOCUMENT_NAME} uploaded successfully.")
            except Exception as e:
                logging.error(f"Failed to upload file: {e}")

    def _show_signature_fields_array(self, fields):
        if len(fields.list) == 0:
            logging.info(f"Signature fileds is empty!")
        else:
            for item in fields.list:
                logging.info(f"Signature filed ID: '{item.signature.contact}'")

    def get_signature_fileds(self):
        """Extract signature fields in the PDF document."""
        if self.pdf_api:          
            try:
                response = self.pdf_api.get_document_signature_fields(Config.PDF_DOCUMENT_NAME)
                if response.code == 200:
                    logging.info(f"get_signature_fileds(): Signature fields successfully extracted in to the '{Config.PDF_DOCUMENT_NAME}' document:")
                    self._show_signature_fields_array(response.fields)
                else:
                    logging.error(f"get_signature_fileds(): Failed to extract signatures in the document. Response code: {response.code}")
            except Exception as e:
                logging.error(f"get_signature_fileds(): Error while extrcting signature: {e}")


if __name__ == "__main__":
    pdf_sign = PdfSignatures()
    pdf_sign.upload_document()
    pdf_sign.get_signature_fileds()