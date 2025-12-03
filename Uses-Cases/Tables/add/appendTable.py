import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, Table, Row, Cell, FontStyles, GraphInfo, TextRect, TextState, Color, BorderInfo
# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"settings/credentials.json")
    LOCAL_FOLDER = Path(r"test_data")
    PDF_DOCUMENT_NAME = "sample.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    PAGE_NUMBER = 2

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

    def _init_table (self):
        """ Initialize new table """
        num_of_cols = 5
        num_of_rows = 5

        header_text_state = TextState(
            font = "Arial Bold",
            font_size = 11,
            foreground_color = Color( a = 255, r = 255, g = 255, b = 255 ),
            font_style = FontStyles.BOLD,
        )

        common_text_state = TextState (
            font = "Arial Bold",
            font_size = 11,
            foreground_color = Color( a=255, r = 112, g = 112, b = 112 ),
            font_style=FontStyles.REGULAR
        )

        col_widths = ""
        for col_index in range(0,num_of_cols):
            col_widths += " 70"

        table_rows = [];

        border_table_border = GraphInfo(
            color = Color(a = 255, r = 0, g = 255, b = 0 ),
            line_width = 0.5
        )

        for row_index in range(0, num_of_rows):
            row_cells = []

            for col_index in range(0, num_of_cols):
                cell = Cell( default_cell_text_state = common_text_state)

                if row_index == 0:  # header cells
                    cell.background_color = Color(a = 255, r = 128, g = 128, b=128)
                    cell.default_cell_text_state = header_text_state
                else:
                    cell.background_color = Color(a =255, r =255, g =255, b =255)

                text_rect = TextRect()
                if row_index == 0:
                    text_rect.text = f"header #{col_index}"
                else:
                    text_rect.text = f"value '({row_index},{col_index})'"
                cell.paragraphs = [ text_rect]

                row_cells.append(cell)

            row = Row(cells=row_cells)

            table_rows.append(row)

        table = Table(left=150,top=250, column_widths=col_widths, rows=table_rows)

        table.default_cell_border = BorderInfo(
            top = border_table_border,
            right = border_table_border,
            bottom = border_table_border,
            left = border_table_border,
            rounded_border_radius = 2
        )

        return table

    def add_table_on_page (self):
        """ Append table to the PDF document page. """
        if self.pdf_api:
            try:
                new_table = self._init_table()

                resultTabs = self.pdf_api.post_page_tables( Config.PDF_DOCUMENT_NAME, Config.PAGE_NUMBER, [ new_table ])

                if resultTabs.code == 200:
                    logging.info(f"add_table_on_page(): Table was appended to the document '{Config.PDF_DOCUMENT_NAME}' on page #'{Config.PAGE_NUMBER}'.")
                else:
                    logging.error(f"add_table_on_page(): Failed to add new table to the document '{Config.PDF_DOCUMENT_NAME}'.")
            except Exception as e:
                logging.error(f"add_table_on_page(): Failed to append table: {e}")

if __name__ == "__main__":
    pdf_tables = PdfTables()
    pdf_tables.upload_document()
    pdf_tables.add_table_on_page()
    pdf_tables.download_result()
