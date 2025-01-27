import json
from asposepdfcloud import ApiClient, PdfApi
from asposepdfcloud.models.link_annotations_response import LinkAnnotationsResponse
from asposepdfcloud.models.link_annotation_response import LinkAnnotationResponse


class ConfigParams:
    """
    A class to hold configuration parameters for PDF processing.

    Attributes:
        LOCAL_PATH (str): The local directory path for storing files.
        PDF_DOCUMENT_NAME (str): The name of the PDF document to process.
        NEW_LINK_ACTION (tuple): The action URL for new links.
        PAGE_NUMBER (int): The page number to process.
        LINK_FIND_ID (str): The ID of the link annotation to find.
    """

    LOCAL_PATH = "C:\\Samples\\"
    PDF_DOCUMENT_NAME = "sample.pdf"
    NEW_LINK_ACTION = "https://reference.aspose.cloud/pdf/"
    PAGE_NUMBER = 2
    LINK_FIND_ID = "GI5UO32UN5KVESKBMN2GS33OHMZTEMJMGUYDQLBTGYYCYNJSGE"


class PdfLinks:
    """
    A utility class for managing PDF links using Aspose PDF Cloud API.

    This class provides methods for uploading and downloading PDF files,
    retrieving link annotations from a specific page of a PDF, and other
    related PDF link operations.

    Attributes:
        pdf_api (AsposePdfApi): An instance of the Aspose PDF Cloud API client.
        credentials_file (str): Path to the credentials file for authentication.

    Methods:
        upload_file():
            Uploads a PDF document to the Aspose Cloud server.

        get_all_links():
            Retrieves all link annotations from a specific page of a PDF document.

        get_link_by_id(link_id: str):
            Retrieves a specific link annotation from a PDF document.
    """

    pdf_api = None
    credentials_file = "./credentials.json"

    def __init__(self):
        credentials = None

        with open(self.credentials_file, "r", encoding="utf-8") as file:
            credentials = json.load(file)

        if not credentials or credentials["key"] == "" or credentials["id"] == "":
            print("Error: No credentials found in the file.")
            return

        pdf_api_client = ApiClient(credentials["key"], credentials["id"])
        self.pdf_api = PdfApi(pdf_api_client)

    def upload_file(self, file_name: str):
        """
        Uploads a PDF document to the Aspose Cloud server.

        This method uploads a PDF document from the local path specified
        in the configuration to the Aspose Cloud server for further processing.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs during the upload request.

        Returns:
            None
        """

        if not self.pdf_api:
            return

        self.pdf_api.upload_file(
            file_name,
            ConfigParams.LOCAL_PATH + file_name,
        )

    def get_all_links(self, file_name: str, page_number: int):
        """
        Retrieves all link annotations from a specific page of a PDF document.

        This method fetches link annotations from a specified page in the
        PDF document and prints their details (ID and action) if they exist.

        Args:
            file_name (str): The name of the PDF document to process.
            page_number (int): The page number to retrieve link annotations from.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs during the request.

        Returns:
            None
        """

        if not self.pdf_api:
            return

        result_links: LinkAnnotationsResponse = self.pdf_api.get_page_link_annotations(
            file_name, page_number
        )
        if result_links.code == 200 and result_links.links.list:
            print(result_links.links.list)
        else:
            print("No links found.")


    def get_link_by_id(self, link_id: str):
        """
        Retrieves a specific link annotation from a PDF document.

        This method fetches a link annotation by its ID from the PDF document
        and prints its details (ID and action) if it exists.

        Args:
            link_id (str): The ID of the link annotation to retrieve.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs during the request.

        Returns:
            None
        """

        if not self.pdf_api:
            return

        result_link: LinkAnnotationResponse = self.pdf_api.get_link_annotation(
            ConfigParams.PDF_DOCUMENT_NAME, link_id
        )
        if result_link.code == 200:
            print("Link ID: " + result_link.link.id + " - Link Action: " + result_link.link.action)

if __name__ == "__main__":
    pdf_links = PdfLinks()
    pdf_links.upload_file(ConfigParams.PDF_DOCUMENT_NAME)
    pdf_links.get_all_links(ConfigParams.PDF_DOCUMENT_NAME, ConfigParams.PAGE_NUMBER)
    pdf_links.get_link_by_id(ConfigParams.LINK_FIND_ID)