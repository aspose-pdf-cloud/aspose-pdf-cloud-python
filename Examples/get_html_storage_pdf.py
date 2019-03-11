from configuration import *
file_name = 'HtmlWithImage.zip'
uploadFile(file_name)

html_file_name = 'HtmlWithImage.html'
opts = {
    "height": 650,
    "width": 250,
    "html_file_name": html_file_name
}
src_path = temp_folder + '/' + file_name
response = pdf_api.get_html_in_storage_to_pdf(src_path, **opts)

pprint(response)