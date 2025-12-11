import os
import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi 
from asposepdfcloud import AsposeResponse, DocumentPageResponse, Page, Rectangle, DocumentConfig, DocumentProperties, DocumentProperty, DisplayProperties, DefaultPageConfig
from asposepdfcloud import ImageStamp, HorizontalAlignment, VerticalAlignment, Rotation

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Config:
	"""Configuration parameters."""
	CREDENTIALS_FILE = Path(r"settings/credentials.json")
	LOCAL_FOLDER = Path(r"test_data")
	REMOTE_FOLDER = "Your_Temp_Pdf_Cloud"
	PDF_DOCUMENT  = "PdfWithScreenAnnotations.pdf"
	PDF_OUTPUT    = "output_sample.pdf"

	ROTATE_PAGES_ANGLE = Rotation.ON90
	ROTATE_PAGES       = "1-2"

	CROP_PAGE_TEMP_FILE             = "sammple_temp_file.png"
	CROP_LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
	CROP_PAGE_NUMBER                = 1
	CROP_HEIGHT                     = 400
	CROP_WIDTH                      = 300
	CROP_LLX                        = 100
	CROP_LLY                        = 200

	RESIZE_PDF_HTML_FILE        = "sammple_temp_file.html"
	RESIZE_RESULT_DOCUMENT_NAME = "output_sample.pdf"
	RESIZE_PAGE_NUMBER          = 2
	RESIZE_NEW_PAGE_WIDTH       = 800
	RESIZE_NEW_PAGE_HEIGHT      = 400

	CROP_PAGE_WIDTH  = 0
	CROP_PAGE_HEIGHT = 0


class PdfChangeLayoutHelper:
	def __init__(self, credentials_file: Path):
		self.pdf_api = None
		self._init_api(credentials_file)

	def _init_api(self, credentials_file: Path):
		"""Initialize the API client."""
		try:
			with credentials_file.open("r", encoding="utf-8") as file:
				credentials = json.load(file)
			api_key, app_id = credentials.get("client_secret"), credentials.get("client_id")
			if not api_key or not app_id:
				raise ValueError("Error: Missing API keys in the credentials file.")
			self.pdf_api = PdfApi(ApiClient(api_key, app_id))
		except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
			logging.error(f"Failed to load credentials: {e}")

	def uploadFile(self, fileName: str, localFolder: Path, remoteFolder: str):
		""" Upload a local fileName to the Aspose Cloud server. """
		if self.pdf_api:
			file_path = localFolder / fileName
			try:
				self.pdf_api.upload_file(os.path.join(remoteFolder, fileName), file_path)
				logging.info(f"upload_file(): File '{fileName}' uploaded successfully.")
			except Exception as e:
				logging.error(f"upload_document(): Failed to upload file: {e}")
	

	def downloadFile(self, document: str, outputDocument: str, localFolder: Path, remoteFolder: Path,  output_prefix: str):
		"""Download the processed PDF document from the Aspose Cloud server."""
		if self.pdf_api:
			try:
				temp_file = self.pdf_api.download_file(str(remoteFolder) + '/' + document)
				local_path = localFolder / ( output_prefix + outputDocument )
				shutil.move(temp_file, str(local_path))
				logging.info(f"download_result(): File successfully downloaded: {local_path}")
			except Exception as e:
				logging.error(f"download_result(): Failed to download file: {e}")

	def getPageInfo(self, document: str, pageNumber: int, tempFolder: str):
		if self.pdf_api:
			args = {
				"folder": tempFolder,
			}
			response: DocumentPageResponse = self.pdf_api.get_page(document, pageNumber, **args)

			if response.code == 200:
				logging.info(f"page {pageNumber} => id: '{response.page.id}', lLx: '{response.page.rectangle.llx}', lLY: '{response.page.rectangle.lly}', uRX: '{response.page.rectangle.urx}', uRY: '{response.page.rectangle.ury}'")
				Config.CROP_PAGE_HEIGHT = response.page.rectangle.ury - response.page.rectangle.lly
				Config.CROP_PAGE_WIDTH = response.page.rectangle.urx - response.page.rectangle.llx
			else:
				logging.error("Unexpected error : can't get pages!!!")

	def extractPdfPage(self, document: str, pageNumber: int, width: int, height: int, localFolder: str, tempFolder: str):
		if self.pdf_api:
			args = {
				"folder": tempFolder,
				"width":  int(width),
				"height": int(height),
			}

			response = self.pdf_api.get_page_convert_to_png(document, pageNumber, **args)
			imageFile = document + ".png"
			imagePath = localFolder / imageFile
			shutil.move(response, str(imagePath))

			self.uploadFile(imageFile, localFolder, tempFolder)

			logging.info(f"Page #{pageNumber} extracted as image.")
			return imageFile
	
	def createDocument(self, newDocumentName: str, width: int, height: int, tempFolder: Path):
		""" Create PDF document with required properties. """
		if self.pdf_api:
			args = {
				"folder" : str(tempFolder)
			}

			document_config = DocumentConfig(
				pages_count = 1,
				document_properties=DocumentProperties(
					list=[
						DocumentProperty(
							built_in=False,
							name='prop1',
							value='Val1',
						)
					]),
				display_properties=DisplayProperties(
					center_window = True,
					hide_menu_bar = True,
				),
				default_page_config=DefaultPageConfig(
					height = height,
					width = width
				),
			)
			response = self.pdf_api.post_create_document(newDocumentName, document_config, **args)
			logging.info(f"Document #{newDocumentName} created.")
			return response
	
	def insertPageAsImage(self, document: str, imageFileValue: str, llx: int, lly: int, tempFolder: str):
		if self.pdf_api:
			args = {
				"folder" : str(tempFolder)
			}

			image_stamp: ImageStamp = ImageStamp(
				background = True,
                horizontal_alignment = HorizontalAlignment.NONE,
                vertical_alignment = VerticalAlignment.NONE,
				rotate = Rotation.NONE,
				rotate_angle = 0,
				opacity = 1,
				x_indent = -llx,
				y_indent = -lly,
				zoom = 1,
				file_name = os.path.join(tempFolder, imageFileValue)
            )

			try:
				responseImageStamp: AsposeResponse = self.pdf_api.post_page_image_stamps(document, 1, [ image_stamp ], **args)
				if responseImageStamp.code != 200:
					logging.info( "Unexpected error on inserting image to the document!")
				else:
					return responseImageStamp

			except Exception as e:
				logging.error(f"add_document_stamps(): Failed to insert image: {e}")
