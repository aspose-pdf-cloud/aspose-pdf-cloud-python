import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, Signature, SignatureType, Rectangle

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"settings/credentials.json")
    LOCAL_FOLDER = Path(r"test_data")
    PDF_DOCUMENT_NAME = "adbe.x509.rsa_sha1.valid.pdf"
    SIGNATURE_FORM_FIELD = 'Signature1'


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

    def verify_signature(self):
        """Verify signature fields in the PDF document."""
        if self.pdf_api:          
            try:
                response = self.pdf_api.get_verify_signature(Config.PDF_DOCUMENT_NAME, Config.SIGNATURE_FORM_FIELD)
                if response.code == 200:
                    if response.valid == True:
                        logging.info(f"verify_signature(): Signature is VALID for the '{Config.PDF_DOCUMENT_NAME}' documen.")
                    else:
                        logging.error(f"verify_signature(): Signature is NOT VALID for the '{Config.PDF_DOCUMENT_NAME}' documen.")
                else:
                    logging.error(f"verify_signature(): Failed to verify signature for the document. Response code: {response.code}")
            except Exception as e:
                logging.error(f"verify_signature(): Error while verified signature: {e}")


if __name__ == "__main__":
    pdf_sign = PdfSignatures()
    pdf_sign.upload_document()
    pdf_sign.verify_signature()