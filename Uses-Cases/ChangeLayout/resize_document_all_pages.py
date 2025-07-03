import os
import logging
from pathlib import Path
from asposepdfcloud import PdfApi, AsposeResponse, HtmlDocumentType, OutputFormat
from change_layout_helper import PdfChangeLayoutHelper

class PdfResizePages:
	def __init__(self, pdf_api: PdfApi, helper: PdfChangeLayoutHelper):
		self.pdfApi = pdf_api
		self.helper = helper
		
	def resizeAllPages(self, documentName: str, htmlTempDoc: str, width: int, height: int, outputDocumentName: str, localFolder: Path, tempFolder: str):
		self.helper.uploadFile(documentName, localFolder, tempFolder)
		
		htmlTempPath = os.path.join(tempFolder, htmlTempDoc)
		args = {
			"folder":        tempFolder,
			"document_type": HtmlDocumentType.XHTML,
			"output_format": OutputFormat.FOLDER,
		}
		
		response: AsposeResponse = self.pdfApi.put_pdf_in_storage_to_html(documentName, htmlTempPath, **args)
		if response.code != 200:
			logging.error("resizeAllPages(): Unexpected error in PDF to HTML conversion!")
		else:
			logging.info("resizeAllPages(): Successfully convert PDF to HTML!")

			args2 = {
				"dst_folder":		tempFolder,
				"html_file_name":	htmlTempDoc,
				"height":			height,
				"width":			width,
			}
			
			response: AsposeResponse = self.pdfApi.put_html_in_storage_to_pdf(outputDocumentName, htmlTempPath, **args2)
			if response.code != 200:
				logging.error("resizeAllPages(): Unexpected error in HTML to PDF conversion!")
			else:
				logging.info("resizeAllPages(): Successfully convert HTML tot PDF!")
				self.helper.downloadFile(outputDocumentName, outputDocumentName, localFolder, tempFolder, "resized_")







'''
package main

import (
	"fmt"
	"path/filepath"

	asposepdfcloud "github.com/aspose-pdf-cloud/aspose-pdf-cloud-go/v25"
)

func resizeAllPages(pdf_api *asposepdfcloud.PdfApiService, document_name string, htmlTempDoc string, width int, height int, outputDocument string, localFolder string, tempFolder string) {
	uploadFile(pdf_api, document_name)

	htmlTempPath := filepath.Join(tempFolder, htmlTempDoc)

	args := map[string]interface{}{
		"folder":        tempFolder,
		"documentType":  string(asposepdfcloud.HtmlDocumentTypeXhtml),
		"outpputFormat": string(asposepdfcloud.OutputFormatFolder),
	}

	_, response, err := pdf_api.PutPdfInStorageToHtml(document_name, htmlTempPath, args)

	if err != nil {
		fmt.Println(err.Error())
	} else if response.StatusCode < 200 || response.StatusCode > 299 {
		fmt.Println("resizePages(): Can't convert pdf to html!")
	} else {
		fmt.Println("resizePages(): temporary file '" + htmlTempDoc + "' succesfully creaated.")
	}

	args2 := map[string]interface{}{
		"folder":       tempFolder,
		"htmlFileName": htmlTempDoc,
		"height":       float64(height),
		"width":        float64(width),
	}

	_, response, err = pdf_api.PutHtmlInStorageToPdf(outputDocument, htmlTempPath, args2)
	if err != nil {
		fmt.Println(err.Error())
	} else if response.StatusCode < 200 || response.StatusCode > 299 {
		fmt.Println("resizePages(): Can't convert html to pdf!")
	} else {
		fmt.Println("resizePages(): Pages successfully resized.")
		downloadFile(pdf_api, outputDocument, "resized_doc_")
	}
}
'''