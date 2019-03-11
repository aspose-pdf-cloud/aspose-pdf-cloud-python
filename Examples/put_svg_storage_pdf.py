from configuration import *
file_name = 'Simple.svg'
uploadFile(file_name)
result_name = 'fromSvg.pdf'

src_path = temp_folder + '/' + file_name
opts = {
    "dst_folder": temp_folder
}
response = pdf_api.put_svg_in_storage_to_pdf(
    result_name, src_path, **opts)

pprint(response)