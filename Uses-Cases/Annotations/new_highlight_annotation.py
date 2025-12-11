from annotations_helper import Config, PdfAnnotationsHelper, logging
from asposepdfcloud import PdfApi, HighlightAnnotation, Rectangle, Color, Point, AnnotationFlags, HorizontalAlignment, VerticalAlignment

class PdfAddHighlightAnnotations:
    """Class for managing PDF annotations using Aspose PDF Cloud API."""
    def __init__(self, pdf_api: PdfApi, helper: PdfAnnotationsHelper):
        self.pdfApi = pdf_api
        self.helper = helper

    def append_highlight_annotation(self):
        """Append a new highlight text annotation to the PDF document."""
        if self.pdfApi:
            self.helper.uploadFile(Config.PDF_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)

            args = {
			    "folder": Config.REMOTE_FOLDER
		    }

            new_annotation = HighlightAnnotation(
                rect = Rectangle(llx=100, lly=350, urx=450, ury=400),
                name = 'Highlight_Text_Annotation',
                flags = [AnnotationFlags.DEFAULT],
                horizontal_alignment = HorizontalAlignment.LEFT,
                vertical_alignment = VerticalAlignment.TOP,
                rich_text = Config.NEW_HL_ANNOTATION_TEXT,
                subject = Config.NEW_HL_ANNOTATION_SUBJECT,
                contents= Config.NEW_HL_ANNOTATION_CONTENTS,
                title = Config.NEW_HL_ANNOTATION_DESCRIPTION,
                z_index = 1,
                color=Color(a=0xFF, r=0, g=0xFF, b=0),
                quad_points = [
                    Point(100, 350),
                    Point(450, 350),
                    Point(100, 400),
                    Point(100, 350)
                ],
                modified = '03/27/2025 00:00:00.000 AM',
            )
            try:
                response = self.pdfApi.post_page_highlight_annotations(Config.PDF_DOCUMENT_NAME, Config.PAGE_NUMBER, [new_annotation], **args)
                if response.code == 200:
                    logging.info(f"append_highlight_annotation(): annotation '{Config.NEW_HL_ANNOTATION_TEXT}' added to the document '{Config.PDF_DOCUMENT_NAME}'.")
                    self.helper.downloadFile(Config.PDF_DOCUMENT_NAME, Config.LOCAL_RESULT_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER, "add_highlight_")
                else:
                    logging.error(f"append_highlight_annotation(): Failed to add annotation to the document. Response code: {response.code}")
            except Exception as e:
                logging.error(f"append_highlight_annotation(): Error while adding annotation: {e}")