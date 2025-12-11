import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, SplitRangePdfOptions, PageRange, SplitResultResponse

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"settings/credentials.json")
    LOCAL_FOLDER = Path(r"test_data")
    PDF_DOCUMENT_NAME = "sample.pdf"

spltRanges: SplitRangePdfOptions = SplitRangePdfOptions([PageRange(1,2), PageRange(3,4)])

class PdfSplitter:
    """ Class for managing PDF pages using Aspose PDF Cloud API. """
    def __init__(self, credentials_file: Path = Config.CREDENTIALS_FILE):
        self.pdf_api = None
        self._init_api(credentials_file)

    def _init_api(self, credentials_file: Path):
        """ Initialize the API client. """
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
        """ Upload a PDF document to the Aspose Cloud server. """
        if self.pdf_api:
            file_path = Config.LOCAL_FOLDER / Config.PDF_DOCUMENT_NAME
            try:
                self.pdf_api.upload_file(Config.PDF_DOCUMENT_NAME, str(file_path))
                logging.info(f"upload_document(): File {Config.PDF_DOCUMENT_NAME} uploaded successfully.")
            except Exception as e:
                logging.error(f"upload_document(): Failed to upload file: {e}")

    def download_result(self, pageName, pageIndex):
        """ Download the processed PDF document page from the Aspose Cloud server. """
        if self.pdf_api:
            try:
                temp_file = self.pdf_api.download_file(pageName)
                local_path = Config.LOCAL_FOLDER / f"Page_{pageIndex}_{pageName}"
                shutil.move(temp_file, str(local_path))
                logging.info(f"download_result(): File successfully downloaded: {local_path}")
            except Exception as e:
                logging.error(f"download_result(): Failed to download file: {e}")

    def split_document_by_ranges(self):
        """ Split source document by ranges """
        if self.pdf_api:
            try:
                response: SplitResultResponse = self.pdf_api.post_split_range_pdf_document(Config.PDF_DOCUMENT_NAME, spltRanges)

                if response.code == 200:
                    i = 0
                    for a_doc in response.result.documents:
                        self.download_result(a_doc.href, i)
                        i = i + 1
            except Exception as e:
                logging.error(f"split_document_by_pages(): Failed in the PdfSplitter: {e}")

if __name__ == "__main__":
    pdf_splitter = PdfSplitter()
    pdf_splitter.upload_document()
    pdf_splitter.split_document_by_ranges()