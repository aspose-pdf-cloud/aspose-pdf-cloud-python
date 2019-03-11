from configuration import *
url = 'http://google.com'

response =pdf_api.get_web_in_storage_to_pdf(url)


pprint(response)