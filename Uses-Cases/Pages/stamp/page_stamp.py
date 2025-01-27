import shutil
import json

from asposepdfcloud import ApiClient, PdfApi
from asposepdfcloud.models.stamp import Stamp
from asposepdfcloud.models.aspose_response import AsposeResponse


class ConfigParams:
    """
    Holds configuration parameters for PDF processing.

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
    Provides utilities for managing PDF pages using the Aspose PDF Cloud API.

    This class includes methods for uploading and downloading PDF files,
    retrieving page information, adding and deleting pages, and other operations.

    Attributes:
        pdf_api (AsposePdfApi): An instance of the Aspose PDF Cloud API client.
        credentials_file (str): The path to the credentials file for authentication.

    Methods:
        upload_file(file_name: str):
            Uploads a PDF file to the Aspose Cloud server.

        download_file(file_name: str, new_file_name: str):
            Downloads a processed PDF file from the Aspose Cloud server.

        get_words_count():
            Retrieves the word count for each page in a PDF document.
    """

    pdf_api = None
    credentials_file = "./credentials.json"

    def __init__(self):
        """
        Initializes the PdfPages class by setting up the Aspose PDF Cloud API client.

        Raises:
            FileNotFoundError: If the credentials file is missing.
            ValueError: If the credentials are invalid or incomplete.
        """

        with open(self.credentials_file, "r", encoding="utf-8") as file:
            credentials = json.load(file)

        if not credentials or not credentials["key"] or not credentials["id"]:
            raise ValueError("Invalid or missing credentials in the file.")

        pdf_api_client = ApiClient(credentials["key"], credentials["id"])
        self.pdf_api = PdfApi(pdf_api_client)

    def upload_file(self, file_name: str):
        """
        Uploads a PDF file to the Aspose Cloud server.

        Args:
            file_name (str): The name of the file to upload.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs during the upload.
        """

        self.pdf_api.upload_file(file_name, ConfigParams.LOCAL_PATH + file_name)

    def download_file(self, file_name: str, new_file_name: str):
        """
        Downloads a processed PDF file from the Aspose Cloud server.

        Args:
            file_name (str): The name of the file to download.
            new_file_name (str): The name of the downloaded file.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs during the download.
            shutil.Error: If an error occurs while moving the downloaded file.
        """

        file_path = self.pdf_api.download_file(file_name)
        shutil.move(file_path, ConfigParams.LOCAL_PATH + new_file_name)
        print(f"File '{new_file_name}' downloaded to '{ConfigParams.LOCAL_PATH}'.")

    def add_page_text_stamp(self, page_number: int, text_stamp: str):
        """
        Adds a text stamp to a specific page in a PDF document.

        Args:
            page_number (int): The page number to add the stamp to.
            text_stamp (str): The text to use for the stamp.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs while adding the stamp.
        """

        page_stamp: Stamp = Stamp(
            type="Text",
            background=True,
            horizontal_alignment="Center",
            text_alignment="Center",
            value=text_stamp,
            page_index=page_number,
        )

        response: AsposeResponse = self.pdf_api.put_page_add_stamp(
            ConfigParams.PDF_DOCUMENT_NAME, page_number, page_stamp
        )

        if response.code == 200:
            print(f"Text stamp added to page {page_number}.")
            return

        print("Failed to add text stamp.")
        return


if __name__ == "__main__":
    pdf_pages = PdfPages()
    pdf_pages.upload_file(ConfigParams.PDF_DOCUMENT_NAME)
    pdf_pages.add_page_text_stamp(ConfigParams.PAGE_NUMBER, "Aspose PDF Cloud")
    pdf_pages.download_file(
        ConfigParams.PDF_DOCUMENT_NAME, ConfigParams.LOCAL_RESULT_DOCUMENT_NAME
    )
