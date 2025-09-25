from paresr_helpers import ParesrHelper
from pathlib import Path
import json
import logging

class GetTables:
    """Class for extracting tables from PDF document using Aspose PDF Cloud API."""
    def __init__(self, helper: ParesrHelper):
        self.helper = helper

    def Extract(self, documentName: str, localFolder: Path, remoteFolder: Path):
        self.helper.upload_document(documentName, remoteFolder)

        opts = {
            "folder": remoteFolder
        }
        respTables = self.helper.pdf_api.get_document_tables(documentName, **opts)
        if respTables.code != 200:
            logging.error("GetTables(): Unexpected error!")
        else:
            localJson = Path.joinpath(localFolder, "tables_objects.json")
            with open(str(localJson), "w", encoding="utf-8") as localFile:
                for tab in respTables.tables.list:
                    response = self.helper.pdf_api.get_table(documentName, tab.id, **opts)
                    if response.code != 200:
                        logging.error("GetTextBoxes(): Unexpected error!")
                    else:
                        logging.info(f"GetTabels(): Table '{tab.id}' successfully extracted from the document '{documentName}'.")
                        json.dump(tab, localFile, ensure_ascii=False,default=str)
                        localFile.write("\n*********************\n")