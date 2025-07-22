![](https://img.shields.io/badge/api-v3.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/asposepdfcloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/asposepdfcloud) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/asposepdfcloud) [![GitHub license](https://img.shields.io/github/license/aspose-pdf-cloud/aspose-pdf-cloud-python)](https://github.com/aspose-pdf-cloud/aspose-pdf-cloud-python/blob/master/LICENSE)

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

## Enhancements in Version 25.7
- Add possibility to hide subject field in signature appearance.
- A new version of Aspose.PDF Cloud was prepared using the latest version of Aspose.PDF for .NET.

## Bugs fixed in Version 25.7
- PostDeleteStamps removing stamps from PDF page is incorrect.

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

## Get PDF Page Annotations in Python
```python
	# Get your ClientId and ClientSecret from https://dashboard.aspose.cloud (free registration required).
	pdf_api_client = asposepdfcloud.ApiClient('MY_CLIENT_SECRET', 'MY_CLIENT_ID')
	pdf_api = asposepdfcloud.PdfApi(pdf_api_client)
	file_name = 'PdfWithAnnotations.pdf'
	page_number = 2
	response = pdf_api.get_page_annotations(file_name, page_number, folder=temp_folder)
```

## SelfHost Aspose.PDF Cloud
Create **ApiClient** object without **app_key** and **app_sid** parameters, but with **host** parameter set to *url of SelfHost Aspose.PDF Cloud* and **self_host** parameter set to *True*:
```python
	pdf_api_client = asposepdfcloud.ApiClient('', '', 'MY_SELFHOST_URL', True)
```

## Unit Tests
Aspose PDF SDK includes a suite of unit tests within the "test" subdirectory. These Unit Tests also serves as examples of how to use the Aspose PDF SDK.

## Licensing
All Aspose.PDF Cloud SDKs are licensed under [MIT License](LICENSE).
