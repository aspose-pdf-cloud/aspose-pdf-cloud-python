import shutil
import json

from asposepdfcloud import ApiClient, PdfApi
from asposepdfcloud.models.document_pages_response import DocumentPagesResponse
from asposepdfcloud.models.document_page_response import DocumentPageResponse


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

        get_pages_info() -> list:
            Retrieves information about all pages in a PDF document.

        get_page_info(page_number: int):
            Retrieves information about a specific page in a PDF document.

        add_new_page():
            Adds a new page to a PDF document.

        delete_page(page_number: int):
            Deletes a specific page from a PDF document.

        show_pages(pages_list: list, prefix: str):
            Displays information about pages in a PDF document.
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

    def get_pages_info(self) -> list:
        """
        Retrieves information about all pages in a PDF document.

        Returns:
            list: A list of pages in the PDF document.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs during the request.
        """

        result_pages: DocumentPagesResponse = self.pdf_api.get_pages(
            ConfigParams.PDF_DOCUMENT_NAME
        )
        if result_pages.code == 200 and result_pages.pages.list:
            return result_pages.pages.list
        print("Failed to retrieve pages information.")
        return []

    def get_page_info(self, page_number: int):
        """
        Retrieves information about a specific page in a PDF document.

        Args:
            page_number (int): The number of the page to retrieve.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs during the request.
        """

        result_page: DocumentPageResponse = self.pdf_api.get_page(
            ConfigParams.PDF_DOCUMENT_NAME, page_number
        )
        if result_page.code == 200 and result_page.page:
            print(result_page.page)
        else:
            print(f"Failed to retrieve information for page {page_number}.")

    def add_new_page(self):
        """
        Adds a new page to a PDF document.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs during the request.
        """

        result_pages: DocumentPagesResponse = self.pdf_api.put_add_new_page(
            ConfigParams.PDF_DOCUMENT_NAME
        )
        if result_pages.code == 200 and result_pages.pages:
            print("New page added.")
        else:
            print("Failed to add a new page.")

    def delete_page(self, page_number: int):
        """
        Deletes a specific page from a PDF document.

        Args:
            page_number (int): The number of the page to delete.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs during the request.
        """

        result = self.pdf_api.delete_page(ConfigParams.PDF_DOCUMENT_NAME, page_number)
        if result.code == 200:
            print(f"Page {page_number} deleted.")
        else:
            print(f"Failed to delete page {page_number}.")

    def show_pages(self, pages_list: list, prefix: str):
        """
        Displays information about pages in a PDF document.

        Args:
            pages_list (list): A list of pages to display.
            prefix (str): A prefix string to prepend to the output.
        """

        if not pages_list:
            print("No pages found.")
            return
        for i, page in enumerate(pages_list):
            print(f"{prefix}Page {i + 1}: {page}")


if __name__ == "__main__":
    pdf_pages = PdfPages()
    pdf_pages.upload_file(ConfigParams.PDF_DOCUMENT_NAME)
    pages = pdf_pages.get_pages_info()
    pdf_pages.show_pages(pages, "[in] ")
    pdf_pages.get_page_info(ConfigParams.PAGE_NUMBER)
    pdf_pages.add_new_page()
    pdf_pages.delete_page(ConfigParams.PAGE_NUMBER)
    pdf_pages.download_file(
        ConfigParams.PDF_DOCUMENT_NAME, ConfigParams.LOCAL_RESULT_DOCUMENT_NAME
    )
