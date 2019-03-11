from configuration import *
file_name = 'MhtExample.mht'
uploadFile(file_name)
result_name = 'fromMht.pdf'

src_path = temp_folder + '/' + file_name
opts = {
    "dst_folder": temp_folder
}
response = pdf_api.put_mht_in_storage_to_pdf(
    result_name, src_path, **opts)

pprint(response)