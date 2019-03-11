from configuration import *
file_name = '4pages.pdf'
uploadFile(file_name)

opts = {
    "folder": temp_folder
}

response = pdf_api.get_pdf_in_storage_to_xps(file_name, **opts)

pprint(response)
