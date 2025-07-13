
from annotations_helper import Config, PdfAnnotationsHelper, logging
from asposepdfcloud import PdfApi

class PdfDalTextAnnotations:
    """Class for managing PDF annotations using Aspose PDF Cloud API."""
    def __init__(self, pdf_api: PdfApi, helper: PdfAnnotationsHelper):
        self.pdfApi = pdf_api
        self.helper = helper

    def delete_annotation(self):
        """Delete annotation from the PDF document."""
        if self.pdfApi:
            if Config.ANNOTATION_ID is None:
                logging.info(f"delete_annotation(): annotation id not defined!")
                return
            self.helper.uploadFile(Config.PDF_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)

            args = {
			    "folder": Config.REMOTE_FOLDER
		    }
            response = self.pdfApi.delete_annotation(Config.PDF_DOCUMENT_NAME, Config.ANNOTATION_ID, **args)
            self.helper.delete_popup_annotations(Config.ANNOTATION_ID)
            if response.code == 200:
                logging.info(f"delete_annotation(): annotation '{Config.ANNOTATION_ID}' deleted from the document '{Config.PDF_DOCUMENT_NAME}'.")
                self.helper.downloadFile(Config.PDF_DOCUMENT_NAME, Config.LOCAL_RESULT_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER, "del_annotation_")
            else:
                logging.error(f"delete_annotation(): Failed to delete annotation from the document. Response code: {response.code}")