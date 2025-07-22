import os
import logging
from pathlib import Path
from asposepdfcloud import PdfApi, AsposeResponse, DocumentResponse
from change_layout_helper import PdfChangeLayoutHelper, Config

class PdfCropPages:
	def __init__(self, pdf_api: PdfApi, helper: PdfChangeLayoutHelper):
		self.pdfApi = pdf_api
		self.helper = helper

	def cropDocumentPage(self, documentName: str, pageNumber: int, llx: int, lly: int, width: int, height: int, outputDocument: str, localFolder: str, tempFolder: str):
		self.helper.uploadFile(documentName, localFolder, tempFolder)

		self.helper.getPageInfo(documentName, pageNumber, tempFolder)

		imageFile = self.helper.extractPdfPage(documentName, pageNumber, Config.CROP_PAGE_WIDTH, Config.CROP_PAGE_HEIGHT, localFolder, tempFolder)
		newPdf: DocumentResponse = self.helper.createDocument(outputDocument, width, height, tempFolder)
		if newPdf.code != 200:
			logging.error("cropDocumentPage(): Failed to create new PDF document!")
		else:
			response: AsposeResponse = self.helper.insertPageAsImage(outputDocument, imageFile, llx, lly, tempFolder)
			if response.code != 200:
				logging.error("cropDocumentPage(): Can't crop pdf document page!")
			else:
				logging.info("cropDocumentPage(): Page successfully cropped.")
				self.helper.downloadFile(outputDocument, outputDocument, localFolder, tempFolder, "cropped_")