from paresr_helpers import ParesrHelper
from pathlib import Path
import json
import logging

class GetTextBoxes:
    """Class for extracting text boxes from PDF document using Aspose PDF Cloud API."""
    def __init__(self, helper: ParesrHelper):
        self.helper = helper

    def Extract(self, documentName: str, localFolder: Path, remoteFolder: Path):
        self.helper.upload_document(documentName, remoteFolder)

        opts = {
            "folder": remoteFolder
        }
        respTextBoxes = self.helper.pdf_api.get_document_text_box_fields(documentName, **opts)
        if respTextBoxes.code != 200:
            logging.error("GetTextBoxes(): Unexpected error!")
        else:
            localJson = Path.joinpath(localFolder, "text_box_objects.json")
            with open(str(localJson), "w", encoding="utf-8") as localFile:
                for textBox in respTextBoxes.fields.list:
                    response = self.helper.pdf_api.get_text_box_field(documentName, textBox.full_name, **opts)
                    if response.code != 200:
                        logging.error("GetTextBoxes(): Unexpected error!")
                    else:
                        logging.info(f"GetTextBoxes(): TextBox field '{textBox.full_name}' successfully extracted from the document '{documentName}'.")
                        json.dump(textBox, localFile, ensure_ascii=False,default=str)
                        localFile.write("\n*********************\n")