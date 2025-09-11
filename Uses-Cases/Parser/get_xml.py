from paresr_helpers import ParesrHelper, Config
from pathlib import Path
import logging

class ExportFormToXXML:
    """Class for extracting PDF form fields into XML using Aspose PDF Cloud API."""
    def __init__(self, helper: ParesrHelper):
        self.helper = helper

    def Extract(self, documentName: str, outputXMLName: str, localFolder: Path, remoteFolder: str ):
        self.helper.upload_document(documentName, remoteFolder)

        xmlPath = str(Path.joinpath(Path(remoteFolder), outputXMLName))
        opts = {
            "folder": remoteFolder
        }
        response = self.helper.pdf_api.put_export_fields_from_pdf_to_xml_in_storage(documentName, xmlPath, **opts)
        if response.code != 200:
            logging.error("ExportFormToXM(): Unexpected error!")
        else:
            logging.info(f"ExportFormToXML(): Pdf document '{documentName}' form fields successfully exported to '{outputXMLName}' file.")
            self.helper.downloadFile(outputXMLName, outputXMLName, localFolder, remoteFolder, "")