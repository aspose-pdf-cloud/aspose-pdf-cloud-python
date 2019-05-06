# Aspose.PDF Cloud
- API version: 2.0
- Package version: 19.4.0

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

All URIs are relative to *https://api.aspose.cloud/v2.0/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PdfApi* | [**delete_annotation**](docs/PdfApi.md#delete_annotation) | **DELETE** /pdf/\{name}/annotations/\{annotationId} | Delete document annotation by ID
*PdfApi* | [**delete_document_annotations**](docs/PdfApi.md#delete_document_annotations) | **DELETE** /pdf/\{name}/annotations | Delete all annotations from the document
*PdfApi* | [**delete_document_link_annotations**](docs/PdfApi.md#delete_document_link_annotations) | **DELETE** /pdf/\{name}/links | Delete all link annotations from the document
*PdfApi* | [**delete_document_stamps**](docs/PdfApi.md#delete_document_stamps) | **DELETE** /pdf/\{name}/stamps | Delete all stamps from the document
*PdfApi* | [**delete_document_tables**](docs/PdfApi.md#delete_document_tables) | **DELETE** /pdf/\{name}/tables | Delete all tables from the document
*PdfApi* | [**delete_field**](docs/PdfApi.md#delete_field) | **DELETE** /pdf/\{name}/fields/\{fieldName} | Delete document field by name.
*PdfApi* | [**delete_file**](docs/PdfApi.md#delete_file) | **DELETE** /storage/file | Remove a specific file 
*PdfApi* | [**delete_folder**](docs/PdfApi.md#delete_folder) | **DELETE** /storage/folder | Remove a specific folder 
*PdfApi* | [**delete_image**](docs/PdfApi.md#delete_image) | **DELETE** /pdf/\{name}/images/\{imageId} | Delete image from document page.
*PdfApi* | [**delete_link_annotation**](docs/PdfApi.md#delete_link_annotation) | **DELETE** /pdf/\{name}/links/\{linkId} | Delete document page link annotation by ID
*PdfApi* | [**delete_page**](docs/PdfApi.md#delete_page) | **DELETE** /pdf/\{name}/pages/\{pageNumber} | Delete document page by its number.
*PdfApi* | [**delete_page_annotations**](docs/PdfApi.md#delete_page_annotations) | **DELETE** /pdf/\{name}/pages/\{pageNumber}/annotations | Delete all annotations from the page
*PdfApi* | [**delete_page_link_annotations**](docs/PdfApi.md#delete_page_link_annotations) | **DELETE** /pdf/\{name}/pages/\{pageNumber}/links | Delete all link annotations from the page
*PdfApi* | [**delete_page_stamps**](docs/PdfApi.md#delete_page_stamps) | **DELETE** /pdf/\{name}/pages/\{pageNumber}/stamps | Delete all stamps from the page
*PdfApi* | [**delete_page_tables**](docs/PdfApi.md#delete_page_tables) | **DELETE** /pdf/\{name}/pages/\{pageNumber}/tables | Delete all tables from the page
*PdfApi* | [**delete_properties**](docs/PdfApi.md#delete_properties) | **DELETE** /pdf/\{name}/documentproperties | Delete custom document properties.
*PdfApi* | [**delete_property**](docs/PdfApi.md#delete_property) | **DELETE** /pdf/\{name}/documentproperties/\{propertyName} | Delete document property.
*PdfApi* | [**delete_stamp**](docs/PdfApi.md#delete_stamp) | **DELETE** /pdf/\{name}/stamps/\{stampId} | Delete document stamp by ID
*PdfApi* | [**delete_table**](docs/PdfApi.md#delete_table) | **DELETE** /pdf/\{name}/tables/\{tableId} | Delete document table by ID
*PdfApi* | [**get_caret_annotation**](docs/PdfApi.md#get_caret_annotation) | **GET** /pdf/\{name}/annotations/caret/\{annotationId} | Read document page caret annotation by ID.
*PdfApi* | [**get_circle_annotation**](docs/PdfApi.md#get_circle_annotation) | **GET** /pdf/\{name}/annotations/circle/\{annotationId} | Read document page circle annotation by ID.
*PdfApi* | [**get_disc_usage**](docs/PdfApi.md#get_disc_usage) | **GET** /storage/disc | Check the disk usage of the current account 
*PdfApi* | [**get_document**](docs/PdfApi.md#get_document) | **GET** /pdf/\{name} | Read common document info.
*PdfApi* | [**get_document_annotations**](docs/PdfApi.md#get_document_annotations) | **GET** /pdf/\{name}/annotations | Read documant page annotations. Returns only FreeTextAnnotations, TextAnnotations, other annotations will implemented next releases.
*PdfApi* | [**get_document_attachment_by_index**](docs/PdfApi.md#get_document_attachment_by_index) | **GET** /pdf/\{name}/attachments/\{attachmentIndex} | Read document attachment info by its index.
*PdfApi* | [**get_document_attachments**](docs/PdfApi.md#get_document_attachments) | **GET** /pdf/\{name}/attachments | Read document attachments info.
*PdfApi* | [**get_document_caret_annotations**](docs/PdfApi.md#get_document_caret_annotations) | **GET** /pdf/\{name}/annotations/caret | Read document caret annotations.
*PdfApi* | [**get_document_circle_annotations**](docs/PdfApi.md#get_document_circle_annotations) | **GET** /pdf/\{name}/annotations/circle | Read document circle annotations.
*PdfApi* | [**get_document_file_attachment_annotations**](docs/PdfApi.md#get_document_file_attachment_annotations) | **GET** /pdf/\{name}/annotations/fileattachment | Read document FileAttachment annotations.
*PdfApi* | [**get_document_free_text_annotations**](docs/PdfApi.md#get_document_free_text_annotations) | **GET** /pdf/\{name}/annotations/freetext | Read document free text annotations.
*PdfApi* | [**get_document_highlight_annotations**](docs/PdfApi.md#get_document_highlight_annotations) | **GET** /pdf/\{name}/annotations/highlight | Read document highlight annotations.
*PdfApi* | [**get_document_ink_annotations**](docs/PdfApi.md#get_document_ink_annotations) | **GET** /pdf/\{name}/annotations/ink | Read document ink annotations.
*PdfApi* | [**get_document_line_annotations**](docs/PdfApi.md#get_document_line_annotations) | **GET** /pdf/\{name}/annotations/line | Read document line annotations.
*PdfApi* | [**get_document_movie_annotations**](docs/PdfApi.md#get_document_movie_annotations) | **GET** /pdf/\{name}/annotations/movie | Read document movie annotations.
*PdfApi* | [**get_document_poly_line_annotations**](docs/PdfApi.md#get_document_poly_line_annotations) | **GET** /pdf/\{name}/annotations/polyline | Read document polyline annotations.
*PdfApi* | [**get_document_polygon_annotations**](docs/PdfApi.md#get_document_polygon_annotations) | **GET** /pdf/\{name}/annotations/polygon | Read document polygon annotations.
*PdfApi* | [**get_document_popup_annotations**](docs/PdfApi.md#get_document_popup_annotations) | **GET** /pdf/\{name}/annotations/popup | Read document popup annotations.
*PdfApi* | [**get_document_popup_annotations_by_parent**](docs/PdfApi.md#get_document_popup_annotations_by_parent) | **GET** /pdf/\{name}/annotations/\{annotationId}/popup | Read document popup annotations by parent id.
*PdfApi* | [**get_document_properties**](docs/PdfApi.md#get_document_properties) | **GET** /pdf/\{name}/documentproperties | Read document properties.
*PdfApi* | [**get_document_property**](docs/PdfApi.md#get_document_property) | **GET** /pdf/\{name}/documentproperties/\{propertyName} | Read document property by name.
*PdfApi* | [**get_document_redaction_annotations**](docs/PdfApi.md#get_document_redaction_annotations) | **GET** /pdf/\{name}/annotations/redaction | Read document redaction annotations.
*PdfApi* | [**get_document_screen_annotations**](docs/PdfApi.md#get_document_screen_annotations) | **GET** /pdf/\{name}/annotations/screen | Read document screen annotations.
*PdfApi* | [**get_document_sound_annotations**](docs/PdfApi.md#get_document_sound_annotations) | **GET** /pdf/\{name}/annotations/sound | Read document sound annotations.
*PdfApi* | [**get_document_square_annotations**](docs/PdfApi.md#get_document_square_annotations) | **GET** /pdf/\{name}/annotations/square | Read document square annotations.
*PdfApi* | [**get_document_squiggly_annotations**](docs/PdfApi.md#get_document_squiggly_annotations) | **GET** /pdf/\{name}/annotations/squiggly | Read document squiggly annotations.
*PdfApi* | [**get_document_stamp_annotations**](docs/PdfApi.md#get_document_stamp_annotations) | **GET** /pdf/\{name}/annotations/stamp | Read document stamp annotations.
*PdfApi* | [**get_document_stamps**](docs/PdfApi.md#get_document_stamps) | **GET** /pdf/\{name}/stamps | Read document stamps.
*PdfApi* | [**get_document_strike_out_annotations**](docs/PdfApi.md#get_document_strike_out_annotations) | **GET** /pdf/\{name}/annotations/strikeout | Read document StrikeOut annotations.
*PdfApi* | [**get_document_tables**](docs/PdfApi.md#get_document_tables) | **GET** /pdf/\{name}/tables | Read document tables.
*PdfApi* | [**get_document_text_annotations**](docs/PdfApi.md#get_document_text_annotations) | **GET** /pdf/\{name}/annotations/text | Read document text annotations.
*PdfApi* | [**get_document_underline_annotations**](docs/PdfApi.md#get_document_underline_annotations) | **GET** /pdf/\{name}/annotations/underline | Read document underline annotations.
*PdfApi* | [**get_download**](docs/PdfApi.md#get_download) | **GET** /storage/file | Download a specific file 
*PdfApi* | [**get_download_document_attachment_by_index**](docs/PdfApi.md#get_download_document_attachment_by_index) | **GET** /pdf/\{name}/attachments/\{attachmentIndex}/download | Download document attachment content by its index.
*PdfApi* | [**get_epub_in_storage_to_pdf**](docs/PdfApi.md#get_epub_in_storage_to_pdf) | **GET** /pdf/create/epub | Convert EPUB file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_field**](docs/PdfApi.md#get_field) | **GET** /pdf/\{name}/fields/\{fieldName} | Get document field by name.
*PdfApi* | [**get_fields**](docs/PdfApi.md#get_fields) | **GET** /pdf/\{name}/fields | Get document fields.
*PdfApi* | [**get_file_attachment_annotation**](docs/PdfApi.md#get_file_attachment_annotation) | **GET** /pdf/\{name}/annotations/fileattachment/\{annotationId} | Read document page FileAttachment annotation by ID.
*PdfApi* | [**get_file_attachment_annotation_data**](docs/PdfApi.md#get_file_attachment_annotation_data) | **GET** /pdf/\{name}/annotations/fileattachment/\{annotationId}/data | Read document page FileAttachment annotation by ID.
*PdfApi* | [**get_free_text_annotation**](docs/PdfApi.md#get_free_text_annotation) | **GET** /pdf/\{name}/annotations/freetext/\{annotationId} | Read document page free text annotation by ID.
*PdfApi* | [**get_highlight_annotation**](docs/PdfApi.md#get_highlight_annotation) | **GET** /pdf/\{name}/annotations/highlight/\{annotationId} | Read document page highlight annotation by ID.
*PdfApi* | [**get_html_in_storage_to_pdf**](docs/PdfApi.md#get_html_in_storage_to_pdf) | **GET** /pdf/create/html | Convert HTML file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_image**](docs/PdfApi.md#get_image) | **GET** /pdf/\{name}/images/\{imageId} | Read document image by ID.
*PdfApi* | [**get_image_extract_as_gif**](docs/PdfApi.md#get_image_extract_as_gif) | **GET** /pdf/\{name}/images/\{imageId}/extract/gif | Extract document image in GIF format
*PdfApi* | [**get_image_extract_as_jpeg**](docs/PdfApi.md#get_image_extract_as_jpeg) | **GET** /pdf/\{name}/images/\{imageId}/extract/jpeg | Extract document image in JPEG format
*PdfApi* | [**get_image_extract_as_png**](docs/PdfApi.md#get_image_extract_as_png) | **GET** /pdf/\{name}/images/\{imageId}/extract/png | Extract document image in PNG format
*PdfApi* | [**get_image_extract_as_tiff**](docs/PdfApi.md#get_image_extract_as_tiff) | **GET** /pdf/\{name}/images/\{imageId}/extract/tiff | Extract document image in TIFF format
*PdfApi* | [**get_images**](docs/PdfApi.md#get_images) | **GET** /pdf/\{name}/pages/\{pageNumber}/images | Read document images.
*PdfApi* | [**get_ink_annotation**](docs/PdfApi.md#get_ink_annotation) | **GET** /pdf/\{name}/annotations/ink/\{annotationId} | Read document page ink annotation by ID.
*PdfApi* | [**get_is_exist**](docs/PdfApi.md#get_is_exist) | **GET** /storage/exist | Check if a specific file or folder exists
*PdfApi* | [**get_is_storage_exist**](docs/PdfApi.md#get_is_storage_exist) | **GET** /storage/\{name}/exist | Check if storage exists 
*PdfApi* | [**get_la_te_x_in_storage_to_pdf**](docs/PdfApi.md#get_la_te_x_in_storage_to_pdf) | **GET** /pdf/create/latex | Convert LaTeX file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_line_annotation**](docs/PdfApi.md#get_line_annotation) | **GET** /pdf/\{name}/annotations/line/\{annotationId} | Read document page line annotation by ID.
*PdfApi* | [**get_link_annotation**](docs/PdfApi.md#get_link_annotation) | **GET** /pdf/\{name}/links/\{linkId} | Read document link annotation by ID.
*PdfApi* | [**get_list_file_versions**](docs/PdfApi.md#get_list_file_versions) | **GET** /storage/version | Get the file&#39;s versions list 
*PdfApi* | [**get_list_files**](docs/PdfApi.md#get_list_files) | **GET** /storage/folder | Get the file listing of a specific folder 
*PdfApi* | [**get_mht_in_storage_to_pdf**](docs/PdfApi.md#get_mht_in_storage_to_pdf) | **GET** /pdf/create/mht | Convert MHT file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_movie_annotation**](docs/PdfApi.md#get_movie_annotation) | **GET** /pdf/\{name}/annotations/movie/\{annotationId} | Read document page movie annotation by ID.
*PdfApi* | [**get_page**](docs/PdfApi.md#get_page) | **GET** /pdf/\{name}/pages/\{pageNumber} | Read document page info.
*PdfApi* | [**get_page_annotations**](docs/PdfApi.md#get_page_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations | Read document page annotations. Returns only FreeTextAnnotations, TextAnnotations, other annotations will implemented next releases.
*PdfApi* | [**get_page_caret_annotations**](docs/PdfApi.md#get_page_caret_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/caret | Read document page caret annotations.
*PdfApi* | [**get_page_circle_annotations**](docs/PdfApi.md#get_page_circle_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/circle | Read document page circle annotations.
*PdfApi* | [**get_page_convert_to_bmp**](docs/PdfApi.md#get_page_convert_to_bmp) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/bmp | Convert document page to Bmp image and return resulting file in response.
*PdfApi* | [**get_page_convert_to_emf**](docs/PdfApi.md#get_page_convert_to_emf) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/emf | Convert document page to Emf image and return resulting file in response.
*PdfApi* | [**get_page_convert_to_gif**](docs/PdfApi.md#get_page_convert_to_gif) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/gif | Convert document page to Gif image and return resulting file in response.
*PdfApi* | [**get_page_convert_to_jpeg**](docs/PdfApi.md#get_page_convert_to_jpeg) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/jpeg | Convert document page to Jpeg image and return resulting file in response.
*PdfApi* | [**get_page_convert_to_png**](docs/PdfApi.md#get_page_convert_to_png) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/png | Convert document page to Png image and return resulting file in response.
*PdfApi* | [**get_page_convert_to_tiff**](docs/PdfApi.md#get_page_convert_to_tiff) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/tiff | Convert document page to Tiff image  and return resulting file in response.
*PdfApi* | [**get_page_file_attachment_annotations**](docs/PdfApi.md#get_page_file_attachment_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/fileattachment | Read document page FileAttachment annotations.
*PdfApi* | [**get_page_free_text_annotations**](docs/PdfApi.md#get_page_free_text_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/freetext | Read document page free text annotations.
*PdfApi* | [**get_page_highlight_annotations**](docs/PdfApi.md#get_page_highlight_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/highlight | Read document page highlight annotations.
*PdfApi* | [**get_page_ink_annotations**](docs/PdfApi.md#get_page_ink_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/ink | Read document page ink annotations.
*PdfApi* | [**get_page_line_annotations**](docs/PdfApi.md#get_page_line_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/line | Read document page line annotations.
*PdfApi* | [**get_page_link_annotation**](docs/PdfApi.md#get_page_link_annotation) | **GET** /pdf/\{name}/pages/\{pageNumber}/links/\{linkId} | Read document page link annotation by ID.
*PdfApi* | [**get_page_link_annotations**](docs/PdfApi.md#get_page_link_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/links | Read document page link annotations.
*PdfApi* | [**get_page_movie_annotations**](docs/PdfApi.md#get_page_movie_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/movie | Read document page movie annotations.
*PdfApi* | [**get_page_poly_line_annotations**](docs/PdfApi.md#get_page_poly_line_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/polyline | Read document page polyline annotations.
*PdfApi* | [**get_page_polygon_annotations**](docs/PdfApi.md#get_page_polygon_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/polygon | Read document page polygon annotations.
*PdfApi* | [**get_page_popup_annotations**](docs/PdfApi.md#get_page_popup_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/popup | Read document page popup annotations.
*PdfApi* | [**get_page_redaction_annotations**](docs/PdfApi.md#get_page_redaction_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/redaction | Read document page redaction annotations.
*PdfApi* | [**get_page_screen_annotations**](docs/PdfApi.md#get_page_screen_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/screen | Read document page screen annotations.
*PdfApi* | [**get_page_sound_annotations**](docs/PdfApi.md#get_page_sound_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/sound | Read document page sound annotations.
*PdfApi* | [**get_page_square_annotations**](docs/PdfApi.md#get_page_square_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/square | Read document page square annotations.
*PdfApi* | [**get_page_squiggly_annotations**](docs/PdfApi.md#get_page_squiggly_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/squiggly | Read document page squiggly annotations.
*PdfApi* | [**get_page_stamp_annotations**](docs/PdfApi.md#get_page_stamp_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/stamp | Read document page stamp annotations.
*PdfApi* | [**get_page_stamps**](docs/PdfApi.md#get_page_stamps) | **GET** /pdf/\{name}/pages/\{pageNumber}/stamps | Read page document stamps.
*PdfApi* | [**get_page_strike_out_annotations**](docs/PdfApi.md#get_page_strike_out_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/strikeout | Read document page StrikeOut annotations.
*PdfApi* | [**get_page_tables**](docs/PdfApi.md#get_page_tables) | **GET** /pdf/\{name}/pages/\{pageNumber}/tables | Read document page tables.
*PdfApi* | [**get_page_text**](docs/PdfApi.md#get_page_text) | **GET** /pdf/\{name}/pages/\{pageNumber}/text | Read page text items.
*PdfApi* | [**get_page_text_annotations**](docs/PdfApi.md#get_page_text_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/text | Read document page text annotations.
*PdfApi* | [**get_page_underline_annotations**](docs/PdfApi.md#get_page_underline_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/underline | Read document page underline annotations.
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
*PdfApi* | [**get_pdf_in_storage_to_xlsx**](docs/PdfApi.md#get_pdf_in_storage_to_xlsx) | **GET** /pdf/\{name}/convert/xlsx | Converts PDF document (located on storage) to XLSX format and returns resulting file in response content
*PdfApi* | [**get_pdf_in_storage_to_xml**](docs/PdfApi.md#get_pdf_in_storage_to_xml) | **GET** /pdf/\{name}/convert/xml | Converts PDF document (located on storage) to XML format and returns resulting file in response content
*PdfApi* | [**get_pdf_in_storage_to_xps**](docs/PdfApi.md#get_pdf_in_storage_to_xps) | **GET** /pdf/\{name}/convert/xps | Converts PDF document (located on storage) to XPS format and returns resulting file in response content
*PdfApi* | [**get_poly_line_annotation**](docs/PdfApi.md#get_poly_line_annotation) | **GET** /pdf/\{name}/annotations/polyline/\{annotationId} | Read document page polyline annotation by ID.
*PdfApi* | [**get_polygon_annotation**](docs/PdfApi.md#get_polygon_annotation) | **GET** /pdf/\{name}/annotations/polygon/\{annotationId} | Read document page polygon annotation by ID.
*PdfApi* | [**get_popup_annotation**](docs/PdfApi.md#get_popup_annotation) | **GET** /pdf/\{name}/annotations/popup/\{annotationId} | Read document page popup annotation by ID.
*PdfApi* | [**get_ps_in_storage_to_pdf**](docs/PdfApi.md#get_ps_in_storage_to_pdf) | **GET** /pdf/create/ps | Convert PS file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_redaction_annotation**](docs/PdfApi.md#get_redaction_annotation) | **GET** /pdf/\{name}/annotations/redaction/\{annotationId} | Read document page redaction annotation by ID.
*PdfApi* | [**get_screen_annotation**](docs/PdfApi.md#get_screen_annotation) | **GET** /pdf/\{name}/annotations/screen/\{annotationId} | Read document page screen annotation by ID.
*PdfApi* | [**get_screen_annotation_data**](docs/PdfApi.md#get_screen_annotation_data) | **GET** /pdf/\{name}/annotations/screen/\{annotationId}/data | Read document page screen annotation by ID.
*PdfApi* | [**get_sound_annotation**](docs/PdfApi.md#get_sound_annotation) | **GET** /pdf/\{name}/annotations/sound/\{annotationId} | Read document page sound annotation by ID.
*PdfApi* | [**get_sound_annotation_data**](docs/PdfApi.md#get_sound_annotation_data) | **GET** /pdf/\{name}/annotations/sound/\{annotationId}/data | Read document page sound annotation by ID.
*PdfApi* | [**get_square_annotation**](docs/PdfApi.md#get_square_annotation) | **GET** /pdf/\{name}/annotations/square/\{annotationId} | Read document page square annotation by ID.
*PdfApi* | [**get_squiggly_annotation**](docs/PdfApi.md#get_squiggly_annotation) | **GET** /pdf/\{name}/annotations/squiggly/\{annotationId} | Read document page squiggly annotation by ID.
*PdfApi* | [**get_stamp_annotation**](docs/PdfApi.md#get_stamp_annotation) | **GET** /pdf/\{name}/annotations/stamp/\{annotationId} | Read document page stamp annotation by ID.
*PdfApi* | [**get_stamp_annotation_data**](docs/PdfApi.md#get_stamp_annotation_data) | **GET** /pdf/\{name}/annotations/stamp/\{annotationId}/data | Read document page stamp annotation by ID.
*PdfApi* | [**get_strike_out_annotation**](docs/PdfApi.md#get_strike_out_annotation) | **GET** /pdf/\{name}/annotations/strikeout/\{annotationId} | Read document page StrikeOut annotation by ID.
*PdfApi* | [**get_svg_in_storage_to_pdf**](docs/PdfApi.md#get_svg_in_storage_to_pdf) | **GET** /pdf/create/svg | Convert SVG file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_table**](docs/PdfApi.md#get_table) | **GET** /pdf/\{name}/tables/\{tableId} | Read document page table by ID.
*PdfApi* | [**get_text**](docs/PdfApi.md#get_text) | **GET** /pdf/\{name}/text | Read document text.
*PdfApi* | [**get_text_annotation**](docs/PdfApi.md#get_text_annotation) | **GET** /pdf/\{name}/annotations/text/\{annotationId} | Read document page text annotation by ID.
*PdfApi* | [**get_underline_annotation**](docs/PdfApi.md#get_underline_annotation) | **GET** /pdf/\{name}/annotations/underline/\{annotationId} | Read document page underline annotation by ID.
*PdfApi* | [**get_verify_signature**](docs/PdfApi.md#get_verify_signature) | **GET** /pdf/\{name}/verifySignature | Verify signature document.
*PdfApi* | [**get_web_in_storage_to_pdf**](docs/PdfApi.md#get_web_in_storage_to_pdf) | **GET** /pdf/create/web | Convert web page to PDF format and return resulting file in response. 
*PdfApi* | [**get_words_per_page**](docs/PdfApi.md#get_words_per_page) | **GET** /pdf/\{name}/pages/wordCount | Get number of words per document page.
*PdfApi* | [**get_xfa_pdf_in_storage_to_acro_form**](docs/PdfApi.md#get_xfa_pdf_in_storage_to_acro_form) | **GET** /pdf/\{name}/convert/xfatoacroform | Converts PDF document which contatins XFA form (located on storage) to PDF with AcroForm and returns resulting file response content
*PdfApi* | [**get_xml_in_storage_to_pdf**](docs/PdfApi.md#get_xml_in_storage_to_pdf) | **GET** /pdf/create/xml | Convert XML file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_xps_in_storage_to_pdf**](docs/PdfApi.md#get_xps_in_storage_to_pdf) | **GET** /pdf/create/xps | Convert XPS file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**get_xsl_fo_in_storage_to_pdf**](docs/PdfApi.md#get_xsl_fo_in_storage_to_pdf) | **GET** /pdf/create/xslfo | Convert XslFo file (located on storage) to PDF format and return resulting file in response. 
*PdfApi* | [**post_append_document**](docs/PdfApi.md#post_append_document) | **POST** /pdf/\{name}/appendDocument | Append document to existing one.
*PdfApi* | [**post_change_password_document_in_storage**](docs/PdfApi.md#post_change_password_document_in_storage) | **POST** /pdf/\{name}/changepassword | Change document password in storage.
*PdfApi* | [**post_create_field**](docs/PdfApi.md#post_create_field) | **POST** /pdf/\{name}/fields | Create field.
*PdfApi* | [**post_decrypt_document_in_storage**](docs/PdfApi.md#post_decrypt_document_in_storage) | **POST** /pdf/\{name}/decrypt | Decrypt document in storage.
*PdfApi* | [**post_document_image_footer**](docs/PdfApi.md#post_document_image_footer) | **POST** /pdf/\{name}/footer/image | Add document image footer.
*PdfApi* | [**post_document_image_header**](docs/PdfApi.md#post_document_image_header) | **POST** /pdf/\{name}/header/image | Add document image header.
*PdfApi* | [**post_document_page_number_stamps**](docs/PdfApi.md#post_document_page_number_stamps) | **POST** /pdf/\{name}/stamps/pagenumber | Add document page number stamps.
*PdfApi* | [**post_document_text_footer**](docs/PdfApi.md#post_document_text_footer) | **POST** /pdf/\{name}/footer/text | Add document text footer.
*PdfApi* | [**post_document_text_header**](docs/PdfApi.md#post_document_text_header) | **POST** /pdf/\{name}/header/text | Add document text header.
*PdfApi* | [**post_document_text_replace**](docs/PdfApi.md#post_document_text_replace) | **POST** /pdf/\{name}/text/replace | Document&#39;s replace text method.
*PdfApi* | [**post_encrypt_document_in_storage**](docs/PdfApi.md#post_encrypt_document_in_storage) | **POST** /pdf/\{name}/encrypt | Encrypt document in storage.
*PdfApi* | [**post_flatten_document**](docs/PdfApi.md#post_flatten_document) | **POST** /pdf/\{name}/flatten | Flatten the document.
*PdfApi* | [**post_insert_image**](docs/PdfApi.md#post_insert_image) | **POST** /pdf/\{name}/pages/\{pageNumber}/images | Insert image to document page.
*PdfApi* | [**post_move_file**](docs/PdfApi.md#post_move_file) | **POST** /storage/file | Move a specific file
*PdfApi* | [**post_move_folder**](docs/PdfApi.md#post_move_folder) | **POST** /storage/folder | Move a specific folder 
*PdfApi* | [**post_move_page**](docs/PdfApi.md#post_move_page) | **POST** /pdf/\{name}/pages/\{pageNumber}/movePage | Move page to new position.
*PdfApi* | [**post_optimize_document**](docs/PdfApi.md#post_optimize_document) | **POST** /pdf/\{name}/optimize | Optimize document.
*PdfApi* | [**post_page_caret_annotations**](docs/PdfApi.md#post_page_caret_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/caret | Add document page caret annotations.
*PdfApi* | [**post_page_circle_annotations**](docs/PdfApi.md#post_page_circle_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/circle | Add document page circle annotations.
*PdfApi* | [**post_page_file_attachment_annotations**](docs/PdfApi.md#post_page_file_attachment_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/fileattachment | Add document page FileAttachment annotations.
*PdfApi* | [**post_page_free_text_annotations**](docs/PdfApi.md#post_page_free_text_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/freetext | Add document page free text annotations.
*PdfApi* | [**post_page_highlight_annotations**](docs/PdfApi.md#post_page_highlight_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/highlight | Add document page highlight annotations.
*PdfApi* | [**post_page_image_stamps**](docs/PdfApi.md#post_page_image_stamps) | **POST** /pdf/\{name}/pages/\{pageNumber}/stamps/image | Add document page image stamps.
*PdfApi* | [**post_page_ink_annotations**](docs/PdfApi.md#post_page_ink_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/ink | Add document page ink annotations.
*PdfApi* | [**post_page_line_annotations**](docs/PdfApi.md#post_page_line_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/line | Add document page line annotations.
*PdfApi* | [**post_page_link_annotations**](docs/PdfApi.md#post_page_link_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/links | Add document page link annotations.
*PdfApi* | [**post_page_movie_annotations**](docs/PdfApi.md#post_page_movie_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/movie | Add document page movie annotations.
*PdfApi* | [**post_page_pdf_page_stamps**](docs/PdfApi.md#post_page_pdf_page_stamps) | **POST** /pdf/\{name}/pages/\{pageNumber}/stamps/pdfpage | Add document pdf page stamps.
*PdfApi* | [**post_page_poly_line_annotations**](docs/PdfApi.md#post_page_poly_line_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/polyline | Add document page polyline annotations.
*PdfApi* | [**post_page_polygon_annotations**](docs/PdfApi.md#post_page_polygon_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/polygon | Add document page polygon annotations.
*PdfApi* | [**post_page_redaction_annotations**](docs/PdfApi.md#post_page_redaction_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/redaction | Add document page redaction annotations.
*PdfApi* | [**post_page_screen_annotations**](docs/PdfApi.md#post_page_screen_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/screen | Add document page screen annotations.
*PdfApi* | [**post_page_sound_annotations**](docs/PdfApi.md#post_page_sound_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/sound | Add document page sound annotations.
*PdfApi* | [**post_page_square_annotations**](docs/PdfApi.md#post_page_square_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/square | Add document page square annotations.
*PdfApi* | [**post_page_squiggly_annotations**](docs/PdfApi.md#post_page_squiggly_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/squiggly | Add document page squiggly annotations.
*PdfApi* | [**post_page_stamp_annotations**](docs/PdfApi.md#post_page_stamp_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/stamp | Add document page stamp annotations.
*PdfApi* | [**post_page_strike_out_annotations**](docs/PdfApi.md#post_page_strike_out_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/strikeout | Add document page StrikeOut annotations.
*PdfApi* | [**post_page_tables**](docs/PdfApi.md#post_page_tables) | **POST** /pdf/\{name}/pages/\{pageNumber}/tables | Add document page tables.
*PdfApi* | [**post_page_text_annotations**](docs/PdfApi.md#post_page_text_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/text | Add document page text annotations.
*PdfApi* | [**post_page_text_replace**](docs/PdfApi.md#post_page_text_replace) | **POST** /pdf/\{name}/pages/\{pageNumber}/text/replace | Page&#39;s replace text method.
*PdfApi* | [**post_page_text_stamps**](docs/PdfApi.md#post_page_text_stamps) | **POST** /pdf/\{name}/pages/\{pageNumber}/stamps/text | Add document page text stamps.
*PdfApi* | [**post_page_underline_annotations**](docs/PdfApi.md#post_page_underline_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/underline | Add document page underline annotations.
*PdfApi* | [**post_popup_annotation**](docs/PdfApi.md#post_popup_annotation) | **POST** /pdf/\{name}/annotations/\{annotationId}/popup | Add document popup annotations.
*PdfApi* | [**post_sign_document**](docs/PdfApi.md#post_sign_document) | **POST** /pdf/\{name}/sign | Sign document.
*PdfApi* | [**post_sign_page**](docs/PdfApi.md#post_sign_page) | **POST** /pdf/\{name}/pages/\{pageNumber}/sign | Sign page.
*PdfApi* | [**post_split_document**](docs/PdfApi.md#post_split_document) | **POST** /pdf/\{name}/split | Split document to parts.
*PdfApi* | [**put_add_new_page**](docs/PdfApi.md#put_add_new_page) | **PUT** /pdf/\{name}/pages | Add new page to end of the document.
*PdfApi* | [**put_add_text**](docs/PdfApi.md#put_add_text) | **PUT** /pdf/\{name}/pages/\{pageNumber}/text | Add text to PDF document page.
*PdfApi* | [**put_annotations_flatten**](docs/PdfApi.md#put_annotations_flatten) | **PUT** /pdf/\{name}/annotations/flatten | Flattens the annotations of the specified types
*PdfApi* | [**put_caret_annotation**](docs/PdfApi.md#put_caret_annotation) | **PUT** /pdf/\{name}/annotations/caret/\{annotationId} | Replace document caret annotation
*PdfApi* | [**put_change_password_document**](docs/PdfApi.md#put_change_password_document) | **PUT** /pdf/changepassword | Change document password from content.
*PdfApi* | [**put_circle_annotation**](docs/PdfApi.md#put_circle_annotation) | **PUT** /pdf/\{name}/annotations/circle/\{annotationId} | Replace document circle annotation
*PdfApi* | [**put_create**](docs/PdfApi.md#put_create) | **PUT** /storage/file | Upload a specific file 
*PdfApi* | [**put_create_document**](docs/PdfApi.md#put_create_document) | **PUT** /pdf/\{name} | Create empty document.
*PdfApi* | [**put_create_folder**](docs/PdfApi.md#put_create_folder) | **PUT** /storage/folder | Create the folder 
*PdfApi* | [**put_decrypt_document**](docs/PdfApi.md#put_decrypt_document) | **PUT** /pdf/decrypt | Decrypt document from content.
*PdfApi* | [**put_encrypt_document**](docs/PdfApi.md#put_encrypt_document) | **PUT** /pdf/encrypt | Encrypt document from content.
*PdfApi* | [**put_epub_in_storage_to_pdf**](docs/PdfApi.md#put_epub_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/epub | Convert EPUB file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_fields_flatten**](docs/PdfApi.md#put_fields_flatten) | **PUT** /pdf/\{name}/fields/flatten | Flatten form fields in document.
*PdfApi* | [**put_file_attachment_annotation**](docs/PdfApi.md#put_file_attachment_annotation) | **PUT** /pdf/\{name}/annotations/fileattachment/\{annotationId} | Replace document FileAttachment annotation
*PdfApi* | [**put_file_attachment_annotation_data_extract**](docs/PdfApi.md#put_file_attachment_annotation_data_extract) | **PUT** /pdf/\{name}/annotations/fileattachment/\{annotationId}/data/extract | Extract document FileAttachment annotation content to storage
*PdfApi* | [**put_free_text_annotation**](docs/PdfApi.md#put_free_text_annotation) | **PUT** /pdf/\{name}/annotations/freetext/\{annotationId} | Replace document free text annotation
*PdfApi* | [**put_highlight_annotation**](docs/PdfApi.md#put_highlight_annotation) | **PUT** /pdf/\{name}/annotations/highlight/\{annotationId} | Replace document highlight annotation
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
*PdfApi* | [**put_ink_annotation**](docs/PdfApi.md#put_ink_annotation) | **PUT** /pdf/\{name}/annotations/ink/\{annotationId} | Replace document ink annotation
*PdfApi* | [**put_la_te_x_in_storage_to_pdf**](docs/PdfApi.md#put_la_te_x_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/latex | Convert LaTeX file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_line_annotation**](docs/PdfApi.md#put_line_annotation) | **PUT** /pdf/\{name}/annotations/line/\{annotationId} | Replace document line annotation
*PdfApi* | [**put_link_annotation**](docs/PdfApi.md#put_link_annotation) | **PUT** /pdf/\{name}/links/\{linkId} | Replace document page link annotations
*PdfApi* | [**put_merge_documents**](docs/PdfApi.md#put_merge_documents) | **PUT** /pdf/\{name}/merge | Merge a list of documents.
*PdfApi* | [**put_mht_in_storage_to_pdf**](docs/PdfApi.md#put_mht_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/mht | Convert MHT file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_movie_annotation**](docs/PdfApi.md#put_movie_annotation) | **PUT** /pdf/\{name}/annotations/movie/\{annotationId} | Replace document movie annotation
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
*PdfApi* | [**put_pdf_in_request_to_xlsx**](docs/PdfApi.md#put_pdf_in_request_to_xlsx) | **PUT** /pdf/convert/xlsx | Converts PDF document (in request content) to XLSX format and uploads resulting file to storage.
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
*PdfApi* | [**put_pdf_in_storage_to_xlsx**](docs/PdfApi.md#put_pdf_in_storage_to_xlsx) | **PUT** /pdf/\{name}/convert/xlsx | Converts PDF document (located on storage) to XLSX format and uploads resulting file to storage
*PdfApi* | [**put_pdf_in_storage_to_xml**](docs/PdfApi.md#put_pdf_in_storage_to_xml) | **PUT** /pdf/\{name}/convert/xml | Converts PDF document (located on storage) to XML format and uploads resulting file to storage
*PdfApi* | [**put_pdf_in_storage_to_xps**](docs/PdfApi.md#put_pdf_in_storage_to_xps) | **PUT** /pdf/\{name}/convert/xps | Converts PDF document (located on storage) to XPS format and uploads resulting file to storage
*PdfApi* | [**put_poly_line_annotation**](docs/PdfApi.md#put_poly_line_annotation) | **PUT** /pdf/\{name}/annotations/polyline/\{annotationId} | Replace document polyline annotation
*PdfApi* | [**put_polygon_annotation**](docs/PdfApi.md#put_polygon_annotation) | **PUT** /pdf/\{name}/annotations/polygon/\{annotationId} | Replace document polygon annotation
*PdfApi* | [**put_popup_annotation**](docs/PdfApi.md#put_popup_annotation) | **PUT** /pdf/\{name}/annotations/popup/\{annotationId} | Replace document popup annotation
*PdfApi* | [**put_privileges**](docs/PdfApi.md#put_privileges) | **PUT** /pdf/\{name}/privileges | Update privilege document.
*PdfApi* | [**put_ps_in_storage_to_pdf**](docs/PdfApi.md#put_ps_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/ps | Convert PS file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_redaction_annotation**](docs/PdfApi.md#put_redaction_annotation) | **PUT** /pdf/\{name}/annotations/redaction/\{annotationId} | Replace document redaction annotation
*PdfApi* | [**put_replace_image**](docs/PdfApi.md#put_replace_image) | **PUT** /pdf/\{name}/images/\{imageId} | Replace document image.
*PdfApi* | [**put_screen_annotation**](docs/PdfApi.md#put_screen_annotation) | **PUT** /pdf/\{name}/annotations/screen/\{annotationId} | Replace document screen annotation
*PdfApi* | [**put_screen_annotation_data_extract**](docs/PdfApi.md#put_screen_annotation_data_extract) | **PUT** /pdf/\{name}/annotations/screen/\{annotationId}/data/extract | Extract document screen annotation content to storage
*PdfApi* | [**put_searchable_document**](docs/PdfApi.md#put_searchable_document) | **PUT** /pdf/\{name}/ocr | Create searchable PDF document. Generate OCR layer for images in input PDF document.
*PdfApi* | [**put_set_property**](docs/PdfApi.md#put_set_property) | **PUT** /pdf/\{name}/documentproperties/\{propertyName} | Add/update document property.
*PdfApi* | [**put_sound_annotation**](docs/PdfApi.md#put_sound_annotation) | **PUT** /pdf/\{name}/annotations/sound/\{annotationId} | Replace document sound annotation
*PdfApi* | [**put_sound_annotation_data_extract**](docs/PdfApi.md#put_sound_annotation_data_extract) | **PUT** /pdf/\{name}/annotations/sound/\{annotationId}/data/extract | Extract document sound annotation content to storage
*PdfApi* | [**put_square_annotation**](docs/PdfApi.md#put_square_annotation) | **PUT** /pdf/\{name}/annotations/square/\{annotationId} | Replace document square annotation
*PdfApi* | [**put_squiggly_annotation**](docs/PdfApi.md#put_squiggly_annotation) | **PUT** /pdf/\{name}/annotations/squiggly/\{annotationId} | Replace document squiggly annotation
*PdfApi* | [**put_stamp_annotation**](docs/PdfApi.md#put_stamp_annotation) | **PUT** /pdf/\{name}/annotations/stamp/\{annotationId} | Replace document stamp annotation
*PdfApi* | [**put_stamp_annotation_data_extract**](docs/PdfApi.md#put_stamp_annotation_data_extract) | **PUT** /pdf/\{name}/annotations/stamp/\{annotationId}/data/extract | Extract document stamp annotation content to storage
*PdfApi* | [**put_strike_out_annotation**](docs/PdfApi.md#put_strike_out_annotation) | **PUT** /pdf/\{name}/annotations/strikeout/\{annotationId} | Replace document StrikeOut annotation
*PdfApi* | [**put_svg_in_storage_to_pdf**](docs/PdfApi.md#put_svg_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/svg | Convert SVG file (located on storage) to PDF format and upload resulting file to storage. 
*PdfApi* | [**put_table**](docs/PdfApi.md#put_table) | **PUT** /pdf/\{name}/tables/\{tableId} | Replace document page table.
*PdfApi* | [**put_text_annotation**](docs/PdfApi.md#put_text_annotation) | **PUT** /pdf/\{name}/annotations/text/\{annotationId} | Replace document text annotation
*PdfApi* | [**put_underline_annotation**](docs/PdfApi.md#put_underline_annotation) | **PUT** /pdf/\{name}/annotations/underline/\{annotationId} | Replace document underline annotation
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
 - [BorderCornerStyle](docs/BorderCornerStyle.md)
 - [BorderInfo](docs/BorderInfo.md)
 - [CapStyle](docs/CapStyle.md)
 - [CaptionPosition](docs/CaptionPosition.md)
 - [CaretSymbol](docs/CaretSymbol.md)
 - [Cell](docs/Cell.md)
 - [CellRecognized](docs/CellRecognized.md)
 - [Color](docs/Color.md)
 - [ColorDepth](docs/ColorDepth.md)
 - [ColumnAdjustment](docs/ColumnAdjustment.md)
 - [CompressionType](docs/CompressionType.md)
 - [CryptoAlgorithm](docs/CryptoAlgorithm.md)
 - [DiscUsage](docs/DiscUsage.md)
 - [DocFormat](docs/DocFormat.md)
 - [DocRecognitionMode](docs/DocRecognitionMode.md)
 - [DocumentPrivilege](docs/DocumentPrivilege.md)
 - [EpubRecognitionMode](docs/EpubRecognitionMode.md)
 - [FieldType](docs/FieldType.md)
 - [File](docs/File.md)
 - [FileExist](docs/FileExist.md)
 - [FileIcon](docs/FileIcon.md)
 - [FontEncodingRules](docs/FontEncodingRules.md)
 - [FontSavingModes](docs/FontSavingModes.md)
 - [FontStyles](docs/FontStyles.md)
 - [FreeTextIntent](docs/FreeTextIntent.md)
 - [GraphInfo](docs/GraphInfo.md)
 - [HorizontalAlignment](docs/HorizontalAlignment.md)
 - [HtmlDocumentType](docs/HtmlDocumentType.md)
 - [HtmlMarkupGenerationModes](docs/HtmlMarkupGenerationModes.md)
 - [ImageSrcType](docs/ImageSrcType.md)
 - [ImageTemplate](docs/ImageTemplate.md)
 - [ImageTemplatesRequest](docs/ImageTemplatesRequest.md)
 - [Justification](docs/Justification.md)
 - [LettersPositioningMethods](docs/LettersPositioningMethods.md)
 - [LineEnding](docs/LineEnding.md)
 - [LineIntent](docs/LineIntent.md)
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
 - [PermissionsFlags](docs/PermissionsFlags.md)
 - [Point](docs/Point.md)
 - [PolyIntent](docs/PolyIntent.md)
 - [Position](docs/Position.md)
 - [RasterImagesSavingModes](docs/RasterImagesSavingModes.md)
 - [Rectangle](docs/Rectangle.md)
 - [Rotation](docs/Rotation.md)
 - [Row](docs/Row.md)
 - [RowRecognized](docs/RowRecognized.md)
 - [Segment](docs/Segment.md)
 - [ShapeType](docs/ShapeType.md)
 - [Signature](docs/Signature.md)
 - [SignatureType](docs/SignatureType.md)
 - [SoundEncoding](docs/SoundEncoding.md)
 - [SoundIcon](docs/SoundIcon.md)
 - [SplitResult](docs/SplitResult.md)
 - [Stamp](docs/Stamp.md)
 - [StampIcon](docs/StampIcon.md)
 - [StampType](docs/StampType.md)
 - [TableBroken](docs/TableBroken.md)
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
 - [CaretAnnotationResponse](docs/CaretAnnotationResponse.md)
 - [CaretAnnotations](docs/CaretAnnotations.md)
 - [CaretAnnotationsResponse](docs/CaretAnnotationsResponse.md)
 - [CircleAnnotationResponse](docs/CircleAnnotationResponse.md)
 - [CircleAnnotations](docs/CircleAnnotations.md)
 - [CircleAnnotationsResponse](docs/CircleAnnotationsResponse.md)
 - [DiscUsageResponse](docs/DiscUsageResponse.md)
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
 - [FileAttachmentAnnotationResponse](docs/FileAttachmentAnnotationResponse.md)
 - [FileAttachmentAnnotations](docs/FileAttachmentAnnotations.md)
 - [FileAttachmentAnnotationsResponse](docs/FileAttachmentAnnotationsResponse.md)
 - [FileExistResponse](docs/FileExistResponse.md)
 - [FileVersion](docs/FileVersion.md)
 - [FileVersionsResponse](docs/FileVersionsResponse.md)
 - [FilesResponse](docs/FilesResponse.md)
 - [FreeTextAnnotationResponse](docs/FreeTextAnnotationResponse.md)
 - [FreeTextAnnotations](docs/FreeTextAnnotations.md)
 - [FreeTextAnnotationsResponse](docs/FreeTextAnnotationsResponse.md)
 - [HighlightAnnotationResponse](docs/HighlightAnnotationResponse.md)
 - [HighlightAnnotations](docs/HighlightAnnotations.md)
 - [HighlightAnnotationsResponse](docs/HighlightAnnotationsResponse.md)
 - [Image](docs/Image.md)
 - [ImageResponse](docs/ImageResponse.md)
 - [Images](docs/Images.md)
 - [ImagesResponse](docs/ImagesResponse.md)
 - [InkAnnotationResponse](docs/InkAnnotationResponse.md)
 - [InkAnnotations](docs/InkAnnotations.md)
 - [InkAnnotationsResponse](docs/InkAnnotationsResponse.md)
 - [LineAnnotationResponse](docs/LineAnnotationResponse.md)
 - [LineAnnotations](docs/LineAnnotations.md)
 - [LineAnnotationsResponse](docs/LineAnnotationsResponse.md)
 - [LinkAnnotation](docs/LinkAnnotation.md)
 - [LinkAnnotationResponse](docs/LinkAnnotationResponse.md)
 - [LinkAnnotations](docs/LinkAnnotations.md)
 - [LinkAnnotationsResponse](docs/LinkAnnotationsResponse.md)
 - [MovieAnnotationResponse](docs/MovieAnnotationResponse.md)
 - [MovieAnnotations](docs/MovieAnnotations.md)
 - [MovieAnnotationsResponse](docs/MovieAnnotationsResponse.md)
 - [Page](docs/Page.md)
 - [Pages](docs/Pages.md)
 - [PolyLineAnnotationResponse](docs/PolyLineAnnotationResponse.md)
 - [PolyLineAnnotations](docs/PolyLineAnnotations.md)
 - [PolyLineAnnotationsResponse](docs/PolyLineAnnotationsResponse.md)
 - [PolygonAnnotationResponse](docs/PolygonAnnotationResponse.md)
 - [PolygonAnnotations](docs/PolygonAnnotations.md)
 - [PolygonAnnotationsResponse](docs/PolygonAnnotationsResponse.md)
 - [PopupAnnotationResponse](docs/PopupAnnotationResponse.md)
 - [PopupAnnotations](docs/PopupAnnotations.md)
 - [PopupAnnotationsResponse](docs/PopupAnnotationsResponse.md)
 - [RedactionAnnotationResponse](docs/RedactionAnnotationResponse.md)
 - [RedactionAnnotations](docs/RedactionAnnotations.md)
 - [RedactionAnnotationsResponse](docs/RedactionAnnotationsResponse.md)
 - [ScreenAnnotationResponse](docs/ScreenAnnotationResponse.md)
 - [ScreenAnnotations](docs/ScreenAnnotations.md)
 - [ScreenAnnotationsResponse](docs/ScreenAnnotationsResponse.md)
 - [SignatureVerifyResponse](docs/SignatureVerifyResponse.md)
 - [SoundAnnotationResponse](docs/SoundAnnotationResponse.md)
 - [SoundAnnotations](docs/SoundAnnotations.md)
 - [SoundAnnotationsResponse](docs/SoundAnnotationsResponse.md)
 - [SplitResultDocument](docs/SplitResultDocument.md)
 - [SplitResultResponse](docs/SplitResultResponse.md)
 - [SquareAnnotationResponse](docs/SquareAnnotationResponse.md)
 - [SquareAnnotations](docs/SquareAnnotations.md)
 - [SquareAnnotationsResponse](docs/SquareAnnotationsResponse.md)
 - [SquigglyAnnotationResponse](docs/SquigglyAnnotationResponse.md)
 - [SquigglyAnnotations](docs/SquigglyAnnotations.md)
 - [SquigglyAnnotationsResponse](docs/SquigglyAnnotationsResponse.md)
 - [StampAnnotationResponse](docs/StampAnnotationResponse.md)
 - [StampAnnotations](docs/StampAnnotations.md)
 - [StampAnnotationsResponse](docs/StampAnnotationsResponse.md)
 - [StampBase](docs/StampBase.md)
 - [StampInfo](docs/StampInfo.md)
 - [StampsInfo](docs/StampsInfo.md)
 - [StampsInfoResponse](docs/StampsInfoResponse.md)
 - [StorageExistResponse](docs/StorageExistResponse.md)
 - [StrikeOutAnnotationResponse](docs/StrikeOutAnnotationResponse.md)
 - [StrikeOutAnnotations](docs/StrikeOutAnnotations.md)
 - [StrikeOutAnnotationsResponse](docs/StrikeOutAnnotationsResponse.md)
 - [Table](docs/Table.md)
 - [TableRecognized](docs/TableRecognized.md)
 - [TableRecognizedResponse](docs/TableRecognizedResponse.md)
 - [TablesRecognized](docs/TablesRecognized.md)
 - [TablesRecognizedResponse](docs/TablesRecognizedResponse.md)
 - [TextAnnotationResponse](docs/TextAnnotationResponse.md)
 - [TextAnnotations](docs/TextAnnotations.md)
 - [TextAnnotationsResponse](docs/TextAnnotationsResponse.md)
 - [TextRectsResponse](docs/TextRectsResponse.md)
 - [TextReplaceResponse](docs/TextReplaceResponse.md)
 - [UnderlineAnnotationResponse](docs/UnderlineAnnotationResponse.md)
 - [UnderlineAnnotations](docs/UnderlineAnnotations.md)
 - [UnderlineAnnotationsResponse](docs/UnderlineAnnotationsResponse.md)
 - [WordCountResponse](docs/WordCountResponse.md)
 - [AnnotationInfo](docs/AnnotationInfo.md)
 - [ImageFooter](docs/ImageFooter.md)
 - [ImageHeader](docs/ImageHeader.md)
 - [ImageStamp](docs/ImageStamp.md)
 - [MarkupAnnotation](docs/MarkupAnnotation.md)
 - [MovieAnnotation](docs/MovieAnnotation.md)
 - [PageNumberStamp](docs/PageNumberStamp.md)
 - [PdfPageStamp](docs/PdfPageStamp.md)
 - [PopupAnnotation](docs/PopupAnnotation.md)
 - [RedactionAnnotation](docs/RedactionAnnotation.md)
 - [ScreenAnnotation](docs/ScreenAnnotation.md)
 - [TextFooter](docs/TextFooter.md)
 - [TextHeader](docs/TextHeader.md)
 - [TextStamp](docs/TextStamp.md)
 - [CaretAnnotation](docs/CaretAnnotation.md)
 - [CommonFigureAnnotation](docs/CommonFigureAnnotation.md)
 - [FileAttachmentAnnotation](docs/FileAttachmentAnnotation.md)
 - [FreeTextAnnotation](docs/FreeTextAnnotation.md)
 - [HighlightAnnotation](docs/HighlightAnnotation.md)
 - [InkAnnotation](docs/InkAnnotation.md)
 - [LineAnnotation](docs/LineAnnotation.md)
 - [PolyAnnotation](docs/PolyAnnotation.md)
 - [PopupAnnotationWithParent](docs/PopupAnnotationWithParent.md)
 - [SoundAnnotation](docs/SoundAnnotation.md)
 - [SquigglyAnnotation](docs/SquigglyAnnotation.md)
 - [StampAnnotation](docs/StampAnnotation.md)
 - [StrikeOutAnnotation](docs/StrikeOutAnnotation.md)
 - [TextAnnotation](docs/TextAnnotation.md)
 - [UnderlineAnnotation](docs/UnderlineAnnotation.md)
 - [CircleAnnotation](docs/CircleAnnotation.md)
 - [PolyLineAnnotation](docs/PolyLineAnnotation.md)
 - [PolygonAnnotation](docs/PolygonAnnotation.md)
 - [SquareAnnotation](docs/SquareAnnotation.md)

