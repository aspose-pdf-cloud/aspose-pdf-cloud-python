from configuration import *
file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

page_number = 2

response = pdf_api.get_page_strike_out_annotations(
    file_name, page_number, folder=temp_folder)

pprint(response)
