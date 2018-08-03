# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


   Copyright (c) 2018 Aspose.PDF Cloud
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



    OpenAPI spec version: 1.1

"""


from __future__ import absolute_import

import os
import sys
import unittest
import json

import asposepdfcloud
from asposepdfcloud.apis.pdf_api import PdfApi
from asposepdfcloud.rest import ApiException
from asposepdfcloud.models.annotation_response import AnnotationResponse
from asposepdfcloud.models.http_status_code import HttpStatusCode


class PdfTests(unittest.TestCase):

    def setUp(self):
        with open('test/setup.json') as json_file:
            data = json.load(json_file)
            
            self.pdf_api_client = asposepdfcloud.api_client.ApiClient(
                                app_key=str(data['app_key']),
                                app_sid=str(data['app_sid']),
                                host=str(data['product_uri']))

            self.pdf_api = PdfApi(self.pdf_api_client)

            self.output_path = str(data['output_location'])

            self.temp_folder = 'TempPdfCloud'
            self.test_data_path = 'test_data/'


    def uploadFile(self, name):
        self.pdf_api.put_create(self.temp_folder + '/' + name, self.test_data_path + name)

    def tearDown(self):
        pass

    
    # Annotations Tests

    def testGetPageAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, HttpStatusCode.OK)

    
    # Append Tests

    def testPostAppendDocumentUsingQueryParams(self):
        file_name = 'PdfWithImages2.pdf'
        append_file_name = '4pages.pdf'

        self.uploadFile(file_name)
        self.uploadFile(append_file_name)

        opts = {
          "append_file" : self.temp_folder + '/' + append_file_name,
          "start_page" : 2,
          "end_page" : 4,
          "folder" : self.temp_folder
        }

        response = self.pdf_api.post_append_document(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPostAppendDocumentUsingBodyParams(self):
        file_name = 'PdfWithImages2.pdf'
        append_file_name = '4pages.pdf'

        self.uploadFile(file_name)
        self.uploadFile(append_file_name)

        append_document = asposepdfcloud.models.AppendDocument(self.temp_folder + '/' + append_file_name, start_page=2, end_page=4)


        opts = {
            "append_document" : append_document,
            "folder" : self.temp_folder
        }

        response = self.pdf_api.post_append_document(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    # Attachments Tests

    def testGetDocumentAttachmentByIndex(self):
        file_name = 'PdfWithEmbeddedFiles.pdf'
        self.uploadFile(file_name)

        attachment_index = 1
        opts = {
            "folder" : self.temp_folder
        }

        response = self.pdf_api.get_document_attachment_by_index(file_name, attachment_index, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    
    def testGetDocumentAttachments(self):
        file_name = 'PdfWithEmbeddedFiles.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_document_attachments(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)
     
    

    def testGetDownloadDocumentAttachmentByIndex(self):
        file_name = 'PdfWithEmbeddedFiles.pdf'
        self.uploadFile(file_name)

        attachment_index = 1
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_download_document_attachment_by_index(file_name, attachment_index, **opts)
        self.assertIsInstance(response, str);
    

    # Bookmarks Tests

    def testGetDocumentBookmarks(self):
        file_name = 'PdfWithBookmarks.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_document_bookmarks(file_name, **opts)
        self.assertIsInstance(response, str)
    
    # Document Save As Tiff Tests

    def testPutDocumentSaveAsTiffUsingQueryParams(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        opts = {
              "result_file" : '4pages.tiff',
              "brightness" : 0.6,
              "compression" : asposepdfcloud.models.CompressionType.CCITT4,
              "color_depth" : asposepdfcloud.models.ColorDepth.FORMAT1BPP,
              "left_margin" : 0,
              "right_margin" : 0,
              "top_margin" : 0,
              "bottom_margin" : 0,
              "orientation" : asposepdfcloud.models.ShapeType.PORTRAIT, 
              "skip_blank_pages" : True,
              "width" : 1200,
              "height" : 1600,
              "x_resolution" : 200,
              "y_resolution" : 200,
              "page_index" : 2,
              "page_count" : 2,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_document_save_as_tiff(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPutDocumentSaveAsTiffUsingBodyParams(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        export_options = asposepdfcloud.models.TiffExportOptions()
        export_options.result_file = '4pages.tiff'
        export_options.brightness = 0.6
        export_options.compression = asposepdfcloud.models.CompressionType.CCITT4
        export_options.color_depth = asposepdfcloud.models.ColorDepth.FORMAT1BPP
        export_options.left_margin = 0
        export_options.right_margin = 0
        export_options.top_margin = 0
        export_options.bottom_margin = 0
        export_options.orientation = asposepdfcloud.models.ShapeType.PORTRAIT
        export_options.skip_blank_pages = True
        export_options.width = 1200
        export_options.height = 1600
        export_options.x_resolution = 200
        export_options.y_resolution = 200
        export_options.page_index = 2
        export_options.page_count = 2

        opts = {
              "export_options" : export_options,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_document_save_as_tiff(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)

    
    
    # Document Tests

    def testGetDocument(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_document(file_name, **opts)
        self.assertIsInstance(response, str)


    def testPostOptimizeDocument(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        optimize_options = asposepdfcloud.models.OptimizeOptions(
                allow_reuse_page_content=False,
                compress_images=True,
                image_quality=100,
                link_duplcate_streams=True,
                remove_unused_objects=True,
                remove_unused_streams=True,            
                unembed_fonts=True)
        
        opts = {
            "options" : optimize_options,
            "folder" : self.temp_folder
        }

        response = self.pdf_api.post_optimize_document(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)



    def testPostSplitDocument(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }
        response = self.pdf_api.post_split_document(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPutConvertDocument(self):
        url = 'http://pdf995.com/samples/pdf.pdf'
        format = 'tiff'

        opts = {
              "format" : format,
              "url" : url
        }

        response = self.pdf_api.put_convert_document(**opts)
        self.assertIsInstance(response, str)


    def testPutCreateEmptyDocument(self):
        file_name = 'empty.pdf'

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_create_document(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPutCreateDocument(self):
        file_name = 'HtmlExample1.pdf'
        template_name = 'HtmlExample1.html'

        self.uploadFile(template_name)

        opts = {
              "template_file" : self.temp_folder + '/' + template_name,
              "template_type" : 'html',
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_create_document(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPutCreateDocumentFromImages(self):
        image_1 = '33539.jpg'
        self.uploadFile(image_1)

        image_2 = '44781.jpg'
        self.uploadFile(image_2)

        result_doc_name = 'pdffromimagesinquery.pdf'

        images_list = [self.temp_folder + '/' + image_1,  self.temp_folder + '/' + image_2]
        images = asposepdfcloud.models.ImagesListRequest(images_list)
        
        opts = {
              "images" : images,
              "ocr" : False,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_create_document_from_images(result_doc_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)    
    

    # Fields Tests

    def testGetField(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }
        field_name = 'textField'

        response = self.pdf_api.get_field(file_name, field_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetFields(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_fields(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPostCreateField(self):
        file_name = 'Hello_world.pdf'
        self.uploadFile(file_name)

        rect = asposepdfcloud.models.Rectangle(x=50, y=200, width=150, height=200)

        field = asposepdfcloud.models.Field()
        field.name = 'checkboxfield'
        field.values = ['1']
        field.type = 'Boolean'
        field.rect = rect

        page_number = 1

        opts = {
              "field" : field,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.post_create_field(file_name, page_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPutUpdateField(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        field_name = 'textField'

        field = asposepdfcloud.models.Field()
        field.name = field_name
        field.values = ['Text field updated value.']
        field.type = asposepdfcloud.models.FieldType.TEXT

        opts = {
              "field" : field,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_update_field(file_name, field_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)
    

    def testDeleteField(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }
        field_name = 'textField'

        response = self.pdf_api.delete_field(file_name, field_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPutFieldsFlatten(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_fields_flatten(file_name,  **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    # Fragments And Segments Tests

    def testGetFragment(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 1
        fragment_number = 1

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_fragment(file_name, page_number, fragment_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetFragmentTextFormat(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 1
        fragment_number = 1

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_fragment_text_format(file_name, page_number, fragment_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetFragments(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 1

        opts = {
              "folder" : self.temp_folder
        }
        response = self.pdf_api.get_fragments(file_name, page_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetSegment(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 1
        fragment_number = 1
        segment_number = 1

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_segment(file_name, page_number, fragment_number, segment_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetSegmentTextFormat(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 1
        fragment_number = 1
        segment_number = 1

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_segment_text_format(file_name, page_number, fragment_number, segment_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetSegments(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 1
        fragment_number = 1

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_segments(file_name, page_number, fragment_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)

    
    # Images Tests

    def testGetImage(self):
        file_name = 'PdfWithImages2.pdf'
        self.uploadFile(file_name)

        page_number = 1
        image_number = 1
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_image(file_name, page_number, image_number, **opts)
        self.assertIsInstance(response, str)

    def testGetImageWithFormat(self):
        file_name = 'PdfWithImages2.pdf'
        self.uploadFile(file_name)

        page_number = 1
        image_number = 1
        opts = {
              "format" : "jpeg", 
              "height" : 100,
              "width" : 100,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_image(file_name, page_number, image_number, **opts)
        self.assertIsInstance(response, str)

    def testGetImages(self):
        file_name = 'PdfWithImages2.pdf'
        self.uploadFile(file_name)

        page_number = 1
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_images(file_name, page_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPostReplaceImage(self):
        file_name = 'PdfWithImages2.pdf'
        self.uploadFile(file_name)

        image_file_name = 'Koala.jpg'
        self.uploadFile(image_file_name)

        page_number = 1
        image_number = 1
        opts = {
              "image_file" : self.temp_folder + '/' + image_file_name,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.post_replace_image(file_name, page_number, image_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)

    def testPostReplaceImageFromRequest(self):
        file_name = 'PdfWithImages2.pdf'
        self.uploadFile(file_name)

        image_file_name = 'Koala.jpg'

        page_number = 1
        image_number = 1
        opts = {
              "image" : self.test_data_path + image_file_name,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.post_replace_image(file_name, page_number, image_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)
    
    def testPutImagesExtractAsJpeg(self):
        name = "PdfWithImages2.pdf"
        self.uploadFile(name)
        page_number = 1

        dest_folder = "extract_jpg"
        opts = {
            "dest_folder": self.temp_folder + '/' + dest_folder,
            "folder": self.temp_folder
        }
        response = self.pdf_api.put_images_extract_as_jpeg(name, page_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)

    def testPutImagesExtractAsTiff(self):
        name = "PdfWithImages2.pdf"
        self.uploadFile(name)
        page_number = 1

        dest_folder = "extract_tiff"
        opts = {
            "dest_folder": self.temp_folder + '/' + dest_folder,
            "folder": self.temp_folder
        }
        response = self.pdf_api.put_images_extract_as_tiff(name, page_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPutImagesExtractAsGif(self):
        name = "PdfWithImages2.pdf"
        self.uploadFile(name)
        page_number = 1

        dest_folder = "extract_gif"
        opts = {
            "dest_folder": self.temp_folder + '/' + dest_folder,
            "folder": self.temp_folder
        }
        response = self.pdf_api.put_images_extract_as_gif(name, page_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPutImagesExtractAsPng(self):
        name = "PdfWithImages2.pdf"
        self.uploadFile(name)
        page_number = 1

        dest_folder = "extract_png"
        opts = {
            "dest_folder": self.temp_folder + '/' + dest_folder,
            "folder": self.temp_folder
        }
        response = self.pdf_api.put_images_extract_as_png(name, page_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    # Links Tests

    def testGetPageLinkAnnotationByIndex(self):
        file_name = 'PdfWithLinks.pdf'
        self.uploadFile(file_name)

        page_number = 1
        link_index = 1
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_page_link_annotation_by_index(file_name, page_number, link_index, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetPageLinkAnnotations(self):
        file_name = 'PdfWithLinks.pdf'
        self.uploadFile(file_name)

        page_number = 1
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_page_link_annotations(file_name, page_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)

    
    # Merge Tests

    def testPutMergeDocuments(self):
        file_name_list = ['4pages.pdf', 'PdfWithImages2.pdf', 'marketing.pdf']
        for file_name in file_name_list:
            self.uploadFile(file_name)
        
        result_name = 'MergingResult.pdf'

        merge_documents = asposepdfcloud.models.MergeDocuments()
        
        i = 0
        for el in file_name_list:
            file_name_list[i] = self.temp_folder + '/' + el
            i += 1

        merge_documents.list = file_name_list


        opts = {
              "merge_documents" : merge_documents,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_merge_documents(result_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)

    
    # Pages Tests

    def testDeletePage(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 1
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.delete_page(file_name, page_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetPage(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 3
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_page(file_name, page_number, **opts)
        self.assertIsInstance(response, str)

    def testGetPageWithFormat(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 3
        opts = {
              "format" : "jpeg", 
              "width" : 100,
              "height" : 100,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_page(file_name, page_number, **opts)
        self.assertIsInstance(response, str)

    def testGetPages(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_pages(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetWordsPerPage(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_words_per_page(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPostMovePage(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }
        page_number = 1
        new_index = 1

        response = self.pdf_api.post_move_page(file_name, page_number, new_index, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPutAddNewPage(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_add_new_page(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPutPageAddStamp(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        stamp_file_name = 'Penguins.jpg'
        self.uploadFile(stamp_file_name)

        page_number = 1

        stamp = asposepdfcloud.models.Stamp(type=asposepdfcloud.models.StampType.IMAGE)
        stamp.file_name = self.temp_folder + '/' + stamp_file_name
        stamp.background = True
        stamp.width = 200
        stamp.height = 200
        stamp.x_indent = 100
        stamp.y_indent = 100

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_page_add_stamp(file_name, page_number, stamp, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)
    
    
    # Paragraphs Tests

    def testPutAddText(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 1

        rectangle = asposepdfcloud.models.Rectangle(x=100, y=100, width=200, height=200)
        
        foreground_color = asposepdfcloud.models.Color(a=0x00, r=0x00, g=0xFF, b=0x00)
        
        background_color = asposepdfcloud.models.Color(a=0x00, r=0xFF, g=0x00, b=0x00)
        
        text_state = asposepdfcloud.models.TextState(
                    font_size=10, 
                    font='Arial', 
                    foreground_color=foreground_color,
                    background_color=background_color,
                    font_style=asposepdfcloud.models.FontStyles.BOLD)

        segment = asposepdfcloud.models.Segment()
        segment.value = 'segment 1'
        segment.text_state = text_state

        text_line = asposepdfcloud.models.TextLine()
        text_line.horizontal_alignment = asposepdfcloud.models.TextHorizontalAlignment.RIGHT
        text_line.segments = [segment]

        paragraph = asposepdfcloud.models.Paragraph(lines=[text_line])
        paragraph.rectangle = rectangle
        paragraph.left_margin = 10
        paragraph.right_margin = 10
        paragraph.top_margin = 20
        paragraph.bottom_margin = 20
        paragraph.horizontal_alignment = asposepdfcloud.models.TextHorizontalAlignment.FULLJUSTIFY
        paragraph.line_spacing = asposepdfcloud.models.LineSpacing.FONTSIZE
        paragraph.rotation = 10
        paragraph.subsequent_lines_indent = 20
        paragraph.vertical_alignment = asposepdfcloud.models.VerticalAlignment.CENTER
        paragraph.wrap_mode = asposepdfcloud.models.WrapMode.BYWORDS
        

        opts = {
              "paragraph" : paragraph,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_add_text(file_name, page_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)

    
    # Properties Tests

    def testDeleteProperties(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        property_1 = asposepdfcloud.models.DocumentProperty()
        property_1.name = 'prop1'
        property_1.value = 'val1'

        opts_1 = {
              "_property" : property_1,
              "folder" : self.temp_folder
        }

        property_2 = asposepdfcloud.models.DocumentProperty()
        property_2.name = 'prop2'
        property_2.value = 'val2'

        opts_2 = {
              "_property" : property_2,
              "folder" : self.temp_folder
        }

        self.pdf_api.put_set_property(file_name, property_1.name, **opts_1)
        self.pdf_api.put_set_property(file_name, property_2.name, **opts_2)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.delete_properties(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testDeleteProperty(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        property_1 = asposepdfcloud.models.DocumentProperty()
        property_1.name = 'prop1'
        property_1.value = 'val1'

        opts_1 = {
              "_property" : property_1,
              "folder" : self.temp_folder
        }

        self.pdf_api.put_set_property(file_name, property_1.name, **opts_1)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.delete_property(file_name, property_1.name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetDocumentProperties(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        property_1 = asposepdfcloud.models.DocumentProperty()
        property_1.name = 'prop1'
        property_1.value = 'val1'

        opts_1 = {
              "_property" : property_1,
              "folder" : self.temp_folder
        }

        property_2 = asposepdfcloud.models.DocumentProperty()
        property_2.name = 'prop2'
        property_2.value = 'val2'

        opts_2 = {
              "_property" : property_2,
              "folder" : self.temp_folder
        }

        self.pdf_api.put_set_property(file_name, property_1.name, **opts_1)
        self.pdf_api.put_set_property(file_name, property_2.name, **opts_2)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_document_properties(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetDocumentProperty(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        property_1 = asposepdfcloud.models.DocumentProperty()
        property_1.name = 'prop1'
        property_1.value = 'val1'

        opts_1 = {
              "_property" : property_1,
              "folder" : self.temp_folder
        }

        self.pdf_api.put_set_property(file_name, property_1.name, **opts_1)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_document_property(file_name, property_1.name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPutSetProperty(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        property_1 = asposepdfcloud.models.DocumentProperty()
        property_1.name = 'prop1'
        property_1.value = 'val1'

        opts_1 = {
              "_property" : property_1,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_set_property(file_name, property_1.name, **opts_1)
        self.assertEqual(response.code, HttpStatusCode.OK)


    # Sign Tests

    def testPostSignDocument(self):
        file_name = 'BlankWithSignature.pdf'
        self.uploadFile(file_name)

        signature_file_name = 'test1234.pfx'
        self.uploadFile(signature_file_name)

        rectangle = asposepdfcloud.models.Rectangle(x=100, y=100, width=400, height=100)
        
        signature = asposepdfcloud.models.Signature(
                signature_path=self.temp_folder + '/' + signature_file_name,
                signature_type=asposepdfcloud.models.SignatureType.PKCS_7,
                password='test1234',
                contact='testself.mail.ru',
                location='Ukraine',
                visible=True,
                rectangle=rectangle,
                form_field_name='Signature1',
                authority='Sergey Smal',
                date='08/01/2012 12:15:00.000 PM',
                show_properties=False)

        opts = {
              "signature" : signature,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.post_sign_document(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPostSignPage(self):
        file_name = 'BlankWithSignature.pdf'
        self.uploadFile(file_name)

        signature_file_name = 'test1234.pfx'
        self.uploadFile(signature_file_name)

        page_number = 1

        rectangle = asposepdfcloud.models.Rectangle(x=100, y=100, width=400, height=100)

        signature = asposepdfcloud.models.Signature(
                signature_path=self.temp_folder + '/' + signature_file_name,
                signature_type=asposepdfcloud.models.SignatureType.PKCS_7,
                password='test1234',
                contact='testself.mail.ru',
                location='Ukraine',
                visible=True,
                rectangle=rectangle,
                form_field_name='Signature1',
                authority='Sergey Smal',
                date='08/01/2012 12:15:00.000 PM',
                show_properties=False)

        opts = {
              "signature" : signature,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.post_sign_page(file_name, page_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)
    
    def testGetVerifySignature(self):
        file_name = 'BlankWithSignature.pdf'
        self.uploadFile(file_name)

        signature_file_name = 'test1234.pfx'
        self.uploadFile(signature_file_name)

        rectangle = asposepdfcloud.models.Rectangle(x=100, y=100, width=400, height=100)
        
        signature = asposepdfcloud.models.Signature(
                signature_path=self.temp_folder + '/' + signature_file_name,
                signature_type=asposepdfcloud.models.SignatureType.PKCS_7,
                password='test1234',
                contact='testself.mail.ru',
                location='Ukraine',
                visible=True,
                rectangle=rectangle,
                form_field_name='Signature1',
                authority='Sergey Smal',
                date='08/01/2012 12:15:00.000 PM',
                show_properties=False)

        opts = {
              "signature" : signature,
              "folder" : self.temp_folder
        }

        response_sign = self.pdf_api.post_sign_document(file_name, **opts)
        self.assertEqual(response_sign.code, HttpStatusCode.OK)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_verify_signature(file_name, signature.form_field_name, **opts)
        self.assertEqual(response_sign.code, HttpStatusCode.OK)


    # Text Items Tests

    def testGetPageTextItems(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 1
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_page_text_items(file_name, page_number, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetTextItems(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_text_items(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)
    

    # Text Replace Tests

    def testPostDocumentReplaceText(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        text_replace_request = asposepdfcloud.models.TextReplaceRequest(
                old_value='Page',
                new_value='p_a_g_e',
                regex=False)
        

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.post_document_replace_text(file_name, text_replace_request, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPostDocumentReplaceTextList(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        text_replace_request_1 = asposepdfcloud.models.TextReplaceRequest(
                old_value='First',
                new_value='1',
                regex=False)

        text_replace_request_2 = asposepdfcloud.models.TextReplaceRequest(
                old_value='Page',
                new_value='p_a_g_e',
                regex=False)

        text_replace_list_request = asposepdfcloud.models.TextReplaceListRequest(
                text_replaces=[text_replace_request_1, text_replace_request_2])
        
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.post_document_replace_text_list(file_name, text_replace_list_request, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPostPageReplaceText(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 1

        text_replace_request = asposepdfcloud.models.TextReplaceRequest(
                old_value='Page',
                new_value='p_a_g_e',
                regex=False)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.post_page_replace_text(file_name, page_number, text_replace_request, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPostPageReplaceTextList(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 1

        text_replace_request_1 = asposepdfcloud.models.TextReplaceRequest(
                old_value='First',
                new_value='1',
                regex=False)

        text_replace_request_2 = asposepdfcloud.models.TextReplaceRequest(
                old_value='Page',
                new_value='p_a_g_e',
                regex=False)

        text_replace_list_request = asposepdfcloud.models.TextReplaceListRequest(
                text_replaces=[text_replace_request_1, text_replace_request_2])

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.post_page_replace_text_list(file_name, page_number, text_replace_list_request, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)
    

    # OCR Tests

    def testPutSearchableDocument(self):
        file_name = 'rusdoc.pdf'
        self.uploadFile(file_name)

        opts = {
              "lang" : 'rus,eng',
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_searchable_document(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPutSearchableDocumentWithDefaultLang(self):
        file_name = 'rusdoc.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_searchable_document(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)

    
    # Text Tests

    def testGetText(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        x = 0
        y = 0
        width = 0
        height = 0
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_text(file_name, x, y, width, height, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetPageTextByTwoTextOnPage(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 1
        x = 0
        y = 0
        width = 0
        height = 0
        opts = {
              "format" : ['First Page', 'Second Page'],
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_page_text(file_name, page_number, x, y, width, height, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)
    

    # Text Replace Tests

    def testPostDocumentTextReplaceWholeDocByRect(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        rect = asposepdfcloud.models.Rectangle(x=100, y=700, width=300, height=300)

        text_replace = asposepdfcloud.models.TextReplace(
                old_value='Page',
                new_value='p_a_g_e',
                regex=False,
                rect=rect)

        text_replace_list = asposepdfcloud.models.TextReplaceListRequest(
                text_replaces=[text_replace],
                start_index=0,
                count_replace=0)


        opts = {
              "folder" : self.temp_folder
        }

        response  = self.pdf_api.post_document_text_replace(file_name, text_replace_list, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testPostPageTextReplaceByRect(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        page_number = 1

        rect = asposepdfcloud.models.Rectangle(x=100, y=700, width=300, height=300)

        text_replace = asposepdfcloud.models.TextReplace(
                old_value='Page',
                new_value='p_a_g_e',
                regex=False,
                rect=rect)

        text_replace_list = asposepdfcloud.models.TextReplaceListRequest(
                text_replaces=[text_replace],
                start_index=0,
                count_replace=0)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.post_page_text_replace(file_name, page_number, text_replace_list, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    # Convert Tests
    # To Doc
    def testGetPdfInStorageToDoc(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_pdf_in_storage_to_doc(file_name, **opts)
        self.assertIsInstance(response, str)


    def testPutPdfInStorageToDoc(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        result_file_name = "result.doc"

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_pdf_in_storage_to_doc(file_name, self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testPutPdfInRequestToDoc(self):
        file_name = '4pages.pdf'
        result_file_name = "result.doc"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_doc(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    # To PDFA

    def testGetPdfInStorageToPdfA(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_pdf_in_storage_to_pdf_a(file_name, asposepdfcloud.models.PdfAType.PDFA1A, **opts)
        self.assertIsInstance(response, str)


    def testPutPdfInStorageToPdfA(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        result_file_name = "result.pdf"

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_pdf_in_storage_to_pdf_a(
                file_name, 
                self.temp_folder + '/' + result_file_name, 
                asposepdfcloud.models.PdfAType.PDFA1A,
                **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testPutPdfInRequestToPdfA(self):
        file_name = '4pages.pdf'
        result_file_name = "result.pdf"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_pdf_a(
                self.temp_folder + '/' + result_file_name, 
                asposepdfcloud.models.PdfAType.PDFA1A, 
                **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)

    # To Tiff
    def testGetPdfInStorageToTiff(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_pdf_in_storage_to_tiff(file_name, **opts)
        self.assertIsInstance(response, str)


    def testPutPdfInStorageToTiff(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        result_file_name = "result.tiff"

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_pdf_in_storage_to_tiff(file_name, self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testPutPdfInRequestToTiff(self):
        file_name = '4pages.pdf'
        result_file_name = "result.tiff"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_tiff(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    # To SVG

    def testGetPdfInStorageToSvg(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_pdf_in_storage_to_svg(file_name, **opts)
        self.assertIsInstance(response, str)


    def testPutPdfInStorageToSvg(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        result_file_name = "result.svg"

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_pdf_in_storage_to_svg(file_name, self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testPutPdfInRequestToSvg(self):
        file_name = '4pages.pdf'
        result_file_name = "result.svg"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_svg(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)
     
    # To XPS

    def testGetPdfInStorageToXps(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_pdf_in_storage_to_xps(file_name, **opts)
        self.assertIsInstance(response, str)


    def testPutPdfInStorageToXps(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        result_file_name = "result.xps"

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_pdf_in_storage_to_xps(file_name, self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testPutPdfInRequestToXps(self):
        file_name = '4pages.pdf'
        result_file_name = "result.xps"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_xps(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)

    # To XLS
    def testGetPdfInStorageToXls(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_pdf_in_storage_to_xls(file_name, **opts)
        self.assertIsInstance(response, str)


    def testPutPdfInStorageToXls(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        result_file_name = "result.xls"

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_pdf_in_storage_to_xls(file_name, self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testPutPdfInRequestToXls(self):
        file_name = '4pages.pdf'
        result_file_name = "result.xls"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_xls(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    # To HTML
    def testGetPdfInStorageToHtml(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_pdf_in_storage_to_html(file_name, **opts)
        self.assertIsInstance(response, str)


    def testPutPdfInStorageToHtml(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        result_file_name = "result.zip"

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_pdf_in_storage_to_html(file_name, self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testPutPdfInRequestToHtml(self):
        file_name = '4pages.pdf'
        result_file_name = "result.zip"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_html(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    # To EPUB
    def testGetPdfInStorageToEpub(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_pdf_in_storage_to_epub(file_name, **opts)
        self.assertIsInstance(response, str)


    def testPutPdfInStorageToEpub(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        result_file_name = "result.epub"

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_pdf_in_storage_to_epub(file_name, self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testPutPdfInRequestToEpub(self):
        file_name = '4pages.pdf'
        result_file_name = "result.epub"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_epub(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    # To PPTX
    def testGetPdfInStorageToPptx(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_pdf_in_storage_to_pptx(file_name, **opts)
        self.assertIsInstance(response, str)


    def testPutPdfInStorageToPptx(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        result_file_name = "result.pptx"

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_pdf_in_storage_to_pptx(file_name, self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testPutPdfInRequestToPptx(self):
        file_name = '4pages.pdf'
        result_file_name = "result.pptx"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_pptx(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    # To LaTeX
    def testGetPdfInStorageToLaTeX(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_pdf_in_storage_to_la_te_x(file_name, **opts)
        self.assertIsInstance(response, str)


    def testPutPdfInStorageToLaTeX(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        result_file_name = "result.latex"

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_pdf_in_storage_to_la_te_x(file_name, self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testPutPdfInRequestToLaTeX(self):
        file_name = '4pages.pdf'
        result_file_name = "result.latex"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_la_te_x(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    # To Mobi Xml
    def testGetPdfInStorageToMobiXml(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_pdf_in_storage_to_mobi_xml(file_name, **opts)
        self.assertIsInstance(response, str)


    def testPutPdfInStorageToMobiXml(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        result_file_name = "result.mobi"

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_pdf_in_storage_to_mobi_xml(file_name, self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testPutPdfInRequestToMobiXml(self):
        file_name = '4pages.pdf'
        result_file_name = "result.mobi"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_mobi_xml(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    # PDF Xfa To Acro Form
    def testGetXfaPdfInStorageToAcroForm(self):
        file_name = 'PdfWithXfaForm.pdf'
        self.uploadFile(file_name)
        
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_xfa_pdf_in_storage_to_acro_form(file_name, **opts)
        self.assertIsInstance(response, str)


    def testPutXfaPdfInStorageToAcroForm(self):
        file_name = 'PdfWithXfaForm.pdf'
        self.uploadFile(file_name)
        result_file_name = "result.pdf"

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_xfa_pdf_in_storage_to_acro_form(file_name, self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testPutXfaPdfInRequestToAcroForm(self):
        file_name = 'PdfWithXfaForm.pdf'
        result_file_name = "result.pdf"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_xfa_pdf_in_request_to_acro_form(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    # To Xml
    def testGetPdfInStorageToXml(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_pdf_in_storage_to_xml(file_name, **opts)
        self.assertIsInstance(response, str)


    def testPutPdfInStorageToXml(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        result_file_name = "result.xml"

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_pdf_in_storage_to_xml(file_name, self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testPutPdfInRequestToXml(self):
        file_name = '4pages.pdf'
        result_file_name = "result.xml"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_xml(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    # Upload / Download Tests
    
    def testPutCreate(self):
        file_name = '4pages.pdf'
        response = self.pdf_api.put_create(self.temp_folder + '/' + file_name, self.test_data_path + file_name)
        self.assertEqual(response.code, HttpStatusCode.OK)
    
    def testGetDownload(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        response = self.pdf_api.get_download(self.temp_folder + '/' + file_name)
        self.assertIsInstance(response, str)


    # Privileges Tests
    
    def testPutPrivileges(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        documentPrivilege = asposepdfcloud.models.DocumentPrivilege()
        documentPrivilege.allow_copy = False
        documentPrivilege.allow_print = False
        
        opts = {
            "privileges" : documentPrivilege,
            "folder" : self.temp_folder
        }

        response = self.pdf_api.put_privileges(file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)

    # Convert to PDF Tests

    def testGetEpubInStorageToPdf(self):
        file_name = '4pages.epub'
        self.uploadFile(file_name)

        src_path = self.temp_folder + '/' + file_name
        response = self.pdf_api.get_epub_in_storage_to_pdf(src_path)
        self.assertIsInstance(response, str)


    def testPutEpubInStorageToPdf(self):
        file_name = '4pages.epub'
        self.uploadFile(file_name)
        result_name = 'fromEpub.pdf'

        src_path = self.temp_folder + '/' + file_name
        opts = {
            "dst_folder" : self.temp_folder
        }
        response = self.pdf_api.put_epub_in_storage_to_pdf(result_name, src_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testGetWebInStorageToPdf(self):
        url = 'http://google.com'

        response = self.pdf_api.get_web_in_storage_to_pdf(url)
        self.assertIsInstance(response, str)


    def testPutWebInStorageToPdf(self):
        url = 'http://google.com'
        result_name = 'fromWeb.pdf'

        opts = {
            "dst_folder" : self.temp_folder
        }
        response = self.pdf_api.put_web_in_storage_to_pdf(result_name, url, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)



    def testGetLaTeXInStorageToPdf(self):
        file_name = 'TexExample.tex'
        self.uploadFile(file_name)

        src_path = self.temp_folder + '/' + file_name
        response = self.pdf_api.get_la_te_x_in_storage_to_pdf(src_path)
        self.assertIsInstance(response, str)


    def testPutLaTeXInStorageToPdf(self):
        file_name = 'TexExample.tex'
        self.uploadFile(file_name)
        result_name = 'fromTex.pdf'

        src_path = self.temp_folder + '/' + file_name
        opts = {
            "dst_folder" : self.temp_folder
        }
        response = self.pdf_api.put_la_te_x_in_storage_to_pdf(result_name, src_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testGetMhtInStorageToPdf(self):
        file_name = 'MhtExample.mht'
        self.uploadFile(file_name)

        src_path = self.temp_folder + '/' + file_name
        response = self.pdf_api.get_mht_in_storage_to_pdf(src_path)
        self.assertIsInstance(response, str)


    def testPutMhtInStorageToPdf(self):
        file_name = 'MhtExample.mht'
        self.uploadFile(file_name)
        result_name = 'fromMht.pdf'

        src_path = self.temp_folder + '/' + file_name
        opts = {
            "dst_folder" : self.temp_folder
        }
        response = self.pdf_api.put_mht_in_storage_to_pdf(result_name, src_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)



    def testGetHtmlInStorageToPdf(self):
        file_name = 'HtmlWithImage.zip'
        self.uploadFile(file_name)

        html_file_name = 'HtmlWithImage.html'
        opts = {
            "height" : 650,
            "width" : 250
        }
        src_path = self.temp_folder + '/' + file_name
        response = self.pdf_api.get_html_in_storage_to_pdf(src_path, html_file_name, **opts)
        self.assertIsInstance(response, str)


    def testPutHtmlInStorageToPdf(self):
        file_name = 'HtmlWithImage.zip'
        self.uploadFile(file_name)
        html_file_name = 'HtmlWithImage.html'

        result_name = 'fromMht.pdf'

        src_path = self.temp_folder + '/' + file_name
        opts = {
            "dst_folder" : self.temp_folder,
            "height" : 650,
            "width" : 250
        }
        response = self.pdf_api.put_html_in_storage_to_pdf(result_name, src_path, html_file_name, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testGetXslFoInStorageToPdf(self):
        file_name = 'XslfoExample.xslfo'
        self.uploadFile(file_name)

        src_path = self.temp_folder + '/' + file_name
        response = self.pdf_api.get_xsl_fo_in_storage_to_pdf(src_path)
        self.assertIsInstance(response, str)


    def testPutXslFoInStorageToPdf(self):
        file_name = 'XslfoExample.xslfo'
        self.uploadFile(file_name)
        result_name = 'fromXslFo.pdf'

        src_path = self.temp_folder + '/' + file_name
        opts = {
            "dst_folder" : self.temp_folder
        }
        response = self.pdf_api.put_xsl_fo_in_storage_to_pdf(result_name, src_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)



    def testGetXpsInStorageToPdf(self):
        file_name = 'Simple.xps'
        self.uploadFile(file_name)

        src_path = self.temp_folder + '/' + file_name
        response = self.pdf_api.get_xps_in_storage_to_pdf(src_path)
        self.assertIsInstance(response, str)


    def testPutXpsInStorageToPdf(self):
        file_name = 'Simple.xps'
        self.uploadFile(file_name)
        result_name = 'fromXps.pdf'

        src_path = self.temp_folder + '/' + file_name
        opts = {
            "dst_folder" : self.temp_folder
        }
        response = self.pdf_api.put_xps_in_storage_to_pdf(result_name, src_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)



    def testGetSvgInStorageToPdf(self):
        file_name = 'Simple.svg'
        self.uploadFile(file_name)

        src_path = self.temp_folder + '/' + file_name
        response = self.pdf_api.get_svg_in_storage_to_pdf(src_path)
        self.assertIsInstance(response, str)


    def testPutSvgInStorageToPdf(self):
        file_name = 'Simple.svg'
        self.uploadFile(file_name)
        result_name = 'fromSvg.pdf'

        src_path = self.temp_folder + '/' + file_name
        opts = {
            "dst_folder" : self.temp_folder
        }
        response = self.pdf_api.put_svg_in_storage_to_pdf(result_name, src_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)


    def testGetPclInStorageToPdf(self):
        file_name = 'template.pcl'
        self.uploadFile(file_name)

        src_path = self.temp_folder + '/' + file_name
        response = self.pdf_api.get_pcl_in_storage_to_pdf(src_path)
        self.assertIsInstance(response, str)


    def testPutPclInStorageToPdf(self):
        file_name = 'template.pcl'
        self.uploadFile(file_name)
        result_name = 'fromPcl.pdf'

        src_path = self.temp_folder + '/' + file_name
        opts = {
            "dst_folder" : self.temp_folder
        }
        response = self.pdf_api.put_pcl_in_storage_to_pdf(result_name, src_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)



    def testGetXmlInStorageToPdf(self):
        file_name = 'template.xml'
        self.uploadFile(file_name)

        src_path = self.temp_folder + '/' + file_name
        response = self.pdf_api.get_xml_in_storage_to_pdf(src_path)
        self.assertIsInstance(response, str)


    def testPutXmlInStorageToPdf(self):
        file_name = 'template.xml'
        self.uploadFile(file_name)
        result_name = 'fromXml.pdf'

        src_path = self.temp_folder + '/' + file_name
        opts = {
            "dst_folder" : self.temp_folder
        }
        response = self.pdf_api.put_xml_in_storage_to_pdf(result_name, src_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)

    def testGetPsInStorageToPdf(self):
        file_name = 'Typography.PS'
        self.uploadFile(file_name)

        src_path = self.temp_folder + '/' + file_name
        response = self.pdf_api.get_ps_in_storage_to_pdf(src_path)
        self.assertIsInstance(response, str)


    def testPutPsInStorageToPdf(self):
        file_name = 'Typography.PS'
        self.uploadFile(file_name)
        result_name = 'fromPs.pdf'

        src_path = self.temp_folder + '/' + file_name
        opts = {
            "dst_folder" : self.temp_folder
        }
        response = self.pdf_api.put_ps_in_storage_to_pdf(result_name, src_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)

    def testPutImageInStorageToPdf(self):
        data_file_1 = "33539.jpg"
        self.uploadFile(data_file_1)

        data_file_2 = "44781.jpg"
        self.uploadFile(data_file_2)

        result_name = "result.pdf"

        image_template_1 = asposepdfcloud.models.ImageTemplate(image_path=self.temp_folder + '/' + data_file_1, 
                                                               image_src_type=asposepdfcloud.models.ImageSrcType.COMMON)

        image_template_2 = asposepdfcloud.models.ImageTemplate(image_path=self.temp_folder + '/' + data_file_2, 
                                                               image_src_type=asposepdfcloud.models.ImageSrcType.COMMON)

        image_templates_request = asposepdfcloud.models.ImageTemplatesRequest(is_ocr=True, ocr_langs="eng", 
                                        images_list=[image_template_1, image_template_2])

        opts = {
            "dst_folder" : self.temp_folder
        }

        response = self.pdf_api.put_image_in_storage_to_pdf(result_name, image_templates_request, **opts)
        self.assertEqual(response.code, HttpStatusCode.CREATED)

    
    # Page Convert To Images Tests

    def testGetPageConvertToTiff(self):
        name = "4pages.pdf"
        self.uploadFile(name)

        page_number = 2
        opts = {
            "folder" : self.temp_folder
        }

        response = self.pdf_api.get_page_convert_to_tiff(name, page_number, **opts)
        self.assertIsInstance(response, str)


    def testPutPageConvertToTiff(self):
        name = "4pages.pdf"
        self.uploadFile(name) 
        result_file = "page.tiff"
        out_path = self.temp_folder + '/' + result_file
        page_number = 2
        opts = {
            "folder" : self.temp_folder
        }
        response = self.pdf_api.put_page_convert_to_tiff(name, page_number, out_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetPageConvertToJpeg(self):
        name = "4pages.pdf"
        self.uploadFile(name)

        page_number = 2
        opts = {
            "folder" : self.temp_folder
        }

        response = self.pdf_api.get_page_convert_to_jpeg(name, page_number, **opts)
        self.assertIsInstance(response, str)


    def testPutPageConvertToJpeg(self):
        name = "4pages.pdf"
        self.uploadFile(name) 
        result_file = "page.jpeg"
        out_path = self.temp_folder + '/' + result_file
        page_number = 2
        opts = {
            "folder" : self.temp_folder
        }
        response = self.pdf_api.put_page_convert_to_jpeg(name, page_number, out_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)

    def testGetPageConvertToPng(self):
        name = "4pages.pdf"
        self.uploadFile(name)

        page_number = 2
        opts = {
            "folder" : self.temp_folder
        }

        response = self.pdf_api.get_page_convert_to_png(name, page_number, **opts)
        self.assertIsInstance(response, str)


    def testPutPageConvertToPng(self):
        name = "4pages.pdf"
        self.uploadFile(name) 
        result_file = "page.png"
        out_path = self.temp_folder + '/' + result_file
        page_number = 2
        opts = {
            "folder" : self.temp_folder
        }
        response = self.pdf_api.put_page_convert_to_png(name, page_number, out_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)

    def testGetPageConvertToEmf(self):
        name = "4pages.pdf"
        self.uploadFile(name)

        page_number = 2
        opts = {
            "folder" : self.temp_folder
        }

        response = self.pdf_api.get_page_convert_to_emf(name, page_number, **opts)
        self.assertIsInstance(response, str)


    def testPutPageConvertToEmf(self):
        name = "4pages.pdf"
        self.uploadFile(name) 
        result_file = "page.emf"
        out_path = self.temp_folder + '/' + result_file
        page_number = 2
        opts = {
            "folder" : self.temp_folder
        }
        response = self.pdf_api.put_page_convert_to_emf(name, page_number, out_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetPageConvertToBmp(self):
        name = "4pages.pdf"
        self.uploadFile(name)

        page_number = 2
        opts = {
            "folder" : self.temp_folder
        }

        response = self.pdf_api.get_page_convert_to_bmp(name, page_number, **opts)
        self.assertIsInstance(response, str)


    def testPutPageConvertToBmp(self):
        name = "4pages.pdf"
        self.uploadFile(name) 
        result_file = "page.bmp"
        out_path = self.temp_folder + '/' + result_file
        page_number = 2
        opts = {
            "folder" : self.temp_folder
        }
        response = self.pdf_api.put_page_convert_to_bmp(name, page_number, out_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)


    def testGetPageConvertToGif(self):
        name = "4pages.pdf"
        self.uploadFile(name)

        page_number = 2
        opts = {
            "folder" : self.temp_folder
        }

        response = self.pdf_api.get_page_convert_to_gif(name, page_number, **opts)
        self.assertIsInstance(response, str)


    def testPutPageConvertToGif(self):
        name = "4pages.pdf"
        self.uploadFile(name) 
        result_file = "page.gif"
        out_path = self.temp_folder + '/' + result_file
        page_number = 2
        opts = {
            "folder" : self.temp_folder
        }
        response = self.pdf_api.put_page_convert_to_gif(name, page_number, out_path, **opts)
        self.assertEqual(response.code, HttpStatusCode.OK)

if __name__ == '__main__':
    unittest.main()
