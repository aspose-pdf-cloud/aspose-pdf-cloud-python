"""
    1. Load your Application Secret and Key from the JSON file or set credentials in another way
    2. Create an object to connect to the Pdf.Cloud API
    3. Initialize parameters (folders and Pdf document) for next actions
    4. Upload Yyour Pdf document file
    5. Upload Your image file 
    6. Initialize image appending parameters (page and position on page)
    7. Perform the appending image into Pdf document using post_insert_image() function
    8. Check result and perform some actions with response object
    
    All values of variables starting with "YOUR_****" should be replaced by real user values
"""

import os
import json

import asposepdfcloud
from asposepdfcloud.apis.pdf_api import PdfApi

def uploadFile(pdf_api, name, temp_folder, data_path):
    pdf_api.upload_file(temp_folder + '/' + name, data_path + name)


json_file = open('YOUR_APPLICATION_CREDENTIALS.json')

data = json.load(json_file)
            
pdf_api_client = asposepdfcloud.api_client.ApiClient(
    app_key=str(data.get('AppKey', '')),
    app_sid=str(data.get('AppSID', '')),
    host=str(data['ProductUri']),
    self_host=bool(data.get('SelfHost', False)),
)

api = PdfApi(pdf_api_client)

output_path = str(data['YOUR_OUTPUT_FOLDER'])
temp_folder = 'YOUR_TEMP_PDF_CLOUD_FOLDER'

file_name = 'YOUR_PDF_DOCUMENT.pdf'

uploadFile(api, file_name, temp_folder, 'YOUR_PDF_DOCUMENT_FOLDER')

image_file_name = 'YOUR_IMAGE_FILE_NAME.YOUR_EXTENSION'
uploadFile(api, file_name, temp_folder, 'YOUR_IMAGE_FILE_FOLDER')

# Replace values with Your datas
page_number = 1
llx = 10
lly = 10
urx = 100
ury = 100

opts = {
    "image_file_path" : temp_folder + "/" + image_file_name,
    "folder" : temp_folder
}

response = api.post_insert_image(file_name, page_number, llx, lly, urx, ury, **opts)

print (response)