from configuration import *
file_name = 'Simple.svg'
uploadFile(file_name)

src_path = temp_folder + '/' + file_name
response = pdf_api.get_svg_in_storage_to_pdf(src_path)

pprint(response)
