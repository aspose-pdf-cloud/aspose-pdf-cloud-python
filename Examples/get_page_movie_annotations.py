from configuration import *

file_name = 'PdfWithAnnotations1.pdf'
uploadFile(file_name)

page_number = 2

response = pdf_api.get_page_movie_annotations(
    file_name, page_number, folder=temp_folder)

pprint(response)
