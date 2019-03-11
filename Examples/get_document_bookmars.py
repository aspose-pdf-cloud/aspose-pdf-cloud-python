from configuration import *
file_name = 'PdfWithBookmarks.pdf'
uploadFile(file_name)
opts = {
    "folder": temp_folder
}

response = pdf_api.get_document_bookmarks(file_name, **opts)

pprint(response)
