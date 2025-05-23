import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, OptimizeOptions

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
    TEMP_FOLDER = 'TempPdfCloud'
    PDF_DOCUMENT_NAME = "sample.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"

class PdfCompress:
    """Class for compress PDF links using Aspose PDF Cloud API."""
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
            stotage_path = Config.TEMP_FOLDER + '/' + Config.PDF_DOCUMENT_NAME
            try:
                self.pdf_api.upload_file(stotage_path, str(file_path))
                logging.info(f"upload_document(): File {Config.PDF_DOCUMENT_NAME} uploaded successfully.")
            except Exception as e:
                logging.error(f"upload_document(): Failed to upload file: {e}")

    def download_result(self):
        """Download the processed PDF document from the Aspose Cloud server."""
        if self.pdf_api:
            try:
                temp_file = self.pdf_api.download_file(Config.TEMP_FOLDER + '/' + Config.PDF_DOCUMENT_NAME)
                local_path = Config.LOCAL_FOLDER / Config.LOCAL_RESULT_DOCUMENT_NAME
                shutil.move(temp_file, str(local_path))
                logging.info(f"download_result(): File successfully downloaded: {local_path}")
            except Exception as e:
                logging.error(f"download_result(): Failed to download file: {e}")

    def compress_pdf_document(self):
        """Compress the PDF document."""
        if self.pdf_api:
            optimize_options = OptimizeOptions(
                allow_reuse_page_content=False,
                compress_images=True,
                image_quality=100,
                link_duplcate_streams=True,
                remove_unused_objects=True,
                remove_unused_streams=True,            
                unembed_fonts=True
            )        
        opts = {
            "options" : optimize_options,
            "folder" : Config.TEMP_FOLDER
        }
        try:
            response = self.pdf_api.post_optimize_document(Config.PDF_DOCUMENT_NAME, **opts)

            if response.code == 200:
                logging.info(f"compress_pdf_document(): PDF document '{Config.PDF_DOCUMENT_NAME}' successfully compressed.")
            else:
                logging.error(f"compress_pdf_document(): Failed to compress document. Response code: {response.code}")
        except Exception as e:
            logging.error(f"compress_pdf_document(): Error while compress document: {e}")


if __name__ == "__main__":
    pdf_compress = PdfCompress()
    pdf_compress.upload_document()
    pdf_compress.compress_pdf_document()
    pdf_compress.download_result()