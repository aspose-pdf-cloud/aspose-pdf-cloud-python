
from annotations_helper import Config, PdfAnnotationsHelper, logging
from asposepdfcloud import PdfApi

class PdfDelPageAnnotations:
    """Class for managing PDF annotations using Aspose PDF Cloud API."""
    def __init__(self, pdf_api: PdfApi, helper: PdfAnnotationsHelper):
        self.pdfApi = pdf_api
        self.helper = helper

    def delete_page_annotations(self):
        """Delete annotation from the PDF document."""
        if self.pdfApi:
            self.helper.uploadFile(Config.PDF_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)

            args = {
			    "folder": Config.REMOTE_FOLDER
		    }

            response = self.pdfApi.delete_page_annotations(Config.PDF_DOCUMENT_NAME, Config.PAGE_NUMBER, **args)
            if response.code == 200:
                logging.info(f"delete_annotation(): annotations on page '{Config.PAGE_NUMBER}' deleted from the document '{Config.PDF_DOCUMENT_NAME}'.")
                self.helper.downloadFile(Config.PDF_DOCUMENT_NAME, Config.LOCAL_RESULT_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER, "del_page_annotations_")
            else:
                logging.error(f"delete_annotation(): Failed to delete annotation from the document. Response code: {response.code}")