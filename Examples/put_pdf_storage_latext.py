from configuration import *
file_name = '4pages.pdf'
uploadFile(file_name)
result_file_name = "result.latex"

opts = {
    "folder": temp_folder
}

response = pdf_api.put_pdf_in_storage_to_la_te_x(
    file_name, temp_folder + '/' + result_file_name, **opts)

pprint(response)
