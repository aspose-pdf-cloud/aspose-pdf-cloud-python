from configuration import *
file_name = 'PdfWithXfaForm.pdf'
uploadFile(file_name)

opts = {
    "folder": temp_folder
}

response = pdf_api.get_xfa_pdf_in_storage_to_acro_form(file_name, **opts)

pprint(response)
