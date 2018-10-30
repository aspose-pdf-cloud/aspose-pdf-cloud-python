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



    OpenAPI spec version: 2.0
    
"""


from __future__ import absolute_import

# import models into sdk package
from .models.annotation_flags import AnnotationFlags
from .models.annotation_state import AnnotationState
from .models.annotation_type import AnnotationType
from .models.antialiasing_processing_type import AntialiasingProcessingType
from .models.append_document import AppendDocument
from .models.aspose_response import AsposeResponse
from .models.caption_position import CaptionPosition
from .models.color import Color
from .models.color_depth import ColorDepth
from .models.compression_type import CompressionType
from .models.doc_format import DocFormat
from .models.doc_recognition_mode import DocRecognitionMode
from .models.document_privilege import DocumentPrivilege
from .models.epub_recognition_mode import EpubRecognitionMode
from .models.field_type import FieldType
from .models.font_encoding_rules import FontEncodingRules
from .models.font_saving_modes import FontSavingModes
from .models.font_styles import FontStyles
from .models.free_text_intent import FreeTextIntent
from .models.horizontal_alignment import HorizontalAlignment
from .models.html_document_type import HtmlDocumentType
from .models.html_markup_generation_modes import HtmlMarkupGenerationModes
from .models.image_src_type import ImageSrcType
from .models.image_template import ImageTemplate
from .models.image_templates_request import ImageTemplatesRequest
from .models.justification import Justification
from .models.letters_positioning_methods import LettersPositioningMethods
from .models.line_ending import LineEnding
from .models.line_intent import LineIntent
from .models.line_spacing import LineSpacing
from .models.link import Link
from .models.link_action_type import LinkActionType
from .models.link_element import LinkElement
from .models.link_highlighting_mode import LinkHighlightingMode
from .models.margin_info import MarginInfo
from .models.merge_documents import MergeDocuments
from .models.optimize_options import OptimizeOptions
from .models.page_word_count import PageWordCount
from .models.paragraph import Paragraph
from .models.parts_embedding_modes import PartsEmbeddingModes
from .models.pdf_a_type import PdfAType
from .models.point import Point
from .models.poly_intent import PolyIntent
from .models.raster_images_saving_modes import RasterImagesSavingModes
from .models.rectangle_pdf import RectanglePdf
from .models.rotation import Rotation
from .models.segment import Segment
from .models.shape_type import ShapeType
from .models.signature import Signature
from .models.signature_type import SignatureType
from .models.split_result import SplitResult
from .models.stamp import Stamp
from .models.stamp_type import StampType
from .models.text_horizontal_alignment import TextHorizontalAlignment
from .models.text_icon import TextIcon
from .models.text_line import TextLine
from .models.text_rect import TextRect
from .models.text_rects import TextRects
from .models.text_replace import TextReplace
from .models.text_replace_list_request import TextReplaceListRequest
from .models.text_state import TextState
from .models.text_style import TextStyle
from .models.vertical_alignment import VerticalAlignment
from .models.word_count import WordCount
from .models.wrap_mode import WrapMode
from .models.annotation import Annotation
from .models.annotations_info import AnnotationsInfo
from .models.annotations_info_response import AnnotationsInfoResponse
from .models.attachment import Attachment
from .models.attachment_response import AttachmentResponse
from .models.attachments import Attachments
from .models.attachments_response import AttachmentsResponse
from .models.circle_annotation_response import CircleAnnotationResponse
from .models.circle_annotations import CircleAnnotations
from .models.circle_annotations_response import CircleAnnotationsResponse
from .models.document import Document
from .models.document_page_response import DocumentPageResponse
from .models.document_pages_response import DocumentPagesResponse
from .models.document_properties import DocumentProperties
from .models.document_properties_response import DocumentPropertiesResponse
from .models.document_property import DocumentProperty
from .models.document_property_response import DocumentPropertyResponse
from .models.document_response import DocumentResponse
from .models.field import Field
from .models.field_response import FieldResponse
from .models.fields import Fields
from .models.fields_response import FieldsResponse
from .models.free_text_annotation_response import FreeTextAnnotationResponse
from .models.free_text_annotations import FreeTextAnnotations
from .models.free_text_annotations_response import FreeTextAnnotationsResponse
from .models.image import Image
from .models.image_response import ImageResponse
from .models.images import Images
from .models.images_response import ImagesResponse
from .models.line_annotation_response import LineAnnotationResponse
from .models.line_annotations import LineAnnotations
from .models.line_annotations_response import LineAnnotationsResponse
from .models.link_annotation import LinkAnnotation
from .models.link_annotation_response import LinkAnnotationResponse
from .models.link_annotations import LinkAnnotations
from .models.link_annotations_response import LinkAnnotationsResponse
from .models.page import Page
from .models.pages import Pages
from .models.poly_line_annotation_response import PolyLineAnnotationResponse
from .models.poly_line_annotations import PolyLineAnnotations
from .models.poly_line_annotations_response import PolyLineAnnotationsResponse
from .models.polygon_annotation_response import PolygonAnnotationResponse
from .models.polygon_annotations import PolygonAnnotations
from .models.polygon_annotations_response import PolygonAnnotationsResponse
from .models.signature_verify_response import SignatureVerifyResponse
from .models.split_result_document import SplitResultDocument
from .models.split_result_response import SplitResultResponse
from .models.square_annotation_response import SquareAnnotationResponse
from .models.square_annotations import SquareAnnotations
from .models.square_annotations_response import SquareAnnotationsResponse
from .models.text_annotation_response import TextAnnotationResponse
from .models.text_annotations import TextAnnotations
from .models.text_annotations_response import TextAnnotationsResponse
from .models.text_rects_response import TextRectsResponse
from .models.text_replace_response import TextReplaceResponse
from .models.word_count_response import WordCountResponse
from .models.annotation_info import AnnotationInfo
from .models.markup_annotation import MarkupAnnotation
from .models.common_figure_annotation import CommonFigureAnnotation
from .models.free_text_annotation import FreeTextAnnotation
from .models.line_annotation import LineAnnotation
from .models.poly_annotation import PolyAnnotation
from .models.text_annotation import TextAnnotation
from .models.circle_annotation import CircleAnnotation
from .models.poly_line_annotation import PolyLineAnnotation
from .models.polygon_annotation import PolygonAnnotation
from .models.square_annotation import SquareAnnotation

# import apis into sdk package
from .apis.pdf_api import PdfApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
