import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, Stamp, AsposeResponse

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
    PDF_DOCUMENT_NAME = "sample.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    IMAGE_STAMP_FILE ="sample.png"
    PAGE_NUMBER = 2
    STAMP_TEXT = "NEW TEXT STAMP"
    IMAGE_STAMP_LLY = 800
    IMAGE_STAMP_WIDTH = 24
    IMAGE_STAMP_HEIGHT = 24

class PdfStamps:
    """ Class for managing PDF stamps using Aspose PDF Cloud API. """
    def __init__(self, credentials_file: Path = Config.CREDENTIALS_FILE):
        self.pdf_api = None
        self._init_api(credentials_file)

    def _init_api(self, credentials_file: Path):
        """ Initialize the API client. """
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
        """ Check if the API is initialized before making API calls. """
        if not self.pdf_api:
            logging.error("ensure_api_initialized(): PDF API is not initialized. Operation aborted.")
            return False
        return True
    
    def upload_file(self, fileName: str):
        """ Upload a local fileName to the Aspose Cloud server. """
        if not self._ensure_api_initialized():
            return

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
        if not self._ensure_api_initialized():
            return

        try:
            file_path = self.pdf_api.download_file(Config.PDF_DOCUMENT_NAME)
            local_path = Config.LOCAL_FOLDER / Config.LOCAL_RESULT_DOCUMENT_NAME
            shutil.move(file_path, str(local_path))
            logging.info(f"download_result(): File successfully downloaded: {local_path}")
        except Exception as e:
            logging.error(f"download_result(): Failed to download file: {e}")

    def add_document_stamps(self):
        """ Adds a text stamp to a specific page in a PDF document. """

        text_stamp: Stamp = Stamp(
            type="Text",
            background=True,
            horizontal_alignment="Center",
            text_alignment="Center",
            value=Config.STAMP_TEXT
        )

        image_stamp: Stamp = Stamp(
            type = "Image",
            background = True,
            horizontal_alignment = "Center",
            text_alignment = "Center",
            value = "NEW IMAGE STAMP",
            file_name = Config.IMAGE_STAMP_FILE,
            y_indent = Config.IMAGE_STAMP_LLY,
            width = Config.IMAGE_STAMP_WIDTH,
            height = Config.IMAGE_STAMP_HEIGHT
        )

        responseTextStamp: AsposeResponse = self.pdf_api.post_document_text_stamps(Config.PDF_DOCUMENT_NAME, [ text_stamp ])
        responseImageStamp: AsposeResponse = self.pdf_api.post_document_image_stamps(Config.PDF_DOCUMENT_NAME, [ image_stamp ])

        if responseTextStamp.code == 200 and responseImageStamp.code == 200:
            logging.info(f"Text stamp '{Config.STAMP_TEXT}' and image stamp '{Config.IMAGE_STAMP_FILE}' added to the document '{Config.PDF_DOCUMENT_NAME}'.")
        else:
            if responseTextStamp.code != 200:
                logging.error(f"Failed to add text stamp '{Config.STAMP_TEXT}' to the document '{Config.PDF_DOCUMENT_NAME}'.")
            else:
                logging.error(f"Failed to add image stamp '{Config.IMAGE_STAMP_FILE}' to the document '{Config.PDF_DOCUMENT_NAME}'.")

if __name__ == "__main__":
    pdf_stamps = PdfStamps()
    pdf_stamps.upload_document()
    pdf_stamps.upload_file(Config.IMAGE_STAMP_FILE)
    pdf_stamps.add_document_stamps()
    pdf_stamps.download_result()