from paresr_helpers import ParesrHelper
from pathlib import Path
import logging

class ExportFormToFDF:
    """Class for extracting PDF form fields into FDF using Aspose PDF Cloud API."""
    def __init__(self, helper: ParesrHelper):
        self.helper = helper

    def Extract(self, documentName: str, outputFDFName: str, localFolder: Path, remoteFolder: str ):
        self.helper.upload_document(documentName, remoteFolder)

        fdfPath = str(Path.joinpath(Path(remoteFolder), outputFDFName))
        opts = {
            "folder": remoteFolder
        }
        response = self.helper.pdf_api.put_export_fields_from_pdf_to_fdf_in_storage(documentName, fdfPath, **opts)
        if response.code != 200:
            logging.error("ExportFormToFDF(): Unexpected error!")
        else:
            logging.info(f"ExportFormToFDF(): Pdf document '{documentName}' form fields successfully exported to '{outputFDFName}' file.")
            self.helper.downloadFile(outputFDFName, outputFDFName, localFolder, remoteFolder, "")