from configuration import *
file_name = 'MhtExample.mht'
uploadFile(file_name)

src_path = temp_folder + '/' + file_name
response = pdf_api.get_mht_in_storage_to_pdf(src_path)

pprint(response)