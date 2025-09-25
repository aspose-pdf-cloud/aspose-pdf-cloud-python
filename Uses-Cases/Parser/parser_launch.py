from paresr_helpers import ParesrHelper, Config
from get_xml import ExportFormToXXML
from get_fdf import ExportFormToFDF
from get_images import GetImages
from get_tables import GetTables
from get_textboxes import GetTextBoxes

if __name__ == "__main__":
	helper = ParesrHelper(Config.CREDENTIALS_FILE)

	xmlExtractor = ExportFormToXXML(helper)
	xmlExtractor.Extract(Config.PDF_DOCUMENT_NAME, Config.XML_OUTPUT_FILE,  Config.LOCAL_FOLDER, Config.REMOTE_TEMP_FOLDER)

	fdfExtractor = ExportFormToFDF(helper)
	fdfExtractor.Extract(Config.PDF_DOCUMENT_NAME, Config.FDF_OUTPUT_FILE,  Config.LOCAL_FOLDER, Config.REMOTE_TEMP_FOLDER)

	getImages = GetImages(helper)
	getImages.Extract(Config.PDF_DOCUMENT_NAME, Config.PAGE_NUMBER, Config.LOCAL_FOLDER, Config.REMOTE_TEMP_FOLDER)

	getTables = GetTables(helper)
	getTables.Extract(Config.PDF_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_TEMP_FOLDER)

	getTextBoxes = GetTextBoxes(helper)
	getTextBoxes.Extract(Config.PDF_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_TEMP_FOLDER)