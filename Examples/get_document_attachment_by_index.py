from configuration import *
file_name = 'PdfWithEmbeddedFiles.pdf'
uploadFile(file_name)

attachment_index = 1
opts = {
    "folder": temp_folder
}

response = pdf_api.get_document_attachment_by_index(
    file_name, attachment_index, **opts)

pprint(response)
