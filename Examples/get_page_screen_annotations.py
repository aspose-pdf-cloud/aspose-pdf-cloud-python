from configuration import *

file_name = 'PdfWithScreenAnnotations.pdf'
uploadFile(file_name)

page_number = 1

response = pdf_api.get_page_screen_annotations(
    file_name, page_number, folder=temp_folder)

pprint(response)