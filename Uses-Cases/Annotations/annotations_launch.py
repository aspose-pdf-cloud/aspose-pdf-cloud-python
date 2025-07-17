from annotations_helper import PdfAnnotationsHelper, Config
from get_annotations import PdfGetAnnotations
from get_annotation_by_id import PdfGetAnnotationById
from new_highlight_annotation import PdfAddHighlightAnnotations
from new_strikeout_annotation import PdfAddStrikeoutAnnotations
from new_text_annotation import PdfAddFreeTextAnnotations
from new_underline_annotation import PdfAddUnderlineAnnotations
from delete_page_annotations import PdfDelPageAnnotations
from delete_text_annotation import PdfDalTextAnnotations
from replace_annotation import PdfReplaceAnnotations

if __name__ == "__main__":
	helper = PdfAnnotationsHelper(Config.CREDENTIALS_FILE)

	modify_ant = PdfReplaceAnnotations(helper.pdf_api, helper)
	modify_ant.modify_annotation()

	get_ant = PdfGetAnnotations(helper.pdf_api, helper)
	annotation_id =get_ant.request_annotations()

	rq_ant = PdfGetAnnotationById(helper.pdf_api, helper)
	rq_ant.request_annotation(annotation_id)

	del_ant = PdfDalTextAnnotations(helper.pdf_api, helper)
	del_ant.delete_annotation()

	del_page_ant = PdfDelPageAnnotations(helper.pdf_api, helper)
	del_page_ant.delete_page_annotations()

	add_hl = PdfAddHighlightAnnotations(helper.pdf_api, helper)
	add_hl.append_highlight_annotation()
    
	add_so = PdfAddStrikeoutAnnotations(helper.pdf_api, helper)
	add_so.append_strikeout_annotation()

	add_ft = PdfAddFreeTextAnnotations(helper.pdf_api, helper)
	add_ft.append_text_annotation()

	add_ul = PdfAddUnderlineAnnotations(helper.pdf_api, helper)
	add_ul.append_underline_annotation()
