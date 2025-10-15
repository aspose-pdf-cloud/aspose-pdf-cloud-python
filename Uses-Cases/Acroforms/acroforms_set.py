import os
import logging
from pathlib import Path
from acroforms_helper import Config, PdfAcroformsHelper, logging
from asposepdfcloud import ApiClient, PdfApi, Field, FieldType

class PdfAcroformsSetter:
    """ Clas for writing form field values to PDF document"""
    def __init__(self, pdf_api: PdfApi, helper: PdfAcroformsHelper):
        self.pdfApi = pdf_api
        self.helper = helper

    def setField(self, documentName: str, outputDocumentName: str, fieldName: str, localFolder: Path, remoteFolder: str):
        self.helper.uploadFile(documentName, localFolder, remoteFolder)

        field = Field(
            name="EMail",
            type=FieldType.TEXT,
            values=["aspose-pdf-cloud@example.com"]
        )
        try:
            response = self.pdfApi.put_update_field(documentName, fieldName, field, folder=remoteFolder)
            if response.code == 200:
                logging.info(f"PdfAcroformsReplace(): Form filed '{fieldName}' successfully updated in the document.")
                self.helper.downloadFile(documentName, outputDocumentName, localFolder, remoteFolder, "set_form_")
            else:
                logging.error(f"PdfAcroformsReplace(): Failed to update filed 'Email' inn the document. Response code: {response.code}")
        except Exception as e:

            logging.error(f"PdfAcroformsReplace(): Error while updating form field: {e}")
