import shutil
import json
import logging
import os
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi, HighlightAnnotation, Rectangle, Color, Point, AnnotationFlags, HorizontalAlignment, VerticalAlignment, AnnotationType

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"settings/credentials.json")
    LOCAL_FOLDER = Path(r"test_data")
    REMOTE_FOLDER = "Your_Temp_Pdf_Cloud"
    PDF_DOCUMENT_NAME = "PdfWithAnnotations.pdf"
    LOCAL_RESULT_DOCUMENT_NAME = "output_sample.pdf"
    PAGE_NUMBER = 2

    ANNOTATION_ID = "GI5TAOZRGU3CYNZSGEWDCNZWFQ3TGOI"

    NEW_HL_ANNOTATION_TEXT = "NEW HIGHLIGHT TEXT ANNOTATION"
    NEW_HL_ANNOTATION_DESCRIPTION = 'This is a sample highlight annotation'
    NEW_HL_ANNOTATION_SUBJECT = "Highlight Text Box Subject"
    NEW_HL_ANNOTATION_CONTENTS = "Highlight annotation sample contents"
	
    NEW_SO_ANNOTATION_TEXT = "NEW STRIKEOUT TEXT ANNOTATION"
    NEW_SO_ANNOTATION_DESCRIPTION = 'This is a sample strikeout annotation'
    NEW_SO_ANNOTATION_SUBJECT = "Strikeout Text Box Subject"
    NEW_SO_ANNOTATION_CONTENTS = "Strikeout annotation sample contents"

    NEW_UL_ANNOTATION_TEXT = "NEW UNDERLINE TEXT ANNOTATION"
    NEW_UL_ANNOTATION_DESCRIPTION = 'This is a sample underline annotation'
    NEW_UL_ANNOTATION_SUBJECT = "Underline Text Box Subject"
    NEW_UL_ANNOTATION_CONTENTS = "Underline annotation sample contents"

    NEW_FT_ANNOTATION_TEXT = "NEW FREE TEXT ANNOTATION"
    NEW_FT_ANNOTATION_DESCRIPTION = 'This is a sample annotation'
    NEW_FT_ANNOTATION_SUBJECT = "Free Text Box Subject"
    NEW_FT_ANNOTATION_CONTENTS = "Free Text annotation sample contents"

    REPLACED_CONTENT = 'This is a replaced sample annotation'

class PdfAnnotationsHelper:
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

	def delete_popup_annotations(self, parent_annotation):
		"""delete popup annotations for typed parent annotation in the page in the PDF document."""
		if self.pdf_api:
			args = {
			    "folder": Config.REMOTE_FOLDER
		    }
			response = self.pdf_api.get_document_popup_annotations(Config.PDF_DOCUMENT_NAME, **args)
			if response.code == 200:
				for annotation in response.annotations.list:
					if annotation.parent.id == parent_annotation:
						self.pdf_api.delete_annotation(Config.PDF_DOCUMENT_NAME, annotation.id, **args)
						logging.info(f"delete_popup_annotations(): popup annotation id = '{annotation.id}' for '{annotation.contents}' deleted in the document '{Config.PDF_DOCUMENT_NAME}'.")
					else:
						logging.error(f"delete_popup_annotations(): Failed to delete popup annotation in the document. Response code: {response.code}")
