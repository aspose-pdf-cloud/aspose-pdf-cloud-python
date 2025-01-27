import shutil
import json

from asposepdfcloud import ApiClient, PdfApi
from asposepdfcloud.models.aspose_response import AsposeResponse


class ConfigParams:
    """
    A class to hold configuration parameters for PDF processing.

    Attributes:
        LOCAL_PATH (str): The local directory path for storing files.
        PDF_DOCUMENT_NAME (str): The name of the PDF document to process.
        LOCAL_RESULT_DOCUMENT_NAME (str): The name of the output PDF file.
        PAGE_NUMBER (int): The page number to process.
    """

    LOCAL_PATH = "C:\\Samples\\"
    PDF_DOCUMENT_NAME = "sample.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    PAGE_NUMBER = 2


class PdfPages:
    """
    A utility class for performing PDF operations using the Aspose PDF Cloud API.

    This class provides methods to upload files, download processed files,
    and manage PDF pages (e.g., adding new pages).

    Methods:
        upload_file(file_name: str):
            Uploads a PDF file to the Aspose Cloud server.

        download_file(file_name: str, new_file_name: str):
            Downloads a processed PDF file from the Aspose Cloud server.

        move_page(page_number: int, new_page_number: int):
            Moves a page to a new location in the PDF document.
    """

    pdf_api = None
    credentials_file = "./credentials.json"

    def __init__(self):
        """
        Initializes the PdfPages class by authenticating with the Aspose PDF Cloud API.

        Reads credentials from a JSON file and sets up the API client.
        """
        credentials = None

        with open(self.credentials_file, "r", encoding="utf-8") as file:
            credentials = json.load(file)

        if not credentials or not credentials.get("key") or not credentials.get("id"):
            print("Error: No valid credentials found in the file.")
            return

        pdf_api_client = ApiClient(credentials["key"], credentials["id"])
        self.pdf_api = PdfApi(pdf_api_client)

    def upload_file(self, file_name: str):
        """
        Uploads a PDF document to the Aspose Cloud server.

        Args:
            file_name (str): The name of the PDF file to upload.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs during the upload.

        Returns:
            None
        """
        if not self.pdf_api:
            return

        self.pdf_api.upload_file(
            file_name,
            ConfigParams.LOCAL_PATH + file_name,
        )

    def download_file(self, file_name: str, new_file_name: str):
        """
        Downloads a processed PDF document from the Aspose Cloud server.

        Args:
            file_name (str): The name of the file to download.
            new_file_name (str): The name of the downloaded file.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs during the download.
            shutil.Error: If an error occurs while moving the downloaded file.

        Returns:
            None
        """
        if not self.pdf_api:
            return

        file_path = self.pdf_api.download_file(file_name)

        shutil.move(file_path, ConfigParams.LOCAL_PATH + new_file_name)

        print(f"File {new_file_name} has been downloaded to {ConfigParams.LOCAL_PATH}")

    def move_page(self, page_number: int, new_page_number: int):
        """
        Moves a page to a new location in the PDF document.

        Args:
            page_number (int): The page number to move.
            new_page_number (int): The new page number for the page.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs during the move operation.

        Returns:
            None
        """
        if not self.pdf_api:
            return

        response: AsposeResponse = self.pdf_api.post_move_page(
            ConfigParams.PDF_DOCUMENT_NAME, page_number, new_page_number
        )

        if response:
            print(f"Page {page_number} has been moved to position {new_page_number}.")


if __name__ == "__main__":
    pdf_pages = PdfPages()
    pdf_pages.upload_file(ConfigParams.PDF_DOCUMENT_NAME)
    pdf_pages.move_page(ConfigParams.PAGE_NUMBER, ConfigParams.PAGE_NUMBER + 1)
    pdf_pages.download_file(
        ConfigParams.PDF_DOCUMENT_NAME, ConfigParams.LOCAL_RESULT_DOCUMENT_NAME
    )
