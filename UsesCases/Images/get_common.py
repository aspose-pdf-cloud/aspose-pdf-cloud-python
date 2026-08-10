"""
    1. Load your Application Secret and Key from the JSON file or set credentials in another way
    2. Create an object to connect to the Pdf.Cloud API
    3. Initialize parameters (folders and Pdf document) for next actions
    4. Upload your Pdf document file
    5. Perform the retreiving image Id from Pdf document using get_images() function
    6. Perform the reading image from Pdf document using get_image() function and image Id value
    7. Parse response for upload image into temporary folder 
    8. Initialize second Pdf document for inserting uploaded image from first Pdf document
    9. Perform the retreiving image Id from second Pdf document using get_images() function
    10. Initialize parameters for replace image in second Pdf document
    11. Perform replacing image actiont using put_replace_image() function
    12. Check result and perform some actions with response object
    
    All values of variables starting with "YOUR_****" should be replaced by real user values
"""

import os
import shutil
import asposepdfcloud

from urllib.parse import urlparse

pdf_api_client = asposepdfcloud.ApiClient("YOUR_APP_KEY", "YOUR_APP_SECRET")
api = asposepdfcloud.PdfApi(pdf_api_client)

temp_folder = 'TempPdfCloud'
data_path = "C:/Samples/"
output_path = "C:/Samples/Output"

document_name = "Sample-Document-01.pdf"
document_name2 = "Sample-Document-02.pdf"

page_number = 1
def uploadFile(name):
    api.upload_file(temp_folder + '/' + name, data_path + name)

uploadFile(document_name)
uploadFile(document_name2)

opts = {
    "folder" : temp_folder
}

responseImages = api.get_images(document_name, page_number, **opts)

image_id = responseImages.images.list[0].id

responseImage = api.get_image(document_name, image_id)

print (responseImage)

file_name_link = responseImage.image.links[0].href

a = urlparse(file_name_link)
image_file_name = os.path.basename(a.path)
image_file_path = temp_folder +"/" + image_file_name

resImage = api.download_file(file_name_link)
shutil.move(resImage, image_file_path)

uploadFile(api, image_file_path, image_file_name)

opts = {
    "image_file_path" : self.temp_folder + '/' + image_file_name,
              "folder" : self.temp_folder
        }
        response = self.pdf_api.put_replace_image(file_name, image_id, **opts)

response = api.put_replace_image(file_name2, image_id2, **opts)

print (response)