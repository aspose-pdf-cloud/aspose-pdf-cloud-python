# Aspose.Pdf for Cloud
[Aspose.Pdf for Cloud](https://products.aspose.cloud/pdf/cloud) is a true REST API that enables you to perform a wide range of document processing operations including creation, manipulation, conversion and rendering of Pdf documents in the cloud.

Our Cloud SDKs are wrappers around REST API in various programming languages, allowing you to process documents in language of your choice quickly and easily, gaining all benefits of strong types and IDE highlights. This repository contains new generation SDKs for Aspose.Pdf for Cloud and examples.

These SDKs are now fully supported. If you have any questions, see any bugs or have enhancement request, feel free to reach out to us at [Free Support Forums](https://forum.aspose.cloud/c/pdf).

## Usage
APIs of this SDK can be called as follows:

```python
from __future__ import absolute_import

import os
import sys

import asposepdfcloud
from asposepdfcloud.apis.pdf_api import PdfApi
from asposepdfcloud.rest import ApiException
from asposepdfcloud.models.annotation_response import AnnotationResponse

class SdkUsage(object):

    def __init__(self):
      # Get App key and App SID from https://cloud.aspose.com
      self.pdf_api_client = asposepdfcloud.api_client.ApiClient(
          app_key='app_key',
          app_sid='app_sid')

      self.pdf_api = PdfApi(self.pdf_api_client)
      self.output_path = str('output_location_path')
      self.temp_folder = 'TempPdf'

    def getPageAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        page_number = 2
        response = self.pdf_api.get_page_annotations(file_name, page_number, folder=self.temp_folder)
        
```
## Unit Tests
Aspose PDF SDK includes a suite of unit tests within the "test" subdirectory. These Unit Tests also serves as examples of how to use the Aspose PDF SDK.

## Licensing
All Aspose.Pdf for Cloud SDKs are licensed under [MIT License](LICENSE).

## Resources
+ [**Website**](https://www.aspose.cloud)
+ [**Product Home**](https://products.aspose.cloud/pdf/cloud)
+ [**Documentation**](https://docs.aspose.cloud/display/pdfcloud/Home)
+ [**Free Support Forum**](https://forum.aspose.cloud/c/pdf)
+ [**Paid Support Helpdesk**](https://helpdesk.aspose.cloud/)
+ [**Blog**](https://blog.aspose.cloud/category/aspose-products/aspose-pdf-product-family/)
