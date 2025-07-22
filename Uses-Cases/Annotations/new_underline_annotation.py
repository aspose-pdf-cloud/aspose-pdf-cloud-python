from annotations_helper import Config, PdfAnnotationsHelper, logging
from asposepdfcloud import ApiClient, PdfApi, UnderlineAnnotation, Rectangle, Color, Point, AnnotationFlags, HorizontalAlignment, VerticalAlignment,AnnotationState

class PdfAddUnderlineAnnotations:
    """Class for managing PDF annotations using Aspose PDF Cloud API."""
    def __init__(self, pdf_api: PdfApi, helper: PdfAnnotationsHelper):
        self.pdfApi = pdf_api
        self.helper = helper

    def append_underline_annotation(self):
        """Append a new underline text annotation to the PDF document."""
        if self.pdfApi:
            self.helper.uploadFile(Config.PDF_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)
            args = {
			    "folder": Config.REMOTE_FOLDER
		    }
            new_annotation = UnderlineAnnotation(
                rect = Rectangle(llx=100, lly=350, urx=450, ury=400),
                name = 'Underline Text Annotation',
                flags = [AnnotationFlags.DEFAULT],
                horizontal_alignment = HorizontalAlignment.CENTER,
                vertical_alignment = VerticalAlignment.TOP,
                rich_text = Config.NEW_UL_ANNOTATION_TEXT,
                subject = Config.NEW_UL_ANNOTATION_SUBJECT,
                title = Config.NEW_UL_ANNOTATION_DESCRIPTION,
                contents= Config.NEW_UL_ANNOTATION_CONTENTS,
                z_index = 1,
                color=Color(a=0xFF, r=0, g=0xFF, b=0),
                quad_points = [
                    Point(10, 10),
                    Point(20, 10),
                    Point(10, 20),
                    Point(10, 10)
                ],
                modified = '03/27/2025 00:00:00.000 AM',
            )
            new_annotation.attribute_map["icon"] = "Icon"
            new_annotation.swagger_types["icon"] = "TextIcon"
            new_annotation.icon = "Star"
            try:
                response = self.pdfApi.post_page_underline_annotations(Config.PDF_DOCUMENT_NAME, Config.PAGE_NUMBER, [new_annotation], **args)
                if response.code == 200:
                    logging.info(f"append_underline_annotation(): annotation '{Config.NEW_UL_ANNOTATION_TEXT}' added to the document '{Config.PDF_DOCUMENT_NAME}'.")
                    self.helper.downloadFile(Config.PDF_DOCUMENT_NAME, Config.LOCAL_RESULT_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER, "add_underline_")
                else:
                    logging.error(f"append_underline_annotation(): Failed to add annotation to the document. Response code: {response.code}")
            except Exception as e:
                logging.error(f"append_underline_annotation(): Error while adding annotation: {e}")