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

# import models into model package
from .annotation_flags import AnnotationFlags
from .annotation_state import AnnotationState
from .annotation_type import AnnotationType
from .antialiasing_processing_type import AntialiasingProcessingType
from .append_document import AppendDocument
from .aspose_response import AsposeResponse
from .caption_position import CaptionPosition
from .color import Color
from .color_depth import ColorDepth
from .compression_type import CompressionType
from .doc_format import DocFormat
from .doc_recognition_mode import DocRecognitionMode
from .document_privilege import DocumentPrivilege
from .epub_recognition_mode import EpubRecognitionMode
from .field_type import FieldType
from .font_encoding_rules import FontEncodingRules
from .font_saving_modes import FontSavingModes
from .font_styles import FontStyles
from .free_text_intent import FreeTextIntent
from .horizontal_alignment import HorizontalAlignment
from .html_document_type import HtmlDocumentType
from .html_markup_generation_modes import HtmlMarkupGenerationModes
from .image_src_type import ImageSrcType
from .image_template import ImageTemplate
from .image_templates_request import ImageTemplatesRequest
from .justification import Justification
from .letters_positioning_methods import LettersPositioningMethods
from .line_ending import LineEnding
from .line_intent import LineIntent
from .line_spacing import LineSpacing
from .link import Link
from .link_action_type import LinkActionType
from .link_element import LinkElement
from .link_highlighting_mode import LinkHighlightingMode
from .margin_info import MarginInfo
from .merge_documents import MergeDocuments
from .optimize_options import OptimizeOptions
from .page_word_count import PageWordCount
from .paragraph import Paragraph
from .parts_embedding_modes import PartsEmbeddingModes
from .pdf_a_type import PdfAType
from .point import Point
from .poly_intent import PolyIntent
from .raster_images_saving_modes import RasterImagesSavingModes
from .rectangle_pdf import RectanglePdf
from .rotation import Rotation
from .segment import Segment
from .shape_type import ShapeType
from .signature import Signature
from .signature_type import SignatureType
from .split_result import SplitResult
from .stamp import Stamp
from .stamp_type import StampType
from .text_horizontal_alignment import TextHorizontalAlignment
from .text_icon import TextIcon
from .text_line import TextLine
from .text_rect import TextRect
from .text_rects import TextRects
from .text_replace import TextReplace
from .text_replace_list_request import TextReplaceListRequest
from .text_state import TextState
from .text_style import TextStyle
from .vertical_alignment import VerticalAlignment
from .word_count import WordCount
from .wrap_mode import WrapMode
from .annotation import Annotation
from .annotations_info import AnnotationsInfo
from .annotations_info_response import AnnotationsInfoResponse
from .attachment import Attachment
from .attachment_response import AttachmentResponse
from .attachments import Attachments
from .attachments_response import AttachmentsResponse
from .circle_annotation_response import CircleAnnotationResponse
from .circle_annotations import CircleAnnotations
from .circle_annotations_response import CircleAnnotationsResponse
from .document import Document
from .document_page_response import DocumentPageResponse
from .document_pages_response import DocumentPagesResponse
from .document_properties import DocumentProperties
from .document_properties_response import DocumentPropertiesResponse
from .document_property import DocumentProperty
from .document_property_response import DocumentPropertyResponse
from .document_response import DocumentResponse
from .field import Field
from .field_response import FieldResponse
from .fields import Fields
from .fields_response import FieldsResponse
from .free_text_annotation_response import FreeTextAnnotationResponse
from .free_text_annotations import FreeTextAnnotations
from .free_text_annotations_response import FreeTextAnnotationsResponse
from .image import Image
from .image_response import ImageResponse
from .images import Images
from .images_response import ImagesResponse
from .line_annotation_response import LineAnnotationResponse
from .line_annotations import LineAnnotations
from .line_annotations_response import LineAnnotationsResponse
from .link_annotation import LinkAnnotation
from .link_annotation_response import LinkAnnotationResponse
from .link_annotations import LinkAnnotations
from .link_annotations_response import LinkAnnotationsResponse
from .page import Page
from .pages import Pages
from .poly_line_annotation_response import PolyLineAnnotationResponse
from .poly_line_annotations import PolyLineAnnotations
from .poly_line_annotations_response import PolyLineAnnotationsResponse
from .polygon_annotation_response import PolygonAnnotationResponse
from .polygon_annotations import PolygonAnnotations
from .polygon_annotations_response import PolygonAnnotationsResponse
from .signature_verify_response import SignatureVerifyResponse
from .split_result_document import SplitResultDocument
from .split_result_response import SplitResultResponse
from .square_annotation_response import SquareAnnotationResponse
from .square_annotations import SquareAnnotations
from .square_annotations_response import SquareAnnotationsResponse
from .text_annotation_response import TextAnnotationResponse
from .text_annotations import TextAnnotations
from .text_annotations_response import TextAnnotationsResponse
from .text_rects_response import TextRectsResponse
from .text_replace_response import TextReplaceResponse
from .word_count_response import WordCountResponse
from .annotation_info import AnnotationInfo
from .markup_annotation import MarkupAnnotation
from .common_figure_annotation import CommonFigureAnnotation
from .free_text_annotation import FreeTextAnnotation
from .line_annotation import LineAnnotation
from .poly_annotation import PolyAnnotation
from .text_annotation import TextAnnotation
from .circle_annotation import CircleAnnotation
from .poly_line_annotation import PolyLineAnnotation
from .polygon_annotation import PolygonAnnotation
from .square_annotation import SquareAnnotation
