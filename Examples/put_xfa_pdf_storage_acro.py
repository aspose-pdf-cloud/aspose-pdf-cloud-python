from configuration import *
file_name = 'PdfWithXfaForm.pdf'
uploadFile(file_name)
result_file_name = "result.pdf"

opts = {
    "folder": temp_folder
}

response = pdf_api.put_xfa_pdf_in_storage_to_acro_form(
    file_name, temp_folder + '/' + result_file_name, **opts)

pprint(response)
