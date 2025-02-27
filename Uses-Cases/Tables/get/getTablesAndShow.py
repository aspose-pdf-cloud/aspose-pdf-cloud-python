import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, Table, Row, Cell, FontStyles, GraphInfo, TextRect, TextState, Color, BorderInfo
# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
    PDF_DOCUMENT_NAME = "sample.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    PAGE_NUMBER = 2
    TABLE_ID = "GE5TCOZSGAYCYNRQGUWDINZVFQ3DGMA"

class PdfTables:
    """ Class for managing PDF tables using Aspose PDF Cloud API. """
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

    def upload_document(self):
        """ Upload a PDF document to the Aspose Cloud server. """
        if not self.pdf_api:
            logging.error("upload_document(): PDF API is not initialized. Operation aborted.")
        else:
            file_path = Config.LOCAL_FOLDER / Config.PDF_DOCUMENT_NAME
            try:
                self.pdf_api.upload_file(Config.PDF_DOCUMENT_NAME, str(file_path))
                logging.info(f"upload_document(): File {Config.PDF_DOCUMENT_NAME} uploaded successfully.")
            except Exception as e:
                logging.error(f"upload_document(): Failed to upload file: {e}")

    def _show_tables_info(self, tables, prefix):
        if tables and len(tables) > 0 :
            for table in tables:
                logging.info(f"{prefix} => id: '{table.id}', page: '{table.page_num}', rows: '{len(table.row_list)}', columns: '{len(table.row_list[0].cell_list)}'")
        else:
            logging.error(f"showBoormarks() error: array of tables is empty!")

    def get_all_tables(self):
        if not self.pdf_api:
            logging.error("get_all_tables(): PDF API is not initialized. Operation aborted.")
        else:
            resultTabs = self.pdf_api.get_document_tables(Config.PDF_DOCUMENT_NAME)

            if resultTabs.code == 200 and resultTabs.tables:
                if not resultTabs.tables.list or len(resultTabs.tables.list) == 0:
                    logging.error("get_all_tables(): Unexpected error - tables is null or empty!!!")
                self._show_tables_info(resultTabs.tables.list, "All tables")
                return resultTabs.tables.list
            else:
                logging.error("get_all_tables(): Unexpected error - can't get links!!!")
    
    def get_table_by_id (self):
        if not self.pdf_api:
            logging.error("get_table_by_id(): PDF API is not initialized. Operation aborted.")
        else:
            resultTabs =self.pdf_api.get_table(Config.PDF_DOCUMENT_NAME, Config.TABLE_ID)

            if resultTabs.code == 200 and resultTabs.table:
                self._show_tables_info( [ resultTabs.table ], "Table by Id")
                return resultTabs.table
            else:
                logging.error("get_table_by_id(): Unexpected error - can't get links!!!")

if __name__ == "__main__":
    pdf_tables = PdfTables()
    pdf_tables.upload_document()
    pdf_tables.get_all_tables()
    pdf_tables.get_table_by_id()
