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

## Breaking Changes in Version 25.10
**Authentication Parameter Changes**:

    AppId → ClientId

    AppSecret → ClientSecret

## Enhancements in Version 25.10
- A new version of Aspose.PDF Cloud was prepared using the latest version of Aspose.PDF for .NET.

## Bugs fixed in Version 25.10
- Method PutBookmark does not change bookmark color.
- TextReplace shows hidden text in the output file.
## Requirements.
Python 2.7 and 3.4+

## Platform Independence

Aspose.Pdf Cloud's platform independent document manipulation API is a true REST API that can be used from any platform. You can use it with any language or platform that supports REST, be it the web, desktop, mobile, or the cloud. The API integrates with other cloud services to provide you the flexibility you require for processing documents. It is suitable for the most types of businesses, documents, or content.

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

## Get PDF Page Annotations in Python
```python
	# Get your ClientId and ClientSecret from https://dashboard.aspose.cloud (free registration required).
	pdf_api_client = asposepdfcloud.ApiClient('MY_CLIENT_SECRET', 'MY_CLIENT_ID')
	pdf_api = asposepdfcloud.PdfApi(pdf_api_client)
	file_name = 'sample.pdf'
	page_number = 1
	response = pdf_api.get_page_annotations(file_name, page_number, folder=temp_folder)
```

## SelfHost Aspose.PDF Cloud
Create **ApiClient** object without **client_secret** and **client_id** parameters, but with **host** parameter set to *url of [SelfHost Aspose.PDF Cloud](https://hub.docker.com/r/aspose/pdf-cloud)* and **self_host** parameter set to *True*:
```python
	pdf_api_client = asposepdfcloud.ApiClient('', '', 'MY_SELFHOST_URL', True)
```

## Use cases

The Aspose.PDF Cloud SDK includes a set of ready-to-run use cases in the "[Uses-Cases](Uses-Cases)" directory. These examples illustrate common operations such as managing annotations, attachments, text, and more.

1. Add your API credentials **client_id** and **client_secret** into [settings/credentials.json](settings/credentials.json):

```
{
  "client_secret": "YOUR_CLIENT_SECRET",
  "client_id": "YOUR_CLIENT_ID"
}
```
2. Launch use case:
```
python Uses-Cases/Annotations/annotations_launch.py
```

## Unit Tests
Aspose PDF SDK includes a suite of unit tests. These Unit Tests also serves as examples of how to use the Aspose PDF SDK.

## Licensing
All Aspose.PDF Cloud SDKs are licensed under [MIT License](LICENSE).
