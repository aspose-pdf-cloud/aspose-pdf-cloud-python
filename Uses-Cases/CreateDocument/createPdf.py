import shutil
import json
import logging
import pathlib
import math
from asposepdfcloud import ApiClient, PdfApi, Direction, PageMode, PageLayout, DocumentConfig, DocumentProperties, DocumentProperty, DisplayProperties, DefaultPageConfig

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = pathlib.Path(r"settings/credentials.json")
    LOCAL_FOLDER = pathlib.Path(r"test_data")
    TEMP_FOLDER = 'TempPdfCloud'
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    PAGE_WIDTH = 590
    PAGE_HEIGHT = 894
    PAGES_COUNT = 5

class PdfPageChanges:
    """ Class for managing PDF page changes using Aspose PDF Cloud API. """
    def __init__(self, credentials_file: pathlib.Path = Config.CREDENTIALS_FILE):
        self.pdf_api = None
        self._init_api(credentials_file)

    def _init_api(self, credentials_file: pathlib.Path):
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

    def download_result(self):
        """ Download the processed PDF document from the Aspose Cloud server. """
        if self.pdf_api:
            try:
                temp_file = self.pdf_api.download_file(Config.TEMP_FOLDER + '/' + Config.LOCAL_RESULT_DOCUMENT_NAME)
                local_path = Config.LOCAL_FOLDER / Config.LOCAL_RESULT_DOCUMENT_NAME
                shutil.move(temp_file, str(local_path))
                logging.info(f"download_result(): File successfully downloaded: {local_path}")
            except Exception as e:
                logging.error(f"download_result(): Failed to download file: {e}")

    
    def create_document(self):
        """ Create PDF document with required properties. """
        opts = {
            "folder" : Config.TEMP_FOLDER
        }

        document_config = DocumentConfig(
            document_properties=DocumentProperties(
                list=[
                    DocumentProperty(
                        built_in=False,
                        name='prop1',
                        value='Val1',
                    )
                ]),
            display_properties=DisplayProperties(
                center_window = True,
                hide_menu_bar = True,
                direction = Direction.L2R,
                display_doc_title = True,
                hide_tool_bar = True,
                hide_window_ui = True,
                non_full_screen_page_mode = PageMode.USETHUMBS,
                page_layout = PageLayout.TWOPAGELEFT,
                page_mode = PageMode.USETHUMBS
            ),
            default_page_config=DefaultPageConfig(
                height=Config.PAGE_HEIGHT,
                width=Config.PAGE_WIDTH
            ),
            pages_count=Config.PAGES_COUNT
        )
        response = self.pdf_api.post_create_document(Config.LOCAL_RESULT_DOCUMENT_NAME, document_config, **opts)
        logging.info(f"Document #{Config.LOCAL_RESULT_DOCUMENT_NAME} created.")
        return response

if __name__ == "__main__":
    pdf_pages = PdfPageChanges()
    pdf_pages.create_document()
    pdf_pages.download_result()
