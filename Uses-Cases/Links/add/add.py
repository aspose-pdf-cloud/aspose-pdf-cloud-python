import shutil
import json

from asposepdfcloud import ApiClient, PdfApi
from asposepdfcloud.models.link_annotation import LinkAnnotation
from asposepdfcloud.models.color import Color
from asposepdfcloud.models.link import Link
from asposepdfcloud.models.rectangle import Rectangle
from asposepdfcloud.models.aspose_response import AsposeResponse


class ConfigParams:
    """
    A class to hold configuration parameters for PDF processing.

    Attributes:
        LOCAL_PATH (str): The local directory path for storing files.
        PDF_DOCUMENT_NAME (str): The name of the PDF document to process.
        LOCAL_RESULT_DOCUMENT_NAME (str): The name of the output PDF file.
        NEW_LINK_ACTION (tuple): The action URL for new links.
        PAGE_NUMBER (int): The page number to process.
        LINK_POS_LLX (float): The lower-left X coordinate of the link rectangle.
        LINK_POS_LLY (float): The lower-left Y coordinate of the link rectangle.
        LINK_POS_URX (float): The upper-right X coordinate of the link rectangle.
        LINK_POS_URY (float): The upper-right Y coordinate of the link rectangle.
    """

    LOCAL_PATH = "C:\\Samples\\"
    PDF_DOCUMENT_NAME = "sample.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    NEW_LINK_ACTION = "https://reference.aspose.cloud/pdf/"
    PAGE_NUMBER = 2
    LINK_POS_LLX = 244.914
    LINK_POS_LLY = 488.622
    LINK_POS_URX = 284.776
    LINK_POS_URY = 498.588


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

        download_file():
            Downloads a processed PDF document from the Aspose Cloud server.

        append_link():
            Appends a new link annotation to a specific page of a PDF document.

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

    def download_file(self, file_name: str, new_file_name: str):
        """
        Downloads a processed PDF document from the Aspose Cloud server.

        This method retrieves a PDF document from the server and saves it
        to the specified local path with a new name defined in the configuration.

        Args:
            file_name (str): The name of the file to download.
            new_file_name (str): The name of the downloaded file.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs during the download request.
            shutil.Error: If an error occurs while moving the downloaded file.

        Returns:
            None
        """

        if not self.pdf_api:
            return

        file_path = self.pdf_api.download_file(file_name)

        shutil.move(
            file_path, ConfigParams.LOCAL_PATH + new_file_name
        )

        print(
            "File "
            + new_file_name
            + " has been downloaded to "
            + ConfigParams.LOCAL_PATH
        )

    def append_link(self):
        """
        Appends a new link annotation to a specific page of a PDF document.

        This method creates a new link annotation with a specified action, color,
        position, and highlighting style, and then adds it to a specified page
        in the PDF document.

        Raises:
            asposepdfcloud.rest.ApiException: If an error occurs during the API request.

        Returns:
            None
        """

        if not self.pdf_api:
            return

        link_color: Color = Color(a=255, r=0, g=255, b=0)

        link_rectangle: Rectangle = Rectangle(
            llx=ConfigParams.LINK_POS_LLX,
            lly=ConfigParams.LINK_POS_LLY,
            urx=ConfigParams.LINK_POS_URX,
            ury=ConfigParams.LINK_POS_URY,
        )

        link_item: Link = Link(
            href=ConfigParams.NEW_LINK_ACTION, rel="self", type=None, title=None
        )

        new_link: LinkAnnotation = LinkAnnotation(
            links=[link_item],
            action_type="GoToURIAction",
            action=ConfigParams.NEW_LINK_ACTION,
            highlighting="Invert",
            color=link_color,
            rect=link_rectangle,
        )

        add_response: AsposeResponse = self.pdf_api.post_page_link_annotations(
            ConfigParams.PDF_DOCUMENT_NAME, ConfigParams.PAGE_NUMBER, [new_link]
        )

        if add_response.code == 200:
            print("Link has been added to the page.")
        else:
            print("Failed to add a link to the page.")


if __name__ == "__main__":
    pdf_links = PdfLinks()
    pdf_links.upload_file(ConfigParams.PDF_DOCUMENT_NAME)
    pdf_links.append_link()
    pdf_links.download_file(ConfigParams.PDF_DOCUMENT_NAME, ConfigParams.LOCAL_RESULT_DOCUMENT_NAME)