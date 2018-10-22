# Aspose.PDF Cloud
- API version: 2.0
- Package version: 18.9.0

[Aspose.PDF Cloud](https://products.aspose.cloud/pdf) is a true REST API that enables you to perform a wide range of document processing operations including creation, manipulation, conversion and rendering of Pdf documents in the cloud.

Our Cloud SDKs are wrappers around REST API in various programming languages, allowing you to process documents in language of your choice quickly and easily, gaining all benefits of strong types and IDE highlights. This repository contains new generation SDKs for Aspose.PDF Cloud and examples.

These SDKs are now fully supported. If you have any questions, see any bugs or have enhancement request, feel free to reach out to us at [Free Support Forums](https://forum.aspose.cloud/c/pdf).

## Requirements.

Python 2.7 and 3.4+


## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/aspose-pdf-cloud/aspose-pdf-cloud-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/aspose-pdf-cloud/aspose-pdf-cloud-python.git`)

Then import the package:
```python
import asposepdfcloud
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import asposepdfcloud
```

### Usage
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
All Aspose.PDF Cloud SDKs are licensed under [MIT License](LICENSE).

## Resources
+ [**Website**](https://www.aspose.cloud)
+ [**Product Home**](https://products.aspose.cloud/pdf/cloud)
+ [**Documentation**](https://docs.aspose.cloud/display/pdfcloud/Home)
+ [**Free Support Forum**](https://forum.aspose.cloud/c/pdf)
+ [**Paid Support Helpdesk**](https://helpdesk.aspose.cloud/)
+ [**Blog**](https://blog.aspose.cloud/category/aspose-products/aspose-pdf-product-family/)


## Documentation for API Endpoints

All URIs are relative to *https://api.aspose.cloud/v2.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PdfApi* | [**delete_annotation**](docs/PdfApi.md#delete_annotation) | **DELETE** /pdf/\{name}/annotations/\{annotationId} | Delete document annotation by ID
*PdfApi* | [**delete_document_annotations**](docs/PdfApi.md#delete_document_annotations) | **DELETE** /pdf/\{name}/annotations | Delete all annotations from the document
*PdfApi* | [**delete_document_link_annotations**](docs/PdfApi.md#delete_document_link_annotations) | **DELETE** /pdf/\{name}/links | Delete all link annotations from the document
*PdfApi* | [**delete_field**](docs/PdfApi.md#delete_field) | **DELETE** /pdf/\{name}/fields/\{fieldName} | Delete document field by name.
*PdfApi* | [**delete_image**](docs/PdfApi.md#delete_image) | **DELETE** /pdf/\{name}/images/\{imageId} | Delete image from document page.
*PdfApi* | [**delete_link_annotation**](docs/PdfApi.md#delete_link_annotation) | **DELETE** /pdf/\{name}/links/\{linkId} | Delete document page link annotation by ID
*PdfApi* | [**delete_page**](docs/PdfApi.md#delete_page) | **DELETE** /pdf/\{name}/pages/\{pageNumber} | Delete document page by its number.
*PdfApi* | [**delete_page_annotations**](docs/PdfApi.md#delete_page_annotations) | **DELETE** /pdf/\{name}/pages/\{pageNumber}/annotations | Delete all annotations from the page
*PdfApi* | [**delete_page_link_annotations**](docs/PdfApi.md#delete_page_link_annotations) | **DELETE** /pdf/\{name}/pages/\{pageNumber}/links | Delete all link annotations from the page
*PdfApi* | [**delete_properties**](docs/PdfApi.md#delete_properties) | **DELETE** /pdf/\{name}/documentproperties | Delete custom document properties.
*PdfApi* | [**delete_property**](docs/PdfApi.md#delete_property) | **DELETE** /pdf/\{name}/documentproperties/\{propertyName} | Delete document property.
*PdfApi* | [**get_document**](docs/PdfApi.md#get_document) | **GET** /pdf/\{name} | Read common document info.
*PdfApi* | [**get_document_annotations**](docs/PdfApi.md#get_document_annotations) | **GET** /pdf/\{name}/annotations | Read documant page annotations. Returns only FreeTextAnnotations, TextAnnotations, other annotations will implemented next releases.
*PdfApi* | [**get_document_attachment_by_index**](docs/PdfApi.md#get_document_attachment_by_index) | **GET** /pdf/\{name}/attachments/\{attachmentIndex} | Read document attachment info by its index.
*PdfApi* | [**get_document_attachments**](docs/PdfApi.md#get_document_attachments) | **GET** /pdf/\{name}/attachments | Read document attachments info.
*PdfApi* | [**get_document_bookmarks**](docs/PdfApi.md#get_document_bookmarks) | **GET** /pdf/\{name}/bookmarks | Read document bookmark/bookmarks (including children).
*PdfApi* | [**get_document_free_text_annotations**](docs/PdfApi.md#get_document_free_text_annotations) | **GET** /pdf/\{name}/annotations/freetext | Read document free text annotations.
*PdfApi* | [**get_document_properties**](docs/PdfApi.md#get_document_properties) | **GET** /pdf/\{name}/documentproperties | Read document properties.
*PdfApi* | [**get_document_property**](docs/PdfApi.md#get_document_property) | **GET** /pdf/\{name}/documentproperties/\{propertyName} | Read document property by name.
*PdfApi* | [**get_document_text_annotations**](docs/PdfApi.md#get_document_text_annotations) | **GET** /pdf/\{name}/annotations/text | Read document text annotations.
*PdfApi* | [**get_download**](docs/PdfApi.md#get_download) | **GET** /storage/file | Download a specific file 
*PdfApi* | [**get_download_document_attachment_by_index**](docs/PdfApi.md#get_download_document_attachment_by_index) | **GET** /pdf/\{name}/attachments/\{attachmentIndex}/download | Download document attachment content by its index.
*PdfApi* | [**get_epub_in_storage_to_pdf**](docs/PdfApi.md#get_epub_in_storage_to_pdf) | **GET** /pdf/create/epub | Convert EPUB file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_field**](docs/PdfApi.md#get_field) | **GET** /pdf/\{name}/fields/\{fieldName} | Get document field by name.
*PdfApi* | [**get_fields**](docs/PdfApi.md#get_fields) | **GET** /pdf/\{name}/fields | Get document fields.
*PdfApi* | [**get_free_text_annotation**](docs/PdfApi.md#get_free_text_annotation) | **GET** /pdf/\{name}/annotations/freetext/\{annotationId} | Read document page free text annotation by ID.
*PdfApi* | [**get_html_in_storage_to_pdf**](docs/PdfApi.md#get_html_in_storage_to_pdf) | **GET** /pdf/create/html | Convert HTML file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_image**](docs/PdfApi.md#get_image) | **GET** /pdf/\{name}/images/\{imageId} | Read document image by ID.
*PdfApi* | [**get_image_extract_as_gif**](docs/PdfApi.md#get_image_extract_as_gif) | **GET** /pdf/\{name}/images/\{imageId}/extract/gif | Extract document image in GIF format
*PdfApi* | [**get_image_extract_as_jpeg**](docs/PdfApi.md#get_image_extract_as_jpeg) | **GET** /pdf/\{name}/images/\{imageId}/extract/jpeg | Extract document image in JPEG format
*PdfApi* | [**get_image_extract_as_png**](docs/PdfApi.md#get_image_extract_as_png) | **GET** /pdf/\{name}/images/\{imageId}/extract/png | Extract document image in PNG format
*PdfApi* | [**get_image_extract_as_tiff**](docs/PdfApi.md#get_image_extract_as_tiff) | **GET** /pdf/\{name}/images/\{imageId}/extract/tiff | Extract document image in TIFF format
*PdfApi* | [**get_images**](docs/PdfApi.md#get_images) | **GET** /pdf/\{name}/pages/\{pageNumber}/images | Read document images.
*PdfApi* | [**get_la_te_x_in_storage_to_pdf**](docs/PdfApi.md#get_la_te_x_in_storage_to_pdf) | **GET** /pdf/create/latex | Convert LaTeX file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_link_annotation**](docs/PdfApi.md#get_link_annotation) | **GET** /pdf/\{name}/links/\{linkId} | Read document link annotation by ID.
*PdfApi* | [**get_mht_in_storage_to_pdf**](docs/PdfApi.md#get_mht_in_storage_to_pdf) | **GET** /pdf/create/mht | Convert MHT file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_page**](docs/PdfApi.md#get_page) | **GET** /pdf/\{name}/pages/\{pageNumber} | Read document page info.
*PdfApi* | [**get_page_annotations**](docs/PdfApi.md#get_page_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations | Read documant page annotations. Returns only FreeTextAnnotations, TextAnnotations, other annotations will implemented next releases.
*PdfApi* | [**get_page_convert_to_bmp**](docs/PdfApi.md#get_page_convert_to_bmp) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/bmp | Convert document page to Bmp image and return resulting file in response.
*PdfApi* | [**get_page_convert_to_emf**](docs/PdfApi.md#get_page_convert_to_emf) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/emf | Convert document page to Emf image and return resulting file in response.
*PdfApi* | [**get_page_convert_to_gif**](docs/PdfApi.md#get_page_convert_to_gif) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/gif | Convert document page to Gif image and return resulting file in response.
*PdfApi* | [**get_page_convert_to_jpeg**](docs/PdfApi.md#get_page_convert_to_jpeg) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/jpeg | Convert document page to Jpeg image and return resulting file in response.
*PdfApi* | [**get_page_convert_to_png**](docs/PdfApi.md#get_page_convert_to_png) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/png | Convert document page to Png image and return resulting file in response.
*PdfApi* | [**get_page_convert_to_tiff**](docs/PdfApi.md#get_page_convert_to_tiff) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/tiff | Convert document page to Tiff image  and return resulting file in response.
*PdfApi* | [**get_page_free_text_annotations**](docs/PdfApi.md#get_page_free_text_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/freetext | Read document page free text annotations.
*PdfApi* | [**get_page_link_annotation**](docs/PdfApi.md#get_page_link_annotation) | **GET** /pdf/\{name}/pages/\{pageNumber}/links/\{linkId} | Read document page link annotation by ID.
*PdfApi* | [**get_page_link_annotations**](docs/PdfApi.md#get_page_link_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/links | Read document page link annotations.
*PdfApi* | [**get_page_text**](docs/PdfApi.md#get_page_text) | **GET** /pdf/\{name}/pages/\{pageNumber}/text | Read page text items.
*PdfApi* | [**get_page_text_annotations**](docs/PdfApi.md#get_page_text_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/text | Read document page text annotations.
*PdfApi* | [**get_pages**](docs/PdfApi.md#get_pages) | **GET** /pdf/\{name}/pages | Read document pages info.
*PdfApi* | [**get_pcl_in_storage_to_pdf**](docs/PdfApi.md#get_pcl_in_storage_to_pdf) | **GET** /pdf/create/pcl | Convert PCL file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_pdf_in_storage_to_doc**](docs/PdfApi.md#get_pdf_in_storage_to_doc) | **GET** /pdf/\{name}/convert/doc | Converts PDF document (located on storage) to DOC format and returns resulting file in response content
*PdfApi* | [**get_pdf_in_storage_to_epub**](docs/PdfApi.md#get_pdf_in_storage_to_epub) | **GET** /pdf/\{name}/convert/epub | Converts PDF document (located on storage) to EPUB format and returns resulting file in response content
*PdfApi* | [**get_pdf_in_storage_to_html**](docs/PdfApi.md#get_pdf_in_storage_to_html) | **GET** /pdf/\{name}/convert/html | Converts PDF document (located on storage) to Html format and returns resulting file in response content
*PdfApi* | [**get_pdf_in_storage_to_la_te_x**](docs/PdfApi.md#get_pdf_in_storage_to_la_te_x) | **GET** /pdf/\{name}/convert/latex | Converts PDF document (located on storage) to LaTeX format and returns resulting file in response content
*PdfApi* | [**get_pdf_in_storage_to_mobi_xml**](docs/PdfApi.md#get_pdf_in_storage_to_mobi_xml) | **GET** /pdf/\{name}/convert/mobixml | Converts PDF document (located on storage) to MOBIXML format and returns resulting file in response content
*PdfApi* | [**get_pdf_in_storage_to_pdf_a**](docs/PdfApi.md#get_pdf_in_storage_to_pdf_a) | **GET** /pdf/\{name}/convert/pdfa | Converts PDF document (located on storage) to PdfA format and returns resulting file in response content
*PdfApi* | [**get_pdf_in_storage_to_pptx**](docs/PdfApi.md#get_pdf_in_storage_to_pptx) | **GET** /pdf/\{name}/convert/pptx | Converts PDF document (located on storage) to PPTX format and returns resulting file in response content
*PdfApi* | [**get_pdf_in_storage_to_svg**](docs/PdfApi.md#get_pdf_in_storage_to_svg) | **GET** /pdf/\{name}/convert/svg | Converts PDF document (located on storage) to SVG format and returns resulting file in response content
*PdfApi* | [**get_pdf_in_storage_to_tiff**](docs/PdfApi.md#get_pdf_in_storage_to_tiff) | **GET** /pdf/\{name}/convert/tiff | Converts PDF document (located on storage) to TIFF format and returns resulting file in response content
*PdfApi* | [**get_pdf_in_storage_to_xls**](docs/PdfApi.md#get_pdf_in_storage_to_xls) | **GET** /pdf/\{name}/convert/xls | Converts PDF document (located on storage) to XLS format and returns resulting file in response content
*PdfApi* | [**get_pdf_in_storage_to_xml**](docs/PdfApi.md#get_pdf_in_storage_to_xml) | **GET** /pdf/\{name}/convert/xml | Converts PDF document (located on storage) to XML format and returns resulting file in response content
*PdfApi* | [**get_pdf_in_storage_to_xps**](docs/PdfApi.md#get_pdf_in_storage_to_xps) | **GET** /pdf/\{name}/convert/xps | Converts PDF document (located on storage) to XPS format and returns resulting file in response content
*PdfApi* | [**get_ps_in_storage_to_pdf**](docs/PdfApi.md#get_ps_in_storage_to_pdf) | **GET** /pdf/create/ps | Convert PS file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_svg_in_storage_to_pdf**](docs/PdfApi.md#get_svg_in_storage_to_pdf) | **GET** /pdf/create/svg | Convert SVG file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_text**](docs/PdfApi.md#get_text) | **GET** /pdf/\{name}/text | Read document text.
*PdfApi* | [**get_text_annotation**](docs/PdfApi.md#get_text_annotation) | **GET** /pdf/\{name}/annotations/text/\{annotationId} | Read document page text annotation by ID.
*PdfApi* | [**get_verify_signature**](docs/PdfApi.md#get_verify_signature) | **GET** /pdf/\{name}/verifySignature | Verify signature document.
*PdfApi* | [**get_web_in_storage_to_pdf**](docs/PdfApi.md#get_web_in_storage_to_pdf) | **GET** /pdf/create/web | Convert web page to PDF format and return resulting file in response. 
*PdfApi* | [**get_words_per_page**](docs/PdfApi.md#get_words_per_page) | **GET** /pdf/\{name}/pages/wordCount | Get number of words per document page.
*PdfApi* | [**get_xfa_pdf_in_storage_to_acro_form**](docs/PdfApi.md#get_xfa_pdf_in_storage_to_acro_form) | **GET** /pdf/\{name}/convert/xfatoacroform | Converts PDF document which contatins XFA form (located on storage) to PDF with AcroForm and returns resulting file response content
*PdfApi* | [**get_xml_in_storage_to_pdf**](docs/PdfApi.md#get_xml_in_storage_to_pdf) | **GET** /pdf/create/xml | Convert XML file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_xps_in_storage_to_pdf**](docs/PdfApi.md#get_xps_in_storage_to_pdf) | **GET** /pdf/create/xps | Convert XPS file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_xsl_fo_in_storage_to_pdf**](docs/PdfApi.md#get_xsl_fo_in_storage_to_pdf) | **GET** /pdf/create/xslfo | Convert XslFo file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**post_append_document**](docs/PdfApi.md#post_append_document) | **POST** /pdf/\{name}/appendDocument | Append document to existing one.
*PdfApi* | [**post_create_field**](docs/PdfApi.md#post_create_field) | **POST** /pdf/\{name}/fields | Create field.
*PdfApi* | [**post_document_text_replace**](docs/PdfApi.md#post_document_text_replace) | **POST** /pdf/\{name}/text/replace | Document&#39;s replace text method.
*PdfApi* | [**post_insert_image**](docs/PdfApi.md#post_insert_image) | **POST** /pdf/\{name}/pages/\{pageNumber}/images | Insert image to document page.
*PdfApi* | [**post_move_page**](docs/PdfApi.md#post_move_page) | **POST** /pdf/\{name}/pages/\{pageNumber}/movePage | Move page to new position.
*PdfApi* | [**post_optimize_document**](docs/PdfApi.md#post_optimize_document) | **POST** /pdf/\{name}/optimize | Optimize document.
*PdfApi* | [**post_page_free_text_annotations**](docs/PdfApi.md#post_page_free_text_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/freetext | Add document page free text annotations.
*PdfApi* | [**post_page_link_annotations**](docs/PdfApi.md#post_page_link_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/links | Add document page link annotations.
*PdfApi* | [**post_page_text_annotations**](docs/PdfApi.md#post_page_text_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/text | Add document page text annotations.
*PdfApi* | [**post_page_text_replace**](docs/PdfApi.md#post_page_text_replace) | **POST** /pdf/\{name}/pages/\{pageNumber}/text/replace | Page&#39;s replace text method.
*PdfApi* | [**post_sign_document**](docs/PdfApi.md#post_sign_document) | **POST** /pdf/\{name}/sign | Sign document.
*PdfApi* | [**post_sign_page**](docs/PdfApi.md#post_sign_page) | **POST** /pdf/\{name}/pages/\{pageNumber}/sign | Sign page.
*PdfApi* | [**post_split_document**](docs/PdfApi.md#post_split_document) | **POST** /pdf/\{name}/split | Split document to parts.
*PdfApi* | [**put_add_new_page**](docs/PdfApi.md#put_add_new_page) | **PUT** /pdf/\{name}/pages | Add new page to end of the document.
*PdfApi* | [**put_add_text**](docs/PdfApi.md#put_add_text) | **PUT** /pdf/\{name}/pages/\{pageNumber}/text | Add text to PDF document page.
*PdfApi* | [**put_create**](docs/PdfApi.md#put_create) | **PUT** /storage/file | Upload a specific file 
*PdfApi* | [**put_create_document**](docs/PdfApi.md#put_create_document) | **PUT** /pdf/\{name} | Create empty document.
*PdfApi* | [**put_epub_in_storage_to_pdf**](docs/PdfApi.md#put_epub_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/epub | Convert EPUB file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_fields_flatten**](docs/PdfApi.md#put_fields_flatten) | **PUT** /pdf/\{name}/fields/flatten | Flatten form fields in document.
*PdfApi* | [**put_free_text_annotation**](docs/PdfApi.md#put_free_text_annotation) | **PUT** /pdf/\{name}/annotations/freetext/\{annotationId} | Replace document free text annotation
*PdfApi* | [**put_html_in_storage_to_pdf**](docs/PdfApi.md#put_html_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/html | Convert HTML file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_image_extract_as_gif**](docs/PdfApi.md#put_image_extract_as_gif) | **PUT** /pdf/\{name}/images/\{imageId}/extract/gif | Extract document image in GIF format to folder
*PdfApi* | [**put_image_extract_as_jpeg**](docs/PdfApi.md#put_image_extract_as_jpeg) | **PUT** /pdf/\{name}/images/\{imageId}/extract/jpeg | Extract document image in JPEG format to folder
*PdfApi* | [**put_image_extract_as_png**](docs/PdfApi.md#put_image_extract_as_png) | **PUT** /pdf/\{name}/images/\{imageId}/extract/png | Extract document image in PNG format to folder
*PdfApi* | [**put_image_extract_as_tiff**](docs/PdfApi.md#put_image_extract_as_tiff) | **PUT** /pdf/\{name}/images/\{imageId}/extract/tiff | Extract document image in TIFF format to folder
*PdfApi* | [**put_image_in_storage_to_pdf**](docs/PdfApi.md#put_image_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/images | Convert image file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_images_extract_as_gif**](docs/PdfApi.md#put_images_extract_as_gif) | **PUT** /pdf/\{name}/pages/\{pageNumber}/images/extract/gif | Extract document images in GIF format to folder.
*PdfApi* | [**put_images_extract_as_jpeg**](docs/PdfApi.md#put_images_extract_as_jpeg) | **PUT** /pdf/\{name}/pages/\{pageNumber}/images/extract/jpeg | Extract document images in JPEG format to folder.
*PdfApi* | [**put_images_extract_as_png**](docs/PdfApi.md#put_images_extract_as_png) | **PUT** /pdf/\{name}/pages/\{pageNumber}/images/extract/png | Extract document images in PNG format to folder.
*PdfApi* | [**put_images_extract_as_tiff**](docs/PdfApi.md#put_images_extract_as_tiff) | **PUT** /pdf/\{name}/pages/\{pageNumber}/images/extract/tiff | Extract document images in TIFF format to folder.
*PdfApi* | [**put_la_te_x_in_storage_to_pdf**](docs/PdfApi.md#put_la_te_x_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/latex | Convert LaTeX file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_link_annotation**](docs/PdfApi.md#put_link_annotation) | **PUT** /pdf/\{name}/links/\{linkId} | Replace document page link annotations
*PdfApi* | [**put_merge_documents**](docs/PdfApi.md#put_merge_documents) | **PUT** /pdf/\{name}/merge | Merge a list of documents.
*PdfApi* | [**put_mht_in_storage_to_pdf**](docs/PdfApi.md#put_mht_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/mht | Convert MHT file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_page_add_stamp**](docs/PdfApi.md#put_page_add_stamp) | **PUT** /pdf/\{name}/pages/\{pageNumber}/stamp | Add page stamp.
*PdfApi* | [**put_page_convert_to_bmp**](docs/PdfApi.md#put_page_convert_to_bmp) | **PUT** /pdf/\{name}/pages/\{pageNumber}/convert/bmp | Convert document page to bmp image and upload resulting file to storage.
*PdfApi* | [**put_page_convert_to_emf**](docs/PdfApi.md#put_page_convert_to_emf) | **PUT** /pdf/\{name}/pages/\{pageNumber}/convert/emf | Convert document page to emf image and upload resulting file to storage.
*PdfApi* | [**put_page_convert_to_gif**](docs/PdfApi.md#put_page_convert_to_gif) | **PUT** /pdf/\{name}/pages/\{pageNumber}/convert/gif | Convert document page to gif image and upload resulting file to storage.
*PdfApi* | [**put_page_convert_to_jpeg**](docs/PdfApi.md#put_page_convert_to_jpeg) | **PUT** /pdf/\{name}/pages/\{pageNumber}/convert/jpeg | Convert document page to Jpeg image and upload resulting file to storage.
*PdfApi* | [**put_page_convert_to_png**](docs/PdfApi.md#put_page_convert_to_png) | **PUT** /pdf/\{name}/pages/\{pageNumber}/convert/png | Convert document page to png image and upload resulting file to storage.
*PdfApi* | [**put_page_convert_to_tiff**](docs/PdfApi.md#put_page_convert_to_tiff) | **PUT** /pdf/\{name}/pages/\{pageNumber}/convert/tiff | Convert document page to Tiff image and upload resulting file to storage.
*PdfApi* | [**put_pcl_in_storage_to_pdf**](docs/PdfApi.md#put_pcl_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/pcl | Convert PCL file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_pdf_in_request_to_doc**](docs/PdfApi.md#put_pdf_in_request_to_doc) | **PUT** /pdf/convert/doc | Converts PDF document (in request content) to DOC format and uploads resulting file to storage.
*PdfApi* | [**put_pdf_in_request_to_epub**](docs/PdfApi.md#put_pdf_in_request_to_epub) | **PUT** /pdf/convert/epub | Converts PDF document (in request content) to EPUB format and uploads resulting file to storage.
*PdfApi* | [**put_pdf_in_request_to_html**](docs/PdfApi.md#put_pdf_in_request_to_html) | **PUT** /pdf/convert/html | Converts PDF document (in request content) to Html format and uploads resulting file to storage.
*PdfApi* | [**put_pdf_in_request_to_la_te_x**](docs/PdfApi.md#put_pdf_in_request_to_la_te_x) | **PUT** /pdf/convert/latex | Converts PDF document (in request content) to LaTeX format and uploads resulting file to storage.
*PdfApi* | [**put_pdf_in_request_to_mobi_xml**](docs/PdfApi.md#put_pdf_in_request_to_mobi_xml) | **PUT** /pdf/convert/mobixml | Converts PDF document (in request content) to MOBIXML format and uploads resulting file to storage.
*PdfApi* | [**put_pdf_in_request_to_pdf_a**](docs/PdfApi.md#put_pdf_in_request_to_pdf_a) | **PUT** /pdf/convert/pdfa | Converts PDF document (in request content) to PdfA format and uploads resulting file to storage.
*PdfApi* | [**put_pdf_in_request_to_pptx**](docs/PdfApi.md#put_pdf_in_request_to_pptx) | **PUT** /pdf/convert/pptx | Converts PDF document (in request content) to PPTX format and uploads resulting file to storage.
*PdfApi* | [**put_pdf_in_request_to_svg**](docs/PdfApi.md#put_pdf_in_request_to_svg) | **PUT** /pdf/convert/svg | Converts PDF document (in request content) to SVG format and uploads resulting file to storage.
*PdfApi* | [**put_pdf_in_request_to_tiff**](docs/PdfApi.md#put_pdf_in_request_to_tiff) | **PUT** /pdf/convert/tiff | Converts PDF document (in request content) to TIFF format and uploads resulting file to storage.
*PdfApi* | [**put_pdf_in_request_to_xls**](docs/PdfApi.md#put_pdf_in_request_to_xls) | **PUT** /pdf/convert/xls | Converts PDF document (in request content) to XLS format and uploads resulting file to storage.
*PdfApi* | [**put_pdf_in_request_to_xml**](docs/PdfApi.md#put_pdf_in_request_to_xml) | **PUT** /pdf/convert/xml | Converts PDF document (in request content) to XML format and uploads resulting file to storage.
*PdfApi* | [**put_pdf_in_request_to_xps**](docs/PdfApi.md#put_pdf_in_request_to_xps) | **PUT** /pdf/convert/xps | Converts PDF document (in request content) to XPS format and uploads resulting file to storage.
*PdfApi* | [**put_pdf_in_storage_to_doc**](docs/PdfApi.md#put_pdf_in_storage_to_doc) | **PUT** /pdf/\{name}/convert/doc | Converts PDF document (located on storage) to DOC format and uploads resulting file to storage
*PdfApi* | [**put_pdf_in_storage_to_epub**](docs/PdfApi.md#put_pdf_in_storage_to_epub) | **PUT** /pdf/\{name}/convert/epub | Converts PDF document (located on storage) to EPUB format and uploads resulting file to storage
*PdfApi* | [**put_pdf_in_storage_to_html**](docs/PdfApi.md#put_pdf_in_storage_to_html) | **PUT** /pdf/\{name}/convert/html | Converts PDF document (located on storage) to Html format and uploads resulting file to storage
*PdfApi* | [**put_pdf_in_storage_to_la_te_x**](docs/PdfApi.md#put_pdf_in_storage_to_la_te_x) | **PUT** /pdf/\{name}/convert/latex | Converts PDF document (located on storage) to LaTeX format and uploads resulting file to storage
*PdfApi* | [**put_pdf_in_storage_to_mobi_xml**](docs/PdfApi.md#put_pdf_in_storage_to_mobi_xml) | **PUT** /pdf/\{name}/convert/mobixml | Converts PDF document (located on storage) to MOBIXML format and uploads resulting file to storage
*PdfApi* | [**put_pdf_in_storage_to_pdf_a**](docs/PdfApi.md#put_pdf_in_storage_to_pdf_a) | **PUT** /pdf/\{name}/convert/pdfa | Converts PDF document (located on storage) to PdfA format and uploads resulting file to storage
*PdfApi* | [**put_pdf_in_storage_to_pptx**](docs/PdfApi.md#put_pdf_in_storage_to_pptx) | **PUT** /pdf/\{name}/convert/pptx | Converts PDF document (located on storage) to PPTX format and uploads resulting file to storage
*PdfApi* | [**put_pdf_in_storage_to_svg**](docs/PdfApi.md#put_pdf_in_storage_to_svg) | **PUT** /pdf/\{name}/convert/svg | Converts PDF document (located on storage) to SVG format and uploads resulting file to storage
*PdfApi* | [**put_pdf_in_storage_to_tiff**](docs/PdfApi.md#put_pdf_in_storage_to_tiff) | **PUT** /pdf/\{name}/convert/tiff | Converts PDF document (located on storage) to TIFF format and uploads resulting file to storage
*PdfApi* | [**put_pdf_in_storage_to_xls**](docs/PdfApi.md#put_pdf_in_storage_to_xls) | **PUT** /pdf/\{name}/convert/xls | Converts PDF document (located on storage) to XLS format and uploads resulting file to storage
*PdfApi* | [**put_pdf_in_storage_to_xml**](docs/PdfApi.md#put_pdf_in_storage_to_xml) | **PUT** /pdf/\{name}/convert/xml | Converts PDF document (located on storage) to XML format and uploads resulting file to storage
*PdfApi* | [**put_pdf_in_storage_to_xps**](docs/PdfApi.md#put_pdf_in_storage_to_xps) | **PUT** /pdf/\{name}/convert/xps | Converts PDF document (located on storage) to XPS format and uploads resulting file to storage
*PdfApi* | [**put_privileges**](docs/PdfApi.md#put_privileges) | **PUT** /pdf/\{name}/privileges | Update privilege document.
*PdfApi* | [**put_ps_in_storage_to_pdf**](docs/PdfApi.md#put_ps_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/ps | Convert PS file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_replace_image**](docs/PdfApi.md#put_replace_image) | **PUT** /pdf/\{name}/images/\{imageId} | Replace document image.
*PdfApi* | [**put_searchable_document**](docs/PdfApi.md#put_searchable_document) | **PUT** /pdf/\{name}/ocr | Create searchable PDF document. Generate OCR layer for images in input PDF document.
*PdfApi* | [**put_set_property**](docs/PdfApi.md#put_set_property) | **PUT** /pdf/\{name}/documentproperties/\{propertyName} | Add/update document property.
*PdfApi* | [**put_svg_in_storage_to_pdf**](docs/PdfApi.md#put_svg_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/svg | Convert SVG file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_text_annotation**](docs/PdfApi.md#put_text_annotation) | **PUT** /pdf/\{name}/annotations/text/\{annotationId} | Replace document text annotation
*PdfApi* | [**put_update_field**](docs/PdfApi.md#put_update_field) | **PUT** /pdf/\{name}/fields/\{fieldName} | Update field.
*PdfApi* | [**put_update_fields**](docs/PdfApi.md#put_update_fields) | **PUT** /pdf/\{name}/fields | Update fields.
*PdfApi* | [**put_web_in_storage_to_pdf**](docs/PdfApi.md#put_web_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/web | Convert web page to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_xfa_pdf_in_request_to_acro_form**](docs/PdfApi.md#put_xfa_pdf_in_request_to_acro_form) | **PUT** /pdf/convert/xfatoacroform | Converts PDF document which contatins XFA form (in request content) to PDF with AcroForm and uploads resulting file to storage.
*PdfApi* | [**put_xfa_pdf_in_storage_to_acro_form**](docs/PdfApi.md#put_xfa_pdf_in_storage_to_acro_form) | **PUT** /pdf/\{name}/convert/xfatoacroform | Converts PDF document which contatins XFA form (located on storage) to PDF with AcroForm and uploads resulting file to storage
*PdfApi* | [**put_xml_in_storage_to_pdf**](docs/PdfApi.md#put_xml_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/xml | Convert XML file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_xps_in_storage_to_pdf**](docs/PdfApi.md#put_xps_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/xps | Convert XPS file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_xsl_fo_in_storage_to_pdf**](docs/PdfApi.md#put_xsl_fo_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/xslfo | Convert XslFo file (located on storage) to PDF format and upload resulting file to storage. 


## Documentation For Models

 - [AnnotationFlags](docs/AnnotationFlags.md)
 - [AnnotationState](docs/AnnotationState.md)
 - [AnnotationType](docs/AnnotationType.md)
 - [AntialiasingProcessingType](docs/AntialiasingProcessingType.md)
 - [AppendDocument](docs/AppendDocument.md)
 - [AsposeResponse](docs/AsposeResponse.md)
 - [Color](docs/Color.md)
 - [ColorDepth](docs/ColorDepth.md)
 - [CompressionType](docs/CompressionType.md)
 - [DocFormat](docs/DocFormat.md)
 - [DocRecognitionMode](docs/DocRecognitionMode.md)
 - [DocumentPrivilege](docs/DocumentPrivilege.md)
 - [EpubRecognitionMode](docs/EpubRecognitionMode.md)
 - [FieldType](docs/FieldType.md)
 - [FontEncodingRules](docs/FontEncodingRules.md)
 - [FontSavingModes](docs/FontSavingModes.md)
 - [FontStyles](docs/FontStyles.md)
 - [FreeTextIntent](docs/FreeTextIntent.md)
 - [HorizontalAlignment](docs/HorizontalAlignment.md)
 - [HtmlDocumentType](docs/HtmlDocumentType.md)
 - [HtmlMarkupGenerationModes](docs/HtmlMarkupGenerationModes.md)
 - [ImageSrcType](docs/ImageSrcType.md)
 - [ImageTemplate](docs/ImageTemplate.md)
 - [ImageTemplatesRequest](docs/ImageTemplatesRequest.md)
 - [Justification](docs/Justification.md)
 - [LettersPositioningMethods](docs/LettersPositioningMethods.md)
 - [LineSpacing](docs/LineSpacing.md)
 - [Link](docs/Link.md)
 - [LinkActionType](docs/LinkActionType.md)
 - [LinkElement](docs/LinkElement.md)
 - [LinkHighlightingMode](docs/LinkHighlightingMode.md)
 - [MarginInfo](docs/MarginInfo.md)
 - [MergeDocuments](docs/MergeDocuments.md)
 - [OptimizeOptions](docs/OptimizeOptions.md)
 - [PageWordCount](docs/PageWordCount.md)
 - [Paragraph](docs/Paragraph.md)
 - [PartsEmbeddingModes](docs/PartsEmbeddingModes.md)
 - [PdfAType](docs/PdfAType.md)
 - [RasterImagesSavingModes](docs/RasterImagesSavingModes.md)
 - [RectanglePdf](docs/RectanglePdf.md)
 - [Rotation](docs/Rotation.md)
 - [Segment](docs/Segment.md)
 - [ShapeType](docs/ShapeType.md)
 - [Signature](docs/Signature.md)
 - [SignatureType](docs/SignatureType.md)
 - [SplitResult](docs/SplitResult.md)
 - [Stamp](docs/Stamp.md)
 - [StampType](docs/StampType.md)
 - [TextHorizontalAlignment](docs/TextHorizontalAlignment.md)
 - [TextIcon](docs/TextIcon.md)
 - [TextLine](docs/TextLine.md)
 - [TextRect](docs/TextRect.md)
 - [TextRects](docs/TextRects.md)
 - [TextReplace](docs/TextReplace.md)
 - [TextReplaceListRequest](docs/TextReplaceListRequest.md)
 - [TextState](docs/TextState.md)
 - [TextStyle](docs/TextStyle.md)
 - [VerticalAlignment](docs/VerticalAlignment.md)
 - [WordCount](docs/WordCount.md)
 - [WrapMode](docs/WrapMode.md)
 - [Annotation](docs/Annotation.md)
 - [AnnotationsInfo](docs/AnnotationsInfo.md)
 - [AnnotationsInfoResponse](docs/AnnotationsInfoResponse.md)
 - [Attachment](docs/Attachment.md)
 - [AttachmentResponse](docs/AttachmentResponse.md)
 - [Attachments](docs/Attachments.md)
 - [AttachmentsResponse](docs/AttachmentsResponse.md)
 - [Document](docs/Document.md)
 - [DocumentPageResponse](docs/DocumentPageResponse.md)
 - [DocumentPagesResponse](docs/DocumentPagesResponse.md)
 - [DocumentProperties](docs/DocumentProperties.md)
 - [DocumentPropertiesResponse](docs/DocumentPropertiesResponse.md)
 - [DocumentProperty](docs/DocumentProperty.md)
 - [DocumentPropertyResponse](docs/DocumentPropertyResponse.md)
 - [DocumentResponse](docs/DocumentResponse.md)
 - [Field](docs/Field.md)
 - [FieldResponse](docs/FieldResponse.md)
 - [Fields](docs/Fields.md)
 - [FieldsResponse](docs/FieldsResponse.md)
 - [FreeTextAnnotationResponse](docs/FreeTextAnnotationResponse.md)
 - [FreeTextAnnotations](docs/FreeTextAnnotations.md)
 - [FreeTextAnnotationsResponse](docs/FreeTextAnnotationsResponse.md)
 - [Image](docs/Image.md)
 - [ImageResponse](docs/ImageResponse.md)
 - [Images](docs/Images.md)
 - [ImagesResponse](docs/ImagesResponse.md)
 - [LinkAnnotation](docs/LinkAnnotation.md)
 - [LinkAnnotationResponse](docs/LinkAnnotationResponse.md)
 - [LinkAnnotations](docs/LinkAnnotations.md)
 - [LinkAnnotationsResponse](docs/LinkAnnotationsResponse.md)
 - [Page](docs/Page.md)
 - [Pages](docs/Pages.md)
 - [SignatureVerifyResponse](docs/SignatureVerifyResponse.md)
 - [SplitResultDocument](docs/SplitResultDocument.md)
 - [SplitResultResponse](docs/SplitResultResponse.md)
 - [TextAnnotationResponse](docs/TextAnnotationResponse.md)
 - [TextAnnotations](docs/TextAnnotations.md)
 - [TextAnnotationsResponse](docs/TextAnnotationsResponse.md)
 - [TextRectsResponse](docs/TextRectsResponse.md)
 - [TextReplaceResponse](docs/TextReplaceResponse.md)
 - [WordCountResponse](docs/WordCountResponse.md)
 - [AnnotationInfo](docs/AnnotationInfo.md)
 - [MarkupAnnotation](docs/MarkupAnnotation.md)
 - [FreeTextAnnotation](docs/FreeTextAnnotation.md)
 - [TextAnnotation](docs/TextAnnotation.md)

