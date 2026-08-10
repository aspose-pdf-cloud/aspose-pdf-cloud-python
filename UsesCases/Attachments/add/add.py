"""
    1. Import required libraries
    2. Define callback functiions for append new attachment into this Pdf file
    3. Initialize credentials for calling Pdf.Cloud.Python REST API functions
    4. Create Pdf.Cloud.Python REST API object
    5. Initialize new AttachmentInfo object
    6. Perform appending attachment into Pdf file using post_add_document_attachment() function
    
    All values of variables starting with "YOUR_****" should be replaced by real user values
"""

import asposepdfcloud
from asposepdfcloud.models import AttachmentInfo

pdf_api_client = asposepdfcloud.ApiClient("YOUR_APP_KEY", "YOUR_APP_SECRET")
api = asposepdfcloud.PdfApi(pdf_api_client)

document_name = "C:/Samples/Sample-Document-01.pdf"
storage_file_name = "Sample-Document-01.pdf"

new_attachment_file = "C:/Samples/Sample-Attachment-Image.png"
new_attachment_mime = "image/png"

attachment_info = AttachmentInfo(
    name=new_attachment_file,
    mime_type=new_attachment_mime
)

def uploadFile(name, storage):
    upload_result = api.upload_file(storage, name)
    print(upload_result.status)
    print(upload_result.uploaded[0])

def show_attachment(response):
    print("Attachment was successfully added : \n Links : ", response.links)
    print("\n Description : ", response.description)
    print("\n MIME Type : ", response.mime_type)
    print("\n Name : ", response.name)
    print("\n Creation Date : ", response.creation_date)
    print("\n Modification date : ", response.modification_date)
    print("\n Size : ", response.size)

uploadFile(document_name, storage_file_name)

api.post_add_document_attachment(document_name, attachment_info, callback=show_attachment)