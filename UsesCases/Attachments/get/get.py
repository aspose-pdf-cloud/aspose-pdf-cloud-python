"""
    1. Import required libraries
    2. Define callback functiions for read attachments from Pdf file and append new attachment into this Pdf file
    3. Initialize credentials for calling Pdf.Cloud.Python REST API functions
    4. Create Pdf.Cloud.Python REST API object
    5. Initialize Pdf ile name and attachment index
    6. Perform reading attachments from Pdf file using get_document_attachment_by_index() function
    
    All values of variables starting with "YOUR_****" should be replaced by real user values
"""

import asposepdfcloud

pdf_api_client = asposepdfcloud.ApiClient("YOUR_APP_KEY", "YOUR_APP_SECRET")
api = asposepdfcloud.PdfApi(pdf_api_client)

document_name = "C:/Samples/Sample-Document-01.pdf"
storage_file_name = "Sample-Document-01.pdf"

def uploadFile(name, storage):
    upload_result = api.upload_file(storage, name)
    print(upload_result.status)
    print(upload_result.uploaded[0])

def show_attachments(response):
    print("Attachments received successfully : \n List : ", response.list)

    for attach in response.list:
        print("Attachment was successfully added : \n Links : ", attach.links)
        print("\n Description : ", attach.description)
        print("\n MIME Type : ", attach.mime_type)
        print("\n Name : ", attach.name)
        print("\n Creation Date : ", attach.creation_date)
        print("\n Modification date : ", attach.modification_date)
        print("\n Size : ", attach.size)
        print("\n Check Sum : ", attach.check_sum)


uploadFile(document_name, storage_file_name)

api.get_document_attachments(document_name, callback=show_attachments)