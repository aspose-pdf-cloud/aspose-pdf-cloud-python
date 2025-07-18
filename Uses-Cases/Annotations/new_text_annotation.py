from annotations_helper import Config, PdfAnnotationsHelper, logging
from asposepdfcloud import ApiClient, PdfApi, FreeTextAnnotation, Rectangle, TextStyle, Color, FreeTextIntent, Justification, AnnotationFlags, HorizontalAlignment

class PdfAddFreeTextAnnotations:
    """Class for managing PDF annotations using Aspose PDF Cloud API."""
    def __init__(self, pdf_api: PdfApi, helper: PdfAnnotationsHelper):
        self.pdfApi = pdf_api
        self.helper = helper

    def append_text_annotation(self):
        """Append a new free text annotation to the PDF document."""
        if self.pdfApi:
            self.helper.uploadFile(Config.PDF_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)
            
            args = {
			    "folder": Config.REMOTE_FOLDER
		    }

            text_style = TextStyle(
                font_size=20,
                font='Arial', 
                foreground_color=Color(a=0xFF, r=0, g=0xFF, b=0),
                background_color=Color(a=0xFF, r=0xFF, g=0, b=0)
            )

            new_annotation = FreeTextAnnotation(
                rect = Rectangle(llx=100, lly=350, urx=450, ury=400),
                text_style = text_style,
                name = 'Free Text Annotation',
                flags = [AnnotationFlags.DEFAULT],
                horizontal_alignment = HorizontalAlignment.CENTER,
                intent = FreeTextIntent.FREETEXTTYPEWRITER,
                rich_text = Config.NEW_FT_ANNOTATION_TEXT,
                subject = Config.NEW_FT_ANNOTATION_SUBJECT,
                contents = Config.NEW_FT_ANNOTATION_CONTENTS,
                title = Config.NEW_FT_ANNOTATION_DESCRIPTION,
                z_index = 1,
                justification = Justification.CENTER,
            )
            new_annotation.attribute_map["icon"] = "Icon"
            new_annotation.swagger_types["icon"] = "TextIcon"
            new_annotation.icon = "Help"

            try:
                response = self.pdfApi.post_page_free_text_annotations(Config.PDF_DOCUMENT_NAME, Config.PAGE_NUMBER, [new_annotation], **args)
                if response.code == 200:
                    logging.info(f"append_text_annotation(): annotation '{Config.NEW_FT_ANNOTATION_TEXT}' added to the document '{Config.PDF_DOCUMENT_NAME}'.")
                    self.helper.downloadFile(Config.PDF_DOCUMENT_NAME, Config.LOCAL_RESULT_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER, "add_freetext_")
                else:
                    logging.error(f"append_text_annotation(): Failed to add annotation to the document. Response code: {response.code}")
            except Exception as e:
                logging.error(f"append_text_annotation(): Error while adding annotation: {e}")