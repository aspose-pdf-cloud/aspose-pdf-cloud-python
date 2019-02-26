# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


   Copyright (c) 2019 Aspose.PDF Cloud
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
from asposepdfcloud.models import text_style

import os
import sys
import unittest
import json

import asposepdfcloud
from asposepdfcloud.apis.pdf_api import PdfApi
from asposepdfcloud.rest import ApiException
#from asposepdfcloud.models.annotations_ import AnnotationInfoResponse


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

    def testGetDocumentAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)


    def testDeleteDocumentAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.delete_document_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)


    def testGetPageAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)


    def testDeletePageAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.delete_page_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)


    def testDeleteAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.delete_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)
    

    def testPutAnnotationsFlatten(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)
        end_page = 2
        annotation_types = [asposepdfcloud.models.AnnotationType.STAMP]

        response = self.pdf_api.put_annotations_flatten(file_name, end_page=end_page, annotation_types=annotation_types, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    # FileAttachment Annotations Tests

    def testGetDocumentFileAttachmentAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_file_attachment_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageFileAttachmentAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_file_attachment_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetFileAttachmentAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_file_attachment_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_file_attachment_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageFileAttachmentAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        attachment_file = '4pages.pdf'
        self.uploadFile(attachment_file)

        page_number = 1

        annotation = asposepdfcloud.models.FileAttachmentAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.modified = '01/01/2018 12:00:00.000 AM'
        annotation.file_path = self.temp_folder + '/' + attachment_file
        annotation.file_name = attachment_file

        response = self.pdf_api.post_page_file_attachment_annotations(file_name, page_number, [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutFileAttachmentAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        attachment_file = '4pages.pdf'
        self.uploadFile(attachment_file)

        annotation = asposepdfcloud.models.FileAttachmentAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.modified = '01/01/2018 12:00:00.000 AM'
        annotation.file_path = self.temp_folder + '/' + attachment_file
        annotation.file_name = attachment_file

        response_annotations = self.pdf_api.get_document_file_attachment_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_file_attachment_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)

    def testGetFileAttachmentAnnotationData(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_file_attachment_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_file_attachment_annotation_data(file_name, annotation_id, folder=self.temp_folder)
        self.assertIsInstance(response, str)

    def testPutFileAttachmentAnnotationDataExtract(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_file_attachment_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_file_attachment_annotation_data_extract(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    # Stamp Annotations Tests

    def testGetDocumentStampAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_stamp_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageStampAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_stamp_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetStampAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_stamp_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_stamp_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageStampAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        attachment_file = '4pages.pdf'
        self.uploadFile(attachment_file)

        page_number = 1

        annotation = asposepdfcloud.models.StampAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.modified = '01/01/2018 12:00:00.000 AM'
        annotation.file_path = self.temp_folder + '/' + attachment_file

        response = self.pdf_api.post_page_stamp_annotations(file_name, page_number, [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutStampAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        attachment_file = '4pages.pdf'
        self.uploadFile(attachment_file)

        annotation = asposepdfcloud.models.StampAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.modified = '01/01/2018 12:00:00.000 AM'
        annotation.file_path = self.temp_folder + '/' + attachment_file

        response_annotations = self.pdf_api.get_document_stamp_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_stamp_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)

    def testGetStampAnnotationData(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_stamp_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_stamp_annotation_data(file_name, annotation_id, folder=self.temp_folder)
        self.assertIsInstance(response, str)

    def testPutStampAnnotationDataExtract(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_stamp_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_stamp_annotation_data_extract(file_name, annotation_id, out_file_path='stamp.dat', folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    # Screen Annotations Tests

    def testGetDocumentScreenAnnotations(self):
        file_name = 'PdfWithScreenAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_screen_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageScreenAnnotations(self):
        file_name = 'PdfWithScreenAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        response = self.pdf_api.get_page_screen_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetScreenAnnotation(self):
        file_name = 'PdfWithScreenAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_screen_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_screen_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageScreenAnnotations(self):
        file_name = 'PdfWithScreenAnnotations.pdf'
        self.uploadFile(file_name)

        attachment_file = 'ScreenMovie.swf'
        self.uploadFile(attachment_file)

        page_number = 1

        annotation = asposepdfcloud.models.ScreenAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.modified = '01/01/2018 12:00:00.000 AM'
        annotation.file_path = self.temp_folder + '/' + attachment_file

        response = self.pdf_api.post_page_screen_annotations(file_name, page_number, [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutScreenAnnotation(self):
        file_name = 'PdfWithScreenAnnotations.pdf'
        self.uploadFile(file_name)

        attachment_file = 'ScreenMovie.swf'
        self.uploadFile(attachment_file)

        annotation = asposepdfcloud.models.ScreenAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.modified = '01/01/2018 12:00:00.000 AM'
        annotation.file_path = self.temp_folder + '/' + attachment_file

        response_annotations = self.pdf_api.get_document_screen_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_screen_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)
    """
    def testGetScreenAnnotationData(self):
        file_name = 'PdfWithScreenAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_screen_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_screen_annotation_data(file_name, annotation_id, folder=self.temp_folder)
        self.assertIsInstance(response, str)

    def testPutScreenAnnotationDataExtract(self):
        file_name = 'PdfWithScreenAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_screen_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_screen_annotation_data_extract(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 201)
    """

    # Sound Annotations Tests

    def testGetDocumentSoundAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_sound_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageSoundAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_sound_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetSoundAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_sound_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_sound_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageSoundAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        attachment_file = '4pages.pdf'
        self.uploadFile(attachment_file)

        page_number = 1

        annotation = asposepdfcloud.models.SoundAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.modified = '01/01/2018 12:00:00.000 AM'
        annotation.file_path = self.temp_folder + '/' + attachment_file

        response = self.pdf_api.post_page_sound_annotations(file_name, page_number, [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutSoundAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        attachment_file = '4pages.pdf'
        self.uploadFile(attachment_file)

        annotation = asposepdfcloud.models.SoundAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.modified = '01/01/2018 12:00:00.000 AM'
        annotation.file_path = self.temp_folder + '/' + attachment_file

        response_annotations = self.pdf_api.get_document_sound_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_sound_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)

    def testGetSoundAnnotationData(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_sound_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_sound_annotation_data(file_name, annotation_id, folder=self.temp_folder)
        self.assertIsInstance(response, str)

    def testPutSoundAnnotationDataExtract(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_sound_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_sound_annotation_data_extract(file_name, annotation_id, out_file_path="outFile.dat", folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    # Redaction Annotations Tests

    def testGetDocumentRedactionAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_redaction_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageRedactionAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_redaction_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetRedactionAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_redaction_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_redaction_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageRedactionAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        annotation = asposepdfcloud.models.RedactionAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.z_index = 1
        annotation.quad_point = [
            asposepdfcloud.models.Point(10, 40),
            asposepdfcloud.models.Point(30, 40)
        ]
        annotation.modified = '01/01/2018 12:00:00.000 AM'

        response = self.pdf_api.post_page_redaction_annotations(file_name, page_number, [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutRedactionAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)
        
        page_number = 1

        annotation = asposepdfcloud.models.RedactionAnnotation()
        annotation.name = 'Test Name Updated'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.z_index = 1
        annotation.quad_point = [
            asposepdfcloud.models.Point(10, 40),
            asposepdfcloud.models.Point(30, 40)
        ]
        annotation.modified = '01/01/2018 12:01:02.000 AM'

        response = self.pdf_api.post_page_redaction_annotations(file_name, page_number, [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)

        response_annotations = self.pdf_api.get_document_redaction_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_redaction_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    # Movie Annotations Tests

    def testGetDocumentMovieAnnotations(self):
        file_name = 'PdfWithAnnotations1.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_movie_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageMovieAnnotations(self):
        file_name = 'PdfWithAnnotations1.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_movie_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetMovieAnnotation(self):
        file_name = 'PdfWithAnnotations1.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_movie_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_movie_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageMovieAnnotations(self):
        file_name = 'PdfWithAnnotations1.pdf'
        self.uploadFile(file_name)

        attachment_file = '4pages.pdf'
        self.uploadFile(attachment_file)

        page_number = 1

        annotation = asposepdfcloud.models.MovieAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.z_index = 1
        annotation.modified = '01/01/2018 12:00:00.000 AM'
        annotation.file_path = self.temp_folder + '/' + attachment_file
        
        response = self.pdf_api.post_page_movie_annotations(file_name, page_number, [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutMovieAnnotation(self):
        file_name = 'PdfWithAnnotations1.pdf'
        self.uploadFile(file_name)

        attachment_file = '4pages.pdf'
        self.uploadFile(attachment_file)

        annotation = asposepdfcloud.models.MovieAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.z_index = 1
        annotation.modified = '01/01/2018 12:00:00.000 AM'
        annotation.file_path = self.temp_folder + '/' + attachment_file
        
        response_annotations = self.pdf_api.get_document_movie_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_movie_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)

    # PolyLine Annotations Tests

    def testGetDocumentPolyLineAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_poly_line_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPagePolyLineAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_poly_line_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPolyLineAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_poly_line_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_poly_line_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPagePolyLineAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        annotation = asposepdfcloud.models.PolyLineAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.vertices = [
                asposepdfcloud.models.Point(10, 10),
                asposepdfcloud.models.Point(20, 10),
                asposepdfcloud.models.Point(10, 20),
                asposepdfcloud.models.Point(10, 10)
            ]

        response = self.pdf_api.post_page_poly_line_annotations(file_name, page_number,  [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutPolyLineAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)


        annotation = asposepdfcloud.models.PolyLineAnnotation()
        annotation.name = 'Test Name Updated'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text Updated'
        annotation.subject = 'Subj Updated'
        annotation.z_index = 1
        annotation.title = 'Title Updated'
        annotation.vertices = [
                        asposepdfcloud.models.Point(10, 10),
                        asposepdfcloud.models.Point(20, 10),
                        asposepdfcloud.models.Point(10, 20),
                        asposepdfcloud.models.Point(10, 10)
                    ]
        response_annotations = self.pdf_api.get_document_poly_line_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_poly_line_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)

    # Polygon Annotations Tests

    def testGetDocumentPolygonAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_polygon_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPagePolygonAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_polygon_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPolygonAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_polygon_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_polygon_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPagePolygonAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        annotation = asposepdfcloud.models.PolygonAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.vertices = [
                asposepdfcloud.models.Point(10, 10),
                asposepdfcloud.models.Point(20, 10),
                asposepdfcloud.models.Point(10, 20),
                asposepdfcloud.models.Point(10, 10)
            ]

        response = self.pdf_api.post_page_polygon_annotations(file_name, page_number,  [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutPolygonAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)


        annotation = asposepdfcloud.models.PolygonAnnotation()
        annotation.name = 'Test Name Updated'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text Updated'
        annotation.subject = 'Subj Updated'
        annotation.z_index = 1
        annotation.title = 'Title Updated'
        annotation.vertices = [
                        asposepdfcloud.models.Point(10, 10),
                        asposepdfcloud.models.Point(20, 10),
                        asposepdfcloud.models.Point(10, 20),
                        asposepdfcloud.models.Point(10, 10)
                    ]
        response_annotations = self.pdf_api.get_document_polygon_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_polygon_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)

    # Circle Annotations Tests

    def testGetDocumentCircleAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_circle_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageCircleAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_circle_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetCircleAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_circle_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_circle_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageCircleAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        annotation = asposepdfcloud.models.CircleAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'

        response = self.pdf_api.post_page_circle_annotations(file_name, page_number,  [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutCircleAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)


        annotation = asposepdfcloud.models.CircleAnnotation()
        annotation.name = 'Test Name Updated'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text Updated'
        annotation.subject = 'Subj Updated'
        annotation.z_index = 1
        annotation.title = 'Title Updated'

        response_annotations = self.pdf_api.get_document_circle_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_circle_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)

    # Square Annotations Tests

    def testGetDocumentSquareAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_square_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageSquareAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_square_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetSquareAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_square_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_square_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageSquareAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        annotation = asposepdfcloud.models.SquareAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'

        response = self.pdf_api.post_page_square_annotations(file_name, page_number,  [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutSquareAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)


        annotation = asposepdfcloud.models.SquareAnnotation()
        annotation.name = 'Test Name Updated'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text Updated'
        annotation.subject = 'Subj Updated'
        annotation.z_index = 1
        annotation.title = 'Title Updated'

        response_annotations = self.pdf_api.get_document_square_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_square_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    # Line Annotations Tests

    def testGetDocumentLineAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_line_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageLineAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_line_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetLineAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_line_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_line_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageLineAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        annotation = asposepdfcloud.models.LineAnnotation()
        annotation.name = 'Test Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.starting = asposepdfcloud.models.Point(10, 10)
        annotation.ending = asposepdfcloud.models.Point(100, 100)

        response = self.pdf_api.post_page_line_annotations(file_name, page_number,  [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutLineAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)


        annotation = asposepdfcloud.models.LineAnnotation()
        annotation.name = 'Test Name Updated'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text Updated'
        annotation.subject = 'Subj Updated'
        annotation.z_index = 1
        annotation.starting = asposepdfcloud.models.Point(10, 10)
        annotation.ending = asposepdfcloud.models.Point(100, 100)

        response_annotations = self.pdf_api.get_document_line_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_line_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)

    # Free Text Annotations Tests

    def testGetDocumentFreeTextAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_free_text_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageFreeTextAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_free_text_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetFreeTextAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_free_text_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_free_text_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageFreeTextAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        text_style = asposepdfcloud.models.TextStyle(font_size=12, font='Arial', 
                foreground_color=asposepdfcloud.models.Color(a=0xFF, r=0, g=0xFF, b=0),
                background_color=asposepdfcloud.models.Color(a=0xFF, r=0xFF, g=0, b=0))

        annotation = asposepdfcloud.models.FreeTextAnnotation()
        annotation.name = 'Test Free Text'
        annotation.text_style = text_style
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.intent = asposepdfcloud.models.FreeTextIntent.FREETEXTTYPEWRITER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Text Box Subj'
        annotation.z_index = 1
        annotation.justification = asposepdfcloud.models.Justification.CENTER
        annotation.title = 'Title'

        response = self.pdf_api.post_page_free_text_annotations(file_name, page_number,  [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutFreeTextAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)


        text_style = asposepdfcloud.models.TextStyle(font_size=12, font='Arial', 
                foreground_color=asposepdfcloud.models.Color(a=0xFF, r=0, g=0xFF, b=0),
                background_color=asposepdfcloud.models.Color(a=0xFF, r=0xFF, g=0, b=0))

        annotation = asposepdfcloud.models.FreeTextAnnotation()
        annotation.name = 'Test Free Text'
        annotation.text_style = text_style
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.intent = asposepdfcloud.models.FreeTextIntent.FREETEXTTYPEWRITER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Text Box Subj'
        annotation.z_index = 1
        annotation.justification = asposepdfcloud.models.Justification.CENTER
        annotation.title = 'Title'

        response_annotations = self.pdf_api.get_document_free_text_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_free_text_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)

    # Text Annotations Tests

    def testGetDocumentTextAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_text_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageTextAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_text_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetTextAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_text_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_text_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageTextAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        annotation = asposepdfcloud.models.TextAnnotation()
        annotation.name = 'Test Free Text'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Text Box Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.state = asposepdfcloud.models.AnnotationState.UNDEFINED

        response = self.pdf_api.post_page_text_annotations(file_name, page_number,  [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutTextAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)


        annotation = asposepdfcloud.models.TextAnnotation()
        annotation.name = 'Test Free Text'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Text Box Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.state = asposepdfcloud.models.AnnotationState.UNDEFINED

        response_annotations = self.pdf_api.get_document_text_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_text_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    # Highlight Annotations Tests

    def testGetDocumentHighlightAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_highlight_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageHighlightAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_highlight_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetHighlightAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_highlight_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_highlight_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageHighlightAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        annotation = asposepdfcloud.models.HighlightAnnotation()
        annotation.name = 'Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.quad_points = [
                asposepdfcloud.models.Point(10, 10),
                asposepdfcloud.models.Point(20, 10),
                asposepdfcloud.models.Point(10, 20),
                asposepdfcloud.models.Point(10, 10)
            ]
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response = self.pdf_api.post_page_highlight_annotations(file_name, page_number,  [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutHighlightAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)


        annotation = asposepdfcloud.models.HighlightAnnotation()
        annotation.name = 'Name Updated'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Text Updated'
        annotation.subject = 'Subj Updated'
        annotation.z_index = 1
        annotation.title = 'Title Updated'
        annotation.quad_points = [
                asposepdfcloud.models.Point(10, 10),
                asposepdfcloud.models.Point(20, 10),
                asposepdfcloud.models.Point(10, 20),
                asposepdfcloud.models.Point(10, 10)
            ]
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response_annotations = self.pdf_api.get_document_highlight_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_highlight_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    # Underline Annotations Tests

    def testGetDocumentUnderlineAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_underline_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageUnderlineAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_underline_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetUnderlineAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_underline_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_underline_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageUnderlineAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        annotation = asposepdfcloud.models.UnderlineAnnotation()
        annotation.name = 'Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.quad_points = [
                asposepdfcloud.models.Point(10, 10),
                asposepdfcloud.models.Point(20, 10),
                asposepdfcloud.models.Point(10, 20),
                asposepdfcloud.models.Point(10, 10)
            ]
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response = self.pdf_api.post_page_underline_annotations(file_name, page_number,  [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutUnderlineAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)


        annotation = asposepdfcloud.models.UnderlineAnnotation()
        annotation.name = 'Name Updated'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Text Updated'
        annotation.subject = 'Subj Updated'
        annotation.z_index = 1
        annotation.title = 'Title Updated'
        annotation.quad_points = [
                asposepdfcloud.models.Point(10, 10),
                asposepdfcloud.models.Point(20, 10),
                asposepdfcloud.models.Point(10, 20),
                asposepdfcloud.models.Point(10, 10)
            ]
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response_annotations = self.pdf_api.get_document_underline_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_underline_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)

    # Squiggly Annotations Tests

    def testGetDocumentSquigglyAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_squiggly_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageSquigglyAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_squiggly_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetSquigglyAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_squiggly_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_squiggly_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageSquigglyAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        annotation = asposepdfcloud.models.SquigglyAnnotation()
        annotation.name = 'Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.quad_points = [
                asposepdfcloud.models.Point(10, 10),
                asposepdfcloud.models.Point(20, 10),
                asposepdfcloud.models.Point(10, 20),
                asposepdfcloud.models.Point(10, 10)
            ]
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response = self.pdf_api.post_page_squiggly_annotations(file_name, page_number,  [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutSquigglyAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)


        annotation = asposepdfcloud.models.SquigglyAnnotation()
        annotation.name = 'Name Updated'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Text Updated'
        annotation.subject = 'Subj Updated'
        annotation.z_index = 1
        annotation.title = 'Title Updated'
        annotation.quad_points = [
                asposepdfcloud.models.Point(10, 10),
                asposepdfcloud.models.Point(20, 10),
                asposepdfcloud.models.Point(10, 20),
                asposepdfcloud.models.Point(10, 10)
            ]
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response_annotations = self.pdf_api.get_document_squiggly_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_squiggly_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    # StrikeOut Annotations Tests

    def testGetDocumentStrikeOutAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_strike_out_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageStrikeOutAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_strike_out_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetStrikeOutAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_strike_out_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_strike_out_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageStrikeOutAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        annotation = asposepdfcloud.models.StrikeOutAnnotation()
        annotation.name = 'Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.quad_points = [
                asposepdfcloud.models.Point(10, 10),
                asposepdfcloud.models.Point(20, 10),
                asposepdfcloud.models.Point(10, 20),
                asposepdfcloud.models.Point(10, 10)
            ]
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response = self.pdf_api.post_page_strike_out_annotations(file_name, page_number,  [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutStrikeOutAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)


        annotation = asposepdfcloud.models.StrikeOutAnnotation()
        annotation.name = 'Name Updated'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Text Updated'
        annotation.subject = 'Subj Updated'
        annotation.z_index = 1
        annotation.title = 'Title Updated'
        annotation.quad_points = [
                asposepdfcloud.models.Point(10, 10),
                asposepdfcloud.models.Point(20, 10),
                asposepdfcloud.models.Point(10, 20),
                asposepdfcloud.models.Point(10, 10)
            ]
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response_annotations = self.pdf_api.get_document_strike_out_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_strike_out_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)

    # Caret Annotations Tests

    def testGetDocumentCaretAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_caret_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageCaretAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_caret_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetCaretAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_caret_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_caret_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageCaretAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        annotation = asposepdfcloud.models.CaretAnnotation()
        annotation.name = 'Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.frame = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response = self.pdf_api.post_page_caret_annotations(file_name, page_number,  [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutCaretAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)


        annotation = asposepdfcloud.models.CaretAnnotation()
        annotation.name = 'Name Updated'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Text Updated'
        annotation.subject = 'Subj Updated'
        annotation.z_index = 1
        annotation.title = 'Title Updated'
        annotation.frame = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response_annotations = self.pdf_api.get_document_caret_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_caret_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)


        # Ink Annotations Tests

    def testGetDocumentInkAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_ink_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPageInkAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_ink_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetInkAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_ink_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_ink_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPageInkAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 1

        annotation = asposepdfcloud.models.InkAnnotation()
        annotation.name = 'Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Rich Text'
        annotation.subject = 'Subj'
        annotation.z_index = 1
        annotation.title = 'Title'
        annotation.ink_list = [
                [
                    asposepdfcloud.models.Point(10, 40),
                    asposepdfcloud.models.Point(30, 40),
                ],
                [
                    asposepdfcloud.models.Point(10, 20),
                    asposepdfcloud.models.Point(20, 20),
                    asposepdfcloud.models.Point(30, 20),
                ]
            ]
        annotation.cap_style = asposepdfcloud.models.CapStyle.ROUNDED
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response = self.pdf_api.post_page_ink_annotations(file_name, page_number,  [annotation], folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutInkAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)


        annotation = asposepdfcloud.models.InkAnnotation()
        annotation.name = 'Name Updated'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.rich_text = 'Text Updated'
        annotation.subject = 'Subj Updated'
        annotation.z_index = 1
        annotation.title = 'Title Updated'
        annotation.ink_list = [
                [
                    asposepdfcloud.models.Point(10, 40),
                    asposepdfcloud.models.Point(30, 40),
                ],
                [
                    asposepdfcloud.models.Point(10, 20),
                    asposepdfcloud.models.Point(20, 20),
                    asposepdfcloud.models.Point(30, 20),
                ]
            ]
        annotation.cap_style = asposepdfcloud.models.CapStyle.ROUNDED
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response_annotations = self.pdf_api.get_document_ink_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_ink_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)

    # Popup Annotations Tests

    def testGetDocumentPopupAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response = self.pdf_api.get_document_popup_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetDocumentPopupAnnotationsByParent(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        parent_id = 'GI5TAOZRGU3CYNZSGEWDCNZWFQ3TGOI'

        response = self.pdf_api.get_document_popup_annotations_by_parent(file_name, parent_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPagePopupAnnotations(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        page_number = 2

        response = self.pdf_api.get_page_popup_annotations(file_name, page_number, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testGetPopupAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        response_annotations = self.pdf_api.get_document_popup_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.get_popup_annotation(file_name, annotation_id, folder=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostPopupAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)

        parent_id = 'GI5TCMR3GE2TQLBSGM3CYMJYGUWDENRV'

        annotation = asposepdfcloud.models.PopupAnnotation()
        annotation.name = 'Name'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.z_index = 1
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response = self.pdf_api.post_popup_annotation(file_name, parent_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)


    def testPutPopupAnnotation(self):
        file_name = 'PdfWithAnnotations.pdf'
        self.uploadFile(file_name)


        annotation = asposepdfcloud.models.PopupAnnotation()
        annotation.name = 'Name Updated'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.z_index = 1
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response_annotations = self.pdf_api.get_document_popup_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_popup_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)
        self.assertEqual(response.code, 201)

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
        self.assertEqual(response.code, 200)


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
        self.assertEqual(response.code, 200)


    # Attachments Tests

    def testGetDocumentAttachmentByIndex(self):
        file_name = 'PdfWithEmbeddedFiles.pdf'
        self.uploadFile(file_name)

        attachment_index = 1
        opts = {
            "folder" : self.temp_folder
        }

        response = self.pdf_api.get_document_attachment_by_index(file_name, attachment_index, **opts)
        self.assertEqual(response.code, 200)


    
    def testGetDocumentAttachments(self):
        file_name = 'PdfWithEmbeddedFiles.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_document_attachments(file_name, **opts)
        self.assertEqual(response.code, 200)
     
    

    def testGetDownloadDocumentAttachmentByIndex(self):
        file_name = 'PdfWithEmbeddedFiles.pdf'
        self.uploadFile(file_name)

        attachment_index = 1
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_download_document_attachment_by_index(file_name, attachment_index, **opts)
        self.assertIsInstance(response, str)
    

    # Bookmarks Tests

    def testGetDocumentBookmarks(self):
        file_name = 'PdfWithBookmarks.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_document_bookmarks(file_name, **opts)
        self.assertIsInstance(response, str)
    
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
        self.assertEqual(response.code, 201)


    def testPutPdfInRequestToDoc(self):
        file_name = '4pages.pdf'
        result_file_name = "result.doc"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_doc(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)

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
        self.assertEqual(response.code, 201)


    def testPutPdfInRequestToTiff(self):
        file_name = '4pages.pdf'
        result_file_name = "result.tiff"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_tiff(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)


    def testPutPdfInRequestToSvg(self):
        file_name = '4pages.pdf'
        result_file_name = "result.svg"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_svg(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, 201)
     
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
        self.assertEqual(response.code, 201)


    def testPutPdfInRequestToXps(self):
        file_name = '4pages.pdf'
        result_file_name = "result.xps"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_xps(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, 201)

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
        self.assertEqual(response.code, 201)


    def testPutPdfInRequestToXls(self):
        file_name = '4pages.pdf'
        result_file_name = "result.xls"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_xls(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)


    def testPutPdfInRequestToHtml(self):
        file_name = '4pages.pdf'
        result_file_name = "result.zip"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_html(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)


    def testPutPdfInRequestToEpub(self):
        file_name = '4pages.pdf'
        result_file_name = "result.epub"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_epub(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)


    def testPutPdfInRequestToPptx(self):
        file_name = '4pages.pdf'
        result_file_name = "result.pptx"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_pptx(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)


    def testPutPdfInRequestToLaTeX(self):
        file_name = '4pages.pdf'
        result_file_name = "result.latex"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_la_te_x(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)


    def testPutPdfInRequestToMobiXml(self):
        file_name = '4pages.pdf'
        result_file_name = "result.mobi"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_mobi_xml(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)


    def testPutXfaPdfInRequestToAcroForm(self):
        file_name = 'PdfWithXfaForm.pdf'
        result_file_name = "result.pdf"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_xfa_pdf_in_request_to_acro_form(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)


    def testPutPdfInRequestToXml(self):
        file_name = '4pages.pdf'
        result_file_name = "result.xml"

        opts = {
              "file" : self.test_data_path + file_name
        }

        response = self.pdf_api.put_pdf_in_request_to_xml(self.temp_folder + '/' + result_file_name, **opts)
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)



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
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)



    def testGetHtmlInStorageToPdf(self):
        file_name = 'HtmlWithImage.zip'
        self.uploadFile(file_name)

        html_file_name = 'HtmlWithImage.html'
        opts = {
            "height": 650,
            "width": 250,
            "html_file_name": html_file_name 
        }
        src_path = self.temp_folder + '/' + file_name
        response = self.pdf_api.get_html_in_storage_to_pdf(src_path, **opts)
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
            "width" : 250,
            "html_file_name": html_file_name
        }
        response = self.pdf_api.put_html_in_storage_to_pdf(result_name, src_path, **opts)
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)



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
        self.assertEqual(response.code, 201)



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
        self.assertEqual(response.code, 201)


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
        self.assertEqual(response.code, 201)



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
        self.assertEqual(response.code, 201)

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
        self.assertEqual(response.code, 201)

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
        self.assertEqual(response.code, 201)

    
    # Document Tests

    def testGetDocument(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_document(file_name, **opts)
        self.assertEqual(response.code, 200)


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
        self.assertEqual(response.code, 200)



    def testPostSplitDocument(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }
        response = self.pdf_api.post_split_document(file_name, **opts)
        self.assertEqual(response.code, 200)


    def testPutCreateEmptyDocument(self):
        file_name = 'empty.pdf'

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_create_document(file_name, **opts)
        self.assertEqual(response.code, 200)
   

    # Fields Tests

    def testGetField(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }
        field_name = 'textField'

        response = self.pdf_api.get_field(file_name, field_name, **opts)
        self.assertEqual(response.code, 200)


    def testGetFields(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_fields(file_name, **opts)
        self.assertEqual(response.code, 200)


    def testPostCreateField(self):
        file_name = 'Hello_world.pdf'
        self.uploadFile(file_name)

        rect = asposepdfcloud.models.Rectangle(50, 200, 200, 400)

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
        self.assertEqual(response.code, 200)


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
        self.assertEqual(response.code, 200)
    

    def testPutUpdateFields(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        field_name = 'textField'

        field = asposepdfcloud.models.Field()
        field.name = field_name
        field.values = ['Text field updated value.']
        field.type = asposepdfcloud.models.FieldType.TEXT

        fields = asposepdfcloud.models.Fields()
        fields.list = [field]

        opts = {
              "fields" : fields,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_update_fields(file_name, **opts)
        self.assertEqual(response.code, 200)


    def testDeleteField(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }
        field_name = 'textField'

        response = self.pdf_api.delete_field(file_name, field_name, **opts)
        self.assertEqual(response.code, 200)


    def testPostFlattenDocument(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        opts = {
              "hide_buttons": True,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.post_flatten_document(file_name,  **opts)
        self.assertEqual(response.code, 200)

    def testPutFieldsFlatten(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_fields_flatten(file_name,  **opts)
        self.assertEqual(response.code, 200)

    # Images Tests

    def testGetImage(self):
        file_name = 'PdfWithImages2.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        page_number = 1
        responseImages = self.pdf_api.get_images(file_name, page_number, **opts)
        self.assertEqual(responseImages.code, 200)
        image_id = responseImages.images.list[0].id


        response = self.pdf_api.get_image(file_name, image_id, **opts)
        self.assertEqual(response.code, 200)


    def testDeleteImage(self):
        file_name = 'PdfWithImages2.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        page_number = 1
        responseImages = self.pdf_api.get_images(file_name, page_number, **opts)
        self.assertEqual(responseImages.code, 200)
        image_id = responseImages.images.list[0].id


        response = self.pdf_api.delete_image(file_name, image_id, **opts)
        self.assertEqual(response.code, 200)


    def testGetImages(self):
        file_name = 'PdfWithImages2.pdf'
        self.uploadFile(file_name)

        page_number = 1
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_images(file_name, page_number, **opts)
        self.assertEqual(response.code, 200)


    def testPutReplaceImage(self):
        file_name = 'PdfWithImages2.pdf'
        self.uploadFile(file_name)

        image_file_name = 'Koala.jpg'
        self.uploadFile(image_file_name)

        opts = {
              "folder" : self.temp_folder
        }
        page_number = 1
        responseImages = self.pdf_api.get_images(file_name, page_number, **opts)
        self.assertEqual(responseImages.code, 200)
        image_id = responseImages.images.list[0].id

        opts = {
              "image_file_path" : self.temp_folder + '/' + image_file_name,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_replace_image(file_name, image_id, **opts)
        self.assertEqual(response.code, 200)

    def testPostInsertImage(self):
        file_name = 'PdfWithImages2.pdf'
        self.uploadFile(file_name)

        image_file_name = 'Koala.jpg'
        self.uploadFile(image_file_name)

        page_number = 1
        llx = 10
        lly = 10
        urx = 100
        ury = 100

        opts = {
              "image_file_path" : self.temp_folder + "/" + image_file_name,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.post_insert_image(file_name, page_number, llx, lly, urx, ury, **opts)
        self.assertEqual(response.code, 201)
    
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
        self.assertEqual(response.code, 200)

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
        self.assertEqual(response.code, 200)


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
        self.assertEqual(response.code, 200)


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
        self.assertEqual(response.code, 200)


    def testPutImageExtractAsJpeg(self):
        name = "PdfWithImages2.pdf"
        self.uploadFile(name)
        
        opts = {
              "folder" : self.temp_folder
        }
        page_number = 1
        responseImages = self.pdf_api.get_images(name, page_number, **opts)
        self.assertEqual(responseImages.code, 200)
        image_id = responseImages.images.list[0].id

        dest_folder = "extract_jpg"
        opts = {
            "dest_folder": self.temp_folder + '/' + dest_folder,
            "folder": self.temp_folder
        }
        response = self.pdf_api.put_image_extract_as_jpeg(name, image_id, **opts)
        self.assertEqual(response.code, 200)

    def testGetImageExtractAsJpeg(self):
        name = "PdfWithImages2.pdf"
        self.uploadFile(name)
        
        opts = {
              "folder" : self.temp_folder
        }
        page_number = 1
        responseImages = self.pdf_api.get_images(name, page_number, **opts)
        self.assertEqual(responseImages.code, 200)
        image_id = responseImages.images.list[0].id

        response = self.pdf_api.get_image_extract_as_jpeg(name, image_id, **opts)
        self.assertIsInstance(response, str)

    def testPutImageExtractAsTiff(self):
        name = "PdfWithImages2.pdf"
        self.uploadFile(name)
        
        opts = {
              "folder" : self.temp_folder
        }
        page_number = 1
        responseImages = self.pdf_api.get_images(name, page_number, **opts)
        self.assertEqual(responseImages.code, 200)
        image_id = responseImages.images.list[0].id

        dest_folder = "extract_tiff"
        opts = {
            "dest_folder": self.temp_folder + '/' + dest_folder,
            "folder": self.temp_folder
        }
        response = self.pdf_api.put_image_extract_as_tiff(name, image_id, **opts)
        self.assertEqual(response.code, 200)

    def testGetImageExtractAsTiff(self):
        name = "PdfWithImages2.pdf"
        self.uploadFile(name)
        
        opts = {
              "folder" : self.temp_folder
        }
        page_number = 1
        responseImages = self.pdf_api.get_images(name, page_number, **opts)
        self.assertEqual(responseImages.code, 200)
        image_id = responseImages.images.list[0].id

        response = self.pdf_api.get_image_extract_as_tiff(name, image_id, **opts)
        self.assertIsInstance(response, str)

    def testPutImageExtractAsGif(self):
        name = "PdfWithImages2.pdf"
        self.uploadFile(name)
        
        opts = {
              "folder" : self.temp_folder
        }
        page_number = 1
        responseImages = self.pdf_api.get_images(name, page_number, **opts)
        self.assertEqual(responseImages.code, 200)
        image_id = responseImages.images.list[0].id

        dest_folder = "extract_gif"
        opts = {
            "dest_folder": self.temp_folder + '/' + dest_folder,
            "folder": self.temp_folder
        }
        response = self.pdf_api.put_image_extract_as_gif(name, image_id, **opts)
        self.assertEqual(response.code, 200)

    def testGetImageExtractAsGif(self):
        name = "PdfWithImages2.pdf"
        self.uploadFile(name)
        
        opts = {
              "folder" : self.temp_folder
        }
        page_number = 1
        responseImages = self.pdf_api.get_images(name, page_number, **opts)
        self.assertEqual(responseImages.code, 200)
        image_id = responseImages.images.list[0].id

        response = self.pdf_api.get_image_extract_as_gif(name, image_id, **opts)
        self.assertIsInstance(response, str)


    def testPutImageExtractAsPng(self):
        name = "PdfWithImages2.pdf"
        self.uploadFile(name)
        
        opts = {
              "folder" : self.temp_folder
        }
        page_number = 1
        responseImages = self.pdf_api.get_images(name, page_number, **opts)
        self.assertEqual(responseImages.code, 200)
        image_id = responseImages.images.list[0].id

        dest_folder = "extract_png"
        opts = {
            "dest_folder": self.temp_folder + '/' + dest_folder,
            "folder": self.temp_folder
        }
        response = self.pdf_api.put_image_extract_as_png(name, image_id, **opts)
        self.assertEqual(response.code, 200)

    def testGetImageExtractAsPng(self):
        name = "PdfWithImages2.pdf"
        self.uploadFile(name)
        
        opts = {
              "folder" : self.temp_folder
        }
        page_number = 1
        responseImages = self.pdf_api.get_images(name, page_number, **opts)
        self.assertEqual(responseImages.code, 200)
        image_id = responseImages.images.list[0].id

        response = self.pdf_api.get_image_extract_as_png(name, image_id, **opts)
        self.assertIsInstance(response, str)


    # Links Tests

    def testGetPageLinkAnnotation(self):
        file_name = 'PdfWithLinks.pdf'
        self.uploadFile(file_name)

        page_number = 1
        opts = {
              "folder" : self.temp_folder
        }
        annotations_response = self.pdf_api.get_page_link_annotations(file_name, page_number, **opts)
        self.assertEqual(annotations_response.code, 200)
        link_id = annotations_response.links.list[0].id

        response = self.pdf_api.get_page_link_annotation(file_name, page_number, link_id, **opts)
        self.assertEqual(response.code, 200)

    def testDeleteLinkAnnotation(self):
        file_name = 'PdfWithLinks.pdf'
        self.uploadFile(file_name)

        page_number = 1
        opts = {
              "folder" : self.temp_folder
        }
        annotations_response = self.pdf_api.get_page_link_annotations(file_name, page_number, **opts)
        self.assertEqual(annotations_response.code, 200)
        link_id = annotations_response.links.list[0].id

        response = self.pdf_api.delete_link_annotation(file_name, link_id, **opts)
        self.assertEqual(response.code, 200)

    def testGetPageLinkAnnotations(self):
        file_name = 'PdfWithLinks.pdf'
        self.uploadFile(file_name)

        page_number = 1
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_page_link_annotations(file_name, page_number, **opts)
        self.assertEqual(response.code, 200)

    def testPostPageLinkAnnotations(self):
        file_name = 'PdfWithLinks.pdf'
        self.uploadFile(file_name)

        page_number = 1
        opts = {
              "folder" : self.temp_folder
        }

        rect = asposepdfcloud.models.Rectangle(100, 100, 500, 500)

        linkAnnotation = asposepdfcloud.models.LinkAnnotation()
        linkAnnotation.action_type = asposepdfcloud.models.LinkActionType.GOTOURIACTION
        linkAnnotation.action = "https://products.aspose.cloud/pdf"
        linkAnnotation.rect = rect

        response = self.pdf_api.post_page_link_annotations(file_name, page_number, [linkAnnotation], **opts)
        self.assertEqual(response.code, 201)

    def testPutLinkAnnotation(self):
        file_name = 'PdfWithLinks.pdf'
        self.uploadFile(file_name)

        page_number = 1
        opts = {
              "folder" : self.temp_folder
        }
        
        annotations_response = self.pdf_api.get_page_link_annotations(file_name, page_number, **opts)
        self.assertEqual(annotations_response.code, 200)
        link_id = annotations_response.links.list[0].id

        rect = asposepdfcloud.models.Rectangle(100, 100, 500, 500)

        linkAnnotation = asposepdfcloud.models.LinkAnnotation()
        linkAnnotation.action_type = asposepdfcloud.models.LinkActionType.GOTOURIACTION
        linkAnnotation.action = "https://products.aspose.cloud/pdf"
        linkAnnotation.rect = rect

        response = self.pdf_api.put_link_annotation(file_name, link_id, linkAnnotation, **opts)
        self.assertEqual(response.code, 201)
    
    def testDeletePageLinkAnnotations(self):
        file_name = 'PdfWithLinks.pdf'
        self.uploadFile(file_name)

        page_number = 1
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.delete_page_link_annotations(file_name, page_number, **opts)
        self.assertEqual(response.code, 200)

    def testDeleteDocumentLinkAnnotations(self):
        file_name = 'PdfWithLinks.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.delete_document_link_annotations(file_name, **opts)
        self.assertEqual(response.code, 200)

    def testGetLinkAnnotation(self):
        file_name = 'PdfWithLinks.pdf'
        self.uploadFile(file_name)

        page_number = 1
        opts = {
              "folder" : self.temp_folder
        }

        response_annotations = self.pdf_api.get_page_link_annotations(file_name, page_number, **opts)
        self.assertEqual(response_annotations.code, 200)
        link_id = response_annotations.links.list[0].id

        response = self.pdf_api.get_link_annotation(file_name, link_id, **opts)
        self.assertEqual(response.code, 200)


    # Merge Tests

    def testPutMergeDocuments(self):
        file_name_list = ['4pages.pdf', 'PdfWithImages2.pdf', 'marketing.pdf']
        for file_name in file_name_list:
            self.uploadFile(file_name)
        
        result_name = 'MergingResult.pdf'

        
        
        i = 0
        for el in file_name_list:
            file_name_list[i] = self.temp_folder + '/' + el
            i += 1

        merge_documents = asposepdfcloud.models.MergeDocuments(file_name_list)

        opts = {
              "merge_documents" : merge_documents,
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_merge_documents(result_name, **opts)
        self.assertEqual(response.code, 200)

    
    # OCR Tests

    def testPutSearchableDocument(self):
        file_name = 'rusdoc.pdf'
        self.uploadFile(file_name)

        opts = {
              "lang" : 'rus,eng',
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_searchable_document(file_name, **opts)
        self.assertEqual(response.code, 200)

    def testPutSearchableDocumentWithDefaultLang(self):
        file_name = 'rusdoc.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_searchable_document(file_name, **opts)
        self.assertEqual(response.code, 200)


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
        self.assertEqual(response.code, 200)


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
        self.assertEqual(response.code, 200)

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
        self.assertEqual(response.code, 200)

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
        self.assertEqual(response.code, 200)


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
        self.assertEqual(response.code, 200)


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
        self.assertEqual(response.code, 200)
    
    # Pages Tests

    def testDeletePage(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 1
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.delete_page(file_name, page_number, **opts)
        self.assertEqual(response.code, 200)


    def testGetPage(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 3
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_page(file_name, page_number, **opts)
        self.assertEqual(response.code, 200)

    def testGetPages(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_pages(file_name, **opts)
        self.assertEqual(response.code, 200)


    def testGetWordsPerPage(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_words_per_page(file_name, **opts)
        self.assertEqual(response.code, 200)


    def testPostMovePage(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }
        page_number = 1
        new_index = 1

        response = self.pdf_api.post_move_page(file_name, page_number, new_index, **opts)
        self.assertEqual(response.code, 200)


    def testPutAddNewPage(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_add_new_page(file_name, **opts)
        self.assertEqual(response.code, 200)


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
        self.assertEqual(response.code, 200)
    
    
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
        self.assertEqual(response.code, 200)


    # Properties Tests

    def testDeleteProperties(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        property_1 = asposepdfcloud.models.DocumentProperty()
        property_1.name = 'prop1'
        property_1.value = 'val1'

        opts = {
              "folder" : self.temp_folder
        }

        property_2 = asposepdfcloud.models.DocumentProperty()
        property_2.name = 'prop2'
        property_2.value = 'val2'

        self.pdf_api.put_set_property(file_name, property_1.name, property_1.value, **opts)
        self.pdf_api.put_set_property(file_name, property_2.name, property_2.value, **opts)

        response = self.pdf_api.delete_properties(file_name, **opts)
        self.assertEqual(response.code, 200)


    def testDeleteProperty(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        property_1 = asposepdfcloud.models.DocumentProperty()
        property_1.name = 'prop1'
        property_1.value = 'val1'

        opts = {
              "folder" : self.temp_folder
        }

        self.pdf_api.put_set_property(file_name, property_1.name, property_1.value, **opts)

        response = self.pdf_api.delete_property(file_name, property_1.name, **opts)
        self.assertEqual(response.code, 200)


    def testGetDocumentProperties(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        property_1 = asposepdfcloud.models.DocumentProperty()
        property_1.name = 'prop1'
        property_1.value = 'val1'

        opts = {
              "folder" : self.temp_folder
        }

        property_2 = asposepdfcloud.models.DocumentProperty()
        property_2.name = 'prop2'
        property_2.value = 'val2'

        self.pdf_api.put_set_property(file_name, property_1.name, property_1.value, **opts)
        self.pdf_api.put_set_property(file_name, property_2.name, property_2.value, **opts)

        response = self.pdf_api.get_document_properties(file_name, **opts)
        self.assertEqual(response.code, 200)


    def testGetDocumentProperty(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        property_1 = asposepdfcloud.models.DocumentProperty()
        property_1.name = 'prop1'
        property_1.value = 'val1'

        opts = {
              "folder" : self.temp_folder
        }

        self.pdf_api.put_set_property(file_name, property_1.name, property_1.value, **opts)

        response = self.pdf_api.get_document_property(file_name, property_1.name, **opts)
        self.assertEqual(response.code, 200)


    def testPutSetProperty(self):
        file_name = 'PdfWithAcroForm.pdf'
        self.uploadFile(file_name)

        property_1 = asposepdfcloud.models.DocumentProperty()
        property_1.name = 'prop1'
        property_1.value = 'val1'

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.put_set_property(file_name, property_1.name, property_1.value, **opts)
        self.assertEqual(response.code, 200)

    
    # Sign Tests

    def testPostSignDocument(self):
        file_name = 'BlankWithSignature.pdf'
        self.uploadFile(file_name)

        signature_file_name = 'test1234.pfx'
        self.uploadFile(signature_file_name)

        rectangle = asposepdfcloud.models.Rectangle(100, 100, 500, 500)
        
        signature = asposepdfcloud.models.Signature(
                signature_path=self.temp_folder + '/' + signature_file_name,
                signature_type=asposepdfcloud.models.SignatureType.PKCS7,
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
        self.assertEqual(response.code, 200)


    def testPostSignPage(self):
        file_name = 'BlankWithSignature.pdf'
        self.uploadFile(file_name)

        signature_file_name = 'test1234.pfx'
        self.uploadFile(signature_file_name)

        page_number = 1

        rectangle = asposepdfcloud.models.Rectangle(100, 100, 500, 500)

        signature = asposepdfcloud.models.Signature(
                signature_path=self.temp_folder + '/' + signature_file_name,
                signature_type=asposepdfcloud.models.SignatureType.PKCS7,
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
        self.assertEqual(response.code, 200)
    
    def testGetVerifySignature(self):
        file_name = 'BlankWithSignature.pdf'
        self.uploadFile(file_name)

        signature_file_name = 'test1234.pfx'
        self.uploadFile(signature_file_name)

        rectangle = asposepdfcloud.models.Rectangle(100, 100, 500, 500)
        
        signature = asposepdfcloud.models.Signature(
                signature_path=self.temp_folder + '/' + signature_file_name,
                signature_type=asposepdfcloud.models.SignatureType.PKCS7,
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
        self.assertEqual(response_sign.code, 200)

        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_verify_signature(file_name, signature.form_field_name, **opts)
        self.assertEqual(response.code, 200)


    # Text Replace Tests

    def testPostDocumentTextReplace(self):
        file_name = 'marketing.pdf'
        self.uploadFile(file_name)
        
        rect = asposepdfcloud.models.Rectangle(100, 100, 300, 300)

        text_replace = asposepdfcloud.models.TextReplace(
                old_value='market',
                new_value='m_a_r_k_e_t',
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
        self.assertEqual(response.code, 200)


    def testPostPageTextReplaceByRect(self):
        file_name = 'marketing.pdf'
        self.uploadFile(file_name)
        page_number = 1

        rect = asposepdfcloud.models.Rectangle(100, 100, 400, 400)

        text_replace = asposepdfcloud.models.TextReplace(
                old_value='market',
                new_value='m_a_r_k_e_t',
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
        self.assertEqual(response.code, 200)


    # Text Tests

    def testGetText(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        llx = 0
        lly = 0
        urx = 0
        ury = 0
        opts = {
              "folder" : self.temp_folder
        }

        response = self.pdf_api.get_text(file_name, llx, lly, urx, ury, **opts)
        self.assertEqual(response.code, 200)


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
        self.assertEqual(response.code, 200)


    def testPutAddText(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)

        page_number = 1

        rectangle = asposepdfcloud.models.Rectangle(100, 100, 300, 300)
        
        foreground_color = asposepdfcloud.models.Color(a=0x00, r=0x00, g=0xFF, b=0x00)
        
        background_color = asposepdfcloud.models.Color(a=0x00, r=0xFF, g=0x00, b=0x00)
        
        text_state = asposepdfcloud.models.TextState(
                    font_size=10, 
                    font='Arial', 
                    foreground_color=foreground_color,
                    background_color=background_color,
                    font_style=asposepdfcloud.models.FontStyles.BOLD)

        segment = asposepdfcloud.models.Segment(value='segment 1', text_state=text_state)

        text_line = asposepdfcloud.models.TextLine(horizontal_alignment=asposepdfcloud.models.TextHorizontalAlignment.RIGHT,
            segments=[segment])

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
        self.assertEqual(response.code, 200)


    # Storage Tests
    
    def testPutCreate(self):
        file_name = '4pages.pdf'
        response = self.pdf_api.put_create(self.temp_folder + '/' + file_name, self.test_data_path + file_name)
        self.assertEqual(response.code, 200)
    
    def testGetDownload(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        response = self.pdf_api.get_download(self.temp_folder + '/' + file_name)
        self.assertIsInstance(response, str)

    def testGetListFiles(self):
        response = self.pdf_api.get_list_files(path=self.temp_folder)
        self.assertEqual(response.code, 200)

    def testPostMoveFile(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        src = self.temp_folder + '/' + file_name
        dest = self.temp_folder + '/4pages_renamed.pdf'

        response = self.pdf_api.post_move_file(src, dest)
        self.assertEqual(response.code, 200)

    def testDeleteFile(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        path = self.temp_folder + '/' + file_name
        
        response = self.pdf_api.delete_file(path)
        self.assertEqual(response.code, 200)

    def testPutCreateFolder(self):

        path = self.temp_folder + '/testFolder'
        
        response = self.pdf_api.put_create_folder(path)
        self.assertEqual(response.code, 200)

    def testPostMoveFolder(self):

        src = self.temp_folder + '/testFolder'
        response_create_folder = self.pdf_api.put_create_folder(src)
        self.assertEqual(response_create_folder.code, 200)

        dest = self.temp_folder + '/testFolderRednamed'

        response = self.pdf_api.post_move_folder(src, dest)
        self.assertEqual(response.code, 200)

    def testDeleteFolder(self):

        path = self.temp_folder + '/testFolder'
        response_create_folder = self.pdf_api.put_create_folder(path)
        self.assertEqual(response_create_folder.code, 200)

        response = self.pdf_api.delete_folder(path)
        self.assertEqual(response.code, 200)

    def testGetIsStorageExist(self):
        name = 'PDF-CI'
        
        response = self.pdf_api.get_is_storage_exist(name)
        self.assertEqual(response.code, 200)

    def testGetIsExist(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        path = self.temp_folder + '/' + file_name
        
        response = self.pdf_api.get_is_exist(path)
        self.assertEqual(response.code, 200)

    def testGetDiscUsage(self):
        
        response = self.pdf_api.get_disc_usage()
        self.assertEqual(response.code, 200)

    def testGetListFileVersion(self):
        file_name = '4pages.pdf'
        self.uploadFile(file_name)
        path = self.temp_folder + '/' + file_name
        
        response = self.pdf_api.get_list_file_versions(path)
        self.assertEqual(response.code, 200)

if __name__ == '__main__':
    unittest.main()
