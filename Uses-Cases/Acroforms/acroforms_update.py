import os
import logging
from pathlib import Path
from acroforms_helper import Config, PdfAcroformsHelper, logging
from asposepdfcloud import ApiClient, PdfApi, Field, Fields, FieldType, Rectangle

class PdfAcroformsUpdate:
    def __init__(self, pdf_api: PdfApi, helper: PdfAcroformsHelper):
        self.pdfApi = pdf_api
        self.helper = helper

    def updField(self, documentName: str, outputDocumentName: str, fieldName: str, localFolder: Path, remoteFolder: str):
        self.helper.uploadFile(documentName, localFolder, remoteFolder)

        field = Field(
            name=fieldName,
            type=FieldType.TEXT,
            values=["aspose-pdf-cloud@example.com"],
            rect= Rectangle( llx=125, lly=735, urx=200, ury=752),
        )
        
        fields = Fields(list=[field])

        try:
            response = self.pdfApi.put_update_fields(documentName, fields, folder=remoteFolder)
            if response.code == 200:
                logging.info(f"PdfAcroformsUpdate(): Form filed '{fieldName}' successfully updated in the document.")
                self.helper.downloadFile(documentName, outputDocumentName, localFolder, remoteFolder, "update_form_")
            else:
                logging.error(f"PdfAcroformsUpdate(): Failed to update fileds in the document. Response code: {response.code}")
        except Exception as e:
            logging.error(f"PdfAcroformsUpdate(): Error while updating form field: {e}")