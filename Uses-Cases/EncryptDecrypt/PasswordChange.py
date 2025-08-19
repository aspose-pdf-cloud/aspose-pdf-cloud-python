import shutil
import json
import logging
from pathlib import Path
import base64
from asposepdfcloud import ApiClient, PdfApi

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
    PDF_DOCUMENT_NAME = "sample_encrypted.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    DOCUMENT_PASSWORD = 'Owner-Password'
    NEW_USER_PASSWORD = "NEW-User-Password"
    NEW_OWNER_PASSWORD = "NEW-Owner-Password"
    
class pdfEncoder:
    """Class for replacing password in PDF encrypted document using Aspose PDF Cloud API."""
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
                local_path = Config.LOCAL_FOLDER / ("password_change_" + Config.LOCAL_RESULT_DOCUMENT_NAME)
                shutil.move(temp_file, str(local_path))
                logging.info(f"download_result(): File successfully downloaded: {local_path}")
            except Exception as e:
                logging.error(f"download_result(): Failed to download file: {e}")

    def change_passwords(self):
        """Decrypt the PDF document."""
        if self.pdf_api:
            try:
                password_encoded = base64.b64encode(bytes(Config.DOCUMENT_PASSWORD, encoding='utf-8'))

                new_owner_pwd_encoded = base64.b64encode(bytes(Config.NEW_OWNER_PASSWORD, encoding='utf-8'))
                new_user_pwd_encoded = base64.b64encode(bytes(Config.NEW_USER_PASSWORD, encoding='utf-8'))

                response = self.pdf_api.post_change_password_document_in_storage(Config.PDF_DOCUMENT_NAME, password_encoded, new_user_pwd_encoded, new_owner_pwd_encoded)
                if response.code == 200:
                    logging.info(f"change_passwords(): Password in document #{Config.PDF_DOCUMENT_NAME} successfully modified.")
                else:
                    logging.error(f"change_passwords(): Failed to chnage passowd in document #{Config.PDF_DOCUMENT_NAME}. Response code: {response.code}")
            except Exception as e:
                logging.error(f"change_passwords(): Error while change passwords in document: {e}")


if __name__ == "__main__":
    pdf_encoder = pdfEncoder()
    pdf_encoder.upload_document()
    pdf_encoder.change_passwords()
    pdf_encoder.download_result()

