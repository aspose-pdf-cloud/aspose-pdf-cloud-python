from configuration import *

file_name = 'PdfWithAnnotations1.pdf'
uploadFile(file_name)

response = pdf_api.get_document_movie_annotations(
    file_name, folder=temp_folder)

pprint(response)