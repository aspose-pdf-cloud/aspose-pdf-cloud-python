from configuration import *
file_name = 'PdfWithEmbeddedFiles.pdf'
uploadFile(file_name)

opts = {
    "folder": temp_folder
}

response = pdf_api.get_document_attachments(file_name, **opts)

pprint(response)
