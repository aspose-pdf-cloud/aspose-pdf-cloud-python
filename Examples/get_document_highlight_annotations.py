from configuration import *
file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

response = pdf_api.get_document_highlight_annotations(
    file_name, folder=temp_folder)

pprint(response)
