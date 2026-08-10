import os
import logging
from pathlib import Path
from acroforms_helper import Config, PdfAcroformsHelper, logging
from asposepdfcloud import ApiClient, PdfApi, TextBoxField, Rectangle, Border, Dash

class PdfAcroformsAdd:
	""" Class for adding form field to PDF document"""
    def __init__(self, pdf_api: PdfApi, helper: PdfAcroformsHelper):
        self.pdfApi = pdf_api
        self.helper = helper

    def addField(self, documentName: str, outputDocumentName: str, localFolder: Path, remoteFolder: str):
        self.helper.uploadFile(documentName, localFolder, remoteFolder)

        textBox = TextBoxField(
            page_index=1,
            partial_name= "EMail",
		    rect=        Rectangle(llx=100, lly=100, urx=180, ury=120),
		    value=      "aspose-pdf-cloud@example.com",
		    border=     Border(
			    width=5,
			    dash=Dash(on=1, off=1)
            )
        )
        try:
            response = self.pdfApi.put_text_box_field(documentName, "EMail", textBox, folder=remoteFolder)
            if response.code == 200:
                logging.info("PdfAcroformsAdd(): Form filed 'Email' successfully added to the page #1.")
                self.helper.downloadFile(documentName, outputDocumentName, localFolder, remoteFolder, "add_form_")
            else:
                logging.error(f"PdfAcroformsAdd(): Failed to add filed 'Email' to the page #1. Response code: {response.code}")
        except Exception as e:

            logging.error(f"PdfAcroformsAdd(): Error while adding form field: {e}")

