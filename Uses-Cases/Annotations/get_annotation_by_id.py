from annotations_helper import Config, PdfAnnotationsHelper, logging
from asposepdfcloud import PdfApi, AnnotationsInfoResponse

class PdfGetAnnotationById:
    """Class for managing PDF annotations using Aspose PDF Cloud API."""
    def __init__(self, pdf_api: PdfApi, helper: PdfAnnotationsHelper):
        self.pdfApi = pdf_api
        self.helper = helper

    def request_annotation(self, annotation_id):
        """Get annotation from the page in the PDF document."""
        if self.pdfApi:
            self.helper.uploadFile(Config.PDF_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)

            args = {
			    "folder": Config.REMOTE_FOLDER
		    }
            response = self.pdfApi.get_text_annotation(Config.PDF_DOCUMENT_NAME, annotation_id, **args)
            if response.code == 200:
                logging.info(f"get_annotationn(): annotation '{annotation_id}' successfully found '{response.annotation.contents}' in the document '{Config.PDF_DOCUMENT_NAME}'.")
            else:
                logging.error(f"get_annotation(): Failed to get annotation in the document. Response code: {response.code}")