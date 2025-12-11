import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, Signature, SignatureType, SignatureField, Rectangle

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"settings/credentials.json")
    LOCAL_FOLDER = Path(r"test_data")
    PDF_DOCUMENT_NAME = "adbe.x509.rsa_sha1.valid.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    LOCAL_SIGNATURE_PATH = Path(r"test_data")
    SIGNATURE_PFX = "33226.p12"
    SIGNATURE_FORM_FIELD = 'Signature1'
    SIGNATURE_PASSWORD='sIikZSmz'
    SIGNATURE_CONTACT='Contact'
    SIGNATURE_LOCATION='Location'
    SIGNATURE_AUTHORITY='Sergey Smal'
    SIGNATURE_DATE='04/19/2025 12:15:00.000 PM'
    SIGNATURE_RECT = Rectangle(100, 100, 0, 0)


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

    def upload_file(self, local_path: Path, fileName: str):
        """ Upload a local fileName to the Aspose Cloud server. """
        if self.pdf_api:
            file_path = local_path / fileName
            try:
                self.pdf_api.upload_file(fileName, str(file_path))
                logging.info(f"upload_file(): File '{fileName}' uploaded successfully.")
            except Exception as e:
                logging.error(f"upload_document(): Failed to upload file: {e}")

    def upload_document(self):
        """ Upload a PDF document to the Aspose Cloud server. """
        self.upload_file(Config.LOCAL_FOLDER, Config.PDF_DOCUMENT_NAME)


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

    def replace_signature(self):
        """Append a new signature to the PDF document."""
        if self.pdf_api:
            
            signature = Signature(
                signature_path=Config.SIGNATURE_PFX,
                signature_type=SignatureType.PKCS7,
                password=Config.SIGNATURE_PASSWORD,
                contact=Config.SIGNATURE_CONTACT,
                location=Config.SIGNATURE_LOCATION,
                visible=True,
                rectangle=Config.SIGNATURE_RECT,
                form_field_name=Config.SIGNATURE_FORM_FIELD,
                authority=Config.SIGNATURE_AUTHORITY,
                date=Config.SIGNATURE_DATE,
                show_properties=False)
            
            field = SignatureField(page_index=1)
            field.signature = signature
            field.partial_name = 'sign1'
            field.rect = Config.SIGNATURE_RECT

            try:
                response = self.pdf_api.put_signature_field(Config.PDF_DOCUMENT_NAME, Config.SIGNATURE_FORM_FIELD, field)
                if response.code == 200:
                    logging.info(f"append_signature(): Signature '{Config.SIGNATURE_CONTACT}' successfully added to the document.")
                else:
                    logging.error(f"append_signature(): Failed to add signature to the document. Response code: {response.code}")
            except Exception as e:
                logging.error(f"append_signature(): Error while adding signature: {e}")


if __name__ == "__main__":
    pdf_sign = PdfSignatures()
    pdf_sign.upload_document()
    pdf_sign.upload_file(Config.LOCAL_SIGNATURE_PATH, Config.SIGNATURE_PFX)
    pdf_sign.replace_signature()
    pdf_sign.download_result()