import os
import logging
from pathlib import Path
from acroforms_helper import Config, PdfAcroformsHelper, logging
from asposepdfcloud import ApiClient, PdfApi, TextBoxField, Rectangle, Border, Dash

class PdfAcroformsDel:
    """ Class for deleting form field from PDF document"""
    def __init__(self, pdf_api: PdfApi, helper: PdfAcroformsHelper):
        self.pdfApi = pdf_api
        self.helper = helper

    def delField(self, documentName: str, outputDocumentName: str, fieldName: str, localFolder: Path, remoteFolder: str):
        self.helper.uploadFile(documentName, localFolder, remoteFolder)

        try:
            response = self.pdfApi.delete_field(documentName, fieldName, folder=remoteFolder)
            if response.code == 200:
                logging.info(f"PdfAcroformsDel(): Form filed '{fieldName}' successfully deleted from docuemnt.")
                self.helper.downloadFile(documentName, outputDocumentName, localFolder, remoteFolder, "del_form_")
            else:
                logging.error(f"PdfAcroformsDel(): Failed to reomve filed '{fieldName}' from document. Response code: {response.code}")
        except Exception as e:

            logging.error(f"PdfAcroformsDel(): Error while deleting form field: {e}")

