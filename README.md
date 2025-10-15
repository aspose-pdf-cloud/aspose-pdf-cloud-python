![](https://img.shields.io/badge/api-v3.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/asposepdfcloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/asposepdfcloud) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/asposepdfcloud) [![GitHub license](https://img.shields.io/github/license/aspose-pdf-cloud/aspose-pdf-cloud-python)](https://github.com/aspose-pdf-cloud/aspose-pdf-cloud-python/blob/master/LICENSE)

# ⚠️ Deprecated Package: `asposepdfcloud`

> **This package is deprecated and no longer maintained.**

The ***[asposepdfcloud](https://pypi.org/project/asposepdfcloud/)*** Python package has been **deprecated** in favor of the new unified **[aspose-pdf-cloud](https://pypi.org/project/aspose-pdf-cloud/)** package.

## 🚀 What You Should Do

**Please migrate to the new package immediately:**

```bash
# Uninstall the old package
pip uninstall asposepdfcloud

# Install the new, actively maintained package
pip install aspose-pdf-cloud
```

# Python REST API to Process PDF in Cloud
[Aspose.PDF Cloud](https://products.aspose.cloud/pdf) is a true REST API that enables you to perform a wide range of document processing operations including creation, manipulation, conversion and rendering of PDF documents in the cloud.

Our Cloud SDKs are wrappers around REST API in various programming languages, allowing you to process documents in language of your choice quickly and easily, gaining all benefits of strong types and IDE highlights. This repository contains new generation SDKs for Aspose.PDF Cloud and examples.

These SDKs are now fully supported. If you have any questions, see any bugs or have enhancement request, feel free to reach out to us at [Free Support Forums](https://forum.aspose.cloud/c/pdf).

Extract Text & Images of a PDF document online https://products.aspose.app/pdf/parser.

## PDF Processing Features
- Add PDF document's header & footer in text or image format.
- Add tables & stamps (text or image) to PDF documents.
- Append multiple PDF documents to an existing file.
- Work with PDF attachments, annotations, & form fields.
- Apply encryption or decryption to PDF documents & set a password.
- Delete all stamps & tables from a page or entire PDF document.
- Delete a specific stamp or table from the PDF document by its ID.
- Replace single or multiple instances of text on a PDF page or from the entire document.
- Extensive support for converting PDF documents to various other file formats.
- Extract various elements of PDF files & make PDF documents optimized.

## Read & Write PDF Formats
PDF, EPUB, HTML, TeX, SVG, XML, XPS, FDF, XFDF

## Save PDF As
XLS, XLSX, PPTX, DOC, DOCX, MobiXML, JPEG, EMF, PNG, BMP, GIF, TIFF, Text

## Read PDF Formats
MHT, PCL, PS, XSLFO, MD

## Enhancements in Version 25.9
- A new version of Aspose.PDF Cloud was prepared using the latest version of Aspose.PDF for .NET.

## Requirements.
Python 2.7 and 3.4+

## Platform Independence

Aspose.Pdf Cloud’s platform independent document manipulation API is a true REST API that can be used from any platform. You can use it with any language or platform that supports REST, be it the web, desktop, mobile, or the cloud. The API integrates with other cloud services to provide you the flexibility you require for processing documents. It is suitable for the most types of businesses, documents, or content.

## Getting Started with Aspose.Pdf Cloud SDK for Python

Firstly, create an account at [Aspose for Cloud](https://dashboard.aspose.cloud/#/apps) to get your application information and free quota to use the API.
Now execute from the command line command to fetch the SDK. 
```sh
pip install asposepdfcloud
```

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/aspose-pdf-cloud/aspose-pdf-cloud-python.git
```


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

## SelfHost Aspose.PDF Cloud
Create **ApiClient** object without **client_secret** and **client_id** parameters, but with **host** parameter set to *url of [SelfHost Aspose.PDF Cloud](https://hub.docker.com/r/aspose/pdf-cloud)* and **self_host** parameter set to *True*:
```python
	pdf_api_client = asposepdfcloud.ApiClient('', '', 'MY_SELFHOST_URL', True)
```

## Examples

#### Get PDF Page Annotations in Python
```python
	# Get your ClientId and ClientSecret from https://dashboard.aspose.cloud (free registration required).
	pdf_api_client = asposepdfcloud.ApiClient('MY_CLIENT_SECRET', 'MY_CLIENT_ID')
	pdf_api = asposepdfcloud.PdfApi(pdf_api_client)
	file_name = 'PdfWithAnnotations.pdf'
	page_number = 2
	response = pdf_api.get_page_annotations(file_name, page_number, folder=temp_folder)
```

Aspose PDF Cloud SDK includes a suite of uses cases within the "[Uses-Cases](Uses-Cases)" subdirectory. These folder serves as examples of how to use the Aspose PDF Cloud SDK:

#### Annotations
- **[`annotations_helper.py`](Uses-Cases/Annotations/annotations_helper.py)** – Provides configuration and helper methods for managing PDF annotations, including file upload/download and popup annotation deletion.
- **[`annotations_launch.py`](Uses-Cases/Annotations/annotations_launch.py)** – Runs a full annotation workflow: get, add (highlight/strikeout/underline/free text), delete, and replace annotations in a PDF.
- **[`delete_page_annotations.py`](Uses-Cases/Annotations/delete_page_annotations.py)** – Deletes all annotations from a specified page in a PDF document.
- **[`delete_text_annotation.py`](Uses-Cases/Annotations/delete_text_annotation.py)** – Deletes a specific text annotation by its ID from a PDF document.
- **[`get_annotation_by_id.py`](Uses-Cases/Annotations/get_annotation_by_id.py)** – Retrieves a specific annotation by its ID from a PDF document.
- **[`get_annotations.py`](Uses-Cases/Annotations/get_annotations.py)** – Retrieves all annotations from a specified page in a PDF document.
- **[`new_highlight_annotation.py`](Uses-Cases/Annotations/new_highlight_annotation.py)** – Adds a new highlight annotation to a PDF document.
- **[`new_strikeout_annotation.py`](Uses-Cases/Annotations/new_strikeout_annotation.py)** – Adds a new strikeout annotation to a PDF document.
- **[`new_text_annotation.py`](Uses-Cases/Annotations/new_text_annotation.py)** – Adds a new free text annotation to a PDF document.
- **[`new_underline_annotation.py`](Uses-Cases/Annotations/new_underline_annotation.py)** – Adds a new underline annotation to a PDF document.
- **[`replace_annotation.py`](Uses-Cases/Annotations/replace_annotation.py)** – Replaces an existing annotation with new content in a PDF document.

#### Attachments
- **[`appendAttachments.py`](Uses-Cases/Attachments/add/appendAttachments.py)** – Appends a new attachment (e.g., video file) to a PDF document.
- **[`getAttachmentAndSave.py`](Uses-Cases/Attachments/get/getAttachmentAndSave.py)** – Retrieves attachments from a PDF document and saves them locally.

#### Bookmarks
- **[`appendBookmarks.py`](Uses-Cases/Bookmarks/add/appendBookmarks.py)** – Adds a new bookmark to a PDF document.
- **[`getBookmarkByPathAndShow.py`](Uses-Cases/Bookmarks/get/getBookmarkByPathAndShow.py)** – Retrieves and displays a specific bookmark by its path.
- **[`getBookmarksAndShow.py`](Uses-Cases/Bookmarks/get/getBookmarksAndShow.py)** – Retrieves and displays all bookmarks in a PDF document.
- **[`removeBookmark.py`](Uses-Cases/Bookmarks/remove/removeBookmark.py)** – Removes a specific bookmark by its path from a PDF document.
- **[`replaceBookmark.py`](Uses-Cases/Bookmarks/replace/replaceBookmark.py)** – Replaces an existing bookmark with a new title or properties.

#### ChangeLayout
- **[`change_layout_helper.py`](Uses-Cases/ChangeLayout/change_layout_helper.py)** – Provides helper methods for PDF layout changes: rotation, resizing, cropping, and page extraction.
- **[`change_layout_launch.py`](Uses-Cases/ChangeLayout/change_layout_launch.py)** – Executes layout modification workflows: crop pages, resize all pages, and rotate document pages.
- **[`crop_document_page.py`](Uses-Cases/ChangeLayout/crop_document_page.py)** – Crops a specific page in a PDF document to a defined rectangle.
- **[`resize_document_all_pages.py`](Uses-Cases/ChangeLayout/resize_document_all_pages.py)** – Resizes all pages in a PDF document to new dimensions.
- **[`rotate_documents_pages.py`](Uses-Cases/ChangeLayout/rotate_documents_pages.py)** – Rotates specified pages in a PDF document by a given angle.

#### Compares
- **[`compare_pdf_documents.py`](Uses-Cases/Compares/compare_pdf_documents.py)** – Compares two PDF documents and generates a difference report.
- **[`compares_helper.py`](Uses-Cases/Compares/compares_helper.py)** – Provides helper methods for comparing PDF documents, including file upload and download.
- **[`compares_launch.py`](Uses-Cases/Compares/compares_launch.py)** – Launches the PDF comparison workflow.

#### CompressDocument
- **[`compressPdf.py`](Uses-Cases/CompressDocument/compressPdf.py)** – Compresses a PDF document by optimizing images, removing unused objects, and more.

#### CreateDocument
- **[`createPdf.py`](Uses-Cases/CreateDocument/createPdf.py)** – Creates a new PDF document with custom properties, display settings, and multiple pages.
- **[`createPdfSimple.py`](Uses-Cases/CreateDocument/createPdfSimple.py)** – Creates a simple empty PDF document and downloads it.

#### EncryptDecrypt
- **[`decryptDocument.py`](Uses-Cases/EncryptDecrypt/decryptDocument.py)** – Decrypts a password-protected PDF document.
- **[`encryptDocument.py`](Uses-Cases/EncryptDecrypt/encryptDocument.py)** – Encrypts a PDF document with user and owner passwords using a specified algorithm.

#### Links
- **[`appendLink.py`](Uses-Cases/Links/add/appendLink.py)** – Adds a new hyperlink annotation to a PDF page.
- **[`getLinksAndShow.py`](Uses-Cases/Links/get/getLinksAndShow.py)** – Retrieves and displays all hyperlink annotations in a PDF document.
- **[`removeLink.py`](Uses-Cases/Links/remove/removeLink.py)** – Removes a specific hyperlink annotation by its ID.
- **[`replaceLink.py`](Uses-Cases/Links/replace/replaceLink.py)** – Replaces an existing hyperlink annotation with a new URL.

#### Pages
- **[`appendNewPage.py`](Uses-Cases/Pages/add/appendNewPage.py)** – Appends a new page to the end of a PDF document.
- **[`getPageInfoAndSavePng.py`](Uses-Cases/Pages/get/getPageInfoAndSavePng.py)** – Retrieves page information and saves a specific page as a PNG image.
- **[`movePageNewPosition.py`](Uses-Cases/Pages/move/movePageNewPosition.py)** – Moves a page to a new position within the PDF document.
- **[`removePage.py`](Uses-Cases/Pages/remove/removePage.py)** – Deletes a specific page from a PDF document.
- **[`pageAppendTextStamp.py`](Uses-Cases/Pages/stamp/pageAppendTextStamp.py)** – Adds a text stamp to a specific page in a PDF document.
- **[`wordsCountOnPages.py`](Uses-Cases/Pages/wordsCount/wordsCountOnPages.py)** – Retrieves the word count for each page in a PDF document.

#### Parser
- **[`get_fdf.py`](Uses-Cases/Parser/get_fdf.py)** – Exports PDF form fields to an FDF file.
- **[`get_images.py`](Uses-Cases/Parser/get_images.py)** – Extracts images from a specific page in a PDF document.
- **[`get_tables.py`](Uses-Cases/Parser/get_tables.py)** – Extracts tables from a PDF document and saves them as JSON.
- **[`get_textboxes.py`](Uses-Cases/Parser/get_textboxes.py)** – Extracts text box fields from a PDF document and saves them as JSON.
- **[`get_xml.py`](Uses-Cases/Parser/get_xml.py)** – Exports PDF form fields to an XML file.
- **[`paresr_helpers.py`](Uses-Cases/Parser/paresr_helpers.py)** – Provides helper methods for parsing PDF elements like forms, images, tables, and text boxes.
- **[`parser_launch.py`](Uses-Cases/Parser/parser_launch.py)** – Runs a full parsing workflow: export forms to XML/FDF, extract images, tables, and text boxes.

#### Signatures
- **[`addDocumentSignature.py`](Uses-Cases/Signatures/addDocumentSignature.py)** – Adds a digital signature to a PDF document.
- **[`getDocumentSignatures.py`](Uses-Cases/Signatures/getDocumentSignatures.py)** – Retrieves and displays all signature fields in a PDF document.
- **[`replaceDocumentSignature.py`](Uses-Cases/Signatures/replaceDocumentSignature.py)** – Replaces an existing digital signature in a PDF document.
- **[`verifySignature.py`](Uses-Cases/Signatures/verifySignature.py)** – Verifies the validity of a digital signature in a PDF document.

#### Split
- **[`splitPages.py`](Uses-Cases/Split/splitPages.py)** – Splits a PDF document into individual pages.
- **[`splitRanges.py`](Uses-Cases/Split/splitRanges.py)** – Splits a PDF document into specified page ranges.

#### Stamps
- **[`appendStamps.py`](Uses-Cases/Stamps/add/appendStamps.py)** – Adds text and image stamps to a PDF document.
- **[`removeStamps.py`](Uses-Cases/Stamps/remove/removeStamps.py)** – Removes stamps from a PDF document, either by page or by stamp ID.

#### Tables
- **[`appendTable.py`](Uses-Cases/Tables/add/appendTable.py)** – Appends a new table to a PDF document page.
- **[`getTablesAndShow.py`](Uses-Cases/Tables/get/getTablesAndShow.py)** – Retrieves and displays all tables in a PDF document.
- **[`removeTables.py`](Uses-Cases/Tables/remove/removeTables.py)** – Deletes tables from a PDF document, either by table ID or all tables on a page.
- **[`replaceTable.py`](Uses-Cases/Tables/replace/replaceTable.py)** – Replaces an existing table in a PDF document with a new one.

#### Texts
- **[`replaceTexts.py`](Uses-Cases/Texts/replace/replaceTexts.py)** – Replaces text in a PDF document, either globally or on a specific page.

## Licensing
All Aspose.PDF Cloud SDKs are licensed under [MIT License](LICENSE).