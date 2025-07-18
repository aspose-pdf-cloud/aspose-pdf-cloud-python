from annotations_helper import Config, PdfAnnotationsHelper, logging
from asposepdfcloud import PdfApi, TextAnnotationResponse

class PdfReplaceAnnotations:
    """Class for managing PDF annotations using Aspose PDF Cloud API."""
    def __init__(self, pdf_api: PdfApi, helper: PdfAnnotationsHelper):
        self.pdfApi = pdf_api
        self.helper = helper
        
    def _get_annotation(self, annotation_id):
        """Get annotation from the page in the PDF document."""
        if self.pdfApi:
            args = {
			    "folder": Config.REMOTE_FOLDER
		    }
            response: TextAnnotationResponse = self.pdfApi.get_text_annotation(Config.PDF_DOCUMENT_NAME, annotation_id, **args)
            if response.code == 200:
                logging.info(f"get_annotationn(): annotation '{annotation_id}' successfully found '{response.annotation.contents}' in the document '{Config.PDF_DOCUMENT_NAME}'.")
                return response.annotation
            else:
                logging.error(f"get_annotation(): Failed to get annotation in the document. Response code: {response.code}")
                return None

    def modify_annotation(self):
        if self.pdfApi:
            if Config.ANNOTATION_ID:
                self.helper.uploadFile(Config.PDF_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)
                args = {
                    "folder": Config.REMOTE_FOLDER
                }
                annotation = self._get_annotation(Config.ANNOTATION_ID)
                annotation.contents = Config.REPLACED_CONTENT
                annotation.icon = "Star"
                response = self.pdfApi.put_text_annotation(Config.PDF_DOCUMENT_NAME, Config.ANNOTATION_ID, annotation, **args)
                if response.code == 200:
                    logging.info(f"modify_annotation(): annotation '{annotation.id}' successfully modified in the document '{Config.PDF_DOCUMENT_NAME}'.")
                    self.helper.downloadFile(Config.PDF_DOCUMENT_NAME, Config.LOCAL_RESULT_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER, "replaced_annotatiom_")
                else:
                    logging.error(f"modify_annotation(): Failed to modify annotation in the document. Response code: {response.code}")