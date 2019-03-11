from configuration import *
file_name = 'PdfWithImages2.pdf'
append_file_name = '4pages.pdf'

uploadFile(file_name)
uploadFile(append_file_name)

append_document = asposepdfcloud.models.AppendDocument(
    temp_folder + '/' + append_file_name, start_page=2, end_page=4)

opts = {
    "append_document": append_document,
    "folder": temp_folder
}

response = pdf_api.post_append_document(file_name, **opts)

pprint(response)
