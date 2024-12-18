# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


Copyright (c) 2024 Aspose.PDF Cloud
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



    OpenAPI spec version: 3.0
    
"""


import sys
from setuptools import setup, find_packages

NAME = "asposepdfcloud"
VERSION = "24.12.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi >= 14.05.14", "python-dateutil >= 2.5.3", "setuptools >= 21.0.0"]

setup(
    name=NAME,
    version=VERSION,
    description="Aspose.PDF Cloud",
    long_description='''Aspose.PDF Cloud is a REST API for creating and editing PDF files.
 Most popular features proposed by Aspose.PDF Cloud: PDF to Word, Convert PDF to Image, Merge PDF, Split PDF, Add Images to PDF, Rotate PDF.
 It can also be used to convert PDF files to different formats like DOC, HTML, XPS, TIFF and many more.
 Aspose.PDF Cloud gives you control: create PDFs from scratch or from HTML, XML, template, database, XPS or an image.
 Render PDFs to image formats such as JPEG, PNG, GIF, BMP, TIFF and many others.
 Aspose.PDF Cloud helps you manipulate elements of a PDF file like text, annotations, watermarks, signatures, bookmarks, stamps and so on.
 Its REST API also allows you to manage PDF pages by using features like merging, splitting, and inserting.
 Add images to a PDF file or convert PDF pages to images.''',
    author_email="",
    url="https://products.aspose.cloud/pdf/cloud",
    author='Aspose PDF Cloud',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords=[        "Aspose",
        "Cloud",
        "PDF",
        "Aspose.PDF",
        "Aspose.PDF-Cloud",
        "Aspose.Total-Cloud",
        "REST",
        "API",
        "EPUB",
        "HTML",
        "TEX",
        "MHT",
        "PCL",
        "PS",
        "PostScript",
        "SVG",
        "XML",
        "XPS",
        "XSLFO",
        "MD",
        "Markdown",
        "XLS",
        "XLSX",
        "PPTX",
        "DOC",
        "DOCX",
        "EPUB",
        "HTML",
        "MobiXML",
        "SVG",
        "JPEG",
        "EMF",
        "PNG",
        "BMP",
        "GIF",
        "TIFF",
        "XML",
        "XPS",
        "Text",
        "FDF",
        "XFDF",
        "PDFA3",
        "PDF-to-DOC",
        "PDF-to-DOCX",
        "PDF-to-HTML",
        "PDF-to-PDFA",
        "PDF-to-TIFF",
        "PDF-to-SVG",
        "PDF-to-EPUB",
        "PDF-to-PPTX",
        "PDF-to-TEX",
        "PDF-to-MobiXML",
        "PDF-to-XFA",
        "PDF-to-XML",
        "PDF-to-XPS",
        "PDF-to-XLS",
        "EPUB-to-PDF",
        "Web-to-PDF",
        "TEX-to-PDF",
        "MHT-to-PDF",
        "HTML-to-PDF",
        "PS-to-PDF",
        "PostScript-to-PDF",
        "XSIF-to-PDF",
        "XPS-to-PDF",
        "SVG-to-PDF",
        "DOC-to-PDF",
        "DOCX-to-PDF",
        "PCL-to-PDF",
        "XML-to-PDF",
        "Markdown-to-PDF",
        "MD-to-PDF",
        "Annotation",
        "Line-Annotation",
        "Circle-Annotation",
        "Square-Annotation",
        "Underline-Annotation",
        "Squiggly-Annotation",
        "PDF-Bookmark",
        "PDF-Link",
        "PDF-Attachment",
        "PDF-Document",
        "PDF-Page",
        "PDF-Form-Fields",
        "PDF-Text",
        "PDF-Image",
        "Replace-Text",
        "Fetch-Text",
        "Replace-Image",
        "Extract-Image",
        "Convert-PDF",
        "Convert",
        "Converter",
        "PDF-to-Image",
        "Create-PDF",
        "Convert-PDF",
        "Stamp",
        "PDF-OCR",
        "OCR-Layers",
        ".NET",
        "C#",
        "dotnet",
        "CSharp"
    ],
    install_requires=REQUIRES,
    extras_require={ 
        'test': ["requests >= 2.18.4",
                "coverage >= 4.0.3",
                "nose >= 1.3.7",
                "pluggy >= 0.3.1",
                "py >= 1.4.31",
                "randomize >= 0.13"],
    },
    packages=find_packages(exclude=['test']),
    project_urls={ 
        'Source With Tests': 'https://github.com/aspose-pdf-cloud/aspose-pdf-cloud-python',
        'Website': 'https://www.aspose.cloud',
        'Product Home': 'https://products.aspose.cloud/pdf/cloud',
        'Documentation': 'https://docs.aspose.cloud/display/pdfcloud/Home',
        'Free Support Forum': 'https://forum.aspose.cloud/c/pdf',
        'Paid Support Helpdesk': 'https://helpdesk.aspose.cloud/',
        'Blog': 'https://blog.aspose.cloud/category/aspose-products/aspose-pdf-product-family/',
    },
)
