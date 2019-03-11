import asposepdfcloud
from asposepdfcloud.apis.pdf_api import PdfApi
from asposepdfcloud.rest import ApiException
 
from  pprint import pprint

pdf_api_client = asposepdfcloud.api_client.ApiClient("b125f13bf6b76ed81ee990142d841195",
        "78946fb4-3bd4-4d3e-b309-f9e2ff9ac6f9")

temp_folder = ''
test_data_path=''
pdf_api = PdfApi(pdf_api_client)


def uploadFile(name):
        pdf_api.put_create(temp_folder + '/' + name, test_data_path + name)