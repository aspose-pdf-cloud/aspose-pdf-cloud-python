from configuration import *

file_name = '4pages.pdf'
result_file_name = "result.tiff"

opts = {
    "file": test_data_path + file_name
}

response = pdf_api.put_pdf_in_request_to_tiff(
    temp_folder + '/' + result_file_name, **opts)

pprint(response)
