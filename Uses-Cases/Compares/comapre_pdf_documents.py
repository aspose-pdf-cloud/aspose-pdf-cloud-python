import logging
from pathlib import Path
from asposepdfcloud import PdfApi
from compares_helper import CompareMain

class Config:
    """Configuration parameters."""
    CREDENTIALS_FILE = Path(r"C:\\Projects\\ASPOSE\\Pdf.Cloud\\Credentials\\credentials.json")
    LOCAL_FOLDER = Path(r"C:\Samples")
    REMOTE_FOLDER  = "Your_Temp_Pdf_Cloud"
    PDF_DOCUMENT_1 = "sample_compare_1.pdf"
    PDF_DOCUMENT_2 = "sample_compare_2.pdf"
    PDF_OUTPUT     = "output_compare.pdf"

class ComparePdfDocuments:
	def __init__(self, pdf_api: PdfApi, compare_main: CompareMain):
		self.pdfApi = pdf_api
		self.compareMain = compare_main

	def compareDocument(self):
		self.compareMain.upload_file(Config.PDF_DOCUMENT_1, Config.LOCAL_FOLDER)
		self.compareMain.upload_file(Config.PDF_DOCUMENT_2, Config.LOCAL_FOLDER)
		try:
			response = self.pdfApi.post_compare_pdf(Config.PDF_DOCUMENT_1, Config.PDF_DOCUMENT_2, Config.PDF_OUTPUT)
			if response.code == 200:
				logging.info(f"compareDocument(): Succsessfully compared.")
				self.compareMain.download_result(Config.PDF_OUTPUT, Config.PDF_OUTPUT, Config.LOCAL_FOLDER)
			else:
				logging.error(f"compareDocument(): Failed to compare Pdf documents! Response code: {response.code}")
		except Exception as e:
			logging.error(f"compareDocument(): Error while comparing Pdf documents: {e}")