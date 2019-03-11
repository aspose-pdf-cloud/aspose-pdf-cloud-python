from configuration import *
file_name = 'HtmlWithImage.zip'
uploadFile(file_name)
html_file_name = 'HtmlWithImage.html'

result_name = 'fromMht.pdf'

src_path = temp_folder + '/' + file_name
opts = {
    "dst_folder": temp_folder,
    "height": 650,
    "width": 250,
    "html_file_name": html_file_name
}
response = pdf_api.put_html_in_storage_to_pdf(
    result_name, src_path, **opts)

pprint(response)
