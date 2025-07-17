from annotations_helper import Config, PdfAnnotationsHelper, logging
from asposepdfcloud import PdfApi, AnnotationsInfoResponse

class PdfGetAnnotations:
    """Class for managing PDF annotations using Aspose PDF Cloud API."""
    def __init__(self, pdf_api: PdfApi, helper: PdfAnnotationsHelper):
        self.pdfApi = pdf_api
        self.helper = helper

    def request_annotations(self):
        """Get annotations from the page in the PDF document."""
        if self.pdfApi:
            self.helper.uploadFile(Config.PDF_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)

            args = {
			    "folder": Config.REMOTE_FOLDER
		    }
            annotation_result = ''
            response: AnnotationsInfoResponse = self.pdfApi.get_page_annotations(Config.PDF_DOCUMENT_NAME, Config.PAGE_NUMBER, **args)
            if response.code == 200:
                for annotation in response.annotations.list:
                    if annotation.annotation_type == "Text":
                        logging.info(f"get_annotations(): annotation id={annotation.id} with '{annotation.contents}' content get from the document '{Config.PDF_DOCUMENT_NAME}' on {annotation.page_index} page.")
                        annotation_result = annotation.id
                return annotation_result
            else:
                logging.error(f"get_annotations(): Failed to get annotation in the document. Response code: {response.code}")
                return annotation_result
