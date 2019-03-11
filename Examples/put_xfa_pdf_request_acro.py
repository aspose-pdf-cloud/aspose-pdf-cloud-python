from configuration import *
file_name = 'PdfWithXfaForm.pdf'
result_file_name = "result.pdf"

opts = {
    "file": test_data_path + file_name
}

response = pdf_api.put_xfa_pdf_in_request_to_acro_form(
    temp_folder + '/' + result_file_name, **opts)


pprint(response)