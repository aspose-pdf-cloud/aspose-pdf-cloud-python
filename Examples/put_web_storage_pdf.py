from configuration import *
url = 'http://google.com'
result_name = 'fromWeb.pdf'

opts = {
    "dst_folder": temp_folder
}
response =pdf_api.put_web_in_storage_to_pdf(
    result_name, url, **opts)

pprint(response)