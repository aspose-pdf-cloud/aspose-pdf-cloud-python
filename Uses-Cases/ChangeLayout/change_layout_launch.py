from change_layout_helper import PdfChangeLayoutHelper, Config
from rotate_documents_pages import PdfRotatePages
from resize_document_all_pages import PdfResizePages
from crop_document_page import PdfCropPages

if __name__ == "__main__":
	helper = PdfChangeLayoutHelper(Config.CREDENTIALS_FILE)

	crop = PdfCropPages(helper.pdf_api, helper)
	crop.cropDocumentPage(Config.PDF_DOCUMENT, Config.CROP_PAGE_NUMBER, Config.CROP_LLX, Config.CROP_LLY, Config.CROP_WIDTH, Config.CROP_HEIGHT, Config.CROP_LOCAL_RESULT_DOCUMENT_NAME,  Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)
    
	resize = PdfResizePages(helper.pdf_api, helper)
	resize.resizeAllPages(Config.PDF_DOCUMENT, Config.RESIZE_PDF_HTML_FILE, Config.RESIZE_NEW_PAGE_WIDTH, Config.RESIZE_NEW_PAGE_HEIGHT, Config.RESIZE_RESULT_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)
	
	rotate = PdfRotatePages(helper.pdf_api, helper)
	rotate.rotateDocumentPages(Config.PDF_DOCUMENT, Config.PDF_OUTPUT, Config.ROTATE_PAGES_ANGLE, Config.ROTATE_PAGES)

