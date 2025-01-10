"""
    1. Load your Application Secret and Key from the JSON file or set credentials in another way
    2. Create an object to connect to the Pdf.Cloud API
    3. Initialize parameters (folders and Pdf document) for next actions
    4. Upload your Pdf document file into temporary folder
    5. Initialize image file name
    6. Upload image file into temporary folder
    7. Initialize options to retreive image Id
    8. Perform the retreiving image Id from Pdf document using get_images() function
    9. Initialize options to update image
    10. Perform the updating image in Pdf document using put_replace_image() function and image Id value
    11. Check result and perform some actions with response object
    
    All values of variables starting with "YOUR_****" should be replaced by real user values
"""

import os
import json

import asposepdfcloud
from asposepdfcloud.apis.pdf_api import PdfApi

from urllib.parse import urlparse

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
uploadFile(api, image_file_name, temp_folder, 'YOUR_IMAGE_FILE_FOLDER')

opts = {
    "folder" : temp_folder
}

page_number = 1 # Replace with Your pade number

responseImages = api.get_images(file_name, page_number, **opts)

image_id = responseImages.images.list[0].id

opts = {
    "image_file_path" : temp_folder + '/' + image_file_name,
    "folder" : temp_folder
}

response = api.put_replace_image(file_name, image_id, **opts)

print (response)