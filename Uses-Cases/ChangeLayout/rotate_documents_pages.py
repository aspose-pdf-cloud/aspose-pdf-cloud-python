import logging
from pathlib import Path
from asposepdfcloud import PdfApi, AsposeResponse
from change_layout_helper import PdfChangeLayoutHelper, Config

class PdfRotatePages:
	def __init__(self, pdf_api: PdfApi, helper: PdfChangeLayoutHelper):
		self.pdfApi = pdf_api
		self.helper = helper
        
	def rotateDocumentPages(self, documentName: str, outputDocumentName: str, rotateAngle: str, pages: str):
		self.helper.uploadFile(documentName, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)
        
		args = {
			"folder": Config.REMOTE_FOLDER,
		}
        
		response: AsposeResponse = self.pdfApi.post_document_pages_rotate(documentName, rotateAngle, pages, **args)

		if response.code != 200:
			logging.error("rotateDocumentPages(): Unexpected error!")
		else:
			logging.info(f"rotateDocumentPages(): Pages '{pages}' successfully rotated!")
			self.helper.downloadFile(documentName, outputDocumentName, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER, "rotated_")