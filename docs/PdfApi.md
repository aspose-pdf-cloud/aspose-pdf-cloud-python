# swagger_client.PdfApi

All URIs are relative to *https://api.aspose.cloud/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_annotation**](PdfApi.md#delete_annotation) | **DELETE** /pdf/{name}/annotations/{annotationId} | Delete document annotation by ID
[**delete_document_annotations**](PdfApi.md#delete_document_annotations) | **DELETE** /pdf/{name}/annotations | Delete all annotations from the document
[**delete_document_link_annotations**](PdfApi.md#delete_document_link_annotations) | **DELETE** /pdf/{name}/links | Delete all link annotations from the document
[**delete_field**](PdfApi.md#delete_field) | **DELETE** /pdf/{name}/fields/{fieldName} | Delete document field by name.
[**delete_image**](PdfApi.md#delete_image) | **DELETE** /pdf/{name}/images/{imageId} | Delete image from document page.
[**delete_link_annotation**](PdfApi.md#delete_link_annotation) | **DELETE** /pdf/{name}/links/{linkId} | Delete document page link annotation by ID
[**delete_page**](PdfApi.md#delete_page) | **DELETE** /pdf/{name}/pages/{pageNumber} | Delete document page by its number.
[**delete_page_annotations**](PdfApi.md#delete_page_annotations) | **DELETE** /pdf/{name}/pages/{pageNumber}/annotations | Delete all annotations from the page
[**delete_page_link_annotations**](PdfApi.md#delete_page_link_annotations) | **DELETE** /pdf/{name}/pages/{pageNumber}/links | Delete all link annotations from the page
[**delete_properties**](PdfApi.md#delete_properties) | **DELETE** /pdf/{name}/documentproperties | Delete custom document properties.
[**delete_property**](PdfApi.md#delete_property) | **DELETE** /pdf/{name}/documentproperties/{propertyName} | Delete document property.
[**get_document**](PdfApi.md#get_document) | **GET** /pdf/{name} | Read common document info.
[**get_document_annotations**](PdfApi.md#get_document_annotations) | **GET** /pdf/{name}/annotations | Read documant page annotations. Returns only FreeTextAnnotations, TextAnnotations, other annotations will implemented next releases.
[**get_document_attachment_by_index**](PdfApi.md#get_document_attachment_by_index) | **GET** /pdf/{name}/attachments/{attachmentIndex} | Read document attachment info by its index.
[**get_document_attachments**](PdfApi.md#get_document_attachments) | **GET** /pdf/{name}/attachments | Read document attachments info.
[**get_document_bookmarks**](PdfApi.md#get_document_bookmarks) | **GET** /pdf/{name}/bookmarks | Read document bookmark/bookmarks (including children).
[**get_document_free_text_annotations**](PdfApi.md#get_document_free_text_annotations) | **GET** /pdf/{name}/annotations/freetext | Read document free text annotations.
[**get_document_properties**](PdfApi.md#get_document_properties) | **GET** /pdf/{name}/documentproperties | Read document properties.
[**get_document_property**](PdfApi.md#get_document_property) | **GET** /pdf/{name}/documentproperties/{propertyName} | Read document property by name.
[**get_document_text_annotations**](PdfApi.md#get_document_text_annotations) | **GET** /pdf/{name}/annotations/text | Read document text annotations.
[**get_download**](PdfApi.md#get_download) | **GET** /storage/file | Download a specific file 
[**get_download_document_attachment_by_index**](PdfApi.md#get_download_document_attachment_by_index) | **GET** /pdf/{name}/attachments/{attachmentIndex}/download | Download document attachment content by its index.
[**get_epub_in_storage_to_pdf**](PdfApi.md#get_epub_in_storage_to_pdf) | **GET** /pdf/create/epub | Convert EPUB file (located on storage) to PDF format and return resulting file in response. 
[**get_field**](PdfApi.md#get_field) | **GET** /pdf/{name}/fields/{fieldName} | Get document field by name.
[**get_fields**](PdfApi.md#get_fields) | **GET** /pdf/{name}/fields | Get document fields.
[**get_free_text_annotation**](PdfApi.md#get_free_text_annotation) | **GET** /pdf/{name}/annotations/freetext/{annotationId} | Read document page free text annotation by ID.
[**get_html_in_storage_to_pdf**](PdfApi.md#get_html_in_storage_to_pdf) | **GET** /pdf/create/html | Convert HTML file (located on storage) to PDF format and return resulting file in response. 
[**get_image**](PdfApi.md#get_image) | **GET** /pdf/{name}/images/{imageId} | Read document image by ID.
[**get_image_extract_as_gif**](PdfApi.md#get_image_extract_as_gif) | **GET** /pdf/{name}/images/{imageId}/extract/gif | Extract document image in GIF format
[**get_image_extract_as_jpeg**](PdfApi.md#get_image_extract_as_jpeg) | **GET** /pdf/{name}/images/{imageId}/extract/jpeg | Extract document image in JPEG format
[**get_image_extract_as_png**](PdfApi.md#get_image_extract_as_png) | **GET** /pdf/{name}/images/{imageId}/extract/png | Extract document image in PNG format
[**get_image_extract_as_tiff**](PdfApi.md#get_image_extract_as_tiff) | **GET** /pdf/{name}/images/{imageId}/extract/tiff | Extract document image in TIFF format
[**get_images**](PdfApi.md#get_images) | **GET** /pdf/{name}/pages/{pageNumber}/images | Read document images.
[**get_la_te_x_in_storage_to_pdf**](PdfApi.md#get_la_te_x_in_storage_to_pdf) | **GET** /pdf/create/latex | Convert LaTeX file (located on storage) to PDF format and return resulting file in response. 
[**get_link_annotation**](PdfApi.md#get_link_annotation) | **GET** /pdf/{name}/links/{linkId} | Read document link annotation by ID.
[**get_mht_in_storage_to_pdf**](PdfApi.md#get_mht_in_storage_to_pdf) | **GET** /pdf/create/mht | Convert MHT file (located on storage) to PDF format and return resulting file in response. 
[**get_page**](PdfApi.md#get_page) | **GET** /pdf/{name}/pages/{pageNumber} | Read document page info.
[**get_page_annotations**](PdfApi.md#get_page_annotations) | **GET** /pdf/{name}/pages/{pageNumber}/annotations | Read documant page annotations. Returns only FreeTextAnnotations, TextAnnotations, other annotations will implemented next releases.
[**get_page_convert_to_bmp**](PdfApi.md#get_page_convert_to_bmp) | **GET** /pdf/{name}/pages/{pageNumber}/convert/bmp | Convert document page to Bmp image and return resulting file in response.
[**get_page_convert_to_emf**](PdfApi.md#get_page_convert_to_emf) | **GET** /pdf/{name}/pages/{pageNumber}/convert/emf | Convert document page to Emf image and return resulting file in response.
[**get_page_convert_to_gif**](PdfApi.md#get_page_convert_to_gif) | **GET** /pdf/{name}/pages/{pageNumber}/convert/gif | Convert document page to Gif image and return resulting file in response.
[**get_page_convert_to_jpeg**](PdfApi.md#get_page_convert_to_jpeg) | **GET** /pdf/{name}/pages/{pageNumber}/convert/jpeg | Convert document page to Jpeg image and return resulting file in response.
[**get_page_convert_to_png**](PdfApi.md#get_page_convert_to_png) | **GET** /pdf/{name}/pages/{pageNumber}/convert/png | Convert document page to Png image and return resulting file in response.
[**get_page_convert_to_tiff**](PdfApi.md#get_page_convert_to_tiff) | **GET** /pdf/{name}/pages/{pageNumber}/convert/tiff | Convert document page to Tiff image  and return resulting file in response.
[**get_page_free_text_annotations**](PdfApi.md#get_page_free_text_annotations) | **GET** /pdf/{name}/pages/{pageNumber}/annotations/freetext | Read document page free text annotations.
[**get_page_link_annotation**](PdfApi.md#get_page_link_annotation) | **GET** /pdf/{name}/pages/{pageNumber}/links/{linkId} | Read document page link annotation by ID.
[**get_page_link_annotations**](PdfApi.md#get_page_link_annotations) | **GET** /pdf/{name}/pages/{pageNumber}/links | Read document page link annotations.
[**get_page_text**](PdfApi.md#get_page_text) | **GET** /pdf/{name}/pages/{pageNumber}/text | Read page text items.
[**get_page_text_annotations**](PdfApi.md#get_page_text_annotations) | **GET** /pdf/{name}/pages/{pageNumber}/annotations/text | Read document page text annotations.
[**get_pages**](PdfApi.md#get_pages) | **GET** /pdf/{name}/pages | Read document pages info.
[**get_pcl_in_storage_to_pdf**](PdfApi.md#get_pcl_in_storage_to_pdf) | **GET** /pdf/create/pcl | Convert PCL file (located on storage) to PDF format and return resulting file in response. 
[**get_pdf_in_storage_to_doc**](PdfApi.md#get_pdf_in_storage_to_doc) | **GET** /pdf/{name}/convert/doc | Converts PDF document (located on storage) to DOC format and returns resulting file in response content
[**get_pdf_in_storage_to_epub**](PdfApi.md#get_pdf_in_storage_to_epub) | **GET** /pdf/{name}/convert/epub | Converts PDF document (located on storage) to EPUB format and returns resulting file in response content
[**get_pdf_in_storage_to_html**](PdfApi.md#get_pdf_in_storage_to_html) | **GET** /pdf/{name}/convert/html | Converts PDF document (located on storage) to Html format and returns resulting file in response content
[**get_pdf_in_storage_to_la_te_x**](PdfApi.md#get_pdf_in_storage_to_la_te_x) | **GET** /pdf/{name}/convert/latex | Converts PDF document (located on storage) to LaTeX format and returns resulting file in response content
[**get_pdf_in_storage_to_mobi_xml**](PdfApi.md#get_pdf_in_storage_to_mobi_xml) | **GET** /pdf/{name}/convert/mobixml | Converts PDF document (located on storage) to MOBIXML format and returns resulting file in response content
[**get_pdf_in_storage_to_pdf_a**](PdfApi.md#get_pdf_in_storage_to_pdf_a) | **GET** /pdf/{name}/convert/pdfa | Converts PDF document (located on storage) to PdfA format and returns resulting file in response content
[**get_pdf_in_storage_to_pptx**](PdfApi.md#get_pdf_in_storage_to_pptx) | **GET** /pdf/{name}/convert/pptx | Converts PDF document (located on storage) to PPTX format and returns resulting file in response content
[**get_pdf_in_storage_to_svg**](PdfApi.md#get_pdf_in_storage_to_svg) | **GET** /pdf/{name}/convert/svg | Converts PDF document (located on storage) to SVG format and returns resulting file in response content
[**get_pdf_in_storage_to_tiff**](PdfApi.md#get_pdf_in_storage_to_tiff) | **GET** /pdf/{name}/convert/tiff | Converts PDF document (located on storage) to TIFF format and returns resulting file in response content
[**get_pdf_in_storage_to_xls**](PdfApi.md#get_pdf_in_storage_to_xls) | **GET** /pdf/{name}/convert/xls | Converts PDF document (located on storage) to XLS format and returns resulting file in response content
[**get_pdf_in_storage_to_xml**](PdfApi.md#get_pdf_in_storage_to_xml) | **GET** /pdf/{name}/convert/xml | Converts PDF document (located on storage) to XML format and returns resulting file in response content
[**get_pdf_in_storage_to_xps**](PdfApi.md#get_pdf_in_storage_to_xps) | **GET** /pdf/{name}/convert/xps | Converts PDF document (located on storage) to XPS format and returns resulting file in response content
[**get_ps_in_storage_to_pdf**](PdfApi.md#get_ps_in_storage_to_pdf) | **GET** /pdf/create/ps | Convert PS file (located on storage) to PDF format and return resulting file in response. 
[**get_svg_in_storage_to_pdf**](PdfApi.md#get_svg_in_storage_to_pdf) | **GET** /pdf/create/svg | Convert SVG file (located on storage) to PDF format and return resulting file in response. 
[**get_text**](PdfApi.md#get_text) | **GET** /pdf/{name}/text | Read document text.
[**get_text_annotation**](PdfApi.md#get_text_annotation) | **GET** /pdf/{name}/annotations/text/{annotationId} | Read document page text annotation by ID.
[**get_verify_signature**](PdfApi.md#get_verify_signature) | **GET** /pdf/{name}/verifySignature | Verify signature document.
[**get_web_in_storage_to_pdf**](PdfApi.md#get_web_in_storage_to_pdf) | **GET** /pdf/create/web | Convert web page to PDF format and return resulting file in response. 
[**get_words_per_page**](PdfApi.md#get_words_per_page) | **GET** /pdf/{name}/pages/wordCount | Get number of words per document page.
[**get_xfa_pdf_in_storage_to_acro_form**](PdfApi.md#get_xfa_pdf_in_storage_to_acro_form) | **GET** /pdf/{name}/convert/xfatoacroform | Converts PDF document which contatins XFA form (located on storage) to PDF with AcroForm and returns resulting file response content
[**get_xml_in_storage_to_pdf**](PdfApi.md#get_xml_in_storage_to_pdf) | **GET** /pdf/create/xml | Convert XML file (located on storage) to PDF format and return resulting file in response. 
[**get_xps_in_storage_to_pdf**](PdfApi.md#get_xps_in_storage_to_pdf) | **GET** /pdf/create/xps | Convert XPS file (located on storage) to PDF format and return resulting file in response. 
[**get_xsl_fo_in_storage_to_pdf**](PdfApi.md#get_xsl_fo_in_storage_to_pdf) | **GET** /pdf/create/xslfo | Convert XslFo file (located on storage) to PDF format and return resulting file in response. 
[**post_append_document**](PdfApi.md#post_append_document) | **POST** /pdf/{name}/appendDocument | Append document to existing one.
[**post_create_field**](PdfApi.md#post_create_field) | **POST** /pdf/{name}/fields | Create field.
[**post_document_text_replace**](PdfApi.md#post_document_text_replace) | **POST** /pdf/{name}/text/replace | Document&#39;s replace text method.
[**post_insert_image**](PdfApi.md#post_insert_image) | **POST** /pdf/{name}/pages/{pageNumber}/images | Insert image to document page.
[**post_move_page**](PdfApi.md#post_move_page) | **POST** /pdf/{name}/pages/{pageNumber}/movePage | Move page to new position.
[**post_optimize_document**](PdfApi.md#post_optimize_document) | **POST** /pdf/{name}/optimize | Optimize document.
[**post_page_free_text_annotations**](PdfApi.md#post_page_free_text_annotations) | **POST** /pdf/{name}/pages/{pageNumber}/annotations/freetext | Add document page free text annotations.
[**post_page_link_annotations**](PdfApi.md#post_page_link_annotations) | **POST** /pdf/{name}/pages/{pageNumber}/links | Add document page link annotations.
[**post_page_text_annotations**](PdfApi.md#post_page_text_annotations) | **POST** /pdf/{name}/pages/{pageNumber}/annotations/text | Add document page text annotations.
[**post_page_text_replace**](PdfApi.md#post_page_text_replace) | **POST** /pdf/{name}/pages/{pageNumber}/text/replace | Page&#39;s replace text method.
[**post_sign_document**](PdfApi.md#post_sign_document) | **POST** /pdf/{name}/sign | Sign document.
[**post_sign_page**](PdfApi.md#post_sign_page) | **POST** /pdf/{name}/pages/{pageNumber}/sign | Sign page.
[**post_split_document**](PdfApi.md#post_split_document) | **POST** /pdf/{name}/split | Split document to parts.
[**put_add_new_page**](PdfApi.md#put_add_new_page) | **PUT** /pdf/{name}/pages | Add new page to end of the document.
[**put_add_text**](PdfApi.md#put_add_text) | **PUT** /pdf/{name}/pages/{pageNumber}/text | Add text to PDF document page.
[**put_create**](PdfApi.md#put_create) | **PUT** /storage/file | Upload a specific file 
[**put_create_document**](PdfApi.md#put_create_document) | **PUT** /pdf/{name} | Create empty document.
[**put_epub_in_storage_to_pdf**](PdfApi.md#put_epub_in_storage_to_pdf) | **PUT** /pdf/{name}/create/epub | Convert EPUB file (located on storage) to PDF format and upload resulting file to storage. 
[**put_fields_flatten**](PdfApi.md#put_fields_flatten) | **PUT** /pdf/{name}/fields/flatten | Flatten form fields in document.
[**put_free_text_annotation**](PdfApi.md#put_free_text_annotation) | **PUT** /pdf/{name}/annotations/freetext/{annotationId} | Replace document free text annotation
[**put_html_in_storage_to_pdf**](PdfApi.md#put_html_in_storage_to_pdf) | **PUT** /pdf/{name}/create/html | Convert HTML file (located on storage) to PDF format and upload resulting file to storage. 
[**put_image_extract_as_gif**](PdfApi.md#put_image_extract_as_gif) | **PUT** /pdf/{name}/images/{imageId}/extract/gif | Extract document image in GIF format to folder
[**put_image_extract_as_jpeg**](PdfApi.md#put_image_extract_as_jpeg) | **PUT** /pdf/{name}/images/{imageId}/extract/jpeg | Extract document image in JPEG format to folder
[**put_image_extract_as_png**](PdfApi.md#put_image_extract_as_png) | **PUT** /pdf/{name}/images/{imageId}/extract/png | Extract document image in PNG format to folder
[**put_image_extract_as_tiff**](PdfApi.md#put_image_extract_as_tiff) | **PUT** /pdf/{name}/images/{imageId}/extract/tiff | Extract document image in TIFF format to folder
[**put_image_in_storage_to_pdf**](PdfApi.md#put_image_in_storage_to_pdf) | **PUT** /pdf/{name}/create/images | Convert image file (located on storage) to PDF format and upload resulting file to storage. 
[**put_images_extract_as_gif**](PdfApi.md#put_images_extract_as_gif) | **PUT** /pdf/{name}/pages/{pageNumber}/images/extract/gif | Extract document images in GIF format to folder.
[**put_images_extract_as_jpeg**](PdfApi.md#put_images_extract_as_jpeg) | **PUT** /pdf/{name}/pages/{pageNumber}/images/extract/jpeg | Extract document images in JPEG format to folder.
[**put_images_extract_as_png**](PdfApi.md#put_images_extract_as_png) | **PUT** /pdf/{name}/pages/{pageNumber}/images/extract/png | Extract document images in PNG format to folder.
[**put_images_extract_as_tiff**](PdfApi.md#put_images_extract_as_tiff) | **PUT** /pdf/{name}/pages/{pageNumber}/images/extract/tiff | Extract document images in TIFF format to folder.
[**put_la_te_x_in_storage_to_pdf**](PdfApi.md#put_la_te_x_in_storage_to_pdf) | **PUT** /pdf/{name}/create/latex | Convert LaTeX file (located on storage) to PDF format and upload resulting file to storage. 
[**put_link_annotation**](PdfApi.md#put_link_annotation) | **PUT** /pdf/{name}/links/{linkId} | Replace document page link annotations
[**put_merge_documents**](PdfApi.md#put_merge_documents) | **PUT** /pdf/{name}/merge | Merge a list of documents.
[**put_mht_in_storage_to_pdf**](PdfApi.md#put_mht_in_storage_to_pdf) | **PUT** /pdf/{name}/create/mht | Convert MHT file (located on storage) to PDF format and upload resulting file to storage. 
[**put_page_add_stamp**](PdfApi.md#put_page_add_stamp) | **PUT** /pdf/{name}/pages/{pageNumber}/stamp | Add page stamp.
[**put_page_convert_to_bmp**](PdfApi.md#put_page_convert_to_bmp) | **PUT** /pdf/{name}/pages/{pageNumber}/convert/bmp | Convert document page to bmp image and upload resulting file to storage.
[**put_page_convert_to_emf**](PdfApi.md#put_page_convert_to_emf) | **PUT** /pdf/{name}/pages/{pageNumber}/convert/emf | Convert document page to emf image and upload resulting file to storage.
[**put_page_convert_to_gif**](PdfApi.md#put_page_convert_to_gif) | **PUT** /pdf/{name}/pages/{pageNumber}/convert/gif | Convert document page to gif image and upload resulting file to storage.
[**put_page_convert_to_jpeg**](PdfApi.md#put_page_convert_to_jpeg) | **PUT** /pdf/{name}/pages/{pageNumber}/convert/jpeg | Convert document page to Jpeg image and upload resulting file to storage.
[**put_page_convert_to_png**](PdfApi.md#put_page_convert_to_png) | **PUT** /pdf/{name}/pages/{pageNumber}/convert/png | Convert document page to png image and upload resulting file to storage.
[**put_page_convert_to_tiff**](PdfApi.md#put_page_convert_to_tiff) | **PUT** /pdf/{name}/pages/{pageNumber}/convert/tiff | Convert document page to Tiff image and upload resulting file to storage.
[**put_pcl_in_storage_to_pdf**](PdfApi.md#put_pcl_in_storage_to_pdf) | **PUT** /pdf/{name}/create/pcl | Convert PCL file (located on storage) to PDF format and upload resulting file to storage. 
[**put_pdf_in_request_to_doc**](PdfApi.md#put_pdf_in_request_to_doc) | **PUT** /pdf/convert/doc | Converts PDF document (in request content) to DOC format and uploads resulting file to storage.
[**put_pdf_in_request_to_epub**](PdfApi.md#put_pdf_in_request_to_epub) | **PUT** /pdf/convert/epub | Converts PDF document (in request content) to EPUB format and uploads resulting file to storage.
[**put_pdf_in_request_to_html**](PdfApi.md#put_pdf_in_request_to_html) | **PUT** /pdf/convert/html | Converts PDF document (in request content) to Html format and uploads resulting file to storage.
[**put_pdf_in_request_to_la_te_x**](PdfApi.md#put_pdf_in_request_to_la_te_x) | **PUT** /pdf/convert/latex | Converts PDF document (in request content) to LaTeX format and uploads resulting file to storage.
[**put_pdf_in_request_to_mobi_xml**](PdfApi.md#put_pdf_in_request_to_mobi_xml) | **PUT** /pdf/convert/mobixml | Converts PDF document (in request content) to MOBIXML format and uploads resulting file to storage.
[**put_pdf_in_request_to_pdf_a**](PdfApi.md#put_pdf_in_request_to_pdf_a) | **PUT** /pdf/convert/pdfa | Converts PDF document (in request content) to PdfA format and uploads resulting file to storage.
[**put_pdf_in_request_to_pptx**](PdfApi.md#put_pdf_in_request_to_pptx) | **PUT** /pdf/convert/pptx | Converts PDF document (in request content) to PPTX format and uploads resulting file to storage.
[**put_pdf_in_request_to_svg**](PdfApi.md#put_pdf_in_request_to_svg) | **PUT** /pdf/convert/svg | Converts PDF document (in request content) to SVG format and uploads resulting file to storage.
[**put_pdf_in_request_to_tiff**](PdfApi.md#put_pdf_in_request_to_tiff) | **PUT** /pdf/convert/tiff | Converts PDF document (in request content) to TIFF format and uploads resulting file to storage.
[**put_pdf_in_request_to_xls**](PdfApi.md#put_pdf_in_request_to_xls) | **PUT** /pdf/convert/xls | Converts PDF document (in request content) to XLS format and uploads resulting file to storage.
[**put_pdf_in_request_to_xml**](PdfApi.md#put_pdf_in_request_to_xml) | **PUT** /pdf/convert/xml | Converts PDF document (in request content) to XML format and uploads resulting file to storage.
[**put_pdf_in_request_to_xps**](PdfApi.md#put_pdf_in_request_to_xps) | **PUT** /pdf/convert/xps | Converts PDF document (in request content) to XPS format and uploads resulting file to storage.
[**put_pdf_in_storage_to_doc**](PdfApi.md#put_pdf_in_storage_to_doc) | **PUT** /pdf/{name}/convert/doc | Converts PDF document (located on storage) to DOC format and uploads resulting file to storage
[**put_pdf_in_storage_to_epub**](PdfApi.md#put_pdf_in_storage_to_epub) | **PUT** /pdf/{name}/convert/epub | Converts PDF document (located on storage) to EPUB format and uploads resulting file to storage
[**put_pdf_in_storage_to_html**](PdfApi.md#put_pdf_in_storage_to_html) | **PUT** /pdf/{name}/convert/html | Converts PDF document (located on storage) to Html format and uploads resulting file to storage
[**put_pdf_in_storage_to_la_te_x**](PdfApi.md#put_pdf_in_storage_to_la_te_x) | **PUT** /pdf/{name}/convert/latex | Converts PDF document (located on storage) to LaTeX format and uploads resulting file to storage
[**put_pdf_in_storage_to_mobi_xml**](PdfApi.md#put_pdf_in_storage_to_mobi_xml) | **PUT** /pdf/{name}/convert/mobixml | Converts PDF document (located on storage) to MOBIXML format and uploads resulting file to storage
[**put_pdf_in_storage_to_pdf_a**](PdfApi.md#put_pdf_in_storage_to_pdf_a) | **PUT** /pdf/{name}/convert/pdfa | Converts PDF document (located on storage) to PdfA format and uploads resulting file to storage
[**put_pdf_in_storage_to_pptx**](PdfApi.md#put_pdf_in_storage_to_pptx) | **PUT** /pdf/{name}/convert/pptx | Converts PDF document (located on storage) to PPTX format and uploads resulting file to storage
[**put_pdf_in_storage_to_svg**](PdfApi.md#put_pdf_in_storage_to_svg) | **PUT** /pdf/{name}/convert/svg | Converts PDF document (located on storage) to SVG format and uploads resulting file to storage
[**put_pdf_in_storage_to_tiff**](PdfApi.md#put_pdf_in_storage_to_tiff) | **PUT** /pdf/{name}/convert/tiff | Converts PDF document (located on storage) to TIFF format and uploads resulting file to storage
[**put_pdf_in_storage_to_xls**](PdfApi.md#put_pdf_in_storage_to_xls) | **PUT** /pdf/{name}/convert/xls | Converts PDF document (located on storage) to XLS format and uploads resulting file to storage
[**put_pdf_in_storage_to_xml**](PdfApi.md#put_pdf_in_storage_to_xml) | **PUT** /pdf/{name}/convert/xml | Converts PDF document (located on storage) to XML format and uploads resulting file to storage
[**put_pdf_in_storage_to_xps**](PdfApi.md#put_pdf_in_storage_to_xps) | **PUT** /pdf/{name}/convert/xps | Converts PDF document (located on storage) to XPS format and uploads resulting file to storage
[**put_privileges**](PdfApi.md#put_privileges) | **PUT** /pdf/{name}/privileges | Update privilege document.
[**put_ps_in_storage_to_pdf**](PdfApi.md#put_ps_in_storage_to_pdf) | **PUT** /pdf/{name}/create/ps | Convert PS file (located on storage) to PDF format and upload resulting file to storage. 
[**put_replace_image**](PdfApi.md#put_replace_image) | **PUT** /pdf/{name}/images/{imageId} | Replace document image.
[**put_searchable_document**](PdfApi.md#put_searchable_document) | **PUT** /pdf/{name}/ocr | Create searchable PDF document. Generate OCR layer for images in input PDF document.
[**put_set_property**](PdfApi.md#put_set_property) | **PUT** /pdf/{name}/documentproperties/{propertyName} | Add/update document property.
[**put_svg_in_storage_to_pdf**](PdfApi.md#put_svg_in_storage_to_pdf) | **PUT** /pdf/{name}/create/svg | Convert SVG file (located on storage) to PDF format and upload resulting file to storage. 
[**put_text_annotation**](PdfApi.md#put_text_annotation) | **PUT** /pdf/{name}/annotations/text/{annotationId} | Replace document text annotation
[**put_update_field**](PdfApi.md#put_update_field) | **PUT** /pdf/{name}/fields/{fieldName} | Update field.
[**put_update_fields**](PdfApi.md#put_update_fields) | **PUT** /pdf/{name}/fields | Update fields.
[**put_web_in_storage_to_pdf**](PdfApi.md#put_web_in_storage_to_pdf) | **PUT** /pdf/{name}/create/web | Convert web page to PDF format and upload resulting file to storage. 
[**put_xfa_pdf_in_request_to_acro_form**](PdfApi.md#put_xfa_pdf_in_request_to_acro_form) | **PUT** /pdf/convert/xfatoacroform | Converts PDF document which contatins XFA form (in request content) to PDF with AcroForm and uploads resulting file to storage.
[**put_xfa_pdf_in_storage_to_acro_form**](PdfApi.md#put_xfa_pdf_in_storage_to_acro_form) | **PUT** /pdf/{name}/convert/xfatoacroform | Converts PDF document which contatins XFA form (located on storage) to PDF with AcroForm and uploads resulting file to storage
[**put_xml_in_storage_to_pdf**](PdfApi.md#put_xml_in_storage_to_pdf) | **PUT** /pdf/{name}/create/xml | Convert XML file (located on storage) to PDF format and upload resulting file to storage. 
[**put_xps_in_storage_to_pdf**](PdfApi.md#put_xps_in_storage_to_pdf) | **PUT** /pdf/{name}/create/xps | Convert XPS file (located on storage) to PDF format and upload resulting file to storage. 
[**put_xsl_fo_in_storage_to_pdf**](PdfApi.md#put_xsl_fo_in_storage_to_pdf) | **PUT** /pdf/{name}/create/xslfo | Convert XslFo file (located on storage) to PDF format and upload resulting file to storage. 


# **delete_annotation**
> AsposeResponse delete_annotation(name, annotation_id, storage=storage, folder=folder)

Delete document annotation by ID

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
annotation_id = 'annotation_id_example' # str | The annotation ID.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Delete document annotation by ID
    api_response = api_instance.delete_annotation(name, annotation_id, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->delete_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_annotations**
> AsposeResponse delete_document_annotations(name, storage=storage, folder=folder)

Delete all annotations from the document

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Delete all annotations from the document
    api_response = api_instance.delete_document_annotations(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->delete_document_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_link_annotations**
> AsposeResponse delete_document_link_annotations(name, storage=storage, folder=folder)

Delete all link annotations from the document

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Delete all link annotations from the document
    api_response = api_instance.delete_document_link_annotations(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->delete_document_link_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_field**
> AsposeResponse delete_field(name, field_name, storage=storage, folder=folder)

Delete document field by name.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
field_name = 'field_name_example' # str | The field name/
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Delete document field by name.
    api_response = api_instance.delete_field(name, field_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->delete_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name/ | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image**
> AsposeResponse delete_image(name, image_id, storage=storage, folder=folder)

Delete image from document page.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
image_id = 'image_id_example' # str | Image ID.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Delete image from document page.
    api_response = api_instance.delete_image(name, image_id, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->delete_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_link_annotation**
> AsposeResponse delete_link_annotation(name, link_id, storage=storage, folder=folder)

Delete document page link annotation by ID

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
link_id = 'link_id_example' # str | The link ID.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Delete document page link annotation by ID
    api_response = api_instance.delete_link_annotation(name, link_id, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->delete_link_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **link_id** | **str**| The link ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_page**
> AsposeResponse delete_page(name, page_number, storage=storage, folder=folder)

Delete document page by its number.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Delete document page by its number.
    api_response = api_instance.delete_page(name, page_number, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->delete_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_page_annotations**
> AsposeResponse delete_page_annotations(name, page_number, storage=storage, folder=folder)

Delete all annotations from the page

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Delete all annotations from the page
    api_response = api_instance.delete_page_annotations(name, page_number, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->delete_page_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_page_link_annotations**
> AsposeResponse delete_page_link_annotations(name, page_number, storage=storage, folder=folder)

Delete all link annotations from the page

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Delete all link annotations from the page
    api_response = api_instance.delete_page_link_annotations(name, page_number, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->delete_page_link_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_properties**
> AsposeResponse delete_properties(name, storage=storage, folder=folder)

Delete custom document properties.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | 
storage = 'storage_example' # str |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Delete custom document properties.
    api_response = api_instance.delete_properties(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->delete_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **storage** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property**
> AsposeResponse delete_property(name, property_name, storage=storage, folder=folder)

Delete document property.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | 
property_name = 'property_name_example' # str | 
storage = 'storage_example' # str |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Delete document property.
    api_response = api_instance.delete_property(name, property_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->delete_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **property_name** | **str**|  | 
 **storage** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> DocumentResponse get_document(name, storage=storage, folder=folder)

Read common document info.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read common document info.
    api_response = api_instance.get_document(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_annotations**
> AnnotationsInfoResponse get_document_annotations(name, storage=storage, folder=folder)

Read documant page annotations. Returns only FreeTextAnnotations, TextAnnotations, other annotations will implemented next releases.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read documant page annotations. Returns only FreeTextAnnotations, TextAnnotations, other annotations will implemented next releases.
    api_response = api_instance.get_document_annotations(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_document_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AnnotationsInfoResponse**](AnnotationsInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_attachment_by_index**
> AttachmentResponse get_document_attachment_by_index(name, attachment_index, storage=storage, folder=folder)

Read document attachment info by its index.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
attachment_index = 56 # int | The attachment index.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document attachment info by its index.
    api_response = api_instance.get_document_attachment_by_index(name, attachment_index, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_document_attachment_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **attachment_index** | **int**| The attachment index. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AttachmentResponse**](AttachmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_attachments**
> AttachmentsResponse get_document_attachments(name, storage=storage, folder=folder)

Read document attachments info.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document attachments info.
    api_response = api_instance.get_document_attachments(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_document_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AttachmentsResponse**](AttachmentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_bookmarks**
> file get_document_bookmarks(name, bookmark_path=bookmark_path, storage=storage, folder=folder)

Read document bookmark/bookmarks (including children).

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
bookmark_path = 'bookmark_path_example' # str | The bookmark path. Leave it empty if you want to get all the bookmarks in the document. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document bookmark/bookmarks (including children).
    api_response = api_instance.get_document_bookmarks(name, bookmark_path=bookmark_path, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_document_bookmarks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **bookmark_path** | **str**| The bookmark path. Leave it empty if you want to get all the bookmarks in the document. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_free_text_annotations**
> FreeTextAnnotationsResponse get_document_free_text_annotations(name, storage=storage, folder=folder)

Read document free text annotations.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document free text annotations.
    api_response = api_instance.get_document_free_text_annotations(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_document_free_text_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FreeTextAnnotationsResponse**](FreeTextAnnotationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_properties**
> DocumentPropertiesResponse get_document_properties(name, storage=storage, folder=folder)

Read document properties.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | 
storage = 'storage_example' # str |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Read document properties.
    api_response = api_instance.get_document_properties(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_document_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **storage** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**DocumentPropertiesResponse**](DocumentPropertiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_property**
> DocumentPropertyResponse get_document_property(name, property_name, storage=storage, folder=folder)

Read document property by name.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | 
property_name = 'property_name_example' # str | 
storage = 'storage_example' # str |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Read document property by name.
    api_response = api_instance.get_document_property(name, property_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_document_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **property_name** | **str**|  | 
 **storage** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**DocumentPropertyResponse**](DocumentPropertyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_text_annotations**
> TextAnnotationsResponse get_document_text_annotations(name, storage=storage, folder=folder)

Read document text annotations.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document text annotations.
    api_response = api_instance.get_document_text_annotations(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_document_text_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TextAnnotationsResponse**](TextAnnotationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download**
> file get_download(path, version_id=version_id, storage=storage)

Download a specific file 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
path = 'path_example' # str | Path of the file including the file name and extension e.g. /file.ext
version_id = 'version_id_example' # str | File's version (optional)
storage = 'storage_example' # str | User's storage name (optional)

try: 
    # Download a specific file 
    api_response = api_instance.get_download(path, version_id=version_id, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path of the file including the file name and extension e.g. /file.ext | 
 **version_id** | **str**| File&#39;s version | [optional] 
 **storage** | **str**| User&#39;s storage name | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_document_attachment_by_index**
> file get_download_document_attachment_by_index(name, attachment_index, storage=storage, folder=folder)

Download document attachment content by its index.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
attachment_index = 56 # int | The attachment index.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Download document attachment content by its index.
    api_response = api_instance.get_download_document_attachment_by_index(name, attachment_index, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_download_document_attachment_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **attachment_index** | **int**| The attachment index. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_epub_in_storage_to_pdf**
> file get_epub_in_storage_to_pdf(src_path, storage=storage)

Convert EPUB file (located on storage) to PDF format and return resulting file in response. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.epub)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert EPUB file (located on storage) to PDF format and return resulting file in response. 
    api_response = api_instance.get_epub_in_storage_to_pdf(src_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_epub_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.epub) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field**
> FieldResponse get_field(name, field_name, storage=storage, folder=folder)

Get document field by name.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
field_name = 'field_name_example' # str | The field name/
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Get document field by name.
    api_response = api_instance.get_field(name, field_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name/ | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FieldResponse**](FieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields**
> FieldsResponse get_fields(name, storage=storage, folder=folder)

Get document fields.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Get document fields.
    api_response = api_instance.get_fields(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FieldsResponse**](FieldsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_free_text_annotation**
> FreeTextAnnotationResponse get_free_text_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page free text annotation by ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
annotation_id = 'annotation_id_example' # str | The annotation ID.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document page free text annotation by ID.
    api_response = api_instance.get_free_text_annotation(name, annotation_id, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_free_text_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FreeTextAnnotationResponse**](FreeTextAnnotationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_html_in_storage_to_pdf**
> file get_html_in_storage_to_pdf(src_path, html_file_name, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, storage=storage)

Convert HTML file (located on storage) to PDF format and return resulting file in response. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.zip)
html_file_name = 'html_file_name_example' # str | Name of HTML file in ZIP.
height = 1.2 # float | Page height (optional)
width = 1.2 # float | Page width (optional)
is_landscape = true # bool | Is page landscaped (optional)
margin_left = 1.2 # float | Page margin left (optional)
margin_bottom = 1.2 # float | Page margin bottom (optional)
margin_right = 1.2 # float | Page margin right (optional)
margin_top = 1.2 # float | Page margin top (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert HTML file (located on storage) to PDF format and return resulting file in response. 
    api_response = api_instance.get_html_in_storage_to_pdf(src_path, html_file_name, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_html_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.zip) | 
 **html_file_name** | **str**| Name of HTML file in ZIP. | 
 **height** | **float**| Page height | [optional] 
 **width** | **float**| Page width | [optional] 
 **is_landscape** | **bool**| Is page landscaped | [optional] 
 **margin_left** | **float**| Page margin left | [optional] 
 **margin_bottom** | **float**| Page margin bottom | [optional] 
 **margin_right** | **float**| Page margin right | [optional] 
 **margin_top** | **float**| Page margin top | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image**
> ImageResponse get_image(name, image_id, storage=storage, folder=folder)

Read document image by ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
image_id = 'image_id_example' # str | Image ID.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document image by ID.
    api_response = api_instance.get_image(name, image_id, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ImageResponse**](ImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_extract_as_gif**
> file get_image_extract_as_gif(name, image_id, width=width, height=height, storage=storage, folder=folder)

Extract document image in GIF format

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
image_id = 'image_id_example' # str | Image ID.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Extract document image in GIF format
    api_response = api_instance.get_image_extract_as_gif(name, image_id, width=width, height=height, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_image_extract_as_gif: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_extract_as_jpeg**
> file get_image_extract_as_jpeg(name, image_id, width=width, height=height, storage=storage, folder=folder)

Extract document image in JPEG format

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
image_id = 'image_id_example' # str | Image ID.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Extract document image in JPEG format
    api_response = api_instance.get_image_extract_as_jpeg(name, image_id, width=width, height=height, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_image_extract_as_jpeg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_extract_as_png**
> file get_image_extract_as_png(name, image_id, width=width, height=height, storage=storage, folder=folder)

Extract document image in PNG format

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
image_id = 'image_id_example' # str | Image ID.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Extract document image in PNG format
    api_response = api_instance.get_image_extract_as_png(name, image_id, width=width, height=height, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_image_extract_as_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_extract_as_tiff**
> file get_image_extract_as_tiff(name, image_id, width=width, height=height, storage=storage, folder=folder)

Extract document image in TIFF format

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
image_id = 'image_id_example' # str | Image ID.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Extract document image in TIFF format
    api_response = api_instance.get_image_extract_as_tiff(name, image_id, width=width, height=height, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_image_extract_as_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> ImagesResponse get_images(name, page_number, storage=storage, folder=folder)

Read document images.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document images.
    api_response = api_instance.get_images(name, page_number, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ImagesResponse**](ImagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_la_te_x_in_storage_to_pdf**
> file get_la_te_x_in_storage_to_pdf(src_path, storage=storage)

Convert LaTeX file (located on storage) to PDF format and return resulting file in response. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.tex)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert LaTeX file (located on storage) to PDF format and return resulting file in response. 
    api_response = api_instance.get_la_te_x_in_storage_to_pdf(src_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_la_te_x_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.tex) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link_annotation**
> LinkAnnotationResponse get_link_annotation(name, link_id, storage=storage, folder=folder)

Read document link annotation by ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
link_id = 'link_id_example' # str | The link ID.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document link annotation by ID.
    api_response = api_instance.get_link_annotation(name, link_id, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_link_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **link_id** | **str**| The link ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**LinkAnnotationResponse**](LinkAnnotationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mht_in_storage_to_pdf**
> file get_mht_in_storage_to_pdf(src_path, storage=storage)

Convert MHT file (located on storage) to PDF format and return resulting file in response. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.mht)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert MHT file (located on storage) to PDF format and return resulting file in response. 
    api_response = api_instance.get_mht_in_storage_to_pdf(src_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_mht_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.mht) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page**
> DocumentPageResponse get_page(name, page_number, storage=storage, folder=folder)

Read document page info.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document page info.
    api_response = api_instance.get_page(name, page_number, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**DocumentPageResponse**](DocumentPageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_annotations**
> AnnotationsInfoResponse get_page_annotations(name, page_number, storage=storage, folder=folder)

Read documant page annotations. Returns only FreeTextAnnotations, TextAnnotations, other annotations will implemented next releases.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read documant page annotations. Returns only FreeTextAnnotations, TextAnnotations, other annotations will implemented next releases.
    api_response = api_instance.get_page_annotations(name, page_number, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_page_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AnnotationsInfoResponse**](AnnotationsInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_convert_to_bmp**
> file get_page_convert_to_bmp(name, page_number, width=width, height=height, folder=folder, storage=storage)

Convert document page to Bmp image and return resulting file in response.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert document page to Bmp image and return resulting file in response.
    api_response = api_instance.get_page_convert_to_bmp(name, page_number, width=width, height=height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_page_convert_to_bmp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_convert_to_emf**
> file get_page_convert_to_emf(name, page_number, width=width, height=height, folder=folder, storage=storage)

Convert document page to Emf image and return resulting file in response.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert document page to Emf image and return resulting file in response.
    api_response = api_instance.get_page_convert_to_emf(name, page_number, width=width, height=height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_page_convert_to_emf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_convert_to_gif**
> file get_page_convert_to_gif(name, page_number, width=width, height=height, folder=folder, storage=storage)

Convert document page to Gif image and return resulting file in response.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert document page to Gif image and return resulting file in response.
    api_response = api_instance.get_page_convert_to_gif(name, page_number, width=width, height=height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_page_convert_to_gif: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_convert_to_jpeg**
> file get_page_convert_to_jpeg(name, page_number, width=width, height=height, folder=folder, storage=storage)

Convert document page to Jpeg image and return resulting file in response.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert document page to Jpeg image and return resulting file in response.
    api_response = api_instance.get_page_convert_to_jpeg(name, page_number, width=width, height=height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_page_convert_to_jpeg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_convert_to_png**
> file get_page_convert_to_png(name, page_number, width=width, height=height, folder=folder, storage=storage)

Convert document page to Png image and return resulting file in response.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert document page to Png image and return resulting file in response.
    api_response = api_instance.get_page_convert_to_png(name, page_number, width=width, height=height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_page_convert_to_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_convert_to_tiff**
> file get_page_convert_to_tiff(name, page_number, width=width, height=height, folder=folder, storage=storage)

Convert document page to Tiff image  and return resulting file in response.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert document page to Tiff image  and return resulting file in response.
    api_response = api_instance.get_page_convert_to_tiff(name, page_number, width=width, height=height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_page_convert_to_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_free_text_annotations**
> FreeTextAnnotationsResponse get_page_free_text_annotations(name, page_number, storage=storage, folder=folder)

Read document page free text annotations.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document page free text annotations.
    api_response = api_instance.get_page_free_text_annotations(name, page_number, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_page_free_text_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FreeTextAnnotationsResponse**](FreeTextAnnotationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_link_annotation**
> LinkAnnotationResponse get_page_link_annotation(name, page_number, link_id, storage=storage, folder=folder)

Read document page link annotation by ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
link_id = 'link_id_example' # str | The link ID.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document page link annotation by ID.
    api_response = api_instance.get_page_link_annotation(name, page_number, link_id, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_page_link_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **link_id** | **str**| The link ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**LinkAnnotationResponse**](LinkAnnotationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_link_annotations**
> LinkAnnotationsResponse get_page_link_annotations(name, page_number, storage=storage, folder=folder)

Read document page link annotations.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document page link annotations.
    api_response = api_instance.get_page_link_annotations(name, page_number, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_page_link_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**LinkAnnotationsResponse**](LinkAnnotationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_text**
> TextRectsResponse get_page_text(name, page_number, llx, lly, urx, ury, format=format, regex=regex, split_rects=split_rects, folder=folder, storage=storage)

Read page text items.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | Number of page (starting from 1).
llx = 1.2 # float | 
lly = 1.2 # float | 
urx = 1.2 # float | 
ury = 1.2 # float | 
format = ['format_example'] # list[str] | List of formats for search. (optional)
regex = 'regex_example' # str | Formats are specified as a regular expression. (optional)
split_rects = true # bool | Split result fragments (default is true). (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Read page text items.
    api_response = api_instance.get_page_text(name, page_number, llx, lly, urx, ury, format=format, regex=regex, split_rects=split_rects, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_page_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| Number of page (starting from 1). | 
 **llx** | **float**|  | 
 **lly** | **float**|  | 
 **urx** | **float**|  | 
 **ury** | **float**|  | 
 **format** | [**list[str]**](str.md)| List of formats for search. | [optional] 
 **regex** | **str**| Formats are specified as a regular expression. | [optional] 
 **split_rects** | **bool**| Split result fragments (default is true). | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**TextRectsResponse**](TextRectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_text_annotations**
> TextAnnotationsResponse get_page_text_annotations(name, page_number, storage=storage, folder=folder)

Read document page text annotations.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document page text annotations.
    api_response = api_instance.get_page_text_annotations(name, page_number, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_page_text_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TextAnnotationsResponse**](TextAnnotationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages**
> DocumentPagesResponse get_pages(name, storage=storage, folder=folder)

Read document pages info.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document pages info.
    api_response = api_instance.get_pages(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**DocumentPagesResponse**](DocumentPagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pcl_in_storage_to_pdf**
> file get_pcl_in_storage_to_pdf(src_path, storage=storage)

Convert PCL file (located on storage) to PDF format and return resulting file in response. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.pcl)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert PCL file (located on storage) to PDF format and return resulting file in response. 
    api_response = api_instance.get_pcl_in_storage_to_pdf(src_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_pcl_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.pcl) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_doc**
> file get_pdf_in_storage_to_doc(name, add_return_to_line_end=add_return_to_line_end, format=format, image_resolution_x=image_resolution_x, image_resolution_y=image_resolution_y, max_distance_between_text_lines=max_distance_between_text_lines, mode=mode, recognize_bullets=recognize_bullets, relative_horizontal_proximity=relative_horizontal_proximity, folder=folder, storage=storage)

Converts PDF document (located on storage) to DOC format and returns resulting file in response content

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
add_return_to_line_end = true # bool | Add return to line end. (optional)
format = 'format_example' # str | Allows to specify .doc or .docx file format. (optional)
image_resolution_x = 56 # int | Image resolution X. (optional)
image_resolution_y = 56 # int | Image resolution Y. (optional)
max_distance_between_text_lines = 1.2 # float | Max distance between text lines. (optional)
mode = 'mode_example' # str | Allows to control how a PDF document is converted into a word processing document. (optional)
recognize_bullets = true # bool | Recognize bullets. (optional)
relative_horizontal_proximity = 1.2 # float | Relative horizontal proximity. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to DOC format and returns resulting file in response content
    api_response = api_instance.get_pdf_in_storage_to_doc(name, add_return_to_line_end=add_return_to_line_end, format=format, image_resolution_x=image_resolution_x, image_resolution_y=image_resolution_y, max_distance_between_text_lines=max_distance_between_text_lines, mode=mode, recognize_bullets=recognize_bullets, relative_horizontal_proximity=relative_horizontal_proximity, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_pdf_in_storage_to_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **add_return_to_line_end** | **bool**| Add return to line end. | [optional] 
 **format** | **str**| Allows to specify .doc or .docx file format. | [optional] 
 **image_resolution_x** | **int**| Image resolution X. | [optional] 
 **image_resolution_y** | **int**| Image resolution Y. | [optional] 
 **max_distance_between_text_lines** | **float**| Max distance between text lines. | [optional] 
 **mode** | **str**| Allows to control how a PDF document is converted into a word processing document. | [optional] 
 **recognize_bullets** | **bool**| Recognize bullets. | [optional] 
 **relative_horizontal_proximity** | **float**| Relative horizontal proximity. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_epub**
> file get_pdf_in_storage_to_epub(name, content_recognition_mode=content_recognition_mode, folder=folder, storage=storage)

Converts PDF document (located on storage) to EPUB format and returns resulting file in response content

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
content_recognition_mode = 'content_recognition_mode_example' # str | ?roperty tunes conversion for this or that desirable method of recognition of content. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to EPUB format and returns resulting file in response content
    api_response = api_instance.get_pdf_in_storage_to_epub(name, content_recognition_mode=content_recognition_mode, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_pdf_in_storage_to_epub: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **content_recognition_mode** | **str**| ?roperty tunes conversion for this or that desirable method of recognition of content. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_html**
> file get_pdf_in_storage_to_html(name, additional_margin_width_in_points=additional_margin_width_in_points, compress_svg_graphics_if_any=compress_svg_graphics_if_any, convert_marked_content_to_layers=convert_marked_content_to_layers, default_font_name=default_font_name, document_type=document_type, fixed_layout=fixed_layout, image_resolution=image_resolution, minimal_line_width=minimal_line_width, prevent_glyphs_grouping=prevent_glyphs_grouping, split_css_into_pages=split_css_into_pages, split_into_pages=split_into_pages, use_z_order=use_z_order, antialiasing_processing=antialiasing_processing, css_class_names_prefix=css_class_names_prefix, explicit_list_of_saved_pages=explicit_list_of_saved_pages, font_encoding_strategy=font_encoding_strategy, font_saving_mode=font_saving_mode, html_markup_generation_mode=html_markup_generation_mode, letters_positioning_method=letters_positioning_method, pages_flow_type_depends_on_viewers_screen_size=pages_flow_type_depends_on_viewers_screen_size, parts_embedding_mode=parts_embedding_mode, raster_images_saving_mode=raster_images_saving_mode, remove_empty_areas_on_top_and_bottom=remove_empty_areas_on_top_and_bottom, save_shadowed_texts_as_transparent_texts=save_shadowed_texts_as_transparent_texts, save_transparent_texts=save_transparent_texts, special_folder_for_all_images=special_folder_for_all_images, special_folder_for_svg_images=special_folder_for_svg_images, try_save_text_underlining_and_strikeouting_in_css=try_save_text_underlining_and_strikeouting_in_css, folder=folder, storage=storage)

Converts PDF document (located on storage) to Html format and returns resulting file in response content

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
additional_margin_width_in_points = 56 # int | Defines width of margin that will be forcibly left around that output HTML-areas. (optional)
compress_svg_graphics_if_any = true # bool | The flag that indicates whether found SVG graphics(if any) will be compressed(zipped) into SVGZ format during saving. (optional)
convert_marked_content_to_layers = true # bool | If attribute ConvertMarkedContentToLayers set to true then an all elements inside a PDF marked content (layer) will be put into an HTML div with \"data-pdflayer\" attribute specifying a layer name. This layer name will be extracted from optional properties of PDF marked content. If this attribute is false (by default) then no any layers will be created from PDF marked content. (optional)
default_font_name = 'default_font_name_example' # str | Specifies the name of an installed font which is used to substitute any document font that is not embedded and not installed in the system. If null then default substitution font is used. (optional)
document_type = 'document_type_example' # str | Result document type. (optional)
fixed_layout = true # bool | The value indicating whether that HTML is created as fixed layout. (optional)
image_resolution = 56 # int | Resolution for image rendering. (optional)
minimal_line_width = 56 # int | This attribute sets minimal width of graphic path line. If thickness of line is less than 1px Adobe Acrobat rounds it to this value. So this attribute can be used to emulate this behavior for HTML browsers. (optional)
prevent_glyphs_grouping = true # bool | This attribute switch on the mode when text glyphs will not be grouped into words and strings This mode allows to keep maximum precision during positioning of glyphs on the page and it can be used for conversion documents with music notes or glyphs that should be placed separately each other. This parameter will be applied to document only when the value of FixedLayout attribute is true. (optional)
split_css_into_pages = true # bool | When multipage-mode selected(i.e 'SplitIntoPages' is 'true'), then this attribute defines whether should be created separate CSS-file for each result HTML page. (optional)
split_into_pages = true # bool | The flag that indicates whether each page of source document will be converted into it's own target HTML document, i.e whether result HTML will be splitted into several HTML-pages. (optional)
use_z_order = true # bool | If attribute UseZORder set to true, graphics and text are added to resultant HTML document accordingly Z-order in original PDF document. If this attribute is false all graphics is put as single layer which may cause some unnecessary effects for overlapped objects. (optional)
antialiasing_processing = 'antialiasing_processing_example' # str | The parameter defines required antialiasing measures during conversion of compound background images from PDF to HTML. (optional)
css_class_names_prefix = 'css_class_names_prefix_example' # str | When PDFtoHTML converter generates result CSSs, CSS class names (something like \".stl_01 {}\" ... \".stl_NN {}) are generated and used in result CSS. This property allows forcibly set class name prefix. (optional)
explicit_list_of_saved_pages = [56] # list[int] | With this property You can explicitely define what pages of document should be converted. Pages in this list must have 1-based numbers. I.e. valid numbers of pages must be taken from range (1...[NumberOfPagesInConvertedDocument]) Order of appearing of pages in this list does not affect their order in result HTML page(s) - in result pages allways will go in order in which they are present in source PDF. (optional)
font_encoding_strategy = 'font_encoding_strategy_example' # str | Defines encoding special rule to tune PDF decoding for current document. (optional)
font_saving_mode = 'font_saving_mode_example' # str | Defines font saving mode that will be used during saving of PDF to desirable format. (optional)
html_markup_generation_mode = 'html_markup_generation_mode_example' # str | Sometimes specific reqirments to generation of HTML markup are present. This parameter defines HTML preparing modes that can be used during conversion of PDF to HTML to match such specific requirments. (optional)
letters_positioning_method = 'letters_positioning_method_example' # str | The mode of positioning of letters in words in result HTML. (optional)
pages_flow_type_depends_on_viewers_screen_size = true # bool | If attribute 'SplitOnPages=false', than whole HTML representing all input PDF pages will be put into one big result HTML file. This flag defines whether result HTML will be generated in such way that flow of areas that represent PDF pages in result HTML will depend on screen resolution of viewer. (optional)
parts_embedding_mode = 'parts_embedding_mode_example' # str | It defines whether referenced files (HTML, Fonts,Images, CSSes) will be embedded into main HTML file or will be generated as apart binary entities. (optional)
raster_images_saving_mode = 'raster_images_saving_mode_example' # str | Converted PDF can contain raster images This parameter defines how they should be handled during conversion of PDF to HTML. (optional)
remove_empty_areas_on_top_and_bottom = true # bool | Defines whether in created HTML will be removed top and bottom empty area without any content (if any). (optional)
save_shadowed_texts_as_transparent_texts = true # bool | Pdf can contain texts that are shadowed by another elements (f.e. by images) but can be selected to clipboard in Acrobat Reader (usually it happen when document contains images and OCRed texts extracted from it). This settings tells to converter whether we need save such texts as transparent selectable texts in result HTML to mimic behaviour of Acrobat Reader (othervise such texts are usually saved as hidden, not available for copying to clipboard). (optional)
save_transparent_texts = true # bool | Pdf can contain transparent texts that can be selected to clipboard (usually it happen when document contains images and OCRed texts extracted from it). This settings tells to converter whether we need save such texts as transparent selectable texts in result HTML. (optional)
special_folder_for_all_images = 'special_folder_for_all_images_example' # str | The path to directory to which must be saved any images if they are encountered during saving of document as HTML. If parameter is empty or null then image files(if any) wil be saved together with other files linked to HTML It does not affect anything if CustomImageSavingStrategy property was successfully used to process relevant image file. (optional)
special_folder_for_svg_images = 'special_folder_for_svg_images_example' # str | The path to directory to which must be saved only SVG-images if they are encountered during saving of document as HTML. If parameter is empty or null then SVG files(if any) wil be saved together with other image-files (near to output file) or in special folder for images (if it specified in SpecialImagesFolderIfAny option). It does not affect anything if CustomImageSavingStrategy property was successfully used to process relevant image file. (optional)
try_save_text_underlining_and_strikeouting_in_css = true # bool | PDF itself does not contain underlining markers for texts. It emulated with line situated under text. This option allows converter try guess that this or that line is a text's underlining and put this info into CSS instead of drawing of underlining graphically. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to Html format and returns resulting file in response content
    api_response = api_instance.get_pdf_in_storage_to_html(name, additional_margin_width_in_points=additional_margin_width_in_points, compress_svg_graphics_if_any=compress_svg_graphics_if_any, convert_marked_content_to_layers=convert_marked_content_to_layers, default_font_name=default_font_name, document_type=document_type, fixed_layout=fixed_layout, image_resolution=image_resolution, minimal_line_width=minimal_line_width, prevent_glyphs_grouping=prevent_glyphs_grouping, split_css_into_pages=split_css_into_pages, split_into_pages=split_into_pages, use_z_order=use_z_order, antialiasing_processing=antialiasing_processing, css_class_names_prefix=css_class_names_prefix, explicit_list_of_saved_pages=explicit_list_of_saved_pages, font_encoding_strategy=font_encoding_strategy, font_saving_mode=font_saving_mode, html_markup_generation_mode=html_markup_generation_mode, letters_positioning_method=letters_positioning_method, pages_flow_type_depends_on_viewers_screen_size=pages_flow_type_depends_on_viewers_screen_size, parts_embedding_mode=parts_embedding_mode, raster_images_saving_mode=raster_images_saving_mode, remove_empty_areas_on_top_and_bottom=remove_empty_areas_on_top_and_bottom, save_shadowed_texts_as_transparent_texts=save_shadowed_texts_as_transparent_texts, save_transparent_texts=save_transparent_texts, special_folder_for_all_images=special_folder_for_all_images, special_folder_for_svg_images=special_folder_for_svg_images, try_save_text_underlining_and_strikeouting_in_css=try_save_text_underlining_and_strikeouting_in_css, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_pdf_in_storage_to_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **additional_margin_width_in_points** | **int**| Defines width of margin that will be forcibly left around that output HTML-areas. | [optional] 
 **compress_svg_graphics_if_any** | **bool**| The flag that indicates whether found SVG graphics(if any) will be compressed(zipped) into SVGZ format during saving. | [optional] 
 **convert_marked_content_to_layers** | **bool**| If attribute ConvertMarkedContentToLayers set to true then an all elements inside a PDF marked content (layer) will be put into an HTML div with \&quot;data-pdflayer\&quot; attribute specifying a layer name. This layer name will be extracted from optional properties of PDF marked content. If this attribute is false (by default) then no any layers will be created from PDF marked content. | [optional] 
 **default_font_name** | **str**| Specifies the name of an installed font which is used to substitute any document font that is not embedded and not installed in the system. If null then default substitution font is used. | [optional] 
 **document_type** | **str**| Result document type. | [optional] 
 **fixed_layout** | **bool**| The value indicating whether that HTML is created as fixed layout. | [optional] 
 **image_resolution** | **int**| Resolution for image rendering. | [optional] 
 **minimal_line_width** | **int**| This attribute sets minimal width of graphic path line. If thickness of line is less than 1px Adobe Acrobat rounds it to this value. So this attribute can be used to emulate this behavior for HTML browsers. | [optional] 
 **prevent_glyphs_grouping** | **bool**| This attribute switch on the mode when text glyphs will not be grouped into words and strings This mode allows to keep maximum precision during positioning of glyphs on the page and it can be used for conversion documents with music notes or glyphs that should be placed separately each other. This parameter will be applied to document only when the value of FixedLayout attribute is true. | [optional] 
 **split_css_into_pages** | **bool**| When multipage-mode selected(i.e &#39;SplitIntoPages&#39; is &#39;true&#39;), then this attribute defines whether should be created separate CSS-file for each result HTML page. | [optional] 
 **split_into_pages** | **bool**| The flag that indicates whether each page of source document will be converted into it&#39;s own target HTML document, i.e whether result HTML will be splitted into several HTML-pages. | [optional] 
 **use_z_order** | **bool**| If attribute UseZORder set to true, graphics and text are added to resultant HTML document accordingly Z-order in original PDF document. If this attribute is false all graphics is put as single layer which may cause some unnecessary effects for overlapped objects. | [optional] 
 **antialiasing_processing** | **str**| The parameter defines required antialiasing measures during conversion of compound background images from PDF to HTML. | [optional] 
 **css_class_names_prefix** | **str**| When PDFtoHTML converter generates result CSSs, CSS class names (something like \&quot;.stl_01 {}\&quot; ... \&quot;.stl_NN {}) are generated and used in result CSS. This property allows forcibly set class name prefix. | [optional] 
 **explicit_list_of_saved_pages** | [**list[int]**](int.md)| With this property You can explicitely define what pages of document should be converted. Pages in this list must have 1-based numbers. I.e. valid numbers of pages must be taken from range (1...[NumberOfPagesInConvertedDocument]) Order of appearing of pages in this list does not affect their order in result HTML page(s) - in result pages allways will go in order in which they are present in source PDF. | [optional] 
 **font_encoding_strategy** | **str**| Defines encoding special rule to tune PDF decoding for current document. | [optional] 
 **font_saving_mode** | **str**| Defines font saving mode that will be used during saving of PDF to desirable format. | [optional] 
 **html_markup_generation_mode** | **str**| Sometimes specific reqirments to generation of HTML markup are present. This parameter defines HTML preparing modes that can be used during conversion of PDF to HTML to match such specific requirments. | [optional] 
 **letters_positioning_method** | **str**| The mode of positioning of letters in words in result HTML. | [optional] 
 **pages_flow_type_depends_on_viewers_screen_size** | **bool**| If attribute &#39;SplitOnPages&#x3D;false&#39;, than whole HTML representing all input PDF pages will be put into one big result HTML file. This flag defines whether result HTML will be generated in such way that flow of areas that represent PDF pages in result HTML will depend on screen resolution of viewer. | [optional] 
 **parts_embedding_mode** | **str**| It defines whether referenced files (HTML, Fonts,Images, CSSes) will be embedded into main HTML file or will be generated as apart binary entities. | [optional] 
 **raster_images_saving_mode** | **str**| Converted PDF can contain raster images This parameter defines how they should be handled during conversion of PDF to HTML. | [optional] 
 **remove_empty_areas_on_top_and_bottom** | **bool**| Defines whether in created HTML will be removed top and bottom empty area without any content (if any). | [optional] 
 **save_shadowed_texts_as_transparent_texts** | **bool**| Pdf can contain texts that are shadowed by another elements (f.e. by images) but can be selected to clipboard in Acrobat Reader (usually it happen when document contains images and OCRed texts extracted from it). This settings tells to converter whether we need save such texts as transparent selectable texts in result HTML to mimic behaviour of Acrobat Reader (othervise such texts are usually saved as hidden, not available for copying to clipboard). | [optional] 
 **save_transparent_texts** | **bool**| Pdf can contain transparent texts that can be selected to clipboard (usually it happen when document contains images and OCRed texts extracted from it). This settings tells to converter whether we need save such texts as transparent selectable texts in result HTML. | [optional] 
 **special_folder_for_all_images** | **str**| The path to directory to which must be saved any images if they are encountered during saving of document as HTML. If parameter is empty or null then image files(if any) wil be saved together with other files linked to HTML It does not affect anything if CustomImageSavingStrategy property was successfully used to process relevant image file. | [optional] 
 **special_folder_for_svg_images** | **str**| The path to directory to which must be saved only SVG-images if they are encountered during saving of document as HTML. If parameter is empty or null then SVG files(if any) wil be saved together with other image-files (near to output file) or in special folder for images (if it specified in SpecialImagesFolderIfAny option). It does not affect anything if CustomImageSavingStrategy property was successfully used to process relevant image file. | [optional] 
 **try_save_text_underlining_and_strikeouting_in_css** | **bool**| PDF itself does not contain underlining markers for texts. It emulated with line situated under text. This option allows converter try guess that this or that line is a text&#39;s underlining and put this info into CSS instead of drawing of underlining graphically. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_la_te_x**
> file get_pdf_in_storage_to_la_te_x(name, pages_count=pages_count, folder=folder, storage=storage)

Converts PDF document (located on storage) to LaTeX format and returns resulting file in response content

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
pages_count = 56 # int | Pages count. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to LaTeX format and returns resulting file in response content
    api_response = api_instance.get_pdf_in_storage_to_la_te_x(name, pages_count=pages_count, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_pdf_in_storage_to_la_te_x: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **pages_count** | **int**| Pages count. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_mobi_xml**
> file get_pdf_in_storage_to_mobi_xml(name, folder=folder, storage=storage)

Converts PDF document (located on storage) to MOBIXML format and returns resulting file in response content

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to MOBIXML format and returns resulting file in response content
    api_response = api_instance.get_pdf_in_storage_to_mobi_xml(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_pdf_in_storage_to_mobi_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_pdf_a**
> file get_pdf_in_storage_to_pdf_a(name, type, folder=folder, storage=storage)

Converts PDF document (located on storage) to PdfA format and returns resulting file in response content

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
type = 'type_example' # str | Type of PdfA format.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to PdfA format and returns resulting file in response content
    api_response = api_instance.get_pdf_in_storage_to_pdf_a(name, type, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_pdf_in_storage_to_pdf_a: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **type** | **str**| Type of PdfA format. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_pptx**
> file get_pdf_in_storage_to_pptx(name, separate_images=separate_images, slides_as_images=slides_as_images, folder=folder, storage=storage)

Converts PDF document (located on storage) to PPTX format and returns resulting file in response content

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
separate_images = true # bool | Separate images. (optional)
slides_as_images = true # bool | Slides as images. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to PPTX format and returns resulting file in response content
    api_response = api_instance.get_pdf_in_storage_to_pptx(name, separate_images=separate_images, slides_as_images=slides_as_images, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_pdf_in_storage_to_pptx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **separate_images** | **bool**| Separate images. | [optional] 
 **slides_as_images** | **bool**| Slides as images. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_svg**
> file get_pdf_in_storage_to_svg(name, compress_output_to_zip_archive=compress_output_to_zip_archive, folder=folder, storage=storage)

Converts PDF document (located on storage) to SVG format and returns resulting file in response content

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
compress_output_to_zip_archive = true # bool | Specifies whether output will be created as one zip-archive. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to SVG format and returns resulting file in response content
    api_response = api_instance.get_pdf_in_storage_to_svg(name, compress_output_to_zip_archive=compress_output_to_zip_archive, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_pdf_in_storage_to_svg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **compress_output_to_zip_archive** | **bool**| Specifies whether output will be created as one zip-archive. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_tiff**
> file get_pdf_in_storage_to_tiff(name, brightness=brightness, compression=compression, color_depth=color_depth, left_margin=left_margin, right_margin=right_margin, top_margin=top_margin, bottom_margin=bottom_margin, orientation=orientation, skip_blank_pages=skip_blank_pages, width=width, height=height, x_resolution=x_resolution, y_resolution=y_resolution, page_index=page_index, page_count=page_count, folder=folder, storage=storage)

Converts PDF document (located on storage) to TIFF format and returns resulting file in response content

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
brightness = 1.2 # float | Image brightness. (optional)
compression = 'compression_example' # str | Tiff compression. Possible values are: LZW, CCITT4, CCITT3, RLE, None. (optional)
color_depth = 'color_depth_example' # str | Image color depth. Possible valuse are: Default, Format8bpp, Format4bpp, Format1bpp. (optional)
left_margin = 56 # int | Left image margin. (optional)
right_margin = 56 # int | Right image margin. (optional)
top_margin = 56 # int | Top image margin. (optional)
bottom_margin = 56 # int | Bottom image margin. (optional)
orientation = 'orientation_example' # str | Image orientation. Possible values are: None, Landscape, Portait. (optional)
skip_blank_pages = true # bool | Skip blank pages flag. (optional)
width = 56 # int | Image width. (optional)
height = 56 # int | Image height. (optional)
x_resolution = 56 # int | Horizontal resolution. (optional)
y_resolution = 56 # int | Vertical resolution. (optional)
page_index = 56 # int | Start page to export. (optional)
page_count = 56 # int | Number of pages to export. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to TIFF format and returns resulting file in response content
    api_response = api_instance.get_pdf_in_storage_to_tiff(name, brightness=brightness, compression=compression, color_depth=color_depth, left_margin=left_margin, right_margin=right_margin, top_margin=top_margin, bottom_margin=bottom_margin, orientation=orientation, skip_blank_pages=skip_blank_pages, width=width, height=height, x_resolution=x_resolution, y_resolution=y_resolution, page_index=page_index, page_count=page_count, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_pdf_in_storage_to_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **brightness** | **float**| Image brightness. | [optional] 
 **compression** | **str**| Tiff compression. Possible values are: LZW, CCITT4, CCITT3, RLE, None. | [optional] 
 **color_depth** | **str**| Image color depth. Possible valuse are: Default, Format8bpp, Format4bpp, Format1bpp. | [optional] 
 **left_margin** | **int**| Left image margin. | [optional] 
 **right_margin** | **int**| Right image margin. | [optional] 
 **top_margin** | **int**| Top image margin. | [optional] 
 **bottom_margin** | **int**| Bottom image margin. | [optional] 
 **orientation** | **str**| Image orientation. Possible values are: None, Landscape, Portait. | [optional] 
 **skip_blank_pages** | **bool**| Skip blank pages flag. | [optional] 
 **width** | **int**| Image width. | [optional] 
 **height** | **int**| Image height. | [optional] 
 **x_resolution** | **int**| Horizontal resolution. | [optional] 
 **y_resolution** | **int**| Vertical resolution. | [optional] 
 **page_index** | **int**| Start page to export. | [optional] 
 **page_count** | **int**| Number of pages to export. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_xls**
> file get_pdf_in_storage_to_xls(name, insert_blank_column_at_first=insert_blank_column_at_first, minimize_the_number_of_worksheets=minimize_the_number_of_worksheets, scale_factor=scale_factor, uniform_worksheets=uniform_worksheets, folder=folder, storage=storage)

Converts PDF document (located on storage) to XLS format and returns resulting file in response content

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
insert_blank_column_at_first = true # bool | Insert blank column at first (optional)
minimize_the_number_of_worksheets = true # bool | Minimize the number of worksheets (optional)
scale_factor = 1.2 # float | Scale factor (optional)
uniform_worksheets = true # bool | Uniform worksheets (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to XLS format and returns resulting file in response content
    api_response = api_instance.get_pdf_in_storage_to_xls(name, insert_blank_column_at_first=insert_blank_column_at_first, minimize_the_number_of_worksheets=minimize_the_number_of_worksheets, scale_factor=scale_factor, uniform_worksheets=uniform_worksheets, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_pdf_in_storage_to_xls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **insert_blank_column_at_first** | **bool**| Insert blank column at first | [optional] 
 **minimize_the_number_of_worksheets** | **bool**| Minimize the number of worksheets | [optional] 
 **scale_factor** | **float**| Scale factor | [optional] 
 **uniform_worksheets** | **bool**| Uniform worksheets | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_xml**
> file get_pdf_in_storage_to_xml(name, folder=folder, storage=storage)

Converts PDF document (located on storage) to XML format and returns resulting file in response content

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to XML format and returns resulting file in response content
    api_response = api_instance.get_pdf_in_storage_to_xml(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_pdf_in_storage_to_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_xps**
> file get_pdf_in_storage_to_xps(name, folder=folder, storage=storage)

Converts PDF document (located on storage) to XPS format and returns resulting file in response content

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to XPS format and returns resulting file in response content
    api_response = api_instance.get_pdf_in_storage_to_xps(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_pdf_in_storage_to_xps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ps_in_storage_to_pdf**
> file get_ps_in_storage_to_pdf(src_path, storage=storage)

Convert PS file (located on storage) to PDF format and return resulting file in response. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.ps)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert PS file (located on storage) to PDF format and return resulting file in response. 
    api_response = api_instance.get_ps_in_storage_to_pdf(src_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_ps_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.ps) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_svg_in_storage_to_pdf**
> file get_svg_in_storage_to_pdf(src_path, adjust_page_size=adjust_page_size, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, storage=storage)

Convert SVG file (located on storage) to PDF format and return resulting file in response. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.svg)
adjust_page_size = true # bool | Adjust page size (optional)
height = 1.2 # float | Page height (optional)
width = 1.2 # float | Page width (optional)
is_landscape = true # bool | Is page landscaped (optional)
margin_left = 1.2 # float | Page margin left (optional)
margin_bottom = 1.2 # float | Page margin bottom (optional)
margin_right = 1.2 # float | Page margin right (optional)
margin_top = 1.2 # float | Page margin top (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert SVG file (located on storage) to PDF format and return resulting file in response. 
    api_response = api_instance.get_svg_in_storage_to_pdf(src_path, adjust_page_size=adjust_page_size, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_svg_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.svg) | 
 **adjust_page_size** | **bool**| Adjust page size | [optional] 
 **height** | **float**| Page height | [optional] 
 **width** | **float**| Page width | [optional] 
 **is_landscape** | **bool**| Is page landscaped | [optional] 
 **margin_left** | **float**| Page margin left | [optional] 
 **margin_bottom** | **float**| Page margin bottom | [optional] 
 **margin_right** | **float**| Page margin right | [optional] 
 **margin_top** | **float**| Page margin top | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_text**
> TextRectsResponse get_text(name, llx, lly, urx, ury, format=format, regex=regex, split_rects=split_rects, folder=folder, storage=storage)

Read document text.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
llx = 1.2 # float | 
lly = 1.2 # float | 
urx = 1.2 # float | 
ury = 1.2 # float | 
format = ['format_example'] # list[str] | List of formats for search. (optional)
regex = 'regex_example' # str | Formats are specified as a regular expression. (optional)
split_rects = true # bool | Split result fragments (default is true). (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Read document text.
    api_response = api_instance.get_text(name, llx, lly, urx, ury, format=format, regex=regex, split_rects=split_rects, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **llx** | **float**|  | 
 **lly** | **float**|  | 
 **urx** | **float**|  | 
 **ury** | **float**|  | 
 **format** | [**list[str]**](str.md)| List of formats for search. | [optional] 
 **regex** | **str**| Formats are specified as a regular expression. | [optional] 
 **split_rects** | **bool**| Split result fragments (default is true). | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**TextRectsResponse**](TextRectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_text_annotation**
> TextAnnotationResponse get_text_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page text annotation by ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
annotation_id = 'annotation_id_example' # str | The annotation ID.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Read document page text annotation by ID.
    api_response = api_instance.get_text_annotation(name, annotation_id, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_text_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TextAnnotationResponse**](TextAnnotationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_verify_signature**
> SignatureVerifyResponse get_verify_signature(name, sign_name, storage=storage, folder=folder)

Verify signature document.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
sign_name = 'sign_name_example' # str | Sign name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Verify signature document.
    api_response = api_instance.get_verify_signature(name, sign_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_verify_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **sign_name** | **str**| Sign name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SignatureVerifyResponse**](SignatureVerifyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_in_storage_to_pdf**
> file get_web_in_storage_to_pdf(url, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, storage=storage)

Convert web page to PDF format and return resulting file in response. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
url = 'url_example' # str | Source url
height = 1.2 # float | Page height (optional)
width = 1.2 # float | Page width (optional)
is_landscape = true # bool | Is page landscaped (optional)
margin_left = 1.2 # float | Page margin left (optional)
margin_bottom = 1.2 # float | Page margin bottom (optional)
margin_right = 1.2 # float | Page margin right (optional)
margin_top = 1.2 # float | Page margin top (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert web page to PDF format and return resulting file in response. 
    api_response = api_instance.get_web_in_storage_to_pdf(url, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_web_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| Source url | 
 **height** | **float**| Page height | [optional] 
 **width** | **float**| Page width | [optional] 
 **is_landscape** | **bool**| Is page landscaped | [optional] 
 **margin_left** | **float**| Page margin left | [optional] 
 **margin_bottom** | **float**| Page margin bottom | [optional] 
 **margin_right** | **float**| Page margin right | [optional] 
 **margin_top** | **float**| Page margin top | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_words_per_page**
> WordCountResponse get_words_per_page(name, storage=storage, folder=folder)

Get number of words per document page.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Get number of words per document page.
    api_response = api_instance.get_words_per_page(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_words_per_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**WordCountResponse**](WordCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xfa_pdf_in_storage_to_acro_form**
> file get_xfa_pdf_in_storage_to_acro_form(name, folder=folder, storage=storage)

Converts PDF document which contatins XFA form (located on storage) to PDF with AcroForm and returns resulting file response content

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document which contatins XFA form (located on storage) to PDF with AcroForm and returns resulting file response content
    api_response = api_instance.get_xfa_pdf_in_storage_to_acro_form(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_xfa_pdf_in_storage_to_acro_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xml_in_storage_to_pdf**
> file get_xml_in_storage_to_pdf(src_path, xsl_file_path=xsl_file_path, storage=storage)

Convert XML file (located on storage) to PDF format and return resulting file in response. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.xml)
xsl_file_path = 'xsl_file_path_example' # str | Full XSL source filename (ex. /folder1/folder2/template.xsl) (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert XML file (located on storage) to PDF format and return resulting file in response. 
    api_response = api_instance.get_xml_in_storage_to_pdf(src_path, xsl_file_path=xsl_file_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_xml_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.xml) | 
 **xsl_file_path** | **str**| Full XSL source filename (ex. /folder1/folder2/template.xsl) | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xps_in_storage_to_pdf**
> file get_xps_in_storage_to_pdf(src_path, storage=storage)

Convert XPS file (located on storage) to PDF format and return resulting file in response. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.xps)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert XPS file (located on storage) to PDF format and return resulting file in response. 
    api_response = api_instance.get_xps_in_storage_to_pdf(src_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_xps_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.xps) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xsl_fo_in_storage_to_pdf**
> file get_xsl_fo_in_storage_to_pdf(src_path, storage=storage)

Convert XslFo file (located on storage) to PDF format and return resulting file in response. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.xslfo)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert XslFo file (located on storage) to PDF format and return resulting file in response. 
    api_response = api_instance.get_xsl_fo_in_storage_to_pdf(src_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->get_xsl_fo_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.xslfo) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_append_document**
> DocumentResponse post_append_document(name, append_document=append_document, append_file=append_file, start_page=start_page, end_page=end_page, storage=storage, folder=folder)

Append document to existing one.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The original document name.
append_document = swagger_client.AppendDocument() # AppendDocument | with the append document data. (optional)
append_file = 'append_file_example' # str | Append file server path. (optional)
start_page = 0 # int | Appending start page. (optional) (default to 0)
end_page = 0 # int | Appending end page. (optional) (default to 0)
storage = 'storage_example' # str | The documents storage. (optional)
folder = 'folder_example' # str | The original document folder. (optional)

try: 
    # Append document to existing one.
    api_response = api_instance.post_append_document(name, append_document=append_document, append_file=append_file, start_page=start_page, end_page=end_page, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->post_append_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The original document name. | 
 **append_document** | [**AppendDocument**](AppendDocument.md)| with the append document data. | [optional] 
 **append_file** | **str**| Append file server path. | [optional] 
 **start_page** | **int**| Appending start page. | [optional] [default to 0]
 **end_page** | **int**| Appending end page. | [optional] [default to 0]
 **storage** | **str**| The documents storage. | [optional] 
 **folder** | **str**| The original document folder. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_field**
> AsposeResponse post_create_field(name, page, field=field, storage=storage, folder=folder)

Create field.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page = 56 # int | Document page number.
field = swagger_client.Field() # Field | with the field data. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Create field.
    api_response = api_instance.post_create_field(name, page, field=field, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->post_create_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page** | **int**| Document page number. | 
 **field** | [**Field**](Field.md)| with the field data. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_text_replace**
> TextReplaceResponse post_document_text_replace(name, text_replace, storage=storage, folder=folder)

Document's replace text method.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | 
text_replace = swagger_client.TextReplaceListRequest() # TextReplaceListRequest | 
storage = 'storage_example' # str |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Document's replace text method.
    api_response = api_instance.post_document_text_replace(name, text_replace, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->post_document_text_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **text_replace** | [**TextReplaceListRequest**](TextReplaceListRequest.md)|  | 
 **storage** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**TextReplaceResponse**](TextReplaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_insert_image**
> AsposeResponse post_insert_image(name, page_number, llx, lly, urx, ury, image_file_path=image_file_path, storage=storage, folder=folder, image=image)

Insert image to document page.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
llx = 1.2 # float | Coordinate lower left X.
lly = 1.2 # float | Coordinate lower left Y.
urx = 1.2 # float | Coordinate upper right X.
ury = 1.2 # float | Coordinate upper right Y.
image_file_path = 'image_file_path_example' # str | Path to image file if specified. Request content is used otherwise. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
image = '/path/to/file.txt' # file | Image file. (optional)

try: 
    # Insert image to document page.
    api_response = api_instance.post_insert_image(name, page_number, llx, lly, urx, ury, image_file_path=image_file_path, storage=storage, folder=folder, image=image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->post_insert_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **llx** | **float**| Coordinate lower left X. | 
 **lly** | **float**| Coordinate lower left Y. | 
 **urx** | **float**| Coordinate upper right X. | 
 **ury** | **float**| Coordinate upper right Y. | 
 **image_file_path** | **str**| Path to image file if specified. Request content is used otherwise. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **image** | **file**| Image file. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_move_page**
> AsposeResponse post_move_page(name, page_number, new_index, storage=storage, folder=folder)

Move page to new position.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
new_index = 56 # int | The new page position/index.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Move page to new position.
    api_response = api_instance.post_move_page(name, page_number, new_index, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->post_move_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **new_index** | **int**| The new page position/index. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_optimize_document**
> AsposeResponse post_optimize_document(name, options=options, storage=storage, folder=folder)

Optimize document.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
options = swagger_client.OptimizeOptions() # OptimizeOptions | The optimization options. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Optimize document.
    api_response = api_instance.post_optimize_document(name, options=options, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->post_optimize_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **options** | [**OptimizeOptions**](OptimizeOptions.md)| The optimization options. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_free_text_annotations**
> AsposeResponse post_page_free_text_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page free text annotations.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
annotations = [swagger_client.FreeTextAnnotation()] # list[FreeTextAnnotation] | The array of annotation.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Add document page free text annotations.
    api_response = api_instance.post_page_free_text_annotations(name, page_number, annotations, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->post_page_free_text_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[FreeTextAnnotation]**](FreeTextAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_link_annotations**
> AsposeResponse post_page_link_annotations(name, page_number, links, storage=storage, folder=folder)

Add document page link annotations.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
links = [swagger_client.LinkAnnotation()] # list[LinkAnnotation] | Array of link anotation.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Add document page link annotations.
    api_response = api_instance.post_page_link_annotations(name, page_number, links, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->post_page_link_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **links** | [**list[LinkAnnotation]**](LinkAnnotation.md)| Array of link anotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_text_annotations**
> AsposeResponse post_page_text_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page text annotations.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
annotations = [swagger_client.TextAnnotation()] # list[TextAnnotation] | The array of annotation.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Add document page text annotations.
    api_response = api_instance.post_page_text_annotations(name, page_number, annotations, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->post_page_text_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[TextAnnotation]**](TextAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_text_replace**
> TextReplaceResponse post_page_text_replace(name, page_number, text_replace_list_request, storage=storage, folder=folder)

Page's replace text method.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | 
page_number = 56 # int | 
text_replace_list_request = swagger_client.TextReplaceListRequest() # TextReplaceListRequest | 
storage = 'storage_example' # str |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Page's replace text method.
    api_response = api_instance.post_page_text_replace(name, page_number, text_replace_list_request, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->post_page_text_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **page_number** | **int**|  | 
 **text_replace_list_request** | [**TextReplaceListRequest**](TextReplaceListRequest.md)|  | 
 **storage** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**TextReplaceResponse**](TextReplaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sign_document**
> AsposeResponse post_sign_document(name, signature=signature, storage=storage, folder=folder)

Sign document.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
signature = swagger_client.Signature() # Signature | Signature object containing signature data. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Sign document.
    api_response = api_instance.post_sign_document(name, signature=signature, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->post_sign_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **signature** | [**Signature**](Signature.md)| Signature object containing signature data. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sign_page**
> AsposeResponse post_sign_page(name, page_number, signature=signature, storage=storage, folder=folder)

Sign page.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
signature = swagger_client.Signature() # Signature | Signature object containing signature data. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Sign page.
    api_response = api_instance.post_sign_page(name, page_number, signature=signature, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->post_sign_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **signature** | [**Signature**](Signature.md)| Signature object containing signature data. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_split_document**
> SplitResultResponse post_split_document(name, format=format, _from=_from, to=to, storage=storage, folder=folder)

Split document to parts.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | Document name.
format = 'format_example' # str | Resulting documents format. (optional)
_from = 56 # int | Start page if defined. (optional)
to = 56 # int | End page if defined. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Split document to parts.
    api_response = api_instance.post_split_document(name, format=format, _from=_from, to=to, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->post_split_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **format** | **str**| Resulting documents format. | [optional] 
 **_from** | **int**| Start page if defined. | [optional] 
 **to** | **int**| End page if defined. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SplitResultResponse**](SplitResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_add_new_page**
> DocumentPagesResponse put_add_new_page(name, storage=storage, folder=folder)

Add new page to end of the document.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Add new page to end of the document.
    api_response = api_instance.put_add_new_page(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_add_new_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**DocumentPagesResponse**](DocumentPagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_add_text**
> AsposeResponse put_add_text(name, page_number, paragraph=paragraph, folder=folder, storage=storage)

Add text to PDF document page.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | Number of page (starting from 1).
paragraph = swagger_client.Paragraph() # Paragraph | Paragraph data. (optional)
folder = 'folder_example' # str | Document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Add text to PDF document page.
    api_response = api_instance.put_add_text(name, page_number, paragraph=paragraph, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_add_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| Number of page (starting from 1). | 
 **paragraph** | [**Paragraph**](Paragraph.md)| Paragraph data. | [optional] 
 **folder** | **str**| Document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_create**
> AsposeResponse put_create(path, file, version_id=version_id, storage=storage)

Upload a specific file 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
path = 'path_example' # str | Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext
file = '/path/to/file.txt' # file | File to upload
version_id = 'version_id_example' # str | Source file's version (optional)
storage = 'storage_example' # str | User's storage name (optional)

try: 
    # Upload a specific file 
    api_response = api_instance.put_create(path, file, version_id=version_id, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext | 
 **file** | **file**| File to upload | 
 **version_id** | **str**| Source file&#39;s version | [optional] 
 **storage** | **str**| User&#39;s storage name | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_create_document**
> DocumentResponse put_create_document(name, storage=storage, folder=folder)

Create empty document.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The new document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The new document folder. (optional)

try: 
    # Create empty document.
    api_response = api_instance.put_create_document(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The new document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The new document folder. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_epub_in_storage_to_pdf**
> AsposeResponse put_epub_in_storage_to_pdf(name, src_path, storage=storage, dst_folder=dst_folder)

Convert EPUB file (located on storage) to PDF format and upload resulting file to storage. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.epub)
storage = 'storage_example' # str | The document storage. (optional)
dst_folder = 'dst_folder_example' # str | The destination document folder. (optional)

try: 
    # Convert EPUB file (located on storage) to PDF format and upload resulting file to storage. 
    api_response = api_instance.put_epub_in_storage_to_pdf(name, src_path, storage=storage, dst_folder=dst_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_epub_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.epub) | 
 **storage** | **str**| The document storage. | [optional] 
 **dst_folder** | **str**| The destination document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_fields_flatten**
> AsposeResponse put_fields_flatten(name, storage=storage, folder=folder)

Flatten form fields in document.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Flatten form fields in document.
    api_response = api_instance.put_fields_flatten(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_fields_flatten: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_free_text_annotation**
> FreeTextAnnotationResponse put_free_text_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document free text annotation

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
annotation_id = 'annotation_id_example' # str | The annotation ID.
annotation = swagger_client.FreeTextAnnotation() # FreeTextAnnotation | Annotation.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Replace document free text annotation
    api_response = api_instance.put_free_text_annotation(name, annotation_id, annotation, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_free_text_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**FreeTextAnnotation**](FreeTextAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FreeTextAnnotationResponse**](FreeTextAnnotationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_html_in_storage_to_pdf**
> AsposeResponse put_html_in_storage_to_pdf(name, src_path, html_file_name, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, dst_folder=dst_folder, storage=storage)

Convert HTML file (located on storage) to PDF format and upload resulting file to storage. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.zip)
html_file_name = 'html_file_name_example' # str | Name of HTML file in ZIP.
height = 1.2 # float | Page height (optional)
width = 1.2 # float | Page width (optional)
is_landscape = true # bool | Is page landscaped (optional)
margin_left = 1.2 # float | Page margin left (optional)
margin_bottom = 1.2 # float | Page margin bottom (optional)
margin_right = 1.2 # float | Page margin right (optional)
margin_top = 1.2 # float | Page margin top (optional)
dst_folder = 'dst_folder_example' # str | The destination document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert HTML file (located on storage) to PDF format and upload resulting file to storage. 
    api_response = api_instance.put_html_in_storage_to_pdf(name, src_path, html_file_name, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, dst_folder=dst_folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_html_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.zip) | 
 **html_file_name** | **str**| Name of HTML file in ZIP. | 
 **height** | **float**| Page height | [optional] 
 **width** | **float**| Page width | [optional] 
 **is_landscape** | **bool**| Is page landscaped | [optional] 
 **margin_left** | **float**| Page margin left | [optional] 
 **margin_bottom** | **float**| Page margin bottom | [optional] 
 **margin_right** | **float**| Page margin right | [optional] 
 **margin_top** | **float**| Page margin top | [optional] 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_image_extract_as_gif**
> AsposeResponse put_image_extract_as_gif(name, image_id, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document image in GIF format to folder

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
image_id = 'image_id_example' # str | Image ID.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
dest_folder = 'dest_folder_example' # str | The document folder. (optional)

try: 
    # Extract document image in GIF format to folder
    api_response = api_instance.put_image_extract_as_gif(name, image_id, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_image_extract_as_gif: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_image_extract_as_jpeg**
> AsposeResponse put_image_extract_as_jpeg(name, image_id, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document image in JPEG format to folder

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
image_id = 'image_id_example' # str | Image ID.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
dest_folder = 'dest_folder_example' # str | The document folder. (optional)

try: 
    # Extract document image in JPEG format to folder
    api_response = api_instance.put_image_extract_as_jpeg(name, image_id, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_image_extract_as_jpeg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_image_extract_as_png**
> AsposeResponse put_image_extract_as_png(name, image_id, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document image in PNG format to folder

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
image_id = 'image_id_example' # str | Image ID.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
dest_folder = 'dest_folder_example' # str | The document folder. (optional)

try: 
    # Extract document image in PNG format to folder
    api_response = api_instance.put_image_extract_as_png(name, image_id, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_image_extract_as_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_image_extract_as_tiff**
> AsposeResponse put_image_extract_as_tiff(name, image_id, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document image in TIFF format to folder

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
image_id = 'image_id_example' # str | Image ID.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
dest_folder = 'dest_folder_example' # str | The document folder. (optional)

try: 
    # Extract document image in TIFF format to folder
    api_response = api_instance.put_image_extract_as_tiff(name, image_id, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_image_extract_as_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_image_in_storage_to_pdf**
> AsposeResponse put_image_in_storage_to_pdf(name, image_templates, dst_folder=dst_folder, storage=storage)

Convert image file (located on storage) to PDF format and upload resulting file to storage. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
image_templates = swagger_client.ImageTemplatesRequest() # ImageTemplatesRequest | Image templates
dst_folder = 'dst_folder_example' # str | The destination document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert image file (located on storage) to PDF format and upload resulting file to storage. 
    api_response = api_instance.put_image_in_storage_to_pdf(name, image_templates, dst_folder=dst_folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_image_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_templates** | [**ImageTemplatesRequest**](ImageTemplatesRequest.md)| Image templates | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_images_extract_as_gif**
> AsposeResponse put_images_extract_as_gif(name, page_number, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document images in GIF format to folder.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
dest_folder = 'dest_folder_example' # str | The document folder. (optional)

try: 
    # Extract document images in GIF format to folder.
    api_response = api_instance.put_images_extract_as_gif(name, page_number, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_images_extract_as_gif: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_images_extract_as_jpeg**
> AsposeResponse put_images_extract_as_jpeg(name, page_number, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document images in JPEG format to folder.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
storage = 'storage_example' # str |  (optional)
folder = 'folder_example' # str | The document folder. (optional)
dest_folder = 'dest_folder_example' # str | The document folder. (optional)

try: 
    # Extract document images in JPEG format to folder.
    api_response = api_instance.put_images_extract_as_jpeg(name, page_number, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_images_extract_as_jpeg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **storage** | **str**|  | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_images_extract_as_png**
> AsposeResponse put_images_extract_as_png(name, page_number, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document images in PNG format to folder.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
dest_folder = 'dest_folder_example' # str | The document folder. (optional)

try: 
    # Extract document images in PNG format to folder.
    api_response = api_instance.put_images_extract_as_png(name, page_number, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_images_extract_as_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_images_extract_as_tiff**
> AsposeResponse put_images_extract_as_tiff(name, page_number, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document images in TIFF format to folder.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
dest_folder = 'dest_folder_example' # str | The document folder. (optional)

try: 
    # Extract document images in TIFF format to folder.
    api_response = api_instance.put_images_extract_as_tiff(name, page_number, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_images_extract_as_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_la_te_x_in_storage_to_pdf**
> AsposeResponse put_la_te_x_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)

Convert LaTeX file (located on storage) to PDF format and upload resulting file to storage. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.tex)
dst_folder = 'dst_folder_example' # str | The destination document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert LaTeX file (located on storage) to PDF format and upload resulting file to storage. 
    api_response = api_instance.put_la_te_x_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_la_te_x_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.tex) | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_link_annotation**
> LinkAnnotationResponse put_link_annotation(name, link_id, link, storage=storage, folder=folder)

Replace document page link annotations

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
link_id = 'link_id_example' # str | The link ID.
link = swagger_client.LinkAnnotation() # LinkAnnotation | Link anotation.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Replace document page link annotations
    api_response = api_instance.put_link_annotation(name, link_id, link, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_link_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **link_id** | **str**| The link ID. | 
 **link** | [**LinkAnnotation**](LinkAnnotation.md)| Link anotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**LinkAnnotationResponse**](LinkAnnotationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_merge_documents**
> file put_merge_documents(name, merge_documents=merge_documents, storage=storage, folder=folder)

Merge a list of documents.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | Resulting documen name.
merge_documents = swagger_client.MergeDocuments() # MergeDocuments | with a list of documents. (optional)
storage = 'storage_example' # str | Resulting document storage. (optional)
folder = 'folder_example' # str | Resulting document folder. (optional)

try: 
    # Merge a list of documents.
    api_response = api_instance.put_merge_documents(name, merge_documents=merge_documents, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_merge_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Resulting documen name. | 
 **merge_documents** | [**MergeDocuments**](MergeDocuments.md)| with a list of documents. | [optional] 
 **storage** | **str**| Resulting document storage. | [optional] 
 **folder** | **str**| Resulting document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_mht_in_storage_to_pdf**
> AsposeResponse put_mht_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)

Convert MHT file (located on storage) to PDF format and upload resulting file to storage. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.mht)
dst_folder = 'dst_folder_example' # str | The destination document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert MHT file (located on storage) to PDF format and upload resulting file to storage. 
    api_response = api_instance.put_mht_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_mht_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.mht) | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_page_add_stamp**
> AsposeResponse put_page_add_stamp(name, page_number, stamp, storage=storage, folder=folder)

Add page stamp.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
stamp = swagger_client.Stamp() # Stamp | with data.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Add page stamp.
    api_response = api_instance.put_page_add_stamp(name, page_number, stamp, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_page_add_stamp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **stamp** | [**Stamp**](Stamp.md)| with data. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_page_convert_to_bmp**
> AsposeResponse put_page_convert_to_bmp(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage)

Convert document page to bmp image and upload resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
out_path = 'out_path_example' # str | The out path of result image.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert document page to bmp image and upload resulting file to storage.
    api_response = api_instance.put_page_convert_to_bmp(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_page_convert_to_bmp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **out_path** | **str**| The out path of result image. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_page_convert_to_emf**
> AsposeResponse put_page_convert_to_emf(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage)

Convert document page to emf image and upload resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
out_path = 'out_path_example' # str | The out path of result image.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert document page to emf image and upload resulting file to storage.
    api_response = api_instance.put_page_convert_to_emf(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_page_convert_to_emf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **out_path** | **str**| The out path of result image. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_page_convert_to_gif**
> AsposeResponse put_page_convert_to_gif(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage)

Convert document page to gif image and upload resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
out_path = 'out_path_example' # str | The out path of result image.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert document page to gif image and upload resulting file to storage.
    api_response = api_instance.put_page_convert_to_gif(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_page_convert_to_gif: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **out_path** | **str**| The out path of result image. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_page_convert_to_jpeg**
> AsposeResponse put_page_convert_to_jpeg(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage)

Convert document page to Jpeg image and upload resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
out_path = 'out_path_example' # str | The out path of result image.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert document page to Jpeg image and upload resulting file to storage.
    api_response = api_instance.put_page_convert_to_jpeg(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_page_convert_to_jpeg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **out_path** | **str**| The out path of result image. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_page_convert_to_png**
> AsposeResponse put_page_convert_to_png(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage)

Convert document page to png image and upload resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
out_path = 'out_path_example' # str | The out path of result image.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert document page to png image and upload resulting file to storage.
    api_response = api_instance.put_page_convert_to_png(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_page_convert_to_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **out_path** | **str**| The out path of result image. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_page_convert_to_tiff**
> AsposeResponse put_page_convert_to_tiff(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage)

Convert document page to Tiff image and upload resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
page_number = 56 # int | The page number.
out_path = 'out_path_example' # str | The out path of result image.
width = 56 # int | The converted image width. (optional)
height = 56 # int | The converted image height. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert document page to Tiff image and upload resulting file to storage.
    api_response = api_instance.put_page_convert_to_tiff(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_page_convert_to_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **out_path** | **str**| The out path of result image. | 
 **width** | **int**| The converted image width. | [optional] 
 **height** | **int**| The converted image height. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pcl_in_storage_to_pdf**
> AsposeResponse put_pcl_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)

Convert PCL file (located on storage) to PDF format and upload resulting file to storage. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.pcl)
dst_folder = 'dst_folder_example' # str | The destination document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert PCL file (located on storage) to PDF format and upload resulting file to storage. 
    api_response = api_instance.put_pcl_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pcl_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.pcl) | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_doc**
> AsposeResponse put_pdf_in_request_to_doc(out_path, add_return_to_line_end=add_return_to_line_end, format=format, image_resolution_x=image_resolution_x, image_resolution_y=image_resolution_y, max_distance_between_text_lines=max_distance_between_text_lines, mode=mode, recognize_bullets=recognize_bullets, relative_horizontal_proximity=relative_horizontal_proximity, storage=storage, file=file)

Converts PDF document (in request content) to DOC format and uploads resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.doc)
add_return_to_line_end = true # bool | Add return to line end. (optional)
format = 'format_example' # str | Allows to specify .doc or .docx file format. (optional)
image_resolution_x = 56 # int | Image resolution X. (optional)
image_resolution_y = 56 # int | Image resolution Y. (optional)
max_distance_between_text_lines = 1.2 # float | Max distance between text lines. (optional)
mode = 'mode_example' # str | Allows to control how a PDF document is converted into a word processing document. (optional)
recognize_bullets = true # bool | Recognize bullets. (optional)
relative_horizontal_proximity = 1.2 # float | Relative horizontal proximity. (optional)
storage = 'storage_example' # str | The document storage. (optional)
file = '/path/to/file.txt' # file | A file to be converted. (optional)

try: 
    # Converts PDF document (in request content) to DOC format and uploads resulting file to storage.
    api_response = api_instance.put_pdf_in_request_to_doc(out_path, add_return_to_line_end=add_return_to_line_end, format=format, image_resolution_x=image_resolution_x, image_resolution_y=image_resolution_y, max_distance_between_text_lines=max_distance_between_text_lines, mode=mode, recognize_bullets=recognize_bullets, relative_horizontal_proximity=relative_horizontal_proximity, storage=storage, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_request_to_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.doc) | 
 **add_return_to_line_end** | **bool**| Add return to line end. | [optional] 
 **format** | **str**| Allows to specify .doc or .docx file format. | [optional] 
 **image_resolution_x** | **int**| Image resolution X. | [optional] 
 **image_resolution_y** | **int**| Image resolution Y. | [optional] 
 **max_distance_between_text_lines** | **float**| Max distance between text lines. | [optional] 
 **mode** | **str**| Allows to control how a PDF document is converted into a word processing document. | [optional] 
 **recognize_bullets** | **bool**| Recognize bullets. | [optional] 
 **relative_horizontal_proximity** | **float**| Relative horizontal proximity. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_epub**
> AsposeResponse put_pdf_in_request_to_epub(out_path, content_recognition_mode=content_recognition_mode, storage=storage, file=file)

Converts PDF document (in request content) to EPUB format and uploads resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.epub)
content_recognition_mode = 'content_recognition_mode_example' # str | ?roperty tunes conversion for this or that desirable method of recognition of content. (optional)
storage = 'storage_example' # str | The document storage. (optional)
file = '/path/to/file.txt' # file | A file to be converted. (optional)

try: 
    # Converts PDF document (in request content) to EPUB format and uploads resulting file to storage.
    api_response = api_instance.put_pdf_in_request_to_epub(out_path, content_recognition_mode=content_recognition_mode, storage=storage, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_request_to_epub: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.epub) | 
 **content_recognition_mode** | **str**| ?roperty tunes conversion for this or that desirable method of recognition of content. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_html**
> AsposeResponse put_pdf_in_request_to_html(out_path, additional_margin_width_in_points=additional_margin_width_in_points, compress_svg_graphics_if_any=compress_svg_graphics_if_any, convert_marked_content_to_layers=convert_marked_content_to_layers, default_font_name=default_font_name, document_type=document_type, fixed_layout=fixed_layout, image_resolution=image_resolution, minimal_line_width=minimal_line_width, prevent_glyphs_grouping=prevent_glyphs_grouping, split_css_into_pages=split_css_into_pages, split_into_pages=split_into_pages, use_z_order=use_z_order, antialiasing_processing=antialiasing_processing, css_class_names_prefix=css_class_names_prefix, explicit_list_of_saved_pages=explicit_list_of_saved_pages, font_encoding_strategy=font_encoding_strategy, font_saving_mode=font_saving_mode, html_markup_generation_mode=html_markup_generation_mode, letters_positioning_method=letters_positioning_method, pages_flow_type_depends_on_viewers_screen_size=pages_flow_type_depends_on_viewers_screen_size, parts_embedding_mode=parts_embedding_mode, raster_images_saving_mode=raster_images_saving_mode, remove_empty_areas_on_top_and_bottom=remove_empty_areas_on_top_and_bottom, save_shadowed_texts_as_transparent_texts=save_shadowed_texts_as_transparent_texts, save_transparent_texts=save_transparent_texts, special_folder_for_all_images=special_folder_for_all_images, special_folder_for_svg_images=special_folder_for_svg_images, try_save_text_underlining_and_strikeouting_in_css=try_save_text_underlining_and_strikeouting_in_css, storage=storage, file=file)

Converts PDF document (in request content) to Html format and uploads resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.html)
additional_margin_width_in_points = 56 # int | Defines width of margin that will be forcibly left around that output HTML-areas. (optional)
compress_svg_graphics_if_any = true # bool | The flag that indicates whether found SVG graphics(if any) will be compressed(zipped) into SVGZ format during saving. (optional)
convert_marked_content_to_layers = true # bool | If attribute ConvertMarkedContentToLayers set to true then an all elements inside a PDF marked content (layer) will be put into an HTML div with \"data-pdflayer\" attribute specifying a layer name. This layer name will be extracted from optional properties of PDF marked content. If this attribute is false (by default) then no any layers will be created from PDF marked content. (optional)
default_font_name = 'default_font_name_example' # str | Specifies the name of an installed font which is used to substitute any document font that is not embedded and not installed in the system. If null then default substitution font is used. (optional)
document_type = 'document_type_example' # str | Result document type. (optional)
fixed_layout = true # bool | The value indicating whether that HTML is created as fixed layout. (optional)
image_resolution = 56 # int | Resolution for image rendering. (optional)
minimal_line_width = 56 # int | This attribute sets minimal width of graphic path line. If thickness of line is less than 1px Adobe Acrobat rounds it to this value. So this attribute can be used to emulate this behavior for HTML browsers. (optional)
prevent_glyphs_grouping = true # bool | This attribute switch on the mode when text glyphs will not be grouped into words and strings This mode allows to keep maximum precision during positioning of glyphs on the page and it can be used for conversion documents with music notes or glyphs that should be placed separately each other. This parameter will be applied to document only when the value of FixedLayout attribute is true. (optional)
split_css_into_pages = true # bool | When multipage-mode selected(i.e 'SplitIntoPages' is 'true'), then this attribute defines whether should be created separate CSS-file for each result HTML page. (optional)
split_into_pages = true # bool | The flag that indicates whether each page of source document will be converted into it's own target HTML document, i.e whether result HTML will be splitted into several HTML-pages. (optional)
use_z_order = true # bool | If attribute UseZORder set to true, graphics and text are added to resultant HTML document accordingly Z-order in original PDF document. If this attribute is false all graphics is put as single layer which may cause some unnecessary effects for overlapped objects. (optional)
antialiasing_processing = 'antialiasing_processing_example' # str | The parameter defines required antialiasing measures during conversion of compound background images from PDF to HTML. (optional)
css_class_names_prefix = 'css_class_names_prefix_example' # str | When PDFtoHTML converter generates result CSSs, CSS class names (something like \".stl_01 {}\" ... \".stl_NN {}) are generated and used in result CSS. This property allows forcibly set class name prefix. (optional)
explicit_list_of_saved_pages = [56] # list[int] | With this property You can explicitely define what pages of document should be converted. Pages in this list must have 1-based numbers. I.e. valid numbers of pages must be taken from range (1...[NumberOfPagesInConvertedDocument]) Order of appearing of pages in this list does not affect their order in result HTML page(s) - in result pages allways will go in order in which they are present in source PDF. (optional)
font_encoding_strategy = 'font_encoding_strategy_example' # str | Defines encoding special rule to tune PDF decoding for current document. (optional)
font_saving_mode = 'font_saving_mode_example' # str | Defines font saving mode that will be used during saving of PDF to desirable format. (optional)
html_markup_generation_mode = 'html_markup_generation_mode_example' # str | Sometimes specific reqirments to generation of HTML markup are present. This parameter defines HTML preparing modes that can be used during conversion of PDF to HTML to match such specific requirments. (optional)
letters_positioning_method = 'letters_positioning_method_example' # str | The mode of positioning of letters in words in result HTML. (optional)
pages_flow_type_depends_on_viewers_screen_size = true # bool | If attribute 'SplitOnPages=false', than whole HTML representing all input PDF pages will be put into one big result HTML file. This flag defines whether result HTML will be generated in such way that flow of areas that represent PDF pages in result HTML will depend on screen resolution of viewer. (optional)
parts_embedding_mode = 'parts_embedding_mode_example' # str | It defines whether referenced files (HTML, Fonts,Images, CSSes) will be embedded into main HTML file or will be generated as apart binary entities. (optional)
raster_images_saving_mode = 'raster_images_saving_mode_example' # str | Converted PDF can contain raster images This parameter defines how they should be handled during conversion of PDF to HTML. (optional)
remove_empty_areas_on_top_and_bottom = true # bool | Defines whether in created HTML will be removed top and bottom empty area without any content (if any). (optional)
save_shadowed_texts_as_transparent_texts = true # bool | Pdf can contain texts that are shadowed by another elements (f.e. by images) but can be selected to clipboard in Acrobat Reader (usually it happen when document contains images and OCRed texts extracted from it). This settings tells to converter whether we need save such texts as transparent selectable texts in result HTML to mimic behaviour of Acrobat Reader (othervise such texts are usually saved as hidden, not available for copying to clipboard). (optional)
save_transparent_texts = true # bool | Pdf can contain transparent texts that can be selected to clipboard (usually it happen when document contains images and OCRed texts extracted from it). This settings tells to converter whether we need save such texts as transparent selectable texts in result HTML. (optional)
special_folder_for_all_images = 'special_folder_for_all_images_example' # str | The path to directory to which must be saved any images if they are encountered during saving of document as HTML. If parameter is empty or null then image files(if any) wil be saved together with other files linked to HTML It does not affect anything if CustomImageSavingStrategy property was successfully used to process relevant image file. (optional)
special_folder_for_svg_images = 'special_folder_for_svg_images_example' # str | The path to directory to which must be saved only SVG-images if they are encountered during saving of document as HTML. If parameter is empty or null then SVG files(if any) wil be saved together with other image-files (near to output file) or in special folder for images (if it specified in SpecialImagesFolderIfAny option). It does not affect anything if CustomImageSavingStrategy property was successfully used to process relevant image file. (optional)
try_save_text_underlining_and_strikeouting_in_css = true # bool | PDF itself does not contain underlining markers for texts. It emulated with line situated under text. This option allows converter try guess that this or that line is a text's underlining and put this info into CSS instead of drawing of underlining graphically. (optional)
storage = 'storage_example' # str | The document storage. (optional)
file = '/path/to/file.txt' # file | A file to be converted. (optional)

try: 
    # Converts PDF document (in request content) to Html format and uploads resulting file to storage.
    api_response = api_instance.put_pdf_in_request_to_html(out_path, additional_margin_width_in_points=additional_margin_width_in_points, compress_svg_graphics_if_any=compress_svg_graphics_if_any, convert_marked_content_to_layers=convert_marked_content_to_layers, default_font_name=default_font_name, document_type=document_type, fixed_layout=fixed_layout, image_resolution=image_resolution, minimal_line_width=minimal_line_width, prevent_glyphs_grouping=prevent_glyphs_grouping, split_css_into_pages=split_css_into_pages, split_into_pages=split_into_pages, use_z_order=use_z_order, antialiasing_processing=antialiasing_processing, css_class_names_prefix=css_class_names_prefix, explicit_list_of_saved_pages=explicit_list_of_saved_pages, font_encoding_strategy=font_encoding_strategy, font_saving_mode=font_saving_mode, html_markup_generation_mode=html_markup_generation_mode, letters_positioning_method=letters_positioning_method, pages_flow_type_depends_on_viewers_screen_size=pages_flow_type_depends_on_viewers_screen_size, parts_embedding_mode=parts_embedding_mode, raster_images_saving_mode=raster_images_saving_mode, remove_empty_areas_on_top_and_bottom=remove_empty_areas_on_top_and_bottom, save_shadowed_texts_as_transparent_texts=save_shadowed_texts_as_transparent_texts, save_transparent_texts=save_transparent_texts, special_folder_for_all_images=special_folder_for_all_images, special_folder_for_svg_images=special_folder_for_svg_images, try_save_text_underlining_and_strikeouting_in_css=try_save_text_underlining_and_strikeouting_in_css, storage=storage, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_request_to_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.html) | 
 **additional_margin_width_in_points** | **int**| Defines width of margin that will be forcibly left around that output HTML-areas. | [optional] 
 **compress_svg_graphics_if_any** | **bool**| The flag that indicates whether found SVG graphics(if any) will be compressed(zipped) into SVGZ format during saving. | [optional] 
 **convert_marked_content_to_layers** | **bool**| If attribute ConvertMarkedContentToLayers set to true then an all elements inside a PDF marked content (layer) will be put into an HTML div with \&quot;data-pdflayer\&quot; attribute specifying a layer name. This layer name will be extracted from optional properties of PDF marked content. If this attribute is false (by default) then no any layers will be created from PDF marked content. | [optional] 
 **default_font_name** | **str**| Specifies the name of an installed font which is used to substitute any document font that is not embedded and not installed in the system. If null then default substitution font is used. | [optional] 
 **document_type** | **str**| Result document type. | [optional] 
 **fixed_layout** | **bool**| The value indicating whether that HTML is created as fixed layout. | [optional] 
 **image_resolution** | **int**| Resolution for image rendering. | [optional] 
 **minimal_line_width** | **int**| This attribute sets minimal width of graphic path line. If thickness of line is less than 1px Adobe Acrobat rounds it to this value. So this attribute can be used to emulate this behavior for HTML browsers. | [optional] 
 **prevent_glyphs_grouping** | **bool**| This attribute switch on the mode when text glyphs will not be grouped into words and strings This mode allows to keep maximum precision during positioning of glyphs on the page and it can be used for conversion documents with music notes or glyphs that should be placed separately each other. This parameter will be applied to document only when the value of FixedLayout attribute is true. | [optional] 
 **split_css_into_pages** | **bool**| When multipage-mode selected(i.e &#39;SplitIntoPages&#39; is &#39;true&#39;), then this attribute defines whether should be created separate CSS-file for each result HTML page. | [optional] 
 **split_into_pages** | **bool**| The flag that indicates whether each page of source document will be converted into it&#39;s own target HTML document, i.e whether result HTML will be splitted into several HTML-pages. | [optional] 
 **use_z_order** | **bool**| If attribute UseZORder set to true, graphics and text are added to resultant HTML document accordingly Z-order in original PDF document. If this attribute is false all graphics is put as single layer which may cause some unnecessary effects for overlapped objects. | [optional] 
 **antialiasing_processing** | **str**| The parameter defines required antialiasing measures during conversion of compound background images from PDF to HTML. | [optional] 
 **css_class_names_prefix** | **str**| When PDFtoHTML converter generates result CSSs, CSS class names (something like \&quot;.stl_01 {}\&quot; ... \&quot;.stl_NN {}) are generated and used in result CSS. This property allows forcibly set class name prefix. | [optional] 
 **explicit_list_of_saved_pages** | [**list[int]**](int.md)| With this property You can explicitely define what pages of document should be converted. Pages in this list must have 1-based numbers. I.e. valid numbers of pages must be taken from range (1...[NumberOfPagesInConvertedDocument]) Order of appearing of pages in this list does not affect their order in result HTML page(s) - in result pages allways will go in order in which they are present in source PDF. | [optional] 
 **font_encoding_strategy** | **str**| Defines encoding special rule to tune PDF decoding for current document. | [optional] 
 **font_saving_mode** | **str**| Defines font saving mode that will be used during saving of PDF to desirable format. | [optional] 
 **html_markup_generation_mode** | **str**| Sometimes specific reqirments to generation of HTML markup are present. This parameter defines HTML preparing modes that can be used during conversion of PDF to HTML to match such specific requirments. | [optional] 
 **letters_positioning_method** | **str**| The mode of positioning of letters in words in result HTML. | [optional] 
 **pages_flow_type_depends_on_viewers_screen_size** | **bool**| If attribute &#39;SplitOnPages&#x3D;false&#39;, than whole HTML representing all input PDF pages will be put into one big result HTML file. This flag defines whether result HTML will be generated in such way that flow of areas that represent PDF pages in result HTML will depend on screen resolution of viewer. | [optional] 
 **parts_embedding_mode** | **str**| It defines whether referenced files (HTML, Fonts,Images, CSSes) will be embedded into main HTML file or will be generated as apart binary entities. | [optional] 
 **raster_images_saving_mode** | **str**| Converted PDF can contain raster images This parameter defines how they should be handled during conversion of PDF to HTML. | [optional] 
 **remove_empty_areas_on_top_and_bottom** | **bool**| Defines whether in created HTML will be removed top and bottom empty area without any content (if any). | [optional] 
 **save_shadowed_texts_as_transparent_texts** | **bool**| Pdf can contain texts that are shadowed by another elements (f.e. by images) but can be selected to clipboard in Acrobat Reader (usually it happen when document contains images and OCRed texts extracted from it). This settings tells to converter whether we need save such texts as transparent selectable texts in result HTML to mimic behaviour of Acrobat Reader (othervise such texts are usually saved as hidden, not available for copying to clipboard). | [optional] 
 **save_transparent_texts** | **bool**| Pdf can contain transparent texts that can be selected to clipboard (usually it happen when document contains images and OCRed texts extracted from it). This settings tells to converter whether we need save such texts as transparent selectable texts in result HTML. | [optional] 
 **special_folder_for_all_images** | **str**| The path to directory to which must be saved any images if they are encountered during saving of document as HTML. If parameter is empty or null then image files(if any) wil be saved together with other files linked to HTML It does not affect anything if CustomImageSavingStrategy property was successfully used to process relevant image file. | [optional] 
 **special_folder_for_svg_images** | **str**| The path to directory to which must be saved only SVG-images if they are encountered during saving of document as HTML. If parameter is empty or null then SVG files(if any) wil be saved together with other image-files (near to output file) or in special folder for images (if it specified in SpecialImagesFolderIfAny option). It does not affect anything if CustomImageSavingStrategy property was successfully used to process relevant image file. | [optional] 
 **try_save_text_underlining_and_strikeouting_in_css** | **bool**| PDF itself does not contain underlining markers for texts. It emulated with line situated under text. This option allows converter try guess that this or that line is a text&#39;s underlining and put this info into CSS instead of drawing of underlining graphically. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_la_te_x**
> AsposeResponse put_pdf_in_request_to_la_te_x(out_path, pages_count=pages_count, storage=storage, file=file)

Converts PDF document (in request content) to LaTeX format and uploads resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.tex)
pages_count = 56 # int | Pages count. (optional)
storage = 'storage_example' # str | The document storage. (optional)
file = '/path/to/file.txt' # file | A file to be converted. (optional)

try: 
    # Converts PDF document (in request content) to LaTeX format and uploads resulting file to storage.
    api_response = api_instance.put_pdf_in_request_to_la_te_x(out_path, pages_count=pages_count, storage=storage, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_request_to_la_te_x: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.tex) | 
 **pages_count** | **int**| Pages count. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_mobi_xml**
> AsposeResponse put_pdf_in_request_to_mobi_xml(out_path, storage=storage, file=file)

Converts PDF document (in request content) to MOBIXML format and uploads resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.mobixml)
storage = 'storage_example' # str | The document storage. (optional)
file = '/path/to/file.txt' # file | A file to be converted. (optional)

try: 
    # Converts PDF document (in request content) to MOBIXML format and uploads resulting file to storage.
    api_response = api_instance.put_pdf_in_request_to_mobi_xml(out_path, storage=storage, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_request_to_mobi_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.mobixml) | 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_pdf_a**
> AsposeResponse put_pdf_in_request_to_pdf_a(out_path, type, storage=storage, file=file)

Converts PDF document (in request content) to PdfA format and uploads resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.pdf)
type = 'type_example' # str | Type of PdfA format.
storage = 'storage_example' # str | The document storage. (optional)
file = '/path/to/file.txt' # file | A file to be converted. (optional)

try: 
    # Converts PDF document (in request content) to PdfA format and uploads resulting file to storage.
    api_response = api_instance.put_pdf_in_request_to_pdf_a(out_path, type, storage=storage, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_request_to_pdf_a: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.pdf) | 
 **type** | **str**| Type of PdfA format. | 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_pptx**
> AsposeResponse put_pdf_in_request_to_pptx(out_path, separate_images=separate_images, slides_as_images=slides_as_images, storage=storage, file=file)

Converts PDF document (in request content) to PPTX format and uploads resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.pptx)
separate_images = true # bool | Separate images. (optional)
slides_as_images = true # bool | Slides as images. (optional)
storage = 'storage_example' # str | The document storage. (optional)
file = '/path/to/file.txt' # file | A file to be converted. (optional)

try: 
    # Converts PDF document (in request content) to PPTX format and uploads resulting file to storage.
    api_response = api_instance.put_pdf_in_request_to_pptx(out_path, separate_images=separate_images, slides_as_images=slides_as_images, storage=storage, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_request_to_pptx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.pptx) | 
 **separate_images** | **bool**| Separate images. | [optional] 
 **slides_as_images** | **bool**| Slides as images. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_svg**
> AsposeResponse put_pdf_in_request_to_svg(out_path, storage=storage, file=file)

Converts PDF document (in request content) to SVG format and uploads resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.svg)
storage = 'storage_example' # str | The document storage. (optional)
file = '/path/to/file.txt' # file | A file to be converted. (optional)

try: 
    # Converts PDF document (in request content) to SVG format and uploads resulting file to storage.
    api_response = api_instance.put_pdf_in_request_to_svg(out_path, storage=storage, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_request_to_svg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.svg) | 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_tiff**
> AsposeResponse put_pdf_in_request_to_tiff(out_path, brightness=brightness, compression=compression, color_depth=color_depth, left_margin=left_margin, right_margin=right_margin, top_margin=top_margin, bottom_margin=bottom_margin, orientation=orientation, skip_blank_pages=skip_blank_pages, width=width, height=height, x_resolution=x_resolution, y_resolution=y_resolution, page_index=page_index, page_count=page_count, storage=storage, file=file)

Converts PDF document (in request content) to TIFF format and uploads resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.tiff)
brightness = 1.2 # float | Image brightness. (optional)
compression = 'compression_example' # str | Tiff compression. Possible values are: LZW, CCITT4, CCITT3, RLE, None. (optional)
color_depth = 'color_depth_example' # str | Image color depth. Possible valuse are: Default, Format8bpp, Format4bpp, Format1bpp. (optional)
left_margin = 56 # int | Left image margin. (optional)
right_margin = 56 # int | Right image margin. (optional)
top_margin = 56 # int | Top image margin. (optional)
bottom_margin = 56 # int | Bottom image margin. (optional)
orientation = 'orientation_example' # str | Image orientation. Possible values are: None, Landscape, Portait. (optional)
skip_blank_pages = true # bool | Skip blank pages flag. (optional)
width = 56 # int | Image width. (optional)
height = 56 # int | Image height. (optional)
x_resolution = 56 # int | Horizontal resolution. (optional)
y_resolution = 56 # int | Vertical resolution. (optional)
page_index = 56 # int | Start page to export. (optional)
page_count = 56 # int | Number of pages to export. (optional)
storage = 'storage_example' # str | The document storage. (optional)
file = '/path/to/file.txt' # file | A file to be converted. (optional)

try: 
    # Converts PDF document (in request content) to TIFF format and uploads resulting file to storage.
    api_response = api_instance.put_pdf_in_request_to_tiff(out_path, brightness=brightness, compression=compression, color_depth=color_depth, left_margin=left_margin, right_margin=right_margin, top_margin=top_margin, bottom_margin=bottom_margin, orientation=orientation, skip_blank_pages=skip_blank_pages, width=width, height=height, x_resolution=x_resolution, y_resolution=y_resolution, page_index=page_index, page_count=page_count, storage=storage, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_request_to_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.tiff) | 
 **brightness** | **float**| Image brightness. | [optional] 
 **compression** | **str**| Tiff compression. Possible values are: LZW, CCITT4, CCITT3, RLE, None. | [optional] 
 **color_depth** | **str**| Image color depth. Possible valuse are: Default, Format8bpp, Format4bpp, Format1bpp. | [optional] 
 **left_margin** | **int**| Left image margin. | [optional] 
 **right_margin** | **int**| Right image margin. | [optional] 
 **top_margin** | **int**| Top image margin. | [optional] 
 **bottom_margin** | **int**| Bottom image margin. | [optional] 
 **orientation** | **str**| Image orientation. Possible values are: None, Landscape, Portait. | [optional] 
 **skip_blank_pages** | **bool**| Skip blank pages flag. | [optional] 
 **width** | **int**| Image width. | [optional] 
 **height** | **int**| Image height. | [optional] 
 **x_resolution** | **int**| Horizontal resolution. | [optional] 
 **y_resolution** | **int**| Vertical resolution. | [optional] 
 **page_index** | **int**| Start page to export. | [optional] 
 **page_count** | **int**| Number of pages to export. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_xls**
> AsposeResponse put_pdf_in_request_to_xls(out_path, insert_blank_column_at_first=insert_blank_column_at_first, minimize_the_number_of_worksheets=minimize_the_number_of_worksheets, scale_factor=scale_factor, uniform_worksheets=uniform_worksheets, storage=storage, file=file)

Converts PDF document (in request content) to XLS format and uploads resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.xls)
insert_blank_column_at_first = true # bool | Insert blank column at first (optional)
minimize_the_number_of_worksheets = true # bool | Minimize the number of worksheets (optional)
scale_factor = 1.2 # float | Scale factor (optional)
uniform_worksheets = true # bool | Uniform worksheets (optional)
storage = 'storage_example' # str | The document storage. (optional)
file = '/path/to/file.txt' # file | A file to be converted. (optional)

try: 
    # Converts PDF document (in request content) to XLS format and uploads resulting file to storage.
    api_response = api_instance.put_pdf_in_request_to_xls(out_path, insert_blank_column_at_first=insert_blank_column_at_first, minimize_the_number_of_worksheets=minimize_the_number_of_worksheets, scale_factor=scale_factor, uniform_worksheets=uniform_worksheets, storage=storage, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_request_to_xls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.xls) | 
 **insert_blank_column_at_first** | **bool**| Insert blank column at first | [optional] 
 **minimize_the_number_of_worksheets** | **bool**| Minimize the number of worksheets | [optional] 
 **scale_factor** | **float**| Scale factor | [optional] 
 **uniform_worksheets** | **bool**| Uniform worksheets | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_xml**
> AsposeResponse put_pdf_in_request_to_xml(out_path, storage=storage, file=file)

Converts PDF document (in request content) to XML format and uploads resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.xml)
storage = 'storage_example' # str | The document storage. (optional)
file = '/path/to/file.txt' # file | A file to be converted. (optional)

try: 
    # Converts PDF document (in request content) to XML format and uploads resulting file to storage.
    api_response = api_instance.put_pdf_in_request_to_xml(out_path, storage=storage, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_request_to_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.xml) | 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_xps**
> AsposeResponse put_pdf_in_request_to_xps(out_path, storage=storage, file=file)

Converts PDF document (in request content) to XPS format and uploads resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.xps)
storage = 'storage_example' # str | The document storage. (optional)
file = '/path/to/file.txt' # file | A file to be converted. (optional)

try: 
    # Converts PDF document (in request content) to XPS format and uploads resulting file to storage.
    api_response = api_instance.put_pdf_in_request_to_xps(out_path, storage=storage, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_request_to_xps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.xps) | 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_doc**
> AsposeResponse put_pdf_in_storage_to_doc(name, out_path, add_return_to_line_end=add_return_to_line_end, format=format, image_resolution_x=image_resolution_x, image_resolution_y=image_resolution_y, max_distance_between_text_lines=max_distance_between_text_lines, mode=mode, recognize_bullets=recognize_bullets, relative_horizontal_proximity=relative_horizontal_proximity, folder=folder, storage=storage)

Converts PDF document (located on storage) to DOC format and uploads resulting file to storage

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.doc)
add_return_to_line_end = true # bool | Add return to line end. (optional)
format = 'format_example' # str | Allows to specify .doc or .docx file format. (optional)
image_resolution_x = 56 # int | Image resolution X. (optional)
image_resolution_y = 56 # int | Image resolution Y. (optional)
max_distance_between_text_lines = 1.2 # float | Max distance between text lines. (optional)
mode = 'mode_example' # str | Allows to control how a PDF document is converted into a word processing document. (optional)
recognize_bullets = true # bool | Recognize bullets. (optional)
relative_horizontal_proximity = 1.2 # float | Relative horizontal proximity. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to DOC format and uploads resulting file to storage
    api_response = api_instance.put_pdf_in_storage_to_doc(name, out_path, add_return_to_line_end=add_return_to_line_end, format=format, image_resolution_x=image_resolution_x, image_resolution_y=image_resolution_y, max_distance_between_text_lines=max_distance_between_text_lines, mode=mode, recognize_bullets=recognize_bullets, relative_horizontal_proximity=relative_horizontal_proximity, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_storage_to_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.doc) | 
 **add_return_to_line_end** | **bool**| Add return to line end. | [optional] 
 **format** | **str**| Allows to specify .doc or .docx file format. | [optional] 
 **image_resolution_x** | **int**| Image resolution X. | [optional] 
 **image_resolution_y** | **int**| Image resolution Y. | [optional] 
 **max_distance_between_text_lines** | **float**| Max distance between text lines. | [optional] 
 **mode** | **str**| Allows to control how a PDF document is converted into a word processing document. | [optional] 
 **recognize_bullets** | **bool**| Recognize bullets. | [optional] 
 **relative_horizontal_proximity** | **float**| Relative horizontal proximity. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_epub**
> AsposeResponse put_pdf_in_storage_to_epub(name, out_path, content_recognition_mode=content_recognition_mode, folder=folder, storage=storage)

Converts PDF document (located on storage) to EPUB format and uploads resulting file to storage

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.epub)
content_recognition_mode = 'content_recognition_mode_example' # str | ?roperty tunes conversion for this or that desirable method of recognition of content. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to EPUB format and uploads resulting file to storage
    api_response = api_instance.put_pdf_in_storage_to_epub(name, out_path, content_recognition_mode=content_recognition_mode, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_storage_to_epub: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.epub) | 
 **content_recognition_mode** | **str**| ?roperty tunes conversion for this or that desirable method of recognition of content. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_html**
> AsposeResponse put_pdf_in_storage_to_html(name, out_path, additional_margin_width_in_points=additional_margin_width_in_points, compress_svg_graphics_if_any=compress_svg_graphics_if_any, convert_marked_content_to_layers=convert_marked_content_to_layers, default_font_name=default_font_name, document_type=document_type, fixed_layout=fixed_layout, image_resolution=image_resolution, minimal_line_width=minimal_line_width, prevent_glyphs_grouping=prevent_glyphs_grouping, split_css_into_pages=split_css_into_pages, split_into_pages=split_into_pages, use_z_order=use_z_order, antialiasing_processing=antialiasing_processing, css_class_names_prefix=css_class_names_prefix, explicit_list_of_saved_pages=explicit_list_of_saved_pages, font_encoding_strategy=font_encoding_strategy, font_saving_mode=font_saving_mode, html_markup_generation_mode=html_markup_generation_mode, letters_positioning_method=letters_positioning_method, pages_flow_type_depends_on_viewers_screen_size=pages_flow_type_depends_on_viewers_screen_size, parts_embedding_mode=parts_embedding_mode, raster_images_saving_mode=raster_images_saving_mode, remove_empty_areas_on_top_and_bottom=remove_empty_areas_on_top_and_bottom, save_shadowed_texts_as_transparent_texts=save_shadowed_texts_as_transparent_texts, save_transparent_texts=save_transparent_texts, special_folder_for_all_images=special_folder_for_all_images, special_folder_for_svg_images=special_folder_for_svg_images, try_save_text_underlining_and_strikeouting_in_css=try_save_text_underlining_and_strikeouting_in_css, folder=folder, storage=storage)

Converts PDF document (located on storage) to Html format and uploads resulting file to storage

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.html)
additional_margin_width_in_points = 56 # int | Defines width of margin that will be forcibly left around that output HTML-areas. (optional)
compress_svg_graphics_if_any = true # bool | The flag that indicates whether found SVG graphics(if any) will be compressed(zipped) into SVGZ format during saving. (optional)
convert_marked_content_to_layers = true # bool | If attribute ConvertMarkedContentToLayers set to true then an all elements inside a PDF marked content (layer) will be put into an HTML div with \"data-pdflayer\" attribute specifying a layer name. This layer name will be extracted from optional properties of PDF marked content. If this attribute is false (by default) then no any layers will be created from PDF marked content. (optional)
default_font_name = 'default_font_name_example' # str | Specifies the name of an installed font which is used to substitute any document font that is not embedded and not installed in the system. If null then default substitution font is used. (optional)
document_type = 'document_type_example' # str | Result document type. (optional)
fixed_layout = true # bool | The value indicating whether that HTML is created as fixed layout. (optional)
image_resolution = 56 # int | Resolution for image rendering. (optional)
minimal_line_width = 56 # int | This attribute sets minimal width of graphic path line. If thickness of line is less than 1px Adobe Acrobat rounds it to this value. So this attribute can be used to emulate this behavior for HTML browsers. (optional)
prevent_glyphs_grouping = true # bool | This attribute switch on the mode when text glyphs will not be grouped into words and strings This mode allows to keep maximum precision during positioning of glyphs on the page and it can be used for conversion documents with music notes or glyphs that should be placed separately each other. This parameter will be applied to document only when the value of FixedLayout attribute is true. (optional)
split_css_into_pages = true # bool | When multipage-mode selected(i.e 'SplitIntoPages' is 'true'), then this attribute defines whether should be created separate CSS-file for each result HTML page. (optional)
split_into_pages = true # bool | The flag that indicates whether each page of source document will be converted into it's own target HTML document, i.e whether result HTML will be splitted into several HTML-pages. (optional)
use_z_order = true # bool | If attribute UseZORder set to true, graphics and text are added to resultant HTML document accordingly Z-order in original PDF document. If this attribute is false all graphics is put as single layer which may cause some unnecessary effects for overlapped objects. (optional)
antialiasing_processing = 'antialiasing_processing_example' # str | The parameter defines required antialiasing measures during conversion of compound background images from PDF to HTML. (optional)
css_class_names_prefix = 'css_class_names_prefix_example' # str | When PDFtoHTML converter generates result CSSs, CSS class names (something like \".stl_01 {}\" ... \".stl_NN {}) are generated and used in result CSS. This property allows forcibly set class name prefix. (optional)
explicit_list_of_saved_pages = [56] # list[int] | With this property You can explicitely define what pages of document should be converted. Pages in this list must have 1-based numbers. I.e. valid numbers of pages must be taken from range (1...[NumberOfPagesInConvertedDocument]) Order of appearing of pages in this list does not affect their order in result HTML page(s) - in result pages allways will go in order in which they are present in source PDF. (optional)
font_encoding_strategy = 'font_encoding_strategy_example' # str | Defines encoding special rule to tune PDF decoding for current document. (optional)
font_saving_mode = 'font_saving_mode_example' # str | Defines font saving mode that will be used during saving of PDF to desirable format. (optional)
html_markup_generation_mode = 'html_markup_generation_mode_example' # str | Sometimes specific reqirments to generation of HTML markup are present. This parameter defines HTML preparing modes that can be used during conversion of PDF to HTML to match such specific requirments. (optional)
letters_positioning_method = 'letters_positioning_method_example' # str | The mode of positioning of letters in words in result HTML. (optional)
pages_flow_type_depends_on_viewers_screen_size = true # bool | If attribute 'SplitOnPages=false', than whole HTML representing all input PDF pages will be put into one big result HTML file. This flag defines whether result HTML will be generated in such way that flow of areas that represent PDF pages in result HTML will depend on screen resolution of viewer. (optional)
parts_embedding_mode = 'parts_embedding_mode_example' # str | It defines whether referenced files (HTML, Fonts,Images, CSSes) will be embedded into main HTML file or will be generated as apart binary entities. (optional)
raster_images_saving_mode = 'raster_images_saving_mode_example' # str | Converted PDF can contain raster images This parameter defines how they should be handled during conversion of PDF to HTML. (optional)
remove_empty_areas_on_top_and_bottom = true # bool | Defines whether in created HTML will be removed top and bottom empty area without any content (if any). (optional)
save_shadowed_texts_as_transparent_texts = true # bool | Pdf can contain texts that are shadowed by another elements (f.e. by images) but can be selected to clipboard in Acrobat Reader (usually it happen when document contains images and OCRed texts extracted from it). This settings tells to converter whether we need save such texts as transparent selectable texts in result HTML to mimic behaviour of Acrobat Reader (othervise such texts are usually saved as hidden, not available for copying to clipboard). (optional)
save_transparent_texts = true # bool | Pdf can contain transparent texts that can be selected to clipboard (usually it happen when document contains images and OCRed texts extracted from it). This settings tells to converter whether we need save such texts as transparent selectable texts in result HTML. (optional)
special_folder_for_all_images = 'special_folder_for_all_images_example' # str | The path to directory to which must be saved any images if they are encountered during saving of document as HTML. If parameter is empty or null then image files(if any) wil be saved together with other files linked to HTML It does not affect anything if CustomImageSavingStrategy property was successfully used to process relevant image file. (optional)
special_folder_for_svg_images = 'special_folder_for_svg_images_example' # str | The path to directory to which must be saved only SVG-images if they are encountered during saving of document as HTML. If parameter is empty or null then SVG files(if any) wil be saved together with other image-files (near to output file) or in special folder for images (if it specified in SpecialImagesFolderIfAny option). It does not affect anything if CustomImageSavingStrategy property was successfully used to process relevant image file. (optional)
try_save_text_underlining_and_strikeouting_in_css = true # bool | PDF itself does not contain underlining markers for texts. It emulated with line situated under text. This option allows converter try guess that this or that line is a text's underlining and put this info into CSS instead of drawing of underlining graphically. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to Html format and uploads resulting file to storage
    api_response = api_instance.put_pdf_in_storage_to_html(name, out_path, additional_margin_width_in_points=additional_margin_width_in_points, compress_svg_graphics_if_any=compress_svg_graphics_if_any, convert_marked_content_to_layers=convert_marked_content_to_layers, default_font_name=default_font_name, document_type=document_type, fixed_layout=fixed_layout, image_resolution=image_resolution, minimal_line_width=minimal_line_width, prevent_glyphs_grouping=prevent_glyphs_grouping, split_css_into_pages=split_css_into_pages, split_into_pages=split_into_pages, use_z_order=use_z_order, antialiasing_processing=antialiasing_processing, css_class_names_prefix=css_class_names_prefix, explicit_list_of_saved_pages=explicit_list_of_saved_pages, font_encoding_strategy=font_encoding_strategy, font_saving_mode=font_saving_mode, html_markup_generation_mode=html_markup_generation_mode, letters_positioning_method=letters_positioning_method, pages_flow_type_depends_on_viewers_screen_size=pages_flow_type_depends_on_viewers_screen_size, parts_embedding_mode=parts_embedding_mode, raster_images_saving_mode=raster_images_saving_mode, remove_empty_areas_on_top_and_bottom=remove_empty_areas_on_top_and_bottom, save_shadowed_texts_as_transparent_texts=save_shadowed_texts_as_transparent_texts, save_transparent_texts=save_transparent_texts, special_folder_for_all_images=special_folder_for_all_images, special_folder_for_svg_images=special_folder_for_svg_images, try_save_text_underlining_and_strikeouting_in_css=try_save_text_underlining_and_strikeouting_in_css, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_storage_to_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.html) | 
 **additional_margin_width_in_points** | **int**| Defines width of margin that will be forcibly left around that output HTML-areas. | [optional] 
 **compress_svg_graphics_if_any** | **bool**| The flag that indicates whether found SVG graphics(if any) will be compressed(zipped) into SVGZ format during saving. | [optional] 
 **convert_marked_content_to_layers** | **bool**| If attribute ConvertMarkedContentToLayers set to true then an all elements inside a PDF marked content (layer) will be put into an HTML div with \&quot;data-pdflayer\&quot; attribute specifying a layer name. This layer name will be extracted from optional properties of PDF marked content. If this attribute is false (by default) then no any layers will be created from PDF marked content. | [optional] 
 **default_font_name** | **str**| Specifies the name of an installed font which is used to substitute any document font that is not embedded and not installed in the system. If null then default substitution font is used. | [optional] 
 **document_type** | **str**| Result document type. | [optional] 
 **fixed_layout** | **bool**| The value indicating whether that HTML is created as fixed layout. | [optional] 
 **image_resolution** | **int**| Resolution for image rendering. | [optional] 
 **minimal_line_width** | **int**| This attribute sets minimal width of graphic path line. If thickness of line is less than 1px Adobe Acrobat rounds it to this value. So this attribute can be used to emulate this behavior for HTML browsers. | [optional] 
 **prevent_glyphs_grouping** | **bool**| This attribute switch on the mode when text glyphs will not be grouped into words and strings This mode allows to keep maximum precision during positioning of glyphs on the page and it can be used for conversion documents with music notes or glyphs that should be placed separately each other. This parameter will be applied to document only when the value of FixedLayout attribute is true. | [optional] 
 **split_css_into_pages** | **bool**| When multipage-mode selected(i.e &#39;SplitIntoPages&#39; is &#39;true&#39;), then this attribute defines whether should be created separate CSS-file for each result HTML page. | [optional] 
 **split_into_pages** | **bool**| The flag that indicates whether each page of source document will be converted into it&#39;s own target HTML document, i.e whether result HTML will be splitted into several HTML-pages. | [optional] 
 **use_z_order** | **bool**| If attribute UseZORder set to true, graphics and text are added to resultant HTML document accordingly Z-order in original PDF document. If this attribute is false all graphics is put as single layer which may cause some unnecessary effects for overlapped objects. | [optional] 
 **antialiasing_processing** | **str**| The parameter defines required antialiasing measures during conversion of compound background images from PDF to HTML. | [optional] 
 **css_class_names_prefix** | **str**| When PDFtoHTML converter generates result CSSs, CSS class names (something like \&quot;.stl_01 {}\&quot; ... \&quot;.stl_NN {}) are generated and used in result CSS. This property allows forcibly set class name prefix. | [optional] 
 **explicit_list_of_saved_pages** | [**list[int]**](int.md)| With this property You can explicitely define what pages of document should be converted. Pages in this list must have 1-based numbers. I.e. valid numbers of pages must be taken from range (1...[NumberOfPagesInConvertedDocument]) Order of appearing of pages in this list does not affect their order in result HTML page(s) - in result pages allways will go in order in which they are present in source PDF. | [optional] 
 **font_encoding_strategy** | **str**| Defines encoding special rule to tune PDF decoding for current document. | [optional] 
 **font_saving_mode** | **str**| Defines font saving mode that will be used during saving of PDF to desirable format. | [optional] 
 **html_markup_generation_mode** | **str**| Sometimes specific reqirments to generation of HTML markup are present. This parameter defines HTML preparing modes that can be used during conversion of PDF to HTML to match such specific requirments. | [optional] 
 **letters_positioning_method** | **str**| The mode of positioning of letters in words in result HTML. | [optional] 
 **pages_flow_type_depends_on_viewers_screen_size** | **bool**| If attribute &#39;SplitOnPages&#x3D;false&#39;, than whole HTML representing all input PDF pages will be put into one big result HTML file. This flag defines whether result HTML will be generated in such way that flow of areas that represent PDF pages in result HTML will depend on screen resolution of viewer. | [optional] 
 **parts_embedding_mode** | **str**| It defines whether referenced files (HTML, Fonts,Images, CSSes) will be embedded into main HTML file or will be generated as apart binary entities. | [optional] 
 **raster_images_saving_mode** | **str**| Converted PDF can contain raster images This parameter defines how they should be handled during conversion of PDF to HTML. | [optional] 
 **remove_empty_areas_on_top_and_bottom** | **bool**| Defines whether in created HTML will be removed top and bottom empty area without any content (if any). | [optional] 
 **save_shadowed_texts_as_transparent_texts** | **bool**| Pdf can contain texts that are shadowed by another elements (f.e. by images) but can be selected to clipboard in Acrobat Reader (usually it happen when document contains images and OCRed texts extracted from it). This settings tells to converter whether we need save such texts as transparent selectable texts in result HTML to mimic behaviour of Acrobat Reader (othervise such texts are usually saved as hidden, not available for copying to clipboard). | [optional] 
 **save_transparent_texts** | **bool**| Pdf can contain transparent texts that can be selected to clipboard (usually it happen when document contains images and OCRed texts extracted from it). This settings tells to converter whether we need save such texts as transparent selectable texts in result HTML. | [optional] 
 **special_folder_for_all_images** | **str**| The path to directory to which must be saved any images if they are encountered during saving of document as HTML. If parameter is empty or null then image files(if any) wil be saved together with other files linked to HTML It does not affect anything if CustomImageSavingStrategy property was successfully used to process relevant image file. | [optional] 
 **special_folder_for_svg_images** | **str**| The path to directory to which must be saved only SVG-images if they are encountered during saving of document as HTML. If parameter is empty or null then SVG files(if any) wil be saved together with other image-files (near to output file) or in special folder for images (if it specified in SpecialImagesFolderIfAny option). It does not affect anything if CustomImageSavingStrategy property was successfully used to process relevant image file. | [optional] 
 **try_save_text_underlining_and_strikeouting_in_css** | **bool**| PDF itself does not contain underlining markers for texts. It emulated with line situated under text. This option allows converter try guess that this or that line is a text&#39;s underlining and put this info into CSS instead of drawing of underlining graphically. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_la_te_x**
> AsposeResponse put_pdf_in_storage_to_la_te_x(name, out_path, pages_count=pages_count, folder=folder, storage=storage)

Converts PDF document (located on storage) to LaTeX format and uploads resulting file to storage

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.tex)
pages_count = 56 # int | Pages count. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to LaTeX format and uploads resulting file to storage
    api_response = api_instance.put_pdf_in_storage_to_la_te_x(name, out_path, pages_count=pages_count, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_storage_to_la_te_x: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.tex) | 
 **pages_count** | **int**| Pages count. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_mobi_xml**
> AsposeResponse put_pdf_in_storage_to_mobi_xml(name, out_path, folder=folder, storage=storage)

Converts PDF document (located on storage) to MOBIXML format and uploads resulting file to storage

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.mobixml)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to MOBIXML format and uploads resulting file to storage
    api_response = api_instance.put_pdf_in_storage_to_mobi_xml(name, out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_storage_to_mobi_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.mobixml) | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_pdf_a**
> AsposeResponse put_pdf_in_storage_to_pdf_a(name, out_path, type, folder=folder, storage=storage)

Converts PDF document (located on storage) to PdfA format and uploads resulting file to storage

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.pdf)
type = 'type_example' # str | Type of PdfA format.
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to PdfA format and uploads resulting file to storage
    api_response = api_instance.put_pdf_in_storage_to_pdf_a(name, out_path, type, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_storage_to_pdf_a: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.pdf) | 
 **type** | **str**| Type of PdfA format. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_pptx**
> AsposeResponse put_pdf_in_storage_to_pptx(name, out_path, separate_images=separate_images, slides_as_images=slides_as_images, folder=folder, storage=storage)

Converts PDF document (located on storage) to PPTX format and uploads resulting file to storage

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.pptx)
separate_images = true # bool | Separate images. (optional)
slides_as_images = true # bool | Slides as images. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to PPTX format and uploads resulting file to storage
    api_response = api_instance.put_pdf_in_storage_to_pptx(name, out_path, separate_images=separate_images, slides_as_images=slides_as_images, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_storage_to_pptx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.pptx) | 
 **separate_images** | **bool**| Separate images. | [optional] 
 **slides_as_images** | **bool**| Slides as images. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_svg**
> AsposeResponse put_pdf_in_storage_to_svg(name, out_path, folder=folder, storage=storage)

Converts PDF document (located on storage) to SVG format and uploads resulting file to storage

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.svg)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to SVG format and uploads resulting file to storage
    api_response = api_instance.put_pdf_in_storage_to_svg(name, out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_storage_to_svg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.svg) | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_tiff**
> AsposeResponse put_pdf_in_storage_to_tiff(name, out_path, brightness=brightness, compression=compression, color_depth=color_depth, left_margin=left_margin, right_margin=right_margin, top_margin=top_margin, bottom_margin=bottom_margin, orientation=orientation, skip_blank_pages=skip_blank_pages, width=width, height=height, x_resolution=x_resolution, y_resolution=y_resolution, page_index=page_index, page_count=page_count, folder=folder, storage=storage)

Converts PDF document (located on storage) to TIFF format and uploads resulting file to storage

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.tiff)
brightness = 1.2 # float | Image brightness. (optional)
compression = 'compression_example' # str | Tiff compression. Possible values are: LZW, CCITT4, CCITT3, RLE, None. (optional)
color_depth = 'color_depth_example' # str | Image color depth. Possible valuse are: Default, Format8bpp, Format4bpp, Format1bpp. (optional)
left_margin = 56 # int | Left image margin. (optional)
right_margin = 56 # int | Right image margin. (optional)
top_margin = 56 # int | Top image margin. (optional)
bottom_margin = 56 # int | Bottom image margin. (optional)
orientation = 'orientation_example' # str | Image orientation. Possible values are: None, Landscape, Portait. (optional)
skip_blank_pages = true # bool | Skip blank pages flag. (optional)
width = 56 # int | Image width. (optional)
height = 56 # int | Image height. (optional)
x_resolution = 56 # int | Horizontal resolution. (optional)
y_resolution = 56 # int | Vertical resolution. (optional)
page_index = 56 # int | Start page to export. (optional)
page_count = 56 # int | Number of pages to export. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to TIFF format and uploads resulting file to storage
    api_response = api_instance.put_pdf_in_storage_to_tiff(name, out_path, brightness=brightness, compression=compression, color_depth=color_depth, left_margin=left_margin, right_margin=right_margin, top_margin=top_margin, bottom_margin=bottom_margin, orientation=orientation, skip_blank_pages=skip_blank_pages, width=width, height=height, x_resolution=x_resolution, y_resolution=y_resolution, page_index=page_index, page_count=page_count, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_storage_to_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.tiff) | 
 **brightness** | **float**| Image brightness. | [optional] 
 **compression** | **str**| Tiff compression. Possible values are: LZW, CCITT4, CCITT3, RLE, None. | [optional] 
 **color_depth** | **str**| Image color depth. Possible valuse are: Default, Format8bpp, Format4bpp, Format1bpp. | [optional] 
 **left_margin** | **int**| Left image margin. | [optional] 
 **right_margin** | **int**| Right image margin. | [optional] 
 **top_margin** | **int**| Top image margin. | [optional] 
 **bottom_margin** | **int**| Bottom image margin. | [optional] 
 **orientation** | **str**| Image orientation. Possible values are: None, Landscape, Portait. | [optional] 
 **skip_blank_pages** | **bool**| Skip blank pages flag. | [optional] 
 **width** | **int**| Image width. | [optional] 
 **height** | **int**| Image height. | [optional] 
 **x_resolution** | **int**| Horizontal resolution. | [optional] 
 **y_resolution** | **int**| Vertical resolution. | [optional] 
 **page_index** | **int**| Start page to export. | [optional] 
 **page_count** | **int**| Number of pages to export. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_xls**
> AsposeResponse put_pdf_in_storage_to_xls(name, out_path, insert_blank_column_at_first=insert_blank_column_at_first, minimize_the_number_of_worksheets=minimize_the_number_of_worksheets, scale_factor=scale_factor, uniform_worksheets=uniform_worksheets, folder=folder, storage=storage)

Converts PDF document (located on storage) to XLS format and uploads resulting file to storage

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.xls)
insert_blank_column_at_first = true # bool | Insert blank column at first (optional)
minimize_the_number_of_worksheets = true # bool | Minimize the number of worksheets (optional)
scale_factor = 1.2 # float | Scale factor (optional)
uniform_worksheets = true # bool | Uniform worksheets (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to XLS format and uploads resulting file to storage
    api_response = api_instance.put_pdf_in_storage_to_xls(name, out_path, insert_blank_column_at_first=insert_blank_column_at_first, minimize_the_number_of_worksheets=minimize_the_number_of_worksheets, scale_factor=scale_factor, uniform_worksheets=uniform_worksheets, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_storage_to_xls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.xls) | 
 **insert_blank_column_at_first** | **bool**| Insert blank column at first | [optional] 
 **minimize_the_number_of_worksheets** | **bool**| Minimize the number of worksheets | [optional] 
 **scale_factor** | **float**| Scale factor | [optional] 
 **uniform_worksheets** | **bool**| Uniform worksheets | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_xml**
> AsposeResponse put_pdf_in_storage_to_xml(name, out_path, folder=folder, storage=storage)

Converts PDF document (located on storage) to XML format and uploads resulting file to storage

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.xml)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to XML format and uploads resulting file to storage
    api_response = api_instance.put_pdf_in_storage_to_xml(name, out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_storage_to_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.xml) | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_xps**
> AsposeResponse put_pdf_in_storage_to_xps(name, out_path, folder=folder, storage=storage)

Converts PDF document (located on storage) to XPS format and uploads resulting file to storage

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.xps)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document (located on storage) to XPS format and uploads resulting file to storage
    api_response = api_instance.put_pdf_in_storage_to_xps(name, out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_pdf_in_storage_to_xps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.xps) | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_privileges**
> AsposeResponse put_privileges(name, privileges=privileges, storage=storage, folder=folder)

Update privilege document.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
privileges = swagger_client.DocumentPrivilege() # DocumentPrivilege | Document privileges.  (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Update privilege document.
    api_response = api_instance.put_privileges(name, privileges=privileges, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **privileges** | [**DocumentPrivilege**](DocumentPrivilege.md)| Document privileges.  | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ps_in_storage_to_pdf**
> AsposeResponse put_ps_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)

Convert PS file (located on storage) to PDF format and upload resulting file to storage. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.ps)
dst_folder = 'dst_folder_example' # str | The destination document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert PS file (located on storage) to PDF format and upload resulting file to storage. 
    api_response = api_instance.put_ps_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_ps_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.ps) | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_replace_image**
> ImageResponse put_replace_image(name, image_id, image_file_path=image_file_path, storage=storage, folder=folder, image=image)

Replace document image.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
image_id = 'image_id_example' # str | The image ID.
image_file_path = 'image_file_path_example' # str | Path to image file if specified. Request content is used otherwise. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
image = '/path/to/file.txt' # file | Image file. (optional)

try: 
    # Replace document image.
    api_response = api_instance.put_replace_image(name, image_id, image_file_path=image_file_path, storage=storage, folder=folder, image=image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_replace_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| The image ID. | 
 **image_file_path** | **str**| Path to image file if specified. Request content is used otherwise. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **image** | **file**| Image file. | [optional] 

### Return type

[**ImageResponse**](ImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_searchable_document**
> AsposeResponse put_searchable_document(name, storage=storage, folder=folder, lang=lang)

Create searchable PDF document. Generate OCR layer for images in input PDF document.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
lang = 'lang_example' # str | language for OCR engine. Possible values: eng, ara, bel, ben, bul, ces, dan, deu, ell, fin, fra, heb, hin, ind, isl, ita, jpn, kor, nld, nor, pol, por, ron, rus, spa, swe, tha, tur, ukr, vie, chi_sim, chi_tra or thier combination e.g. eng,rus  (optional)

try: 
    # Create searchable PDF document. Generate OCR layer for images in input PDF document.
    api_response = api_instance.put_searchable_document(name, storage=storage, folder=folder, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_searchable_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **lang** | **str**| language for OCR engine. Possible values: eng, ara, bel, ben, bul, ces, dan, deu, ell, fin, fra, heb, hin, ind, isl, ita, jpn, kor, nld, nor, pol, por, ron, rus, spa, swe, tha, tur, ukr, vie, chi_sim, chi_tra or thier combination e.g. eng,rus  | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_set_property**
> DocumentPropertyResponse put_set_property(name, property_name, value, storage=storage, folder=folder)

Add/update document property.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | 
property_name = 'property_name_example' # str | 
value = 'value_example' # str | 
storage = 'storage_example' # str |  (optional)
folder = 'folder_example' # str |  (optional)

try: 
    # Add/update document property.
    api_response = api_instance.put_set_property(name, property_name, value, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_set_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **property_name** | **str**|  | 
 **value** | **str**|  | 
 **storage** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**DocumentPropertyResponse**](DocumentPropertyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_svg_in_storage_to_pdf**
> AsposeResponse put_svg_in_storage_to_pdf(name, src_path, adjust_page_size=adjust_page_size, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, dst_folder=dst_folder, storage=storage)

Convert SVG file (located on storage) to PDF format and upload resulting file to storage. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.svg)
adjust_page_size = true # bool | Adjust page size (optional)
height = 1.2 # float | Page height (optional)
width = 1.2 # float | Page width (optional)
is_landscape = true # bool | Is page landscaped (optional)
margin_left = 1.2 # float | Page margin left (optional)
margin_bottom = 1.2 # float | Page margin bottom (optional)
margin_right = 1.2 # float | Page margin right (optional)
margin_top = 1.2 # float | Page margin top (optional)
dst_folder = 'dst_folder_example' # str | The destination document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert SVG file (located on storage) to PDF format and upload resulting file to storage. 
    api_response = api_instance.put_svg_in_storage_to_pdf(name, src_path, adjust_page_size=adjust_page_size, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, dst_folder=dst_folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_svg_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.svg) | 
 **adjust_page_size** | **bool**| Adjust page size | [optional] 
 **height** | **float**| Page height | [optional] 
 **width** | **float**| Page width | [optional] 
 **is_landscape** | **bool**| Is page landscaped | [optional] 
 **margin_left** | **float**| Page margin left | [optional] 
 **margin_bottom** | **float**| Page margin bottom | [optional] 
 **margin_right** | **float**| Page margin right | [optional] 
 **margin_top** | **float**| Page margin top | [optional] 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_text_annotation**
> TextAnnotationResponse put_text_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document text annotation

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
annotation_id = 'annotation_id_example' # str | The annotation ID.
annotation = swagger_client.TextAnnotation() # TextAnnotation | Annotation.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Replace document text annotation
    api_response = api_instance.put_text_annotation(name, annotation_id, annotation, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_text_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**TextAnnotation**](TextAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TextAnnotationResponse**](TextAnnotationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_field**
> FieldResponse put_update_field(name, field_name, field=field, storage=storage, folder=folder)

Update field.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
field_name = 'field_name_example' # str | The name of a field to be updated.
field = swagger_client.Field() # Field | with the field data. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Update field.
    api_response = api_instance.put_update_field(name, field_name, field=field, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_update_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The name of a field to be updated. | 
 **field** | [**Field**](Field.md)| with the field data. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FieldResponse**](FieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_fields**
> FieldsResponse put_update_fields(name, fields=fields, storage=storage, folder=folder)

Update fields.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
fields = swagger_client.Fields() # Fields | with the fields data. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try: 
    # Update fields.
    api_response = api_instance.put_update_fields(name, fields=fields, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_update_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **fields** | [**Fields**](Fields.md)| with the fields data. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FieldsResponse**](FieldsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_web_in_storage_to_pdf**
> AsposeResponse put_web_in_storage_to_pdf(name, url, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, dst_folder=dst_folder, storage=storage)

Convert web page to PDF format and upload resulting file to storage. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
url = 'url_example' # str | Source url
height = 1.2 # float | Page height (optional)
width = 1.2 # float | Page width (optional)
is_landscape = true # bool | Is page landscaped (optional)
margin_left = 1.2 # float | Page margin left (optional)
margin_bottom = 1.2 # float | Page margin bottom (optional)
margin_right = 1.2 # float | Page margin right (optional)
margin_top = 1.2 # float | Page margin top (optional)
dst_folder = 'dst_folder_example' # str | The destination document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert web page to PDF format and upload resulting file to storage. 
    api_response = api_instance.put_web_in_storage_to_pdf(name, url, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, dst_folder=dst_folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_web_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **url** | **str**| Source url | 
 **height** | **float**| Page height | [optional] 
 **width** | **float**| Page width | [optional] 
 **is_landscape** | **bool**| Is page landscaped | [optional] 
 **margin_left** | **float**| Page margin left | [optional] 
 **margin_bottom** | **float**| Page margin bottom | [optional] 
 **margin_right** | **float**| Page margin right | [optional] 
 **margin_top** | **float**| Page margin top | [optional] 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_xfa_pdf_in_request_to_acro_form**
> AsposeResponse put_xfa_pdf_in_request_to_acro_form(out_path, storage=storage, file=file)

Converts PDF document which contatins XFA form (in request content) to PDF with AcroForm and uploads resulting file to storage.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.pdf)
storage = 'storage_example' # str | The document storage. (optional)
file = '/path/to/file.txt' # file | A file to be converted. (optional)

try: 
    # Converts PDF document which contatins XFA form (in request content) to PDF with AcroForm and uploads resulting file to storage.
    api_response = api_instance.put_xfa_pdf_in_request_to_acro_form(out_path, storage=storage, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_xfa_pdf_in_request_to_acro_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.pdf) | 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_xfa_pdf_in_storage_to_acro_form**
> AsposeResponse put_xfa_pdf_in_storage_to_acro_form(name, out_path, folder=folder, storage=storage)

Converts PDF document which contatins XFA form (located on storage) to PDF with AcroForm and uploads resulting file to storage

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
out_path = 'out_path_example' # str | Full resulting filename (ex. /folder1/folder2/result.pdf)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Converts PDF document which contatins XFA form (located on storage) to PDF with AcroForm and uploads resulting file to storage
    api_response = api_instance.put_xfa_pdf_in_storage_to_acro_form(name, out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_xfa_pdf_in_storage_to_acro_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.pdf) | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_xml_in_storage_to_pdf**
> AsposeResponse put_xml_in_storage_to_pdf(name, src_path, xsl_file_path=xsl_file_path, dst_folder=dst_folder, storage=storage)

Convert XML file (located on storage) to PDF format and upload resulting file to storage. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.xml)
xsl_file_path = 'xsl_file_path_example' # str | Full XSL source filename (ex. /folder1/folder2/template.xsl) (optional)
dst_folder = 'dst_folder_example' # str | The destination document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert XML file (located on storage) to PDF format and upload resulting file to storage. 
    api_response = api_instance.put_xml_in_storage_to_pdf(name, src_path, xsl_file_path=xsl_file_path, dst_folder=dst_folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_xml_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.xml) | 
 **xsl_file_path** | **str**| Full XSL source filename (ex. /folder1/folder2/template.xsl) | [optional] 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_xps_in_storage_to_pdf**
> AsposeResponse put_xps_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)

Convert XPS file (located on storage) to PDF format and upload resulting file to storage. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.xps)
dst_folder = 'dst_folder_example' # str | The destination document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert XPS file (located on storage) to PDF format and upload resulting file to storage. 
    api_response = api_instance.put_xps_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_xps_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.xps) | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_xsl_fo_in_storage_to_pdf**
> AsposeResponse put_xsl_fo_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)

Convert XslFo file (located on storage) to PDF format and upload resulting file to storage. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PdfApi()
name = 'name_example' # str | The document name.
src_path = 'src_path_example' # str | Full source filename (ex. /folder1/folder2/template.xpsfo)
dst_folder = 'dst_folder_example' # str | The destination document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try: 
    # Convert XslFo file (located on storage) to PDF format and upload resulting file to storage. 
    api_response = api_instance.put_xsl_fo_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PdfApi->put_xsl_fo_in_storage_to_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.xpsfo) | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

