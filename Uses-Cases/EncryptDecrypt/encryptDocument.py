import shutil
import json
import logging
from pathlib import Path
import base64
from asposepdfcloud import ApiClient, PdfApi, CryptoAlgorithm

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
    PDF_DOCUMENT_NAME = "sample.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    ENCRYPT_ALGORITHM = CryptoAlgorithm.AESX256
    USER_PASSWORD = 'User-Password'
    OWNER_PASSWORD = 'Owner-Password'
    
class pdfEncryption:
    """Class for managing PDF encryption using Aspose PDF Cloud API."""
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
        """ Upload a PDF document to the Aspose Cloud server. """
        if self.pdf_api:
            file_path = Config.LOCAL_FOLDER / Config.PDF_DOCUMENT_NAME
            try:
                self.pdf_api.upload_file(Config.PDF_DOCUMENT_NAME, str(file_path))
                logging.info(f"upload_file(): File '{Config.PDF_DOCUMENT_NAME}' uploaded successfully.")
            except Exception as e:
                logging.error(f"upload_document(): Failed to upload file: {e}")

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

    def encrypt_document(self):
        """Encrypt the PDF document."""
        if self.pdf_api:
            try:
                user_password_encoded = base64.b64encode(bytes(Config.USER_PASSWORD, encoding='utf-8'))

                owner_password_encoded = base64.b64encode(bytes(Config.OWNER_PASSWORD, encoding='utf-8'))

                response = self.pdf_api.post_encrypt_document_in_storage(Config.PDF_DOCUMENT_NAME, user_password_encoded, owner_password_encoded, Config.ENCRYPT_ALGORITHM)
                if response.code == 200:
                    logging.info(f"encrypt_document(): Document #{Config.PDF_DOCUMENT_NAME} successfully encrypted.")
                else:
                    logging.error(f"encrypt_document(): Failed to encrypt document #{Config.PDF_DOCUMENT_NAME}. Response code: {response.code}")
            except Exception as e:
                logging.error(f"aencrypt_document(): Error while encrypted document: {e}")


if __name__ == "__main__":
    pdf_encrypt = pdfEncryption()
    pdf_encrypt.upload_document()
    pdf_encrypt.encrypt_document()
    pdf_encrypt.download_result()