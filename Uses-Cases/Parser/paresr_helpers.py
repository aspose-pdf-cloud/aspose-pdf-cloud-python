import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
    REMOTE_TEMP_FOLDER  = "TempPdfCloud"
    PDF_DOCUMENT_NAME = "sample.pdf"
    XML_OUTPUT_FILE = "output_sample.xml"
    FDF_OUTPUT_FILE = "output_sample.fdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    PAGE_NUMBER = 1


class ParesrHelper:
    """Class with helper methods and properties for Parser"""

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
                    raise ValueError("Error: Missing API keys in the credentials file.")
                self.pdf_api = PdfApi(ApiClient(api_key, app_id))
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            logging.error(f"Failed to load credentials: {e}")

    def upload_document(self, documentName: str, remoteFolder: str):
        """Upload a PDF document to the Aspose Cloud server."""
        if self.pdf_api:
            file_path = Config.LOCAL_FOLDER / documentName
            try:
                if remoteFolder == None:
                    self.pdf_api.upload_file(documentName, str(file_path))
                else:
                    opts = { "folder": remoteFolder }
                    self.pdf_api.upload_file(remoteFolder + '/' + documentName, file_path)
                logging.info(f"File {documentName} uploaded successfully.")
            except Exception as e:
                logging.error(f"Failed to upload file: {e}")

    def downloadFile(self, document: str, outputDocument: str, localFolder: Path, remoteFolder: str,  output_prefix: str):
        """Download the processed PDF document from the Aspose Cloud server."""
        if self.pdf_api:
            try:
                temp_file = self.pdf_api.download_file(remoteFolder + '/' + document)
                local_path = localFolder / ( output_prefix + outputDocument )
                shutil.move(temp_file, str(local_path))
                logging.info(f"download_result(): File successfully downloaded: {local_path}")
            except Exception as e:
                logging.error(f"download_result(): Failed to download file: {e}")
