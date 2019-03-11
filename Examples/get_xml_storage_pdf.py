from configuration import *
file_name = 'template.xml'
uploadFile(file_name)

src_path = temp_folder + '/' + file_name
response = pdf_api.get_xml_in_storage_to_pdf(src_path)

pprint(response)
