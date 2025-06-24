import os
import shutil
import json
import logging
from pathlib import Path
from asposepdfcloud import ApiClient, PdfApi

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class CompareMain:
	def __init__(self, credentials_file: Path):
		self.pdf_api = None
		self._init_api(credentials_file)

	def _init_api(self, credentials_file: Path):
		"""Initialize the API client."""
		try:
			with credentials_file.open("r", encoding="utf-8") as file:
				credentials = json.load(file)
			api_key, app_id = credentials.get("key"), credentials.get("id")
			if not api_key or not app_id:
				raise ValueError("Error: Missing API keys in the credentials file.")
			self.pdf_api = PdfApi(ApiClient(api_key, app_id))
		except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
			logging.error(f"Failed to load credentials: {e}")
	
	def upload_file(self, fileName: str, localFolder: Path):
		""" Upload a local fileName to the Aspose Cloud server. """
		if self.pdf_api:
			file_path = localFolder / fileName
			try:
				self.pdf_api.upload_file(fileName, str(file_path))
				logging.info(f"upload_file(): File '{fileName}' uploaded successfully.")
			except Exception as e:
				logging.error(f"upload_document(): Failed to upload file: {e}")

	def download_result(self, document: str, outputDocument: str, localFolder: Path):
		"""Download the processed PDF document from the Aspose Cloud server."""
		if self.pdf_api:
			try:
				temp_file = self.pdf_api.download_file(document)
				local_path = localFolder / outputDocument
				shutil.move(temp_file, str(local_path))
				logging.info(f"download_result(): File successfully downloaded: {local_path}")
			except Exception as e:
				logging.error(f"download_result(): Failed to download file: {e}")
