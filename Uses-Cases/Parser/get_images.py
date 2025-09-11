from paresr_helpers import ParesrHelper
from pathlib import Path
import shutil
import logging

class GetImages:
    """Class for extracting images from PDF document page using Aspose PDF Cloud API."""
    def __init__(self, helper: ParesrHelper):
        self.helper = helper

    def Extract(self, documentName: str, pageNumber: int, localFolder: Path, remoteFolder: Path):
        self.helper.upload_document(documentName, remoteFolder)

        opts = {
            "folder": remoteFolder
        }
        respImages = self.helper.pdf_api.get_images(documentName, pageNumber, **opts)
        if respImages.code != 200:
            logging.error("GetImages(): Unexpected error!")
        else:
            for img in respImages.images.list:
                response = self.helper.pdf_api.get_image_extract_as_png(documentName, img.id, **opts)

                logging.info(f"GetImages(): Images '{img.id}' successfully extracted from the document '{documentName}'.")
                local_path = localFolder / ( img.id + '.png' )
                shutil.move(response, str(local_path))