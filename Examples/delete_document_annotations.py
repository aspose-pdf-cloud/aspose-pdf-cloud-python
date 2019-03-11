from configuration import *

file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)
response = pdf_api.delete_document_annotations(file_name, folder=temp_folder)
pprint(response)