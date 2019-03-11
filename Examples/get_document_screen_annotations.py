from configuration import *

file_name = 'PdfWithScreenAnnotations.pdf'
uploadFile(file_name)

response = pdf_api.get_document_screen_annotations(
    file_name, folder=temp_folder)


pprint(response)
