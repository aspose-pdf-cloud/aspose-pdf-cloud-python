import os
import logging
from pathlib import Path
from acroforms_helper import Config, PdfAcroformsHelper, logging
from asposepdfcloud import ApiClient, PdfApi, FieldsResponse, Field

class PdfAcroformsGet:
    def __init__(self, pdf_api: PdfApi, helper: PdfAcroformsHelper):
        self.pdfApi = pdf_api
        self.helper = helper

    def getField(self, documentName: str, localFolder: Path, remoteFolder: str):
        self.helper.uploadFile(documentName, localFolder, remoteFolder)

        try:
            response: FieldsResponse = self.pdfApi.get_fields(documentName, folder=remoteFolder)
            if response.code == 200:
                for field in response.fields.list:
                    logging.info(f"PdfAcroformsGet(): Form filed '{field}'.")
            else:
                logging.error(f"PdfAcroformsGet(): Failed to get form fileds from document. Response code: {response.code}")
        except Exception as e:
            logging.error(f"PdfAcroformsGet(): Error while extracting form field: {e}")