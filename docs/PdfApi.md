# swagger_client.PdfApi

All URIs are relative to *https://api.aspose.cloud/v3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_file**](PdfApi.md#copy_file) | **PUT** /pdf/storage/file/copy/\{srcPath} | Copy file
[**copy_folder**](PdfApi.md#copy_folder) | **PUT** /pdf/storage/folder/copy/\{srcPath} | Copy folder
[**create_folder**](PdfApi.md#create_folder) | **PUT** /pdf/storage/folder/\{path} | Create the folder
[**delete_annotation**](PdfApi.md#delete_annotation) | **DELETE** /pdf/\{name}/annotations/\{annotationId} | Delete document annotation by ID
[**delete_bookmark**](PdfApi.md#delete_bookmark) | **DELETE** /pdf/\{name}/bookmarks/bookmark/\{bookmarkPath} | Delete document bookmark by ID.
[**delete_document_annotations**](PdfApi.md#delete_document_annotations) | **DELETE** /pdf/\{name}/annotations | Delete all annotations from the document
[**delete_document_bookmarks**](PdfApi.md#delete_document_bookmarks) | **DELETE** /pdf/\{name}/bookmarks/tree | Delete all document bookmarks.
[**delete_document_layer**](PdfApi.md#delete_document_layer) | **DELETE** /pdf/\{name}/layers | Remove document layer.
[**delete_document_link_annotations**](PdfApi.md#delete_document_link_annotations) | **DELETE** /pdf/\{name}/links | Delete all link annotations from the document
[**delete_document_stamps**](PdfApi.md#delete_document_stamps) | **DELETE** /pdf/\{name}/stamps | Delete all stamps from the document
[**delete_document_tables**](PdfApi.md#delete_document_tables) | **DELETE** /pdf/\{name}/tables | Delete all tables from the document
[**delete_field**](PdfApi.md#delete_field) | **DELETE** /pdf/\{name}/fields/\{fieldName} | Delete document field by name.
[**delete_file**](PdfApi.md#delete_file) | **DELETE** /pdf/storage/file/\{path} | Delete file
[**delete_folder**](PdfApi.md#delete_folder) | **DELETE** /pdf/storage/folder/\{path} | Delete folder
[**delete_image**](PdfApi.md#delete_image) | **DELETE** /pdf/\{name}/images/\{imageId} | Delete image from document page.
[**delete_link_annotation**](PdfApi.md#delete_link_annotation) | **DELETE** /pdf/\{name}/links/\{linkId} | Delete document page link annotation by ID
[**delete_page**](PdfApi.md#delete_page) | **DELETE** /pdf/\{name}/pages/\{pageNumber} | Delete document page by its number.
[**delete_page_annotations**](PdfApi.md#delete_page_annotations) | **DELETE** /pdf/\{name}/pages/\{pageNumber}/annotations | Delete all annotations from the page
[**delete_page_link_annotations**](PdfApi.md#delete_page_link_annotations) | **DELETE** /pdf/\{name}/pages/\{pageNumber}/links | Delete all link annotations from the page
[**delete_page_stamps**](PdfApi.md#delete_page_stamps) | **DELETE** /pdf/\{name}/pages/\{pageNumber}/stamps | Delete all stamps from the page
[**delete_page_tables**](PdfApi.md#delete_page_tables) | **DELETE** /pdf/\{name}/pages/\{pageNumber}/tables | Delete all tables from the page
[**delete_properties**](PdfApi.md#delete_properties) | **DELETE** /pdf/\{name}/documentproperties | Delete custom document properties.
[**delete_property**](PdfApi.md#delete_property) | **DELETE** /pdf/\{name}/documentproperties/\{propertyName} | Delete document property.
[**delete_stamp**](PdfApi.md#delete_stamp) | **DELETE** /pdf/\{name}/stamps/\{stampId} | Delete document stamp by ID
[**delete_table**](PdfApi.md#delete_table) | **DELETE** /pdf/\{name}/tables/\{tableId} | Delete document table by ID
[**download_file**](PdfApi.md#download_file) | **GET** /pdf/storage/file/\{path} | Download file
[**get_bookmark**](PdfApi.md#get_bookmark) | **GET** /pdf/\{name}/bookmarks/bookmark/\{bookmarkPath} | Read document bookmark.
[**get_bookmarks**](PdfApi.md#get_bookmarks) | **GET** /pdf/\{name}/bookmarks/list/\{bookmarkPath} | Read document bookmarks node list.
[**get_caret_annotation**](PdfApi.md#get_caret_annotation) | **GET** /pdf/\{name}/annotations/caret/\{annotationId} | Read document page caret annotation by ID.
[**get_check_box_field**](PdfApi.md#get_check_box_field) | **GET** /pdf/\{name}/fields/checkbox/\{fieldName} | Read document checkbox field by name.
[**get_circle_annotation**](PdfApi.md#get_circle_annotation) | **GET** /pdf/\{name}/annotations/circle/\{annotationId} | Read document page circle annotation by ID.
[**get_combo_box_field**](PdfApi.md#get_combo_box_field) | **GET** /pdf/\{name}/fields/combobox/\{fieldName} | Read document combobox field by name.
[**get_disc_usage**](PdfApi.md#get_disc_usage) | **GET** /pdf/storage/disc | Get disc usage
[**get_document**](PdfApi.md#get_document) | **GET** /pdf/\{name} | Read common document info.
[**get_document_annotations**](PdfApi.md#get_document_annotations) | **GET** /pdf/\{name}/annotations | Read document page annotations. Returns only FreeTextAnnotations, TextAnnotations, other annotations will implemented next releases.
[**get_document_attachment_by_index**](PdfApi.md#get_document_attachment_by_index) | **GET** /pdf/\{name}/attachments/\{attachmentIndex} | Read document attachment info by its index.
[**get_document_attachments**](PdfApi.md#get_document_attachments) | **GET** /pdf/\{name}/attachments | Read document attachments info.
[**get_document_bookmarks**](PdfApi.md#get_document_bookmarks) | **GET** /pdf/\{name}/bookmarks/tree | Read document bookmarks tree.
[**get_document_caret_annotations**](PdfApi.md#get_document_caret_annotations) | **GET** /pdf/\{name}/annotations/caret | Read document caret annotations.
[**get_document_check_box_fields**](PdfApi.md#get_document_check_box_fields) | **GET** /pdf/\{name}/fields/checkbox | Read document checkbox fields.
[**get_document_circle_annotations**](PdfApi.md#get_document_circle_annotations) | **GET** /pdf/\{name}/annotations/circle | Read document circle annotations.
[**get_document_combo_box_fields**](PdfApi.md#get_document_combo_box_fields) | **GET** /pdf/\{name}/fields/combobox | Read document combobox fields.
[**get_document_display_properties**](PdfApi.md#get_document_display_properties) | **GET** /pdf/\{name}/displayproperties | Read document display properties.
[**get_document_file_attachment_annotations**](PdfApi.md#get_document_file_attachment_annotations) | **GET** /pdf/\{name}/annotations/fileattachment | Read document FileAttachment annotations.
[**get_document_free_text_annotations**](PdfApi.md#get_document_free_text_annotations) | **GET** /pdf/\{name}/annotations/freetext | Read document free text annotations.
[**get_document_highlight_annotations**](PdfApi.md#get_document_highlight_annotations) | **GET** /pdf/\{name}/annotations/highlight | Read document highlight annotations.
[**get_document_ink_annotations**](PdfApi.md#get_document_ink_annotations) | **GET** /pdf/\{name}/annotations/ink | Read document ink annotations.
[**get_document_layers**](PdfApi.md#get_document_layers) | **GET** /pdf/\{name}/layers | Gets document layers.
[**get_document_line_annotations**](PdfApi.md#get_document_line_annotations) | **GET** /pdf/\{name}/annotations/line | Read document line annotations.
[**get_document_list_box_fields**](PdfApi.md#get_document_list_box_fields) | **GET** /pdf/\{name}/fields/listbox | Read document listbox fields.
[**get_document_movie_annotations**](PdfApi.md#get_document_movie_annotations) | **GET** /pdf/\{name}/annotations/movie | Read document movie annotations.
[**get_document_poly_line_annotations**](PdfApi.md#get_document_poly_line_annotations) | **GET** /pdf/\{name}/annotations/polyline | Read document polyline annotations.
[**get_document_polygon_annotations**](PdfApi.md#get_document_polygon_annotations) | **GET** /pdf/\{name}/annotations/polygon | Read document polygon annotations.
[**get_document_popup_annotations**](PdfApi.md#get_document_popup_annotations) | **GET** /pdf/\{name}/annotations/popup | Read document popup annotations.
[**get_document_popup_annotations_by_parent**](PdfApi.md#get_document_popup_annotations_by_parent) | **GET** /pdf/\{name}/annotations/\{annotationId}/popup | Read document popup annotations by parent id.
[**get_document_properties**](PdfApi.md#get_document_properties) | **GET** /pdf/\{name}/documentproperties | Read document properties.
[**get_document_property**](PdfApi.md#get_document_property) | **GET** /pdf/\{name}/documentproperties/\{propertyName} | Read document property by name.
[**get_document_radio_button_fields**](PdfApi.md#get_document_radio_button_fields) | **GET** /pdf/\{name}/fields/radiobutton | Read document radiobutton fields.
[**get_document_redaction_annotations**](PdfApi.md#get_document_redaction_annotations) | **GET** /pdf/\{name}/annotations/redaction | Read document redaction annotations.
[**get_document_screen_annotations**](PdfApi.md#get_document_screen_annotations) | **GET** /pdf/\{name}/annotations/screen | Read document screen annotations.
[**get_document_signature_fields**](PdfApi.md#get_document_signature_fields) | **GET** /pdf/\{name}/fields/signature | Read document signature fields.
[**get_document_sound_annotations**](PdfApi.md#get_document_sound_annotations) | **GET** /pdf/\{name}/annotations/sound | Read document sound annotations.
[**get_document_square_annotations**](PdfApi.md#get_document_square_annotations) | **GET** /pdf/\{name}/annotations/square | Read document square annotations.
[**get_document_squiggly_annotations**](PdfApi.md#get_document_squiggly_annotations) | **GET** /pdf/\{name}/annotations/squiggly | Read document squiggly annotations.
[**get_document_stamp_annotations**](PdfApi.md#get_document_stamp_annotations) | **GET** /pdf/\{name}/annotations/stamp | Read document stamp annotations.
[**get_document_stamps**](PdfApi.md#get_document_stamps) | **GET** /pdf/\{name}/stamps | Read document stamps.
[**get_document_strike_out_annotations**](PdfApi.md#get_document_strike_out_annotations) | **GET** /pdf/\{name}/annotations/strikeout | Read document StrikeOut annotations.
[**get_document_tables**](PdfApi.md#get_document_tables) | **GET** /pdf/\{name}/tables | Read document tables.
[**get_document_text_annotations**](PdfApi.md#get_document_text_annotations) | **GET** /pdf/\{name}/annotations/text | Read document text annotations.
[**get_document_text_box_fields**](PdfApi.md#get_document_text_box_fields) | **GET** /pdf/\{name}/fields/textbox | Read document text box fields.
[**get_document_underline_annotations**](PdfApi.md#get_document_underline_annotations) | **GET** /pdf/\{name}/annotations/underline | Read document underline annotations.
[**get_download_document_attachment_by_index**](PdfApi.md#get_download_document_attachment_by_index) | **GET** /pdf/\{name}/attachments/\{attachmentIndex}/download | Download document attachment content by its index.
[**get_epub_in_storage_to_pdf**](PdfApi.md#get_epub_in_storage_to_pdf) | **GET** /pdf/create/epub | Convert EPUB file (located on storage) to PDF format and return resulting file in response. 
[**get_export_fields_from_pdf_to_fdf_in_storage**](PdfApi.md#get_export_fields_from_pdf_to_fdf_in_storage) | **GET** /pdf/\{name}/export/fdf | Export fields from from PDF in storage to FDF file.
[**get_export_fields_from_pdf_to_xfdf_in_storage**](PdfApi.md#get_export_fields_from_pdf_to_xfdf_in_storage) | **GET** /pdf/\{name}/export/xfdf | Export fields from from PDF in storage to XFDF file.
[**get_export_fields_from_pdf_to_xml_in_storage**](PdfApi.md#get_export_fields_from_pdf_to_xml_in_storage) | **GET** /pdf/\{name}/export/xml | Export fields from from PDF in storage to XML file.
[**get_field**](PdfApi.md#get_field) | **GET** /pdf/\{name}/fields/\{fieldName} | Get document field by name.
[**get_fields**](PdfApi.md#get_fields) | **GET** /pdf/\{name}/fields | Get document fields.
[**get_file_attachment_annotation**](PdfApi.md#get_file_attachment_annotation) | **GET** /pdf/\{name}/annotations/fileattachment/\{annotationId} | Read document page FileAttachment annotation by ID.
[**get_file_attachment_annotation_data**](PdfApi.md#get_file_attachment_annotation_data) | **GET** /pdf/\{name}/annotations/fileattachment/\{annotationId}/data | Read document page FileAttachment annotation by ID.
[**get_file_versions**](PdfApi.md#get_file_versions) | **GET** /pdf/storage/version/\{path} | Get file versions
[**get_files_list**](PdfApi.md#get_files_list) | **GET** /pdf/storage/folder/\{path} | Get all files and folders within a folder
[**get_free_text_annotation**](PdfApi.md#get_free_text_annotation) | **GET** /pdf/\{name}/annotations/freetext/\{annotationId} | Read document page free text annotation by ID.
[**get_highlight_annotation**](PdfApi.md#get_highlight_annotation) | **GET** /pdf/\{name}/annotations/highlight/\{annotationId} | Read document page highlight annotation by ID.
[**get_html_in_storage_to_pdf**](PdfApi.md#get_html_in_storage_to_pdf) | **GET** /pdf/create/html | Convert HTML file (located on storage) to PDF format and return resulting file in response. 
[**get_image**](PdfApi.md#get_image) | **GET** /pdf/\{name}/images/\{imageId} | Read document image by ID.
[**get_image_extract_as_gif**](PdfApi.md#get_image_extract_as_gif) | **GET** /pdf/\{name}/images/\{imageId}/extract/gif | Extract document image in GIF format
[**get_image_extract_as_jpeg**](PdfApi.md#get_image_extract_as_jpeg) | **GET** /pdf/\{name}/images/\{imageId}/extract/jpeg | Extract document image in JPEG format
[**get_image_extract_as_png**](PdfApi.md#get_image_extract_as_png) | **GET** /pdf/\{name}/images/\{imageId}/extract/png | Extract document image in PNG format
[**get_image_extract_as_tiff**](PdfApi.md#get_image_extract_as_tiff) | **GET** /pdf/\{name}/images/\{imageId}/extract/tiff | Extract document image in TIFF format
[**get_images**](PdfApi.md#get_images) | **GET** /pdf/\{name}/pages/\{pageNumber}/images | Read document images.
[**get_import_fields_from_fdf_in_storage**](PdfApi.md#get_import_fields_from_fdf_in_storage) | **GET** /pdf/\{name}/import/fdf | Update fields from FDF file in storage.
[**get_import_fields_from_xfdf_in_storage**](PdfApi.md#get_import_fields_from_xfdf_in_storage) | **GET** /pdf/\{name}/import/xfdf | Update fields from XFDF file in storage.
[**get_import_fields_from_xml_in_storage**](PdfApi.md#get_import_fields_from_xml_in_storage) | **GET** /pdf/\{name}/import/xml | Import from XML file (located on storage) to PDF format and return resulting file in response. 
[**get_ink_annotation**](PdfApi.md#get_ink_annotation) | **GET** /pdf/\{name}/annotations/ink/\{annotationId} | Read document page ink annotation by ID.
[**get_line_annotation**](PdfApi.md#get_line_annotation) | **GET** /pdf/\{name}/annotations/line/\{annotationId} | Read document page line annotation by ID.
[**get_link_annotation**](PdfApi.md#get_link_annotation) | **GET** /pdf/\{name}/links/\{linkId} | Read document link annotation by ID.
[**get_list_box_field**](PdfApi.md#get_list_box_field) | **GET** /pdf/\{name}/fields/listbox/\{fieldName} | Read document listbox field by name.
[**get_markdown_in_storage_to_pdf**](PdfApi.md#get_markdown_in_storage_to_pdf) | **GET** /pdf/create/markdown | Convert MD file (located on storage) to PDF format and return resulting file in response. 
[**get_mht_in_storage_to_pdf**](PdfApi.md#get_mht_in_storage_to_pdf) | **GET** /pdf/create/mht | Convert MHT file (located on storage) to PDF format and return resulting file in response. 
[**get_movie_annotation**](PdfApi.md#get_movie_annotation) | **GET** /pdf/\{name}/annotations/movie/\{annotationId} | Read document page movie annotation by ID.
[**get_page**](PdfApi.md#get_page) | **GET** /pdf/\{name}/pages/\{pageNumber} | Read document page info.
[**get_page_annotations**](PdfApi.md#get_page_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations | Read document page annotations. Returns only FreeTextAnnotations, TextAnnotations, other annotations will implemented next releases.
[**get_page_caret_annotations**](PdfApi.md#get_page_caret_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/caret | Read document page caret annotations.
[**get_page_check_box_fields**](PdfApi.md#get_page_check_box_fields) | **GET** /pdf/\{name}/page/\{pageNumber}/fields/checkbox | Read document page checkbox fields.
[**get_page_circle_annotations**](PdfApi.md#get_page_circle_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/circle | Read document page circle annotations.
[**get_page_combo_box_fields**](PdfApi.md#get_page_combo_box_fields) | **GET** /pdf/\{name}/page/\{pageNumber}/fields/combobox | Read document page combobox fields.
[**get_page_convert_to_bmp**](PdfApi.md#get_page_convert_to_bmp) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/bmp | Convert document page to Bmp image and return resulting file in response.
[**get_page_convert_to_emf**](PdfApi.md#get_page_convert_to_emf) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/emf | Convert document page to Emf image and return resulting file in response.
[**get_page_convert_to_gif**](PdfApi.md#get_page_convert_to_gif) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/gif | Convert document page to Gif image and return resulting file in response.
[**get_page_convert_to_jpeg**](PdfApi.md#get_page_convert_to_jpeg) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/jpeg | Convert document page to Jpeg image and return resulting file in response.
[**get_page_convert_to_png**](PdfApi.md#get_page_convert_to_png) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/png | Convert document page to Png image and return resulting file in response.
[**get_page_convert_to_tiff**](PdfApi.md#get_page_convert_to_tiff) | **GET** /pdf/\{name}/pages/\{pageNumber}/convert/tiff | Convert document page to Tiff image  and return resulting file in response.
[**get_page_file_attachment_annotations**](PdfApi.md#get_page_file_attachment_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/fileattachment | Read document page FileAttachment annotations.
[**get_page_free_text_annotations**](PdfApi.md#get_page_free_text_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/freetext | Read document page free text annotations.
[**get_page_highlight_annotations**](PdfApi.md#get_page_highlight_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/highlight | Read document page highlight annotations.
[**get_page_ink_annotations**](PdfApi.md#get_page_ink_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/ink | Read document page ink annotations.
[**get_page_line_annotations**](PdfApi.md#get_page_line_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/line | Read document page line annotations.
[**get_page_link_annotation**](PdfApi.md#get_page_link_annotation) | **GET** /pdf/\{name}/pages/\{pageNumber}/links/\{linkId} | Read document page link annotation by ID.
[**get_page_link_annotations**](PdfApi.md#get_page_link_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/links | Read document page link annotations.
[**get_page_list_box_fields**](PdfApi.md#get_page_list_box_fields) | **GET** /pdf/\{name}/page/\{pageNumber}/fields/listbox | Read document page listbox fields.
[**get_page_movie_annotations**](PdfApi.md#get_page_movie_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/movie | Read document page movie annotations.
[**get_page_poly_line_annotations**](PdfApi.md#get_page_poly_line_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/polyline | Read document page polyline annotations.
[**get_page_polygon_annotations**](PdfApi.md#get_page_polygon_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/polygon | Read document page polygon annotations.
[**get_page_popup_annotations**](PdfApi.md#get_page_popup_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/popup | Read document page popup annotations.
[**get_page_radio_button_fields**](PdfApi.md#get_page_radio_button_fields) | **GET** /pdf/\{name}/page/\{pageNumber}/fields/radiobutton | Read document page radiobutton fields.
[**get_page_redaction_annotations**](PdfApi.md#get_page_redaction_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/redaction | Read document page redaction annotations.
[**get_page_screen_annotations**](PdfApi.md#get_page_screen_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/screen | Read document page screen annotations.
[**get_page_signature_fields**](PdfApi.md#get_page_signature_fields) | **GET** /pdf/\{name}/page/\{pageNumber}/fields/signature | Read document page signature fields.
[**get_page_sound_annotations**](PdfApi.md#get_page_sound_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/sound | Read document page sound annotations.
[**get_page_square_annotations**](PdfApi.md#get_page_square_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/square | Read document page square annotations.
[**get_page_squiggly_annotations**](PdfApi.md#get_page_squiggly_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/squiggly | Read document page squiggly annotations.
[**get_page_stamp_annotations**](PdfApi.md#get_page_stamp_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/stamp | Read document page stamp annotations.
[**get_page_stamps**](PdfApi.md#get_page_stamps) | **GET** /pdf/\{name}/pages/\{pageNumber}/stamps | Read page document stamps.
[**get_page_strike_out_annotations**](PdfApi.md#get_page_strike_out_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/strikeout | Read document page StrikeOut annotations.
[**get_page_tables**](PdfApi.md#get_page_tables) | **GET** /pdf/\{name}/pages/\{pageNumber}/tables | Read document page tables.
[**get_page_text**](PdfApi.md#get_page_text) | **GET** /pdf/\{name}/pages/\{pageNumber}/text | Read page text items.
[**get_page_text_annotations**](PdfApi.md#get_page_text_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/text | Read document page text annotations.
[**get_page_text_box_fields**](PdfApi.md#get_page_text_box_fields) | **GET** /pdf/\{name}/page/\{pageNumber}/fields/textbox | Read document page text box fields.
[**get_page_underline_annotations**](PdfApi.md#get_page_underline_annotations) | **GET** /pdf/\{name}/pages/\{pageNumber}/annotations/underline | Read document page underline annotations.
[**get_pages**](PdfApi.md#get_pages) | **GET** /pdf/\{name}/pages | Read document pages info.
[**get_pcl_in_storage_to_pdf**](PdfApi.md#get_pcl_in_storage_to_pdf) | **GET** /pdf/create/pcl | Convert PCL file (located on storage) to PDF format and return resulting file in response. 
[**get_pdf_a_in_storage_to_pdf**](PdfApi.md#get_pdf_a_in_storage_to_pdf) | **GET** /pdf/create/pdfa | Convert PDFA file (located on storage) to PDF format and return resulting file in response. 
[**get_pdf_in_storage_to_doc**](PdfApi.md#get_pdf_in_storage_to_doc) | **GET** /pdf/\{name}/convert/doc | Converts PDF document (located on storage) to DOC format and returns resulting file in response content.
[**get_pdf_in_storage_to_epub**](PdfApi.md#get_pdf_in_storage_to_epub) | **GET** /pdf/\{name}/convert/epub | Converts PDF document (located on storage) to EPUB format and returns resulting file in response content
[**get_pdf_in_storage_to_html**](PdfApi.md#get_pdf_in_storage_to_html) | **GET** /pdf/\{name}/convert/html | Converts PDF document (located on storage) to Html format and returns resulting file in response content
[**get_pdf_in_storage_to_mobi_xml**](PdfApi.md#get_pdf_in_storage_to_mobi_xml) | **GET** /pdf/\{name}/convert/mobixml | Converts PDF document (located on storage) to MOBIXML format and returns resulting ZIP archive file in response content.
[**get_pdf_in_storage_to_pdf_a**](PdfApi.md#get_pdf_in_storage_to_pdf_a) | **GET** /pdf/\{name}/convert/pdfa | Converts PDF document (located on storage) to PdfA format and returns resulting file in response content
[**get_pdf_in_storage_to_pptx**](PdfApi.md#get_pdf_in_storage_to_pptx) | **GET** /pdf/\{name}/convert/pptx | Converts PDF document (located on storage) to PPTX format and returns resulting file in response content
[**get_pdf_in_storage_to_svg**](PdfApi.md#get_pdf_in_storage_to_svg) | **GET** /pdf/\{name}/convert/svg | Converts PDF document (located on storage) to SVG format and returns resulting file in response content
[**get_pdf_in_storage_to_te_x**](PdfApi.md#get_pdf_in_storage_to_te_x) | **GET** /pdf/\{name}/convert/tex | Converts PDF document (located on storage) to TeX format and returns resulting file in response content
[**get_pdf_in_storage_to_text**](PdfApi.md#get_pdf_in_storage_to_text) | **GET** /pdf/\{name}/convert/text | Converts PDF document (located on storage) to Text format and returns resulting file in response content
[**get_pdf_in_storage_to_tiff**](PdfApi.md#get_pdf_in_storage_to_tiff) | **GET** /pdf/\{name}/convert/tiff | Converts PDF document (located on storage) to TIFF format and returns resulting file in response content
[**get_pdf_in_storage_to_xls**](PdfApi.md#get_pdf_in_storage_to_xls) | **GET** /pdf/\{name}/convert/xls | Converts PDF document (located on storage) to XLS format and returns resulting file in response content
[**get_pdf_in_storage_to_xlsx**](PdfApi.md#get_pdf_in_storage_to_xlsx) | **GET** /pdf/\{name}/convert/xlsx | Converts PDF document (located on storage) to XLSX format and returns resulting file in response content
[**get_pdf_in_storage_to_xml**](PdfApi.md#get_pdf_in_storage_to_xml) | **GET** /pdf/\{name}/convert/xml | Converts PDF document (located on storage) to XML format and returns resulting file in response content
[**get_pdf_in_storage_to_xps**](PdfApi.md#get_pdf_in_storage_to_xps) | **GET** /pdf/\{name}/convert/xps | Converts PDF document (located on storage) to XPS format and returns resulting file in response content
[**get_poly_line_annotation**](PdfApi.md#get_poly_line_annotation) | **GET** /pdf/\{name}/annotations/polyline/\{annotationId} | Read document page polyline annotation by ID.
[**get_polygon_annotation**](PdfApi.md#get_polygon_annotation) | **GET** /pdf/\{name}/annotations/polygon/\{annotationId} | Read document page polygon annotation by ID.
[**get_popup_annotation**](PdfApi.md#get_popup_annotation) | **GET** /pdf/\{name}/annotations/popup/\{annotationId} | Read document page popup annotation by ID.
[**get_ps_in_storage_to_pdf**](PdfApi.md#get_ps_in_storage_to_pdf) | **GET** /pdf/create/ps | Convert PS file (located on storage) to PDF format and return resulting file in response. 
[**get_radio_button_field**](PdfApi.md#get_radio_button_field) | **GET** /pdf/\{name}/fields/radiobutton/\{fieldName} | Read document RadioButton field by name.
[**get_redaction_annotation**](PdfApi.md#get_redaction_annotation) | **GET** /pdf/\{name}/annotations/redaction/\{annotationId} | Read document page redaction annotation by ID.
[**get_screen_annotation**](PdfApi.md#get_screen_annotation) | **GET** /pdf/\{name}/annotations/screen/\{annotationId} | Read document page screen annotation by ID.
[**get_screen_annotation_data**](PdfApi.md#get_screen_annotation_data) | **GET** /pdf/\{name}/annotations/screen/\{annotationId}/data | Read document page screen annotation by ID.
[**get_signature_field**](PdfApi.md#get_signature_field) | **GET** /pdf/\{name}/fields/signature/\{fieldName} | Read document signature field by name.
[**get_sound_annotation**](PdfApi.md#get_sound_annotation) | **GET** /pdf/\{name}/annotations/sound/\{annotationId} | Read document page sound annotation by ID.
[**get_sound_annotation_data**](PdfApi.md#get_sound_annotation_data) | **GET** /pdf/\{name}/annotations/sound/\{annotationId}/data | Read document page sound annotation by ID.
[**get_square_annotation**](PdfApi.md#get_square_annotation) | **GET** /pdf/\{name}/annotations/square/\{annotationId} | Read document page square annotation by ID.
[**get_squiggly_annotation**](PdfApi.md#get_squiggly_annotation) | **GET** /pdf/\{name}/annotations/squiggly/\{annotationId} | Read document page squiggly annotation by ID.
[**get_stamp_annotation**](PdfApi.md#get_stamp_annotation) | **GET** /pdf/\{name}/annotations/stamp/\{annotationId} | Read document page stamp annotation by ID.
[**get_stamp_annotation_data**](PdfApi.md#get_stamp_annotation_data) | **GET** /pdf/\{name}/annotations/stamp/\{annotationId}/data | Read document page stamp annotation by ID.
[**get_strike_out_annotation**](PdfApi.md#get_strike_out_annotation) | **GET** /pdf/\{name}/annotations/strikeout/\{annotationId} | Read document page StrikeOut annotation by ID.
[**get_svg_in_storage_to_pdf**](PdfApi.md#get_svg_in_storage_to_pdf) | **GET** /pdf/create/svg | Convert SVG file (located on storage) to PDF format and return resulting file in response. 
[**get_table**](PdfApi.md#get_table) | **GET** /pdf/\{name}/tables/\{tableId} | Read document page table by ID.
[**get_te_x_in_storage_to_pdf**](PdfApi.md#get_te_x_in_storage_to_pdf) | **GET** /pdf/create/tex | Convert TeX file (located on storage) to PDF format and return resulting file in response. 
[**get_text**](PdfApi.md#get_text) | **GET** /pdf/\{name}/text | Read document text.
[**get_text_annotation**](PdfApi.md#get_text_annotation) | **GET** /pdf/\{name}/annotations/text/\{annotationId} | Read document page text annotation by ID.
[**get_text_box_field**](PdfApi.md#get_text_box_field) | **GET** /pdf/\{name}/fields/textbox/\{fieldName} | Read document text box field by name.
[**get_underline_annotation**](PdfApi.md#get_underline_annotation) | **GET** /pdf/\{name}/annotations/underline/\{annotationId} | Read document page underline annotation by ID.
[**get_verify_signature**](PdfApi.md#get_verify_signature) | **GET** /pdf/\{name}/verifySignature | Verify signature document.
[**get_web_in_storage_to_pdf**](PdfApi.md#get_web_in_storage_to_pdf) | **GET** /pdf/create/web | Convert web page to PDF format and return resulting file in response. 
[**get_words_per_page**](PdfApi.md#get_words_per_page) | **GET** /pdf/\{name}/pages/wordCount | Get number of words per document page.
[**get_xfa_pdf_in_storage_to_acro_form**](PdfApi.md#get_xfa_pdf_in_storage_to_acro_form) | **GET** /pdf/\{name}/convert/xfatoacroform | Converts PDF document which contains XFA form (located on storage) to PDF with AcroForm and returns resulting file response content
[**get_xml_in_storage_to_pdf**](PdfApi.md#get_xml_in_storage_to_pdf) | **GET** /pdf/create/xml | Convert XML file (located on storage) to PDF format and return resulting file in response. 
[**get_xmp_metadata_json**](PdfApi.md#get_xmp_metadata_json) | **GET** /pdf/\{name}/xmpmetadata/json | Gets document XMP Metadata as JSON.
[**get_xmp_metadata_xml**](PdfApi.md#get_xmp_metadata_xml) | **GET** /pdf/\{name}/xmpmetadata/xml | Gets document XMP Metadata as XML file.
[**get_xps_in_storage_to_pdf**](PdfApi.md#get_xps_in_storage_to_pdf) | **GET** /pdf/create/xps | Convert XPS file (located on storage) to PDF format and return resulting file in response. 
[**get_xsl_fo_in_storage_to_pdf**](PdfApi.md#get_xsl_fo_in_storage_to_pdf) | **GET** /pdf/create/xslfo | Convert XslFo file (located on storage) to PDF format and return resulting file in response. 
[**move_file**](PdfApi.md#move_file) | **PUT** /pdf/storage/file/move/\{srcPath} | Move file
[**move_folder**](PdfApi.md#move_folder) | **PUT** /pdf/storage/folder/move/\{srcPath} | Move folder
[**object_exists**](PdfApi.md#object_exists) | **GET** /pdf/storage/exist/\{path} | Check if file or folder exists
[**post_add_document_attachment**](PdfApi.md#post_add_document_attachment) | **POST** /pdf/\{name}/attachments | Adds a file attachment to the PDF document.
[**post_append_document**](PdfApi.md#post_append_document) | **POST** /pdf/\{name}/appendDocument | Append document to existing one.
[**post_bookmark**](PdfApi.md#post_bookmark) | **POST** /pdf/\{name}/bookmarks/bookmark/\{bookmarkPath} | Add document bookmarks.
[**post_change_password_document_in_storage**](PdfApi.md#post_change_password_document_in_storage) | **POST** /pdf/\{name}/changepassword | Change document password in storage.
[**post_check_box_fields**](PdfApi.md#post_check_box_fields) | **POST** /pdf/\{name}/fields/checkbox | Add document checkbox fields.
[**post_combo_box_fields**](PdfApi.md#post_combo_box_fields) | **POST** /pdf/\{name}/fields/combobox | Add document combobox fields.
[**post_create_document**](PdfApi.md#post_create_document) | **POST** /pdf/\{name} | Create empty document.
[**post_create_field**](PdfApi.md#post_create_field) | **POST** /pdf/\{name}/fields | Create field.
[**post_decrypt_document_in_storage**](PdfApi.md#post_decrypt_document_in_storage) | **POST** /pdf/\{name}/decrypt | Decrypt document in storage.
[**post_document_image_footer**](PdfApi.md#post_document_image_footer) | **POST** /pdf/\{name}/footer/image | Add document image footer.
[**post_document_image_header**](PdfApi.md#post_document_image_header) | **POST** /pdf/\{name}/header/image | Add document image header.
[**post_document_image_stamps**](PdfApi.md#post_document_image_stamps) | **POST** /pdf/\{name}/stamps/image | Add document pages image stamps.
[**post_document_page_number_stamps**](PdfApi.md#post_document_page_number_stamps) | **POST** /pdf/\{name}/stamps/pagenumber | Add document page number stamps.
[**post_document_text_footer**](PdfApi.md#post_document_text_footer) | **POST** /pdf/\{name}/footer/text | Add document text footer.
[**post_document_text_header**](PdfApi.md#post_document_text_header) | **POST** /pdf/\{name}/header/text | Add document text header.
[**post_document_text_replace**](PdfApi.md#post_document_text_replace) | **POST** /pdf/\{name}/text/replace | Document&#39;s replace text method.
[**post_document_text_stamps**](PdfApi.md#post_document_text_stamps) | **POST** /pdf/\{name}/stamps/text | Add document pages text stamps.
[**post_encrypt_document_in_storage**](PdfApi.md#post_encrypt_document_in_storage) | **POST** /pdf/\{name}/encrypt | Encrypt document in storage.
[**post_flatten_document**](PdfApi.md#post_flatten_document) | **POST** /pdf/\{name}/flatten | Flatten the document.
[**post_html_to_pdf**](PdfApi.md#post_html_to_pdf) | **POST** /pdf/create/html | Convert HTML file (zip archive in request content) to PDF format and return resulting file in response. 
[**post_import_fields_from_fdf**](PdfApi.md#post_import_fields_from_fdf) | **POST** /pdf/\{name}/import/fdf | Update fields from FDF file in request.
[**post_import_fields_from_xfdf**](PdfApi.md#post_import_fields_from_xfdf) | **POST** /pdf/\{name}/import/xfdf | Update fields from XFDF file in request.
[**post_import_fields_from_xml**](PdfApi.md#post_import_fields_from_xml) | **POST** /pdf/\{name}/import/xml | Update fields from XML file in request.
[**post_insert_image**](PdfApi.md#post_insert_image) | **POST** /pdf/\{name}/pages/\{pageNumber}/images | Insert image to document page.
[**post_list_box_fields**](PdfApi.md#post_list_box_fields) | **POST** /pdf/\{name}/fields/listbox | Add document listbox fields.
[**post_move_page**](PdfApi.md#post_move_page) | **POST** /pdf/\{name}/pages/\{pageNumber}/movePage | Move page to new position.
[**post_optimize_document**](PdfApi.md#post_optimize_document) | **POST** /pdf/\{name}/optimize | Optimize document.
[**post_organize_document**](PdfApi.md#post_organize_document) | **POST** /pdf/\{name}/organize | Merge selected pages of a document.
[**post_organize_documents**](PdfApi.md#post_organize_documents) | **POST** /pdf/organize | Merge selected pages of different documents.
[**post_page_caret_annotations**](PdfApi.md#post_page_caret_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/caret | Add document page caret annotations.
[**post_page_certify**](PdfApi.md#post_page_certify) | **POST** /pdf/\{name}/pages/\{pageNumber}/certify | Certify document page.
[**post_page_circle_annotations**](PdfApi.md#post_page_circle_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/circle | Add document page circle annotations.
[**post_page_file_attachment_annotations**](PdfApi.md#post_page_file_attachment_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/fileattachment | Add document page FileAttachment annotations.
[**post_page_free_text_annotations**](PdfApi.md#post_page_free_text_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/freetext | Add document page free text annotations.
[**post_page_highlight_annotations**](PdfApi.md#post_page_highlight_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/highlight | Add document page highlight annotations.
[**post_page_image_stamps**](PdfApi.md#post_page_image_stamps) | **POST** /pdf/\{name}/pages/\{pageNumber}/stamps/image | Add document page image stamps.
[**post_page_ink_annotations**](PdfApi.md#post_page_ink_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/ink | Add document page ink annotations.
[**post_page_line_annotations**](PdfApi.md#post_page_line_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/line | Add document page line annotations.
[**post_page_link_annotations**](PdfApi.md#post_page_link_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/links | Add document page link annotations.
[**post_page_movie_annotations**](PdfApi.md#post_page_movie_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/movie | Add document page movie annotations.
[**post_page_pdf_page_stamps**](PdfApi.md#post_page_pdf_page_stamps) | **POST** /pdf/\{name}/pages/\{pageNumber}/stamps/pdfpage | Add document pdf page stamps.
[**post_page_poly_line_annotations**](PdfApi.md#post_page_poly_line_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/polyline | Add document page polyline annotations.
[**post_page_polygon_annotations**](PdfApi.md#post_page_polygon_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/polygon | Add document page polygon annotations.
[**post_page_redaction_annotations**](PdfApi.md#post_page_redaction_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/redaction | Add document page redaction annotations.
[**post_page_screen_annotations**](PdfApi.md#post_page_screen_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/screen | Add document page screen annotations.
[**post_page_sound_annotations**](PdfApi.md#post_page_sound_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/sound | Add document page sound annotations.
[**post_page_square_annotations**](PdfApi.md#post_page_square_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/square | Add document page square annotations.
[**post_page_squiggly_annotations**](PdfApi.md#post_page_squiggly_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/squiggly | Add document page squiggly annotations.
[**post_page_stamp_annotations**](PdfApi.md#post_page_stamp_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/stamp | Add document page stamp annotations.
[**post_page_strike_out_annotations**](PdfApi.md#post_page_strike_out_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/strikeout | Add document page StrikeOut annotations.
[**post_page_tables**](PdfApi.md#post_page_tables) | **POST** /pdf/\{name}/pages/\{pageNumber}/tables | Add document page tables.
[**post_page_text_annotations**](PdfApi.md#post_page_text_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/text | Add document page text annotations.
[**post_page_text_replace**](PdfApi.md#post_page_text_replace) | **POST** /pdf/\{name}/pages/\{pageNumber}/text/replace | Page&#39;s replace text method.
[**post_page_text_stamps**](PdfApi.md#post_page_text_stamps) | **POST** /pdf/\{name}/pages/\{pageNumber}/stamps/text | Add document page text stamps.
[**post_page_underline_annotations**](PdfApi.md#post_page_underline_annotations) | **POST** /pdf/\{name}/pages/\{pageNumber}/annotations/underline | Add document page underline annotations.
[**post_pdf_to_xlsx**](PdfApi.md#post_pdf_to_xlsx) | **POST** /pdf/convert/xlsx | Converts PDF document (in request content) to XLSX format and uploads and returns resulting file in response content.
[**post_popup_annotation**](PdfApi.md#post_popup_annotation) | **POST** /pdf/\{name}/annotations/\{annotationId}/popup | Add document popup annotations.
[**post_radio_button_fields**](PdfApi.md#post_radio_button_fields) | **POST** /pdf/\{name}/fields/radiobutton | Add document RadioButton fields.
[**post_sign_document**](PdfApi.md#post_sign_document) | **POST** /pdf/\{name}/sign | Sign document.
[**post_sign_page**](PdfApi.md#post_sign_page) | **POST** /pdf/\{name}/pages/\{pageNumber}/sign | Sign page.
[**post_signature_field**](PdfApi.md#post_signature_field) | **POST** /pdf/\{name}/fields/signature | Add document signature field.
[**post_split_document**](PdfApi.md#post_split_document) | **POST** /pdf/\{name}/split | Split document to parts.
[**post_split_range_pdf_document**](PdfApi.md#post_split_range_pdf_document) | **POST** /pdf/\{name}/splitrangepdf | Split document into ranges.
[**post_text_box_fields**](PdfApi.md#post_text_box_fields) | **POST** /pdf/\{name}/fields/textbox | Add document text box fields.
[**post_xmp_metadata**](PdfApi.md#post_xmp_metadata) | **POST** /pdf/\{name}/xmpmetadata | Add or remove XMP Metadata properties.
[**put_add_new_page**](PdfApi.md#put_add_new_page) | **PUT** /pdf/\{name}/pages | Add new page to end of the document.
[**put_add_text**](PdfApi.md#put_add_text) | **PUT** /pdf/\{name}/pages/\{pageNumber}/text | Add text to PDF document page.
[**put_annotations_flatten**](PdfApi.md#put_annotations_flatten) | **PUT** /pdf/\{name}/annotations/flatten | Flattens the annotations of the specified types
[**put_bookmark**](PdfApi.md#put_bookmark) | **PUT** /pdf/\{name}/bookmarks/bookmark/\{bookmarkPath} | Update document bookmark.
[**put_caret_annotation**](PdfApi.md#put_caret_annotation) | **PUT** /pdf/\{name}/annotations/caret/\{annotationId} | Replace document caret annotation
[**put_change_password_document**](PdfApi.md#put_change_password_document) | **PUT** /pdf/changepassword | Change document password from content.
[**put_check_box_field**](PdfApi.md#put_check_box_field) | **PUT** /pdf/\{name}/fields/checkbox/\{fieldName} | Replace document checkbox field
[**put_circle_annotation**](PdfApi.md#put_circle_annotation) | **PUT** /pdf/\{name}/annotations/circle/\{annotationId} | Replace document circle annotation
[**put_combo_box_field**](PdfApi.md#put_combo_box_field) | **PUT** /pdf/\{name}/fields/combobox/\{fieldName} | Replace document combobox field
[**put_create_document**](PdfApi.md#put_create_document) | **PUT** /pdf/\{name} | Create empty document.
[**put_create_pdf_from_layer**](PdfApi.md#put_create_pdf_from_layer) | **PUT** /pdf/\{name}/layers | Create a separate PDF from a PDF Layer and upload resulting file to storage.
[**put_decrypt_document**](PdfApi.md#put_decrypt_document) | **PUT** /pdf/decrypt | Decrypt document from content.
[**put_document_display_properties**](PdfApi.md#put_document_display_properties) | **PUT** /pdf/\{name}/displayproperties | Update document display properties.
[**put_encrypt_document**](PdfApi.md#put_encrypt_document) | **PUT** /pdf/encrypt | Encrypt document from content.
[**put_epub_in_storage_to_pdf**](PdfApi.md#put_epub_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/epub | Convert EPUB file (located on storage) to PDF format and upload resulting file to storage. 
[**put_export_fields_from_pdf_to_fdf_in_storage**](PdfApi.md#put_export_fields_from_pdf_to_fdf_in_storage) | **PUT** /pdf/\{name}/export/fdf | Export fields from from PDF in storage to FDF file in storage.
[**put_export_fields_from_pdf_to_xfdf_in_storage**](PdfApi.md#put_export_fields_from_pdf_to_xfdf_in_storage) | **PUT** /pdf/\{name}/export/xfdf | Export fields from from PDF in storage to XFDF file in storage.
[**put_export_fields_from_pdf_to_xml_in_storage**](PdfApi.md#put_export_fields_from_pdf_to_xml_in_storage) | **PUT** /pdf/\{name}/export/xml | Export fields from from PDF in storage to XML file in storage.
[**put_fields_flatten**](PdfApi.md#put_fields_flatten) | **PUT** /pdf/\{name}/fields/flatten | Flatten form fields in document.
[**put_file_attachment_annotation**](PdfApi.md#put_file_attachment_annotation) | **PUT** /pdf/\{name}/annotations/fileattachment/\{annotationId} | Replace document FileAttachment annotation
[**put_file_attachment_annotation_data_extract**](PdfApi.md#put_file_attachment_annotation_data_extract) | **PUT** /pdf/\{name}/annotations/fileattachment/\{annotationId}/data/extract | Extract document FileAttachment annotation content to storage
[**put_free_text_annotation**](PdfApi.md#put_free_text_annotation) | **PUT** /pdf/\{name}/annotations/freetext/\{annotationId} | Replace document free text annotation
[**put_highlight_annotation**](PdfApi.md#put_highlight_annotation) | **PUT** /pdf/\{name}/annotations/highlight/\{annotationId} | Replace document highlight annotation
[**put_html_in_storage_to_pdf**](PdfApi.md#put_html_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/html | Convert HTML file (located on storage) to PDF format and upload resulting file to storage. 
[**put_image_extract_as_gif**](PdfApi.md#put_image_extract_as_gif) | **PUT** /pdf/\{name}/images/\{imageId}/extract/gif | Extract document image in GIF format to folder
[**put_image_extract_as_jpeg**](PdfApi.md#put_image_extract_as_jpeg) | **PUT** /pdf/\{name}/images/\{imageId}/extract/jpeg | Extract document image in JPEG format to folder
[**put_image_extract_as_png**](PdfApi.md#put_image_extract_as_png) | **PUT** /pdf/\{name}/images/\{imageId}/extract/png | Extract document image in PNG format to folder
[**put_image_extract_as_tiff**](PdfApi.md#put_image_extract_as_tiff) | **PUT** /pdf/\{name}/images/\{imageId}/extract/tiff | Extract document image in TIFF format to folder
[**put_image_in_storage_to_pdf**](PdfApi.md#put_image_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/images | Convert image file (located on storage) to PDF format and upload resulting file to storage. 
[**put_images_extract_as_gif**](PdfApi.md#put_images_extract_as_gif) | **PUT** /pdf/\{name}/pages/\{pageNumber}/images/extract/gif | Extract document images in GIF format to folder.
[**put_images_extract_as_jpeg**](PdfApi.md#put_images_extract_as_jpeg) | **PUT** /pdf/\{name}/pages/\{pageNumber}/images/extract/jpeg | Extract document images in JPEG format to folder.
[**put_images_extract_as_png**](PdfApi.md#put_images_extract_as_png) | **PUT** /pdf/\{name}/pages/\{pageNumber}/images/extract/png | Extract document images in PNG format to folder.
[**put_images_extract_as_tiff**](PdfApi.md#put_images_extract_as_tiff) | **PUT** /pdf/\{name}/pages/\{pageNumber}/images/extract/tiff | Extract document images in TIFF format to folder.
[**put_import_fields_from_fdf_in_storage**](PdfApi.md#put_import_fields_from_fdf_in_storage) | **PUT** /pdf/\{name}/import/fdf | Update fields from FDF file in storage.
[**put_import_fields_from_xfdf_in_storage**](PdfApi.md#put_import_fields_from_xfdf_in_storage) | **PUT** /pdf/\{name}/import/xfdf | Update fields from XFDF file in storage.
[**put_import_fields_from_xml_in_storage**](PdfApi.md#put_import_fields_from_xml_in_storage) | **PUT** /pdf/\{name}/import/xml | Update fields from XML file in storage.
[**put_ink_annotation**](PdfApi.md#put_ink_annotation) | **PUT** /pdf/\{name}/annotations/ink/\{annotationId} | Replace document ink annotation
[**put_line_annotation**](PdfApi.md#put_line_annotation) | **PUT** /pdf/\{name}/annotations/line/\{annotationId} | Replace document line annotation
[**put_link_annotation**](PdfApi.md#put_link_annotation) | **PUT** /pdf/\{name}/links/\{linkId} | Replace document page link annotations
[**put_list_box_field**](PdfApi.md#put_list_box_field) | **PUT** /pdf/\{name}/fields/listbox/\{fieldName} | Replace document listbox field
[**put_markdown_in_storage_to_pdf**](PdfApi.md#put_markdown_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/markdown | Convert MD file (located on storage) to PDF format and upload resulting file to storage. 
[**put_merge_documents**](PdfApi.md#put_merge_documents) | **PUT** /pdf/\{name}/merge | Merge a list of documents.
[**put_mht_in_storage_to_pdf**](PdfApi.md#put_mht_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/mht | Convert MHT file (located on storage) to PDF format and upload resulting file to storage. 
[**put_movie_annotation**](PdfApi.md#put_movie_annotation) | **PUT** /pdf/\{name}/annotations/movie/\{annotationId} | Replace document movie annotation
[**put_page_add_stamp**](PdfApi.md#put_page_add_stamp) | **PUT** /pdf/\{name}/pages/\{pageNumber}/stamp | Add page stamp.
[**put_page_convert_to_bmp**](PdfApi.md#put_page_convert_to_bmp) | **PUT** /pdf/\{name}/pages/\{pageNumber}/convert/bmp | Convert document page to bmp image and upload resulting file to storage.
[**put_page_convert_to_emf**](PdfApi.md#put_page_convert_to_emf) | **PUT** /pdf/\{name}/pages/\{pageNumber}/convert/emf | Convert document page to emf image and upload resulting file to storage.
[**put_page_convert_to_gif**](PdfApi.md#put_page_convert_to_gif) | **PUT** /pdf/\{name}/pages/\{pageNumber}/convert/gif | Convert document page to gif image and upload resulting file to storage.
[**put_page_convert_to_jpeg**](PdfApi.md#put_page_convert_to_jpeg) | **PUT** /pdf/\{name}/pages/\{pageNumber}/convert/jpeg | Convert document page to Jpeg image and upload resulting file to storage.
[**put_page_convert_to_png**](PdfApi.md#put_page_convert_to_png) | **PUT** /pdf/\{name}/pages/\{pageNumber}/convert/png | Convert document page to png image and upload resulting file to storage.
[**put_page_convert_to_tiff**](PdfApi.md#put_page_convert_to_tiff) | **PUT** /pdf/\{name}/pages/\{pageNumber}/convert/tiff | Convert document page to Tiff image and upload resulting file to storage.
[**put_pcl_in_storage_to_pdf**](PdfApi.md#put_pcl_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/pcl | Convert PCL file (located on storage) to PDF format and upload resulting file to storage. 
[**put_pdf_a_in_storage_to_pdf**](PdfApi.md#put_pdf_a_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/pdfa | Convert PDFA file (located on storage) to PDF format and upload resulting file to storage. 
[**put_pdf_in_request_to_doc**](PdfApi.md#put_pdf_in_request_to_doc) | **PUT** /pdf/convert/doc | Converts PDF document (in request content) to DOC format and uploads resulting file to storage.
[**put_pdf_in_request_to_epub**](PdfApi.md#put_pdf_in_request_to_epub) | **PUT** /pdf/convert/epub | Converts PDF document (in request content) to EPUB format and uploads resulting file to storage.
[**put_pdf_in_request_to_html**](PdfApi.md#put_pdf_in_request_to_html) | **PUT** /pdf/convert/html | Converts PDF document (in request content) to Html format and uploads resulting file to storage.
[**put_pdf_in_request_to_mobi_xml**](PdfApi.md#put_pdf_in_request_to_mobi_xml) | **PUT** /pdf/convert/mobixml | Converts PDF document (in request content) to MOBIXML format and uploads resulting ZIP archive file to storage.
[**put_pdf_in_request_to_pdf_a**](PdfApi.md#put_pdf_in_request_to_pdf_a) | **PUT** /pdf/convert/pdfa | Converts PDF document (in request content) to PdfA format and uploads resulting file to storage.
[**put_pdf_in_request_to_pptx**](PdfApi.md#put_pdf_in_request_to_pptx) | **PUT** /pdf/convert/pptx | Converts PDF document (in request content) to PPTX format and uploads resulting file to storage.
[**put_pdf_in_request_to_svg**](PdfApi.md#put_pdf_in_request_to_svg) | **PUT** /pdf/convert/svg | Converts PDF document (in request content) to SVG format and uploads resulting file to storage.
[**put_pdf_in_request_to_te_x**](PdfApi.md#put_pdf_in_request_to_te_x) | **PUT** /pdf/convert/tex | Converts PDF document (in request content) to TeX format and uploads resulting file to storage.
[**put_pdf_in_request_to_tiff**](PdfApi.md#put_pdf_in_request_to_tiff) | **PUT** /pdf/convert/tiff | Converts PDF document (in request content) to TIFF format and uploads resulting file to storage.
[**put_pdf_in_request_to_xls**](PdfApi.md#put_pdf_in_request_to_xls) | **PUT** /pdf/convert/xls | Converts PDF document (in request content) to XLS format and uploads resulting file to storage.
[**put_pdf_in_request_to_xlsx**](PdfApi.md#put_pdf_in_request_to_xlsx) | **PUT** /pdf/convert/xlsx | Converts PDF document (in request content) to XLSX format and uploads resulting file to storage.
[**put_pdf_in_request_to_xml**](PdfApi.md#put_pdf_in_request_to_xml) | **PUT** /pdf/convert/xml | Converts PDF document (in request content) to XML format and uploads resulting file to storage.
[**put_pdf_in_request_to_xps**](PdfApi.md#put_pdf_in_request_to_xps) | **PUT** /pdf/convert/xps | Converts PDF document (in request content) to XPS format and uploads resulting file to storage.
[**put_pdf_in_storage_to_doc**](PdfApi.md#put_pdf_in_storage_to_doc) | **PUT** /pdf/\{name}/convert/doc | Converts PDF document (located on storage) to DOC format and uploads resulting file to storage.
[**put_pdf_in_storage_to_epub**](PdfApi.md#put_pdf_in_storage_to_epub) | **PUT** /pdf/\{name}/convert/epub | Converts PDF document (located on storage) to EPUB format and uploads resulting file to storage
[**put_pdf_in_storage_to_html**](PdfApi.md#put_pdf_in_storage_to_html) | **PUT** /pdf/\{name}/convert/html | Converts PDF document (located on storage) to Html format and uploads resulting file to storage
[**put_pdf_in_storage_to_mobi_xml**](PdfApi.md#put_pdf_in_storage_to_mobi_xml) | **PUT** /pdf/\{name}/convert/mobixml | Converts PDF document (located on storage) to MOBIXML format and uploads resulting ZIP archive file to storage
[**put_pdf_in_storage_to_pdf_a**](PdfApi.md#put_pdf_in_storage_to_pdf_a) | **PUT** /pdf/\{name}/convert/pdfa | Converts PDF document (located on storage) to PdfA format and uploads resulting file to storage
[**put_pdf_in_storage_to_pptx**](PdfApi.md#put_pdf_in_storage_to_pptx) | **PUT** /pdf/\{name}/convert/pptx | Converts PDF document (located on storage) to PPTX format and uploads resulting file to storage
[**put_pdf_in_storage_to_svg**](PdfApi.md#put_pdf_in_storage_to_svg) | **PUT** /pdf/\{name}/convert/svg | Converts PDF document (located on storage) to SVG format and uploads resulting file to storage
[**put_pdf_in_storage_to_te_x**](PdfApi.md#put_pdf_in_storage_to_te_x) | **PUT** /pdf/\{name}/convert/tex | Converts PDF document (located on storage) to TeX format and uploads resulting file to storage
[**put_pdf_in_storage_to_tiff**](PdfApi.md#put_pdf_in_storage_to_tiff) | **PUT** /pdf/\{name}/convert/tiff | Converts PDF document (located on storage) to TIFF format and uploads resulting file to storage
[**put_pdf_in_storage_to_xls**](PdfApi.md#put_pdf_in_storage_to_xls) | **PUT** /pdf/\{name}/convert/xls | Converts PDF document (located on storage) to XLS format and uploads resulting file to storage
[**put_pdf_in_storage_to_xlsx**](PdfApi.md#put_pdf_in_storage_to_xlsx) | **PUT** /pdf/\{name}/convert/xlsx | Converts PDF document (located on storage) to XLSX format and uploads resulting file to storage
[**put_pdf_in_storage_to_xml**](PdfApi.md#put_pdf_in_storage_to_xml) | **PUT** /pdf/\{name}/convert/xml | Converts PDF document (located on storage) to XML format and uploads resulting file to storage
[**put_pdf_in_storage_to_xps**](PdfApi.md#put_pdf_in_storage_to_xps) | **PUT** /pdf/\{name}/convert/xps | Converts PDF document (located on storage) to XPS format and uploads resulting file to storage
[**put_poly_line_annotation**](PdfApi.md#put_poly_line_annotation) | **PUT** /pdf/\{name}/annotations/polyline/\{annotationId} | Replace document polyline annotation
[**put_polygon_annotation**](PdfApi.md#put_polygon_annotation) | **PUT** /pdf/\{name}/annotations/polygon/\{annotationId} | Replace document polygon annotation
[**put_popup_annotation**](PdfApi.md#put_popup_annotation) | **PUT** /pdf/\{name}/annotations/popup/\{annotationId} | Replace document popup annotation
[**put_privileges**](PdfApi.md#put_privileges) | **PUT** /pdf/\{name}/privileges | Update privilege document.
[**put_ps_in_storage_to_pdf**](PdfApi.md#put_ps_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/ps | Convert PS file (located on storage) to PDF format and upload resulting file to storage. 
[**put_radio_button_field**](PdfApi.md#put_radio_button_field) | **PUT** /pdf/\{name}/fields/radiobutton/\{fieldName} | Replace document RadioButton field
[**put_redaction_annotation**](PdfApi.md#put_redaction_annotation) | **PUT** /pdf/\{name}/annotations/redaction/\{annotationId} | Replace document redaction annotation
[**put_replace_image**](PdfApi.md#put_replace_image) | **PUT** /pdf/\{name}/images/\{imageId} | Replace document image.
[**put_replace_multiple_image**](PdfApi.md#put_replace_multiple_image) | **PUT** /pdf/\{name}/images/replace | Replace document multiple image.
[**put_screen_annotation**](PdfApi.md#put_screen_annotation) | **PUT** /pdf/\{name}/annotations/screen/\{annotationId} | Replace document screen annotation
[**put_screen_annotation_data_extract**](PdfApi.md#put_screen_annotation_data_extract) | **PUT** /pdf/\{name}/annotations/screen/\{annotationId}/data/extract | Extract document screen annotation content to storage
[**put_searchable_document**](PdfApi.md#put_searchable_document) | **PUT** /pdf/\{name}/ocr | Create searchable PDF document. Generate OCR layer for images in input PDF document.
[**put_set_property**](PdfApi.md#put_set_property) | **PUT** /pdf/\{name}/documentproperties/\{propertyName} | Add/update document property.
[**put_signature_field**](PdfApi.md#put_signature_field) | **PUT** /pdf/\{name}/fields/signature/\{fieldName} | Replace document signature field.
[**put_sound_annotation**](PdfApi.md#put_sound_annotation) | **PUT** /pdf/\{name}/annotations/sound/\{annotationId} | Replace document sound annotation
[**put_sound_annotation_data_extract**](PdfApi.md#put_sound_annotation_data_extract) | **PUT** /pdf/\{name}/annotations/sound/\{annotationId}/data/extract | Extract document sound annotation content to storage
[**put_square_annotation**](PdfApi.md#put_square_annotation) | **PUT** /pdf/\{name}/annotations/square/\{annotationId} | Replace document square annotation
[**put_squiggly_annotation**](PdfApi.md#put_squiggly_annotation) | **PUT** /pdf/\{name}/annotations/squiggly/\{annotationId} | Replace document squiggly annotation
[**put_stamp_annotation**](PdfApi.md#put_stamp_annotation) | **PUT** /pdf/\{name}/annotations/stamp/\{annotationId} | Replace document stamp annotation
[**put_stamp_annotation_data_extract**](PdfApi.md#put_stamp_annotation_data_extract) | **PUT** /pdf/\{name}/annotations/stamp/\{annotationId}/data/extract | Extract document stamp annotation content to storage
[**put_strike_out_annotation**](PdfApi.md#put_strike_out_annotation) | **PUT** /pdf/\{name}/annotations/strikeout/\{annotationId} | Replace document StrikeOut annotation
[**put_svg_in_storage_to_pdf**](PdfApi.md#put_svg_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/svg | Convert SVG file (located on storage) to PDF format and upload resulting file to storage. 
[**put_table**](PdfApi.md#put_table) | **PUT** /pdf/\{name}/tables/\{tableId} | Replace document page table.
[**put_te_x_in_storage_to_pdf**](PdfApi.md#put_te_x_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/tex | Convert TeX file (located on storage) to PDF format and upload resulting file to storage. 
[**put_text_annotation**](PdfApi.md#put_text_annotation) | **PUT** /pdf/\{name}/annotations/text/\{annotationId} | Replace document text annotation
[**put_text_box_field**](PdfApi.md#put_text_box_field) | **PUT** /pdf/\{name}/fields/textbox/\{fieldName} | Replace document text box field
[**put_underline_annotation**](PdfApi.md#put_underline_annotation) | **PUT** /pdf/\{name}/annotations/underline/\{annotationId} | Replace document underline annotation
[**put_update_field**](PdfApi.md#put_update_field) | **PUT** /pdf/\{name}/fields/\{fieldName} | Update field.
[**put_update_fields**](PdfApi.md#put_update_fields) | **PUT** /pdf/\{name}/fields | Update fields.
[**put_web_in_storage_to_pdf**](PdfApi.md#put_web_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/web | Convert web page to PDF format and upload resulting file to storage. 
[**put_xfa_pdf_in_request_to_acro_form**](PdfApi.md#put_xfa_pdf_in_request_to_acro_form) | **PUT** /pdf/convert/xfatoacroform | Converts PDF document which contains XFA form (in request content) to PDF with AcroForm and uploads resulting file to storage.
[**put_xfa_pdf_in_storage_to_acro_form**](PdfApi.md#put_xfa_pdf_in_storage_to_acro_form) | **PUT** /pdf/\{name}/convert/xfatoacroform | Converts PDF document which contains XFA form (located on storage) to PDF with AcroForm and uploads resulting file to storage
[**put_xml_in_storage_to_pdf**](PdfApi.md#put_xml_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/xml | Convert XML file (located on storage) to PDF format and upload resulting file to storage. 
[**put_xps_in_storage_to_pdf**](PdfApi.md#put_xps_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/xps | Convert XPS file (located on storage) to PDF format and upload resulting file to storage. 
[**put_xsl_fo_in_storage_to_pdf**](PdfApi.md#put_xsl_fo_in_storage_to_pdf) | **PUT** /pdf/\{name}/create/xslfo | Convert XslFo file (located on storage) to PDF format and upload resulting file to storage. 
[**storage_exists**](PdfApi.md#storage_exists) | **GET** /pdf/storage/\{storageName}/exist | Check if storage exists
[**upload_file**](PdfApi.md#upload_file) | **PUT** /pdf/storage/file/\{path} | Upload file


# **copy_file**
> copy_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)

Copy file

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/folder/file.ext&#39; | 
 **dest_path** | **str**| Destination file path | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to copy | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_folder**
> copy_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)

Copy folder

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source folder path e.g. &#39;/src&#39; | 
 **dest_path** | **str**| Destination folder path e.g. &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> create_folder(path, storage_name=storage_name)

Create the folder

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path to create e.g. &#39;folder_1/folder_2/&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_annotation**
> AsposeResponse delete_annotation(name, annotation_id, storage=storage, folder=folder)

Delete document annotation by ID

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bookmark**
> AsposeResponse delete_bookmark(name, bookmark_path, folder=folder, storage=storage, password=password)

Delete document bookmark by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **bookmark_path** | **str**| The bookmark path. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_annotations**
> AsposeResponse delete_document_annotations(name, storage=storage, folder=folder)

Delete all annotations from the document

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_bookmarks**
> AsposeResponse delete_document_bookmarks(name, folder=folder, storage=storage, password=password)

Delete all document bookmarks.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_layer**
> AsposeResponse delete_document_layer(name, page_number, layer_id, folder=folder, storage=storage, pass_base64=pass_base64)

Remove document layer.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| Layer page. | 
 **layer_id** | **str**| Layer Id. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **pass_base64** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_link_annotations**
> AsposeResponse delete_document_link_annotations(name, storage=storage, folder=folder)

Delete all link annotations from the document

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_stamps**
> AsposeResponse delete_document_stamps(name, storage=storage, folder=folder, password=password)

Delete all stamps from the document

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_tables**
> AsposeResponse delete_document_tables(name, storage=storage, folder=folder)

Delete all tables from the document

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_field**
> AsposeResponse delete_field(name, field_name, storage=storage, folder=folder)

Delete document field by name.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name/ | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(path, storage_name=storage_name, version_id=version_id)

Delete file

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to delete | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> delete_folder(path, storage_name=storage_name, recursive=recursive)

Delete folder

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **recursive** | **bool**| Enable to delete folders, subfolders and files | [optional] [default to false]

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image**
> AsposeResponse delete_image(name, image_id, storage=storage, folder=folder)

Delete image from document page.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_link_annotation**
> AsposeResponse delete_link_annotation(name, link_id, storage=storage, folder=folder)

Delete document page link annotation by ID

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **link_id** | **str**| The link ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_page**
> AsposeResponse delete_page(name, page_number, storage=storage, folder=folder)

Delete document page by its number.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_page_annotations**
> AsposeResponse delete_page_annotations(name, page_number, storage=storage, folder=folder)

Delete all annotations from the page

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_page_link_annotations**
> AsposeResponse delete_page_link_annotations(name, page_number, storage=storage, folder=folder)

Delete all link annotations from the page

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_page_stamps**
> AsposeResponse delete_page_stamps(name, page_number, storage=storage, folder=folder, password=password)

Delete all stamps from the page

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_page_tables**
> AsposeResponse delete_page_tables(name, page_number, storage=storage, folder=folder)

Delete all tables from the page

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_properties**
> AsposeResponse delete_properties(name, storage=storage, folder=folder, password=password)

Delete custom document properties.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property**
> AsposeResponse delete_property(name, property_name, storage=storage, folder=folder, password=password)

Delete document property.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **property_name** | **str**| Property name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stamp**
> AsposeResponse delete_stamp(name, stamp_id, storage=storage, folder=folder, password=password)

Delete document stamp by ID

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **stamp_id** | **str**| The stamp ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_table**
> AsposeResponse delete_table(name, table_id, storage=storage, folder=folder)

Delete document table by ID

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_id** | **str**| The table ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> file download_file(path, storage_name=storage_name, version_id=version_id)

Download file

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to download | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bookmark**
> BookmarkResponse get_bookmark(name, bookmark_path, folder=folder, storage=storage, password=password)

Read document bookmark.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **bookmark_path** | **str**| The bookmark path. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**BookmarkResponse**](BookmarkResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bookmarks**
> BookmarksResponse get_bookmarks(name, bookmark_path, folder=folder, storage=storage, password=password)

Read document bookmarks node list.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **bookmark_path** | **str**| The bookmark path. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**BookmarksResponse**](BookmarksResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_caret_annotation**
> CaretAnnotationResponse get_caret_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page caret annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CaretAnnotationResponse**](CaretAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_check_box_field**
> CheckBoxFieldResponse get_check_box_field(name, field_name, storage=storage, folder=folder)

Read document checkbox field by name.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CheckBoxFieldResponse**](CheckBoxFieldResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_circle_annotation**
> CircleAnnotationResponse get_circle_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page circle annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CircleAnnotationResponse**](CircleAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_combo_box_field**
> ComboBoxFieldResponse get_combo_box_field(name, field_name, storage=storage, folder=folder)

Read document combobox field by name.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ComboBoxFieldResponse**](ComboBoxFieldResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disc_usage**
> DiscUsage get_disc_usage(storage_name=storage_name)

Get disc usage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**DiscUsage**](DiscUsage.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> DocumentResponse get_document(name, storage=storage, folder=folder, password=password)

Read common document info.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_annotations**
> AnnotationsInfoResponse get_document_annotations(name, storage=storage, folder=folder)

Read document page annotations. Returns only FreeTextAnnotations, TextAnnotations, other annotations will implemented next releases.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AnnotationsInfoResponse**](AnnotationsInfoResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_attachment_by_index**
> AttachmentResponse get_document_attachment_by_index(name, attachment_index, storage=storage, folder=folder)

Read document attachment info by its index.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **attachment_index** | **int**| The attachment index. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AttachmentResponse**](AttachmentResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_attachments**
> AttachmentsResponse get_document_attachments(name, storage=storage, folder=folder)

Read document attachments info.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AttachmentsResponse**](AttachmentsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_bookmarks**
> BookmarksResponse get_document_bookmarks(name, folder=folder, storage=storage, password=password)

Read document bookmarks tree.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**BookmarksResponse**](BookmarksResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_caret_annotations**
> CaretAnnotationsResponse get_document_caret_annotations(name, storage=storage, folder=folder)

Read document caret annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CaretAnnotationsResponse**](CaretAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_check_box_fields**
> CheckBoxFieldsResponse get_document_check_box_fields(name, storage=storage, folder=folder)

Read document checkbox fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CheckBoxFieldsResponse**](CheckBoxFieldsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_circle_annotations**
> CircleAnnotationsResponse get_document_circle_annotations(name, storage=storage, folder=folder)

Read document circle annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CircleAnnotationsResponse**](CircleAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_combo_box_fields**
> ComboBoxFieldsResponse get_document_combo_box_fields(name, storage=storage, folder=folder)

Read document combobox fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ComboBoxFieldsResponse**](ComboBoxFieldsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_display_properties**
> DisplayPropertiesResponse get_document_display_properties(name, storage=storage, folder=folder)

Read document display properties.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **storage** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**DisplayPropertiesResponse**](DisplayPropertiesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_file_attachment_annotations**
> FileAttachmentAnnotationsResponse get_document_file_attachment_annotations(name, storage=storage, folder=folder)

Read document FileAttachment annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FileAttachmentAnnotationsResponse**](FileAttachmentAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_free_text_annotations**
> FreeTextAnnotationsResponse get_document_free_text_annotations(name, storage=storage, folder=folder)

Read document free text annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FreeTextAnnotationsResponse**](FreeTextAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_highlight_annotations**
> HighlightAnnotationsResponse get_document_highlight_annotations(name, storage=storage, folder=folder)

Read document highlight annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**HighlightAnnotationsResponse**](HighlightAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_ink_annotations**
> InkAnnotationsResponse get_document_ink_annotations(name, storage=storage, folder=folder)

Read document ink annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**InkAnnotationsResponse**](InkAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_layers**
> DocumentLayers get_document_layers(name, folder=folder, storage=storage, pass_base64=pass_base64)

Gets document layers.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **pass_base64** | **str**| The password (Base64). | [optional] 

### Return type

[**DocumentLayers**](DocumentLayers.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_line_annotations**
> LineAnnotationsResponse get_document_line_annotations(name, storage=storage, folder=folder)

Read document line annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**LineAnnotationsResponse**](LineAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_list_box_fields**
> ListBoxFieldsResponse get_document_list_box_fields(name, storage=storage, folder=folder)

Read document listbox fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ListBoxFieldsResponse**](ListBoxFieldsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_movie_annotations**
> MovieAnnotationsResponse get_document_movie_annotations(name, storage=storage, folder=folder)

Read document movie annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**MovieAnnotationsResponse**](MovieAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_poly_line_annotations**
> PolyLineAnnotationsResponse get_document_poly_line_annotations(name, storage=storage, folder=folder)

Read document polyline annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**PolyLineAnnotationsResponse**](PolyLineAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_polygon_annotations**
> PolygonAnnotationsResponse get_document_polygon_annotations(name, storage=storage, folder=folder)

Read document polygon annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**PolygonAnnotationsResponse**](PolygonAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_popup_annotations**
> PopupAnnotationsResponse get_document_popup_annotations(name, storage=storage, folder=folder)

Read document popup annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**PopupAnnotationsResponse**](PopupAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_popup_annotations_by_parent**
> PopupAnnotationsResponse get_document_popup_annotations_by_parent(name, annotation_id, storage=storage, folder=folder)

Read document popup annotations by parent id.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The parent annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**PopupAnnotationsResponse**](PopupAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_properties**
> DocumentPropertiesResponse get_document_properties(name, storage=storage, folder=folder, password=password)

Read document properties.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**DocumentPropertiesResponse**](DocumentPropertiesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_property**
> DocumentPropertyResponse get_document_property(name, property_name, storage=storage, folder=folder, password=password)

Read document property by name.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **property_name** | **str**| Property name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**DocumentPropertyResponse**](DocumentPropertyResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_radio_button_fields**
> RadioButtonFieldsResponse get_document_radio_button_fields(name, storage=storage, folder=folder)

Read document radiobutton fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**RadioButtonFieldsResponse**](RadioButtonFieldsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_redaction_annotations**
> RedactionAnnotationsResponse get_document_redaction_annotations(name, storage=storage, folder=folder)

Read document redaction annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**RedactionAnnotationsResponse**](RedactionAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_screen_annotations**
> ScreenAnnotationsResponse get_document_screen_annotations(name, storage=storage, folder=folder)

Read document screen annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ScreenAnnotationsResponse**](ScreenAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_signature_fields**
> SignatureFieldsResponse get_document_signature_fields(name, storage=storage, folder=folder)

Read document signature fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SignatureFieldsResponse**](SignatureFieldsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_sound_annotations**
> SoundAnnotationsResponse get_document_sound_annotations(name, storage=storage, folder=folder)

Read document sound annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SoundAnnotationsResponse**](SoundAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_square_annotations**
> SquareAnnotationsResponse get_document_square_annotations(name, storage=storage, folder=folder)

Read document square annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SquareAnnotationsResponse**](SquareAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_squiggly_annotations**
> SquigglyAnnotationsResponse get_document_squiggly_annotations(name, storage=storage, folder=folder)

Read document squiggly annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SquigglyAnnotationsResponse**](SquigglyAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_stamp_annotations**
> StampAnnotationsResponse get_document_stamp_annotations(name, storage=storage, folder=folder)

Read document stamp annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**StampAnnotationsResponse**](StampAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_stamps**
> StampsInfoResponse get_document_stamps(name, storage=storage, folder=folder)

Read document stamps.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**StampsInfoResponse**](StampsInfoResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_strike_out_annotations**
> StrikeOutAnnotationsResponse get_document_strike_out_annotations(name, storage=storage, folder=folder)

Read document StrikeOut annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**StrikeOutAnnotationsResponse**](StrikeOutAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_tables**
> TablesRecognizedResponse get_document_tables(name, storage=storage, folder=folder)

Read document tables.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **storage** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**TablesRecognizedResponse**](TablesRecognizedResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_text_annotations**
> TextAnnotationsResponse get_document_text_annotations(name, storage=storage, folder=folder)

Read document text annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TextAnnotationsResponse**](TextAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_text_box_fields**
> TextBoxFieldsResponse get_document_text_box_fields(name, storage=storage, folder=folder)

Read document text box fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TextBoxFieldsResponse**](TextBoxFieldsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_underline_annotations**
> UnderlineAnnotationsResponse get_document_underline_annotations(name, storage=storage, folder=folder)

Read document underline annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**UnderlineAnnotationsResponse**](UnderlineAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_document_attachment_by_index**
> file get_download_document_attachment_by_index(name, attachment_index, storage=storage, folder=folder)

Download document attachment content by its index.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **attachment_index** | **int**| The attachment index. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_epub_in_storage_to_pdf**
> file get_epub_in_storage_to_pdf(src_path, storage=storage)

Convert EPUB file (located on storage) to PDF format and return resulting file in response. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.epub) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_export_fields_from_pdf_to_fdf_in_storage**
> file get_export_fields_from_pdf_to_fdf_in_storage(name, storage=storage, folder=folder)

Export fields from from PDF in storage to FDF file.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_export_fields_from_pdf_to_xfdf_in_storage**
> file get_export_fields_from_pdf_to_xfdf_in_storage(name, storage=storage, folder=folder)

Export fields from from PDF in storage to XFDF file.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_export_fields_from_pdf_to_xml_in_storage**
> file get_export_fields_from_pdf_to_xml_in_storage(name, storage=storage, folder=folder)

Export fields from from PDF in storage to XML file.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field**
> FieldResponse get_field(name, field_name, storage=storage, folder=folder)

Get document field by name.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name (name should be encoded). | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FieldResponse**](FieldResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields**
> FieldsResponse get_fields(name, storage=storage, folder=folder)

Get document fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FieldsResponse**](FieldsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_attachment_annotation**
> FileAttachmentAnnotationResponse get_file_attachment_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page FileAttachment annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FileAttachmentAnnotationResponse**](FileAttachmentAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_attachment_annotation_data**
> file get_file_attachment_annotation_data(name, annotation_id, storage=storage, folder=folder)

Read document page FileAttachment annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_versions**
> FileVersions get_file_versions(path, storage_name=storage_name)

Get file versions

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FileVersions**](FileVersions.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files_list**
> FilesList get_files_list(path, storage_name=storage_name)

Get all files and folders within a folder

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FilesList**](FilesList.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_free_text_annotation**
> FreeTextAnnotationResponse get_free_text_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page free text annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FreeTextAnnotationResponse**](FreeTextAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_highlight_annotation**
> HighlightAnnotationResponse get_highlight_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page highlight annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**HighlightAnnotationResponse**](HighlightAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_html_in_storage_to_pdf**
> file get_html_in_storage_to_pdf(src_path, html_file_name=html_file_name, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, storage=storage)

Convert HTML file (located on storage) to PDF format and return resulting file in response. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.zip) | 
 **html_file_name** | **str**| Name of HTML file in ZIP. | [optional] 
 **height** | **float**| Page height | [optional] 
 **width** | **float**| Page width | [optional] 
 **is_landscape** | **bool**| Is page landscaped | [optional] 
 **margin_left** | **float**| Page margin left | [optional] 
 **margin_bottom** | **float**| Page margin bottom | [optional] 
 **margin_right** | **float**| Page margin right | [optional] 
 **margin_top** | **float**| Page margin top | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image**
> ImageResponse get_image(name, image_id, storage=storage, folder=folder)

Read document image by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ImageResponse**](ImageResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_extract_as_gif**
> file get_image_extract_as_gif(name, image_id, width=width, height=height, storage=storage, folder=folder)

Extract document image in GIF format

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_extract_as_jpeg**
> file get_image_extract_as_jpeg(name, image_id, width=width, height=height, storage=storage, folder=folder)

Extract document image in JPEG format

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_extract_as_png**
> file get_image_extract_as_png(name, image_id, width=width, height=height, storage=storage, folder=folder)

Extract document image in PNG format

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_extract_as_tiff**
> file get_image_extract_as_tiff(name, image_id, width=width, height=height, storage=storage, folder=folder)

Extract document image in TIFF format

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> ImagesResponse get_images(name, page_number, storage=storage, folder=folder)

Read document images.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ImagesResponse**](ImagesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_fields_from_fdf_in_storage**
> file get_import_fields_from_fdf_in_storage(name, fdf_file_path, storage=storage, folder=folder)

Update fields from FDF file in storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **fdf_file_path** | **str**| The Fdf file path. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_fields_from_xfdf_in_storage**
> file get_import_fields_from_xfdf_in_storage(name, xfdf_file_path, storage=storage, folder=folder)

Update fields from XFDF file in storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **xfdf_file_path** | **str**| The XFDF file path. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_fields_from_xml_in_storage**
> file get_import_fields_from_xml_in_storage(name, xml_file_path, storage=storage, folder=folder)

Import from XML file (located on storage) to PDF format and return resulting file in response. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **xml_file_path** | **str**| Full source filename (ex. /folder1/folder2/template.xml) | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ink_annotation**
> InkAnnotationResponse get_ink_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page ink annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**InkAnnotationResponse**](InkAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_line_annotation**
> LineAnnotationResponse get_line_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page line annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**LineAnnotationResponse**](LineAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link_annotation**
> LinkAnnotationResponse get_link_annotation(name, link_id, storage=storage, folder=folder)

Read document link annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **link_id** | **str**| The link ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**LinkAnnotationResponse**](LinkAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_box_field**
> ListBoxFieldResponse get_list_box_field(name, field_name, storage=storage, folder=folder)

Read document listbox field by name.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ListBoxFieldResponse**](ListBoxFieldResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_markdown_in_storage_to_pdf**
> file get_markdown_in_storage_to_pdf(src_path, storage=storage)

Convert MD file (located on storage) to PDF format and return resulting file in response. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.md) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mht_in_storage_to_pdf**
> file get_mht_in_storage_to_pdf(src_path, storage=storage)

Convert MHT file (located on storage) to PDF format and return resulting file in response. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.mht) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_movie_annotation**
> MovieAnnotationResponse get_movie_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page movie annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**MovieAnnotationResponse**](MovieAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page**
> DocumentPageResponse get_page(name, page_number, storage=storage, folder=folder)

Read document page info.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**DocumentPageResponse**](DocumentPageResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_annotations**
> AnnotationsInfoResponse get_page_annotations(name, page_number, storage=storage, folder=folder)

Read document page annotations. Returns only FreeTextAnnotations, TextAnnotations, other annotations will implemented next releases.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AnnotationsInfoResponse**](AnnotationsInfoResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_caret_annotations**
> CaretAnnotationsResponse get_page_caret_annotations(name, page_number, storage=storage, folder=folder)

Read document page caret annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CaretAnnotationsResponse**](CaretAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_check_box_fields**
> CheckBoxFieldsResponse get_page_check_box_fields(name, page_number, storage=storage, folder=folder)

Read document page checkbox fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CheckBoxFieldsResponse**](CheckBoxFieldsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_circle_annotations**
> CircleAnnotationsResponse get_page_circle_annotations(name, page_number, storage=storage, folder=folder)

Read document page circle annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CircleAnnotationsResponse**](CircleAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_combo_box_fields**
> ComboBoxFieldsResponse get_page_combo_box_fields(name, page_number, storage=storage, folder=folder)

Read document page combobox fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ComboBoxFieldsResponse**](ComboBoxFieldsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_convert_to_bmp**
> file get_page_convert_to_bmp(name, page_number, width=width, height=height, folder=folder, storage=storage, password=password)

Convert document page to Bmp image and return resulting file in response.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_convert_to_emf**
> file get_page_convert_to_emf(name, page_number, width=width, height=height, folder=folder, storage=storage, password=password)

Convert document page to Emf image and return resulting file in response.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_convert_to_gif**
> file get_page_convert_to_gif(name, page_number, width=width, height=height, folder=folder, storage=storage, password=password)

Convert document page to Gif image and return resulting file in response.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_convert_to_jpeg**
> file get_page_convert_to_jpeg(name, page_number, width=width, height=height, folder=folder, storage=storage, password=password)

Convert document page to Jpeg image and return resulting file in response.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_convert_to_png**
> file get_page_convert_to_png(name, page_number, width=width, height=height, folder=folder, storage=storage, password=password)

Convert document page to Png image and return resulting file in response.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_convert_to_tiff**
> file get_page_convert_to_tiff(name, page_number, width=width, height=height, folder=folder, storage=storage, password=password)

Convert document page to Tiff image  and return resulting file in response.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_file_attachment_annotations**
> FileAttachmentAnnotationsResponse get_page_file_attachment_annotations(name, page_number, storage=storage, folder=folder)

Read document page FileAttachment annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FileAttachmentAnnotationsResponse**](FileAttachmentAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_free_text_annotations**
> FreeTextAnnotationsResponse get_page_free_text_annotations(name, page_number, storage=storage, folder=folder)

Read document page free text annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FreeTextAnnotationsResponse**](FreeTextAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_highlight_annotations**
> HighlightAnnotationsResponse get_page_highlight_annotations(name, page_number, storage=storage, folder=folder)

Read document page highlight annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**HighlightAnnotationsResponse**](HighlightAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_ink_annotations**
> InkAnnotationsResponse get_page_ink_annotations(name, page_number, storage=storage, folder=folder)

Read document page ink annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**InkAnnotationsResponse**](InkAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_line_annotations**
> LineAnnotationsResponse get_page_line_annotations(name, page_number, storage=storage, folder=folder)

Read document page line annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**LineAnnotationsResponse**](LineAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_link_annotation**
> LinkAnnotationResponse get_page_link_annotation(name, page_number, link_id, storage=storage, folder=folder)

Read document page link annotation by ID.

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

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_link_annotations**
> LinkAnnotationsResponse get_page_link_annotations(name, page_number, storage=storage, folder=folder)

Read document page link annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**LinkAnnotationsResponse**](LinkAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_list_box_fields**
> ListBoxFieldsResponse get_page_list_box_fields(name, page_number, storage=storage, folder=folder)

Read document page listbox fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ListBoxFieldsResponse**](ListBoxFieldsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_movie_annotations**
> MovieAnnotationsResponse get_page_movie_annotations(name, page_number, storage=storage, folder=folder)

Read document page movie annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**MovieAnnotationsResponse**](MovieAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_poly_line_annotations**
> PolyLineAnnotationsResponse get_page_poly_line_annotations(name, page_number, storage=storage, folder=folder)

Read document page polyline annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**PolyLineAnnotationsResponse**](PolyLineAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_polygon_annotations**
> PolygonAnnotationsResponse get_page_polygon_annotations(name, page_number, storage=storage, folder=folder)

Read document page polygon annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**PolygonAnnotationsResponse**](PolygonAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_popup_annotations**
> PopupAnnotationsResponse get_page_popup_annotations(name, page_number, storage=storage, folder=folder)

Read document page popup annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**PopupAnnotationsResponse**](PopupAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_radio_button_fields**
> RadioButtonFieldsResponse get_page_radio_button_fields(name, page_number, storage=storage, folder=folder)

Read document page radiobutton fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**RadioButtonFieldsResponse**](RadioButtonFieldsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_redaction_annotations**
> RedactionAnnotationsResponse get_page_redaction_annotations(name, page_number, storage=storage, folder=folder)

Read document page redaction annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**RedactionAnnotationsResponse**](RedactionAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_screen_annotations**
> ScreenAnnotationsResponse get_page_screen_annotations(name, page_number, storage=storage, folder=folder)

Read document page screen annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ScreenAnnotationsResponse**](ScreenAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_signature_fields**
> SignatureFieldsResponse get_page_signature_fields(name, page_number, storage=storage, folder=folder)

Read document page signature fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SignatureFieldsResponse**](SignatureFieldsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_sound_annotations**
> SoundAnnotationsResponse get_page_sound_annotations(name, page_number, storage=storage, folder=folder)

Read document page sound annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SoundAnnotationsResponse**](SoundAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_square_annotations**
> SquareAnnotationsResponse get_page_square_annotations(name, page_number, storage=storage, folder=folder)

Read document page square annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SquareAnnotationsResponse**](SquareAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_squiggly_annotations**
> SquigglyAnnotationsResponse get_page_squiggly_annotations(name, page_number, storage=storage, folder=folder)

Read document page squiggly annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SquigglyAnnotationsResponse**](SquigglyAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_stamp_annotations**
> StampAnnotationsResponse get_page_stamp_annotations(name, page_number, storage=storage, folder=folder)

Read document page stamp annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**StampAnnotationsResponse**](StampAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_stamps**
> StampsInfoResponse get_page_stamps(name, page_number, storage=storage, folder=folder, password=password)

Read page document stamps.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

[**StampsInfoResponse**](StampsInfoResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_strike_out_annotations**
> StrikeOutAnnotationsResponse get_page_strike_out_annotations(name, page_number, storage=storage, folder=folder)

Read document page StrikeOut annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**StrikeOutAnnotationsResponse**](StrikeOutAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_tables**
> TablesRecognizedResponse get_page_tables(name, page_number, storage=storage, folder=folder)

Read document page tables.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **page_number** | **int**|  | 
 **storage** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**TablesRecognizedResponse**](TablesRecognizedResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_text**
> TextRectsResponse get_page_text(name, page_number, llx, lly, urx, ury, format=format, regex=regex, split_rects=split_rects, folder=folder, storage=storage)

Read page text items.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| Number of page (starting from 1). | 
 **llx** | **float**| X-coordinate of lower - left corner. | 
 **lly** | **float**| Y - coordinate of lower-left corner. | 
 **urx** | **float**| X - coordinate of upper-right corner. | 
 **ury** | **float**| Y - coordinate of upper-right corner. | 
 **format** | **list[str]**| List of formats for search. | [optional] 
 **regex** | **str**| Formats are specified as a regular expression. | [optional] 
 **split_rects** | **bool**| Split result fragments (default is true). | [optional] [default to true]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**TextRectsResponse**](TextRectsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_text_annotations**
> TextAnnotationsResponse get_page_text_annotations(name, page_number, storage=storage, folder=folder)

Read document page text annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TextAnnotationsResponse**](TextAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_text_box_fields**
> TextBoxFieldsResponse get_page_text_box_fields(name, page_number, storage=storage, folder=folder)

Read document page text box fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TextBoxFieldsResponse**](TextBoxFieldsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_underline_annotations**
> UnderlineAnnotationsResponse get_page_underline_annotations(name, page_number, storage=storage, folder=folder)

Read document page underline annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**UnderlineAnnotationsResponse**](UnderlineAnnotationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages**
> DocumentPagesResponse get_pages(name, storage=storage, folder=folder)

Read document pages info.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**DocumentPagesResponse**](DocumentPagesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pcl_in_storage_to_pdf**
> file get_pcl_in_storage_to_pdf(src_path, storage=storage)

Convert PCL file (located on storage) to PDF format and return resulting file in response. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.pcl) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_a_in_storage_to_pdf**
> file get_pdf_a_in_storage_to_pdf(src_path, dont_optimize=dont_optimize, storage=storage)

Convert PDFA file (located on storage) to PDF format and return resulting file in response. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.pdf) | 
 **dont_optimize** | **bool**| If set, document resources will not be optimized. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_doc**
> file get_pdf_in_storage_to_doc(name, add_return_to_line_end=add_return_to_line_end, format=format, image_resolution_x=image_resolution_x, image_resolution_y=image_resolution_y, max_distance_between_text_lines=max_distance_between_text_lines, mode=mode, recognize_bullets=recognize_bullets, relative_horizontal_proximity=relative_horizontal_proximity, folder=folder, storage=storage, password=password)

Converts PDF document (located on storage) to DOC format and returns resulting file in response content.

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
 **password** | **str**| The password (Base64). | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_epub**
> file get_pdf_in_storage_to_epub(name, content_recognition_mode=content_recognition_mode, folder=folder, storage=storage)

Converts PDF document (located on storage) to EPUB format and returns resulting file in response content

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **content_recognition_mode** | **str**| Property tunes conversion for this or that desirable method of recognition of content. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_html**
> file get_pdf_in_storage_to_html(name, additional_margin_width_in_points=additional_margin_width_in_points, compress_svg_graphics_if_any=compress_svg_graphics_if_any, convert_marked_content_to_layers=convert_marked_content_to_layers, default_font_name=default_font_name, document_type=document_type, fixed_layout=fixed_layout, image_resolution=image_resolution, minimal_line_width=minimal_line_width, prevent_glyphs_grouping=prevent_glyphs_grouping, split_css_into_pages=split_css_into_pages, split_into_pages=split_into_pages, use_z_order=use_z_order, antialiasing_processing=antialiasing_processing, css_class_names_prefix=css_class_names_prefix, explicit_list_of_saved_pages=explicit_list_of_saved_pages, font_encoding_strategy=font_encoding_strategy, font_saving_mode=font_saving_mode, html_markup_generation_mode=html_markup_generation_mode, letters_positioning_method=letters_positioning_method, pages_flow_type_depends_on_viewers_screen_size=pages_flow_type_depends_on_viewers_screen_size, parts_embedding_mode=parts_embedding_mode, raster_images_saving_mode=raster_images_saving_mode, remove_empty_areas_on_top_and_bottom=remove_empty_areas_on_top_and_bottom, save_shadowed_texts_as_transparent_texts=save_shadowed_texts_as_transparent_texts, save_transparent_texts=save_transparent_texts, special_folder_for_all_images=special_folder_for_all_images, special_folder_for_svg_images=special_folder_for_svg_images, try_save_text_underlining_and_strikeouting_in_css=try_save_text_underlining_and_strikeouting_in_css, folder=folder, storage=storage, flow_layout_paragraph_full_width=flow_layout_paragraph_full_width)

Converts PDF document (located on storage) to Html format and returns resulting file in response content

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **additional_margin_width_in_points** | **int**| Defines width of margin that will be forcibly left around that output HTML-areas. | [optional] 
 **compress_svg_graphics_if_any** | **bool**| The flag that indicates whether found SVG graphics(if any) will be compressed(zipped) into SVGZ format during saving. | [optional] 
 **convert_marked_content_to_layers** | **bool**| If attribute ConvertMarkedContentToLayers set to true then an all elements inside a PDF marked content (layer) will be put into an HTML div with &quot;data-pdflayer&quot; attribute specifying a layer name. This layer name will be extracted from optional properties of PDF marked content. If this attribute is false (by default) then no any layers will be created from PDF marked content. | [optional] 
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
 **css_class_names_prefix** | **str**| When PDFtoHTML converter generates result CSSs, CSS class names (something like &quot;.stl_01 {}&quot; ... &quot;.stl_NN {}) are generated and used in result CSS. This property allows forcibly set class name prefix. | [optional] 
 **explicit_list_of_saved_pages** | **list[int]**| With this property You can explicitely define what pages of document should be converted. Pages in this list must have 1-based numbers. I.e. valid numbers of pages must be taken from range (1...[NumberOfPagesInConvertedDocument]) Order of appearing of pages in this list does not affect their order in result HTML page(s) - in result pages allways will go in order in which they are present in source PDF. | [optional] 
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
 **flow_layout_paragraph_full_width** | **bool**| This attribute specifies full width paragraph text for Flow mode, FixedLayout &#x3D; false. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_mobi_xml**
> file get_pdf_in_storage_to_mobi_xml(name, folder=folder, storage=storage)

Converts PDF document (located on storage) to MOBIXML format and returns resulting ZIP archive file in response content.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_pdf_a**
> file get_pdf_in_storage_to_pdf_a(name, type, folder=folder, storage=storage, password=password)

Converts PDF document (located on storage) to PdfA format and returns resulting file in response content

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **type** | **str**| Type of PdfA format. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_pptx**
> file get_pdf_in_storage_to_pptx(name, separate_images=separate_images, slides_as_images=slides_as_images, folder=folder, storage=storage, password=password)

Converts PDF document (located on storage) to PPTX format and returns resulting file in response content

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **separate_images** | **bool**| Separate images. | [optional] 
 **slides_as_images** | **bool**| Slides as images. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_svg**
> file get_pdf_in_storage_to_svg(name, compress_output_to_zip_archive=compress_output_to_zip_archive, folder=folder, storage=storage, password=password)

Converts PDF document (located on storage) to SVG format and returns resulting file in response content

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **compress_output_to_zip_archive** | **bool**| Specifies whether output will be created as one zip-archive. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_te_x**
> file get_pdf_in_storage_to_te_x(name, folder=folder, storage=storage)

Converts PDF document (located on storage) to TeX format and returns resulting file in response content

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_text**
> file get_pdf_in_storage_to_text(name, folder=folder, storage=storage)

Converts PDF document (located on storage) to Text format and returns resulting file in response content

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_tiff**
> file get_pdf_in_storage_to_tiff(name, brightness=brightness, compression=compression, color_depth=color_depth, left_margin=left_margin, right_margin=right_margin, top_margin=top_margin, bottom_margin=bottom_margin, orientation=orientation, skip_blank_pages=skip_blank_pages, width=width, height=height, x_resolution=x_resolution, y_resolution=y_resolution, page_index=page_index, page_count=page_count, folder=folder, storage=storage)

Converts PDF document (located on storage) to TIFF format and returns resulting file in response content

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

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_xls**
> file get_pdf_in_storage_to_xls(name, insert_blank_column_at_first=insert_blank_column_at_first, minimize_the_number_of_worksheets=minimize_the_number_of_worksheets, scale_factor=scale_factor, uniform_worksheets=uniform_worksheets, folder=folder, storage=storage, password=password)

Converts PDF document (located on storage) to XLS format and returns resulting file in response content

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **insert_blank_column_at_first** | **bool**| Insert blank column at first | [optional] 
 **minimize_the_number_of_worksheets** | **bool**| Minimize the number of worksheets | [optional] 
 **scale_factor** | **float**| Scale factor (Obsolete) | [optional] 
 **uniform_worksheets** | **bool**| Uniform worksheets | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_xlsx**
> file get_pdf_in_storage_to_xlsx(name, insert_blank_column_at_first=insert_blank_column_at_first, minimize_the_number_of_worksheets=minimize_the_number_of_worksheets, scale_factor=scale_factor, uniform_worksheets=uniform_worksheets, folder=folder, storage=storage, password=password)

Converts PDF document (located on storage) to XLSX format and returns resulting file in response content

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **insert_blank_column_at_first** | **bool**| Insert blank column at first | [optional] 
 **minimize_the_number_of_worksheets** | **bool**| Minimize the number of worksheets | [optional] 
 **scale_factor** | **float**| Scale factor (Obsolete) | [optional] 
 **uniform_worksheets** | **bool**| Uniform worksheets | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_xml**
> file get_pdf_in_storage_to_xml(name, folder=folder, storage=storage)

Converts PDF document (located on storage) to XML format and returns resulting file in response content

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_in_storage_to_xps**
> file get_pdf_in_storage_to_xps(name, folder=folder, storage=storage)

Converts PDF document (located on storage) to XPS format and returns resulting file in response content

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_poly_line_annotation**
> PolyLineAnnotationResponse get_poly_line_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page polyline annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**PolyLineAnnotationResponse**](PolyLineAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_polygon_annotation**
> PolygonAnnotationResponse get_polygon_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page polygon annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**PolygonAnnotationResponse**](PolygonAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_popup_annotation**
> PopupAnnotationResponse get_popup_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page popup annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**PopupAnnotationResponse**](PopupAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ps_in_storage_to_pdf**
> file get_ps_in_storage_to_pdf(src_path, storage=storage)

Convert PS file (located on storage) to PDF format and return resulting file in response. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.ps) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_radio_button_field**
> RadioButtonFieldResponse get_radio_button_field(name, field_name, storage=storage, folder=folder)

Read document RadioButton field by name.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**RadioButtonFieldResponse**](RadioButtonFieldResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_redaction_annotation**
> RedactionAnnotationResponse get_redaction_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page redaction annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**RedactionAnnotationResponse**](RedactionAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_annotation**
> ScreenAnnotationResponse get_screen_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page screen annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ScreenAnnotationResponse**](ScreenAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_annotation_data**
> file get_screen_annotation_data(name, annotation_id, storage=storage, folder=folder)

Read document page screen annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signature_field**
> SignatureFieldResponse get_signature_field(name, field_name, storage=storage, folder=folder)

Read document signature field by name.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SignatureFieldResponse**](SignatureFieldResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sound_annotation**
> SoundAnnotationResponse get_sound_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page sound annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SoundAnnotationResponse**](SoundAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sound_annotation_data**
> file get_sound_annotation_data(name, annotation_id, storage=storage, folder=folder)

Read document page sound annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_square_annotation**
> SquareAnnotationResponse get_square_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page square annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SquareAnnotationResponse**](SquareAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_squiggly_annotation**
> SquigglyAnnotationResponse get_squiggly_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page squiggly annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SquigglyAnnotationResponse**](SquigglyAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stamp_annotation**
> StampAnnotationResponse get_stamp_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page stamp annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**StampAnnotationResponse**](StampAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stamp_annotation_data**
> file get_stamp_annotation_data(name, annotation_id, storage=storage, folder=folder)

Read document page stamp annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_strike_out_annotation**
> StrikeOutAnnotationResponse get_strike_out_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page StrikeOut annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**StrikeOutAnnotationResponse**](StrikeOutAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_svg_in_storage_to_pdf**
> file get_svg_in_storage_to_pdf(src_path, adjust_page_size=adjust_page_size, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, storage=storage)

Convert SVG file (located on storage) to PDF format and return resulting file in response. 

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

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table**
> TableRecognizedResponse get_table(name, table_id, storage=storage, folder=folder)

Read document page table by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_id** | **str**| The table ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TableRecognizedResponse**](TableRecognizedResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_te_x_in_storage_to_pdf**
> file get_te_x_in_storage_to_pdf(src_path, storage=storage)

Convert TeX file (located on storage) to PDF format and return resulting file in response. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.tex) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_text**
> TextRectsResponse get_text(name, llx, lly, urx, ury, format=format, regex=regex, split_rects=split_rects, folder=folder, storage=storage)

Read document text.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **llx** | **float**| X-coordinate of lower - left corner. | 
 **lly** | **float**| Y - coordinate of lower-left corner. | 
 **urx** | **float**| X - coordinate of upper-right corner. | 
 **ury** | **float**| Y - coordinate of upper-right corner. | 
 **format** | **list[str]**| List of formats for search. | [optional] 
 **regex** | **str**| Formats are specified as a regular expression. | [optional] 
 **split_rects** | **bool**| Split result fragments (default is true). | [optional] [default to true]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**TextRectsResponse**](TextRectsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_text_annotation**
> TextAnnotationResponse get_text_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page text annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TextAnnotationResponse**](TextAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_text_box_field**
> TextBoxFieldResponse get_text_box_field(name, field_name, storage=storage, folder=folder)

Read document text box field by name.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TextBoxFieldResponse**](TextBoxFieldResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_underline_annotation**
> UnderlineAnnotationResponse get_underline_annotation(name, annotation_id, storage=storage, folder=folder)

Read document page underline annotation by ID.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**UnderlineAnnotationResponse**](UnderlineAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_verify_signature**
> SignatureVerifyResponse get_verify_signature(name, sign_name, storage=storage, folder=folder)

Verify signature document.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **sign_name** | **str**| Sign name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SignatureVerifyResponse**](SignatureVerifyResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_in_storage_to_pdf**
> file get_web_in_storage_to_pdf(url, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, storage=storage)

Convert web page to PDF format and return resulting file in response. 

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

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_words_per_page**
> WordCountResponse get_words_per_page(name, storage=storage, folder=folder)

Get number of words per document page.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**WordCountResponse**](WordCountResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xfa_pdf_in_storage_to_acro_form**
> file get_xfa_pdf_in_storage_to_acro_form(name, folder=folder, storage=storage)

Converts PDF document which contains XFA form (located on storage) to PDF with AcroForm and returns resulting file response content

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xml_in_storage_to_pdf**
> file get_xml_in_storage_to_pdf(src_path, xsl_file_path=xsl_file_path, storage=storage)

Convert XML file (located on storage) to PDF format and return resulting file in response. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.xml) | 
 **xsl_file_path** | **str**| Full XSL source filename (ex. /folder1/folder2/template.xsl) | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xmp_metadata_json**
> XmpMetadata get_xmp_metadata_json(name, folder=folder, storage=storage, pass_base64=pass_base64)

Gets document XMP Metadata as JSON.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **pass_base64** | **str**| The password (Base64). | [optional] 

### Return type

[**XmpMetadata**](XmpMetadata.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xmp_metadata_xml**
> file get_xmp_metadata_xml(name, folder=folder, storage=storage, pass_base64=pass_base64)

Gets document XMP Metadata as XML file.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **pass_base64** | **str**| The password (Base64). | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xps_in_storage_to_pdf**
> file get_xps_in_storage_to_pdf(src_path, storage=storage)

Convert XPS file (located on storage) to PDF format and return resulting file in response. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.xps) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xsl_fo_in_storage_to_pdf**
> file get_xsl_fo_in_storage_to_pdf(src_path, storage=storage)

Convert XslFo file (located on storage) to PDF format and return resulting file in response. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.xslfo) | 
 **storage** | **str**| The document storage. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_file**
> move_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)

Move file

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/src.ext&#39; | 
 **dest_path** | **str**| Destination file path e.g. &#39;/dest.ext&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to move | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_folder**
> move_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)

Move folder

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Folder path to move e.g. &#39;/folder&#39; | 
 **dest_path** | **str**| Destination folder path to move to e.g &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_exists**
> ObjectExist object_exists(path, storage_name=storage_name, version_id=version_id)

Check if file or folder exists

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File or folder path e.g. &#39;/file.ext&#39; or &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID | [optional] 

### Return type

[**ObjectExist**](ObjectExist.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_add_document_attachment**
> AttachmentsResponse post_add_document_attachment(name, attachment_info, storage=storage, folder=folder)

Adds a file attachment to the PDF document.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **attachment_info** | [**AttachmentInfo**](AttachmentInfo.md)| AttachmentInfoAttachmentInfo instance. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AttachmentsResponse**](AttachmentsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_append_document**
> DocumentResponse post_append_document(name, append_file, start_page=start_page, end_page=end_page, storage=storage, folder=folder)

Append document to existing one.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The original document name. | 
 **append_file** | **str**| Append file server path. | 
 **start_page** | **int**| Appending start page. | [optional] [default to 0]
 **end_page** | **int**| Appending end page. | [optional] [default to 0]
 **storage** | **str**| The documents storage. | [optional] 
 **folder** | **str**| The original document folder. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_bookmark**
> BookmarksResponse post_bookmark(name, bookmark_path, bookmarks, folder=folder, storage=storage, password=password)

Add document bookmarks.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **bookmark_path** | **str**| The parent bookmark path. Specify an empty string when adding a bookmark to the root. | 
 **bookmarks** | [**list[Bookmark]**](Bookmark.md)| The array of bookmark. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**BookmarksResponse**](BookmarksResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_change_password_document_in_storage**
> AsposeResponse post_change_password_document_in_storage(name, owner_password, new_user_password, new_owner_password, storage=storage, folder=folder)

Change document password in storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **owner_password** | **str**| Owner password (encrypted Base64). | 
 **new_user_password** | **str**| New user password (encrypted Base64). | 
 **new_owner_password** | **str**| New owner password (encrypted Base64). | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_check_box_fields**
> AsposeResponse post_check_box_fields(name, fields, storage=storage, folder=folder)

Add document checkbox fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **fields** | [**list[CheckBoxField]**](CheckBoxField.md)| The array of field. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_combo_box_fields**
> AsposeResponse post_combo_box_fields(name, fields, storage=storage, folder=folder)

Add document combobox fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **fields** | [**list[ComboBoxField]**](ComboBoxField.md)| The array of field. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_document**
> DocumentResponse post_create_document(name, document_config, storage=storage, folder=folder)

Create empty document.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The new document name. | 
 **document_config** | [**DocumentConfig**](DocumentConfig.md)| The document config for new document. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The new document folder. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_field**
> AsposeResponse post_create_field(name, page, field, storage=storage, folder=folder)

Create field.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page** | **int**| Document page number. | 
 **field** | [**Field**](Field.md)| Field with the field data. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_decrypt_document_in_storage**
> AsposeResponse post_decrypt_document_in_storage(name, password, storage=storage, folder=folder)

Decrypt document in storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **password** | **str**| The password (encrypted Base64). | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_image_footer**
> AsposeResponse post_document_image_footer(name, image_footer, start_page_number=start_page_number, end_page_number=end_page_number, storage=storage, folder=folder)

Add document image footer.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_footer** | [**ImageFooter**](ImageFooter.md)| The image footer. | 
 **start_page_number** | **int**| The start page number. | [optional] 
 **end_page_number** | **int**| The end page number. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_image_header**
> AsposeResponse post_document_image_header(name, image_header, start_page_number=start_page_number, end_page_number=end_page_number, storage=storage, folder=folder)

Add document image header.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_header** | [**ImageHeader**](ImageHeader.md)| The image header. | 
 **start_page_number** | **int**| The start page number. | [optional] 
 **end_page_number** | **int**| The end page number. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_image_stamps**
> AsposeResponse post_document_image_stamps(name, stamps, storage=storage, folder=folder, password=password)

Add document pages image stamps.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **stamps** | [**list[ImageStamp]**](ImageStamp.md)| The array of stamp. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_page_number_stamps**
> AsposeResponse post_document_page_number_stamps(name, stamp, start_page_number=start_page_number, end_page_number=end_page_number, storage=storage, folder=folder, password=password)

Add document page number stamps.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **stamp** | [**PageNumberStamp**](PageNumberStamp.md)| The stamp. | 
 **start_page_number** | **int**| The start page number. | [optional] 
 **end_page_number** | **int**| The end page number. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_text_footer**
> AsposeResponse post_document_text_footer(name, text_footer, start_page_number=start_page_number, end_page_number=end_page_number, storage=storage, folder=folder)

Add document text footer.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **text_footer** | [**TextFooter**](TextFooter.md)| The text footer. | 
 **start_page_number** | **int**| The start page number. | [optional] 
 **end_page_number** | **int**| The end page number. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_text_header**
> AsposeResponse post_document_text_header(name, text_header, start_page_number=start_page_number, end_page_number=end_page_number, storage=storage, folder=folder)

Add document text header.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **text_header** | [**TextHeader**](TextHeader.md)| The text header. | 
 **start_page_number** | **int**| The start page number. | [optional] 
 **end_page_number** | **int**| The end page number. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_text_replace**
> TextReplaceResponse post_document_text_replace(name, text_replace, storage=storage, folder=folder)

Document's replace text method.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **text_replace** | [**TextReplaceListRequest**](TextReplaceListRequest.md)|  | 
 **storage** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 

### Return type

[**TextReplaceResponse**](TextReplaceResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_text_stamps**
> AsposeResponse post_document_text_stamps(name, stamps, storage=storage, folder=folder, password=password)

Add document pages text stamps.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **stamps** | [**list[TextStamp]**](TextStamp.md)| The array of stamp. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_encrypt_document_in_storage**
> AsposeResponse post_encrypt_document_in_storage(name, user_password, owner_password, crypto_algorithm, permissions_flags=permissions_flags, use_pdf20=use_pdf20, storage=storage, folder=folder)

Encrypt document in storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **user_password** | **str**| User password (encrypted Base64). | 
 **owner_password** | **str**| Owner password (encrypted Base64). | 
 **crypto_algorithm** | **str**| Cryptographic algorithm, see CryptoAlgorithm for details. | 
 **permissions_flags** | [**list[PermissionsFlags]**](PermissionsFlags.md)| Array of document permissions, see PermissionsFlags for details. | [optional] 
 **use_pdf20** | **bool**| Support for revision 6 (Extension 8). | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_flatten_document**
> AsposeResponse post_flatten_document(name, update_appearances=update_appearances, call_events=call_events, hide_buttons=hide_buttons, storage=storage, folder=folder)

Flatten the document.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **update_appearances** | **bool**| If set, all field appearances will be regenerated before flattening. This option may help if field is incorrectly flattened. This option may decrease performance.. | [optional] 
 **call_events** | **bool**| If set, formatting and other JavaScript events will be called. | [optional] 
 **hide_buttons** | **bool**| If set, buttons will be removed from flattened document. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_html_to_pdf**
> file post_html_to_pdf(html_file_name=html_file_name, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top)

Convert HTML file (zip archive in request content) to PDF format and return resulting file in response. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **html_file_name** | **str**| Name of HTML file in ZIP. | [optional] 
 **height** | **float**| Page height | [optional] 
 **width** | **float**| Page width | [optional] 
 **is_landscape** | **bool**| Is page landscaped | [optional] 
 **margin_left** | **float**| Page margin left | [optional] 
 **margin_bottom** | **float**| Page margin bottom | [optional] 
 **margin_right** | **float**| Page margin right | [optional] 
 **margin_top** | **float**| Page margin top | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_import_fields_from_fdf**
> AsposeResponse post_import_fields_from_fdf(name, storage=storage, folder=folder, fdf_data=fdf_data)

Update fields from FDF file in request.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **fdf_data** | **file**| Fdf file. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_import_fields_from_xfdf**
> AsposeResponse post_import_fields_from_xfdf(name, storage=storage, folder=folder, xfdf_data=xfdf_data)

Update fields from XFDF file in request.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **xfdf_data** | **file**| Xfdf file. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_import_fields_from_xml**
> AsposeResponse post_import_fields_from_xml(name, storage=storage, folder=folder, xml_data=xml_data)

Update fields from XML file in request.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **xml_data** | **file**| Xml file. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_insert_image**
> AsposeResponse post_insert_image(name, page_number, llx, lly, urx, ury, image_file_path=image_file_path, storage=storage, folder=folder, image=image)

Insert image to document page.

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

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_list_box_fields**
> AsposeResponse post_list_box_fields(name, fields, storage=storage, folder=folder)

Add document listbox fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **fields** | [**list[ListBoxField]**](ListBoxField.md)| The array of field. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_move_page**
> AsposeResponse post_move_page(name, page_number, new_index, storage=storage, folder=folder)

Move page to new position.

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

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_optimize_document**
> AsposeResponse post_optimize_document(name, options, storage=storage, folder=folder)

Optimize document.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **options** | [**OptimizeOptions**](OptimizeOptions.md)| The optimization options. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organize_document**
> AsposeResponse post_organize_document(name, pages, out_path, storage=storage, folder=folder)

Merge selected pages of a document.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The original document name. | 
 **pages** | **str**| 1-based page numbers of the source document that make up the resulting document. | 
 **out_path** | **str**| Full filename of the resulting document. | 
 **storage** | **str**| The documents storage. | [optional] 
 **folder** | **str**| The source document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organize_documents**
> AsposeResponse post_organize_documents(organize_documents, out_path, storage=storage)

Merge selected pages of different documents.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organize_documents** | [**OrganizeDocumentRequest**](OrganizeDocumentRequest.md)| Array of OrganizeDocumentData to make up the resulting document. | 
 **out_path** | **str**| Full filename of the resulting document. | 
 **storage** | **str**| The documents storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_caret_annotations**
> AsposeResponse post_page_caret_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page caret annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[CaretAnnotation]**](CaretAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_certify**
> AsposeResponse post_page_certify(name, page_number, sign, doc_mdp_access_permission_type, storage=storage, folder=folder)

Certify document page.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **sign** | [**Signature**](Signature.md)| Signature object containing signature data. | 
 **doc_mdp_access_permission_type** | **str**| The access permissions granted for this document. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_circle_annotations**
> AsposeResponse post_page_circle_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page circle annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[CircleAnnotation]**](CircleAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_file_attachment_annotations**
> AsposeResponse post_page_file_attachment_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page FileAttachment annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[FileAttachmentAnnotation]**](FileAttachmentAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_free_text_annotations**
> AsposeResponse post_page_free_text_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page free text annotations.

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

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_highlight_annotations**
> AsposeResponse post_page_highlight_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page highlight annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[HighlightAnnotation]**](HighlightAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_image_stamps**
> AsposeResponse post_page_image_stamps(name, page_number, stamps, storage=storage, folder=folder, password=password)

Add document page image stamps.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **stamps** | [**list[ImageStamp]**](ImageStamp.md)| The array of stamp. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_ink_annotations**
> AsposeResponse post_page_ink_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page ink annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[InkAnnotation]**](InkAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_line_annotations**
> AsposeResponse post_page_line_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page line annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[LineAnnotation]**](LineAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_link_annotations**
> AsposeResponse post_page_link_annotations(name, page_number, links, storage=storage, folder=folder)

Add document page link annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **links** | [**list[LinkAnnotation]**](LinkAnnotation.md)| Array of link annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_movie_annotations**
> AsposeResponse post_page_movie_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page movie annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[MovieAnnotation]**](MovieAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_pdf_page_stamps**
> AsposeResponse post_page_pdf_page_stamps(name, page_number, stamps, storage=storage, folder=folder, password=password)

Add document pdf page stamps.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **stamps** | [**list[PdfPageStamp]**](PdfPageStamp.md)| The array of stamp. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_poly_line_annotations**
> AsposeResponse post_page_poly_line_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page polyline annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[PolyLineAnnotation]**](PolyLineAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_polygon_annotations**
> AsposeResponse post_page_polygon_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page polygon annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[PolygonAnnotation]**](PolygonAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_redaction_annotations**
> AsposeResponse post_page_redaction_annotations(name, page_number, annotations, storage=storage, folder=folder, apply=apply)

Add document page redaction annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[RedactionAnnotation]**](RedactionAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **apply** | **bool**| Apply redaction immediately after adding. | [optional] [default to false]

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_screen_annotations**
> AsposeResponse post_page_screen_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page screen annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[ScreenAnnotation]**](ScreenAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_sound_annotations**
> AsposeResponse post_page_sound_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page sound annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[SoundAnnotation]**](SoundAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_square_annotations**
> AsposeResponse post_page_square_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page square annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[SquareAnnotation]**](SquareAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_squiggly_annotations**
> AsposeResponse post_page_squiggly_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page squiggly annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[SquigglyAnnotation]**](SquigglyAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_stamp_annotations**
> AsposeResponse post_page_stamp_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page stamp annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[StampAnnotation]**](StampAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_strike_out_annotations**
> AsposeResponse post_page_strike_out_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page StrikeOut annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[StrikeOutAnnotation]**](StrikeOutAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_tables**
> AsposeResponse post_page_tables(name, page_number, tables, storage=storage, folder=folder)

Add document page tables.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **tables** | [**list[Table]**](Table.md)| The array of table. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_text_annotations**
> AsposeResponse post_page_text_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page text annotations.

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

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_text_replace**
> TextReplaceResponse post_page_text_replace(name, page_number, text_replace_list_request, storage=storage, folder=folder)

Page's replace text method.

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

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_text_stamps**
> AsposeResponse post_page_text_stamps(name, page_number, stamps, storage=storage, folder=folder, password=password)

Add document page text stamps.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **stamps** | [**list[TextStamp]**](TextStamp.md)| The array of stamp. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_page_underline_annotations**
> AsposeResponse post_page_underline_annotations(name, page_number, annotations, storage=storage, folder=folder)

Add document page underline annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **annotations** | [**list[UnderlineAnnotation]**](UnderlineAnnotation.md)| The array of annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pdf_to_xlsx**
> file post_pdf_to_xlsx(insert_blank_column_at_first=insert_blank_column_at_first, minimize_the_number_of_worksheets=minimize_the_number_of_worksheets, uniform_worksheets=uniform_worksheets, password=password, file=file)

Converts PDF document (in request content) to XLSX format and uploads and returns resulting file in response content.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insert_blank_column_at_first** | **bool**| Insert blank column at first | [optional] 
 **minimize_the_number_of_worksheets** | **bool**| Minimize the number of worksheets | [optional] 
 **uniform_worksheets** | **bool**| Uniform worksheets | [optional] 
 **password** | **str**| The password (Base64). | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

**file**

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_popup_annotation**
> AsposeResponse post_popup_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Add document popup annotations.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The parent annotation ID. | 
 **annotation** | [**PopupAnnotation**](PopupAnnotation.md)| The annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_radio_button_fields**
> AsposeResponse post_radio_button_fields(name, fields, storage=storage, folder=folder)

Add document RadioButton fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **fields** | [**list[RadioButtonField]**](RadioButtonField.md)| The array of field. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sign_document**
> AsposeResponse post_sign_document(name, sign, storage=storage, folder=folder)

Sign document.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **sign** | [**Signature**](Signature.md)| Signature object containing signature data. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sign_page**
> AsposeResponse post_sign_page(name, page_number, sign, storage=storage, folder=folder)

Sign page.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **sign** | [**Signature**](Signature.md)| Signature object containing signature data. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_signature_field**
> AsposeResponse post_signature_field(name, field, storage=storage, folder=folder)

Add document signature field.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field** | [**SignatureField**](SignatureField.md)| The field. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_split_document**
> SplitResultResponse post_split_document(name, format=format, _from=_from, to=to, storage=storage, folder=folder, password=password)

Split document to parts.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Document name. | 
 **format** | **str**| Resulting documents format. | [optional] 
 **_from** | **int**| Start page if defined. | [optional] 
 **to** | **int**| End page if defined. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

[**SplitResultResponse**](SplitResultResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_split_range_pdf_document**
> SplitResultResponse post_split_range_pdf_document(name, options, storage=storage, folder=folder, password=password)

Split document into ranges.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **options** | [**SplitRangePdfOptions**](SplitRangePdfOptions.md)| The splitting options. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

[**SplitResultResponse**](SplitResultResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_text_box_fields**
> AsposeResponse post_text_box_fields(name, fields, storage=storage, folder=folder)

Add document text box fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **fields** | [**list[TextBoxField]**](TextBoxField.md)| The array of field. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_xmp_metadata**
> AsposeResponse post_xmp_metadata(name, metadata, folder=folder, storage=storage, pass_base64=pass_base64)

Add or remove XMP Metadata properties.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **metadata** | [**XmpMetadata**](XmpMetadata.md)| XmpMetadata instance. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **pass_base64** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_add_new_page**
> DocumentPagesResponse put_add_new_page(name, storage=storage, folder=folder)

Add new page to end of the document.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**DocumentPagesResponse**](DocumentPagesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_add_text**
> AsposeResponse put_add_text(name, page_number, paragraph, folder=folder, storage=storage)

Add text to PDF document page.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| Number of page (starting from 1). | 
 **paragraph** | [**Paragraph**](Paragraph.md)| Paragraph data. | 
 **folder** | **str**| Document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_annotations_flatten**
> AsposeResponse put_annotations_flatten(name, start_page=start_page, end_page=end_page, annotation_types=annotation_types, storage=storage, folder=folder)

Flattens the annotations of the specified types

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **start_page** | **int**| The start page number. | [optional] 
 **end_page** | **int**| The end page number. | [optional] 
 **annotation_types** | [**list[AnnotationType]**](AnnotationType.md)| Array of annotation types. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_bookmark**
> BookmarkResponse put_bookmark(name, bookmark_path, bookmark, folder=folder, storage=storage, password=password)

Update document bookmark.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **bookmark_path** | **str**| The bookmark path. | 
 **bookmark** | [**Bookmark**](Bookmark.md)| The bookmark. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**BookmarkResponse**](BookmarkResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_caret_annotation**
> CaretAnnotationResponse put_caret_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document caret annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**CaretAnnotation**](CaretAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CaretAnnotationResponse**](CaretAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_change_password_document**
> AsposeResponse put_change_password_document(out_path, owner_password, new_user_password, new_owner_password, storage=storage, file=file)

Change document password from content.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.doc) | 
 **owner_password** | **str**| Owner password (encrypted Base64). | 
 **new_user_password** | **str**| New user password (encrypted Base64). | 
 **new_owner_password** | **str**| New owner password (encrypted Base64). | 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be changed password. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_check_box_field**
> CheckBoxFieldResponse put_check_box_field(name, field_name, field, storage=storage, folder=folder)

Replace document checkbox field

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name. | 
 **field** | [**CheckBoxField**](CheckBoxField.md)| The field. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CheckBoxFieldResponse**](CheckBoxFieldResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_circle_annotation**
> CircleAnnotationResponse put_circle_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document circle annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**CircleAnnotation**](CircleAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CircleAnnotationResponse**](CircleAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_combo_box_field**
> ComboBoxFieldResponse put_combo_box_field(name, field_name, field, storage=storage, folder=folder)

Replace document combobox field

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name. | 
 **field** | [**ComboBoxField**](ComboBoxField.md)| The field. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ComboBoxFieldResponse**](ComboBoxFieldResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_create_document**
> DocumentResponse put_create_document(name, storage=storage, folder=folder)

Create empty document.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The new document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The new document folder. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_create_pdf_from_layer**
> AsposeResponse put_create_pdf_from_layer(name, page_number, out_path, layer_id, folder=folder, storage=storage, pass_base64=pass_base64)

Create a separate PDF from a PDF Layer and upload resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **out_path** | **str**| The out path of result image. | 
 **layer_id** | **str**| Layer Id. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **pass_base64** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_decrypt_document**
> AsposeResponse put_decrypt_document(out_path, password, storage=storage, file=file)

Decrypt document from content.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.doc) | 
 **password** | **str**| The password (encrypted Base64). | 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be decrypted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_document_display_properties**
> DisplayPropertiesResponse put_document_display_properties(name, display_properties, storage=storage, folder=folder)

Update document display properties.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **display_properties** | [**DisplayProperties**](DisplayProperties.md)| The display properties. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**DisplayPropertiesResponse**](DisplayPropertiesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_encrypt_document**
> AsposeResponse put_encrypt_document(out_path, user_password, owner_password, crypto_algorithm, permissions_flags=permissions_flags, use_pdf20=use_pdf20, storage=storage, file=file)

Encrypt document from content.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.doc) | 
 **user_password** | **str**| User password (encrypted Base64). | 
 **owner_password** | **str**| Owner password (encrypted Base64). | 
 **crypto_algorithm** | **str**| Cryptographic algorithm, see CryptoAlgorithm for details. | 
 **permissions_flags** | [**list[PermissionsFlags]**](PermissionsFlags.md)| Array of document permissions, see PermissionsFlags for details. | [optional] 
 **use_pdf20** | **bool**| Support for revision 6 (Extension 8). | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be encrypted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_epub_in_storage_to_pdf**
> AsposeResponse put_epub_in_storage_to_pdf(name, src_path, storage=storage, dst_folder=dst_folder)

Convert EPUB file (located on storage) to PDF format and upload resulting file to storage. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.epub) | 
 **storage** | **str**| The document storage. | [optional] 
 **dst_folder** | **str**| The destination document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_export_fields_from_pdf_to_fdf_in_storage**
> AsposeResponse put_export_fields_from_pdf_to_fdf_in_storage(name, fdf_output_file_path, storage=storage, folder=folder)

Export fields from from PDF in storage to FDF file in storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **fdf_output_file_path** | **str**| The output Fdf file path. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_export_fields_from_pdf_to_xfdf_in_storage**
> AsposeResponse put_export_fields_from_pdf_to_xfdf_in_storage(name, xfdf_output_file_path, storage=storage, folder=folder)

Export fields from from PDF in storage to XFDF file in storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **xfdf_output_file_path** | **str**| The output xfdf file path. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_export_fields_from_pdf_to_xml_in_storage**
> AsposeResponse put_export_fields_from_pdf_to_xml_in_storage(name, xml_output_file_path, storage=storage, folder=folder)

Export fields from from PDF in storage to XML file in storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **xml_output_file_path** | **str**| The output xml file path. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_fields_flatten**
> AsposeResponse put_fields_flatten(name, storage=storage, folder=folder)

Flatten form fields in document.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_file_attachment_annotation**
> FileAttachmentAnnotationResponse put_file_attachment_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document FileAttachment annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**FileAttachmentAnnotation**](FileAttachmentAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FileAttachmentAnnotationResponse**](FileAttachmentAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_file_attachment_annotation_data_extract**
> AsposeResponse put_file_attachment_annotation_data_extract(name, annotation_id, out_folder=out_folder, storage=storage, folder=folder)

Extract document FileAttachment annotation content to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **out_folder** | **str**| The output folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_free_text_annotation**
> FreeTextAnnotationResponse put_free_text_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document free text annotation

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

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_highlight_annotation**
> HighlightAnnotationResponse put_highlight_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document highlight annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**HighlightAnnotation**](HighlightAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**HighlightAnnotationResponse**](HighlightAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_html_in_storage_to_pdf**
> AsposeResponse put_html_in_storage_to_pdf(name, src_path, html_file_name=html_file_name, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, dst_folder=dst_folder, storage=storage)

Convert HTML file (located on storage) to PDF format and upload resulting file to storage. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.zip) | 
 **html_file_name** | **str**| Name of HTML file in ZIP. | [optional] 
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

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_image_extract_as_gif**
> AsposeResponse put_image_extract_as_gif(name, image_id, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document image in GIF format to folder

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_image_extract_as_jpeg**
> AsposeResponse put_image_extract_as_jpeg(name, image_id, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document image in JPEG format to folder

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_image_extract_as_png**
> AsposeResponse put_image_extract_as_png(name, image_id, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document image in PNG format to folder

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_image_extract_as_tiff**
> AsposeResponse put_image_extract_as_tiff(name, image_id, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document image in TIFF format to folder

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_id** | **str**| Image ID. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_image_in_storage_to_pdf**
> AsposeResponse put_image_in_storage_to_pdf(name, image_templates, dst_folder=dst_folder, storage=storage)

Convert image file (located on storage) to PDF format and upload resulting file to storage. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_templates** | [**ImageTemplatesRequest**](ImageTemplatesRequest.md)| ImageTemplatesRequestImage templates | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_images_extract_as_gif**
> AsposeResponse put_images_extract_as_gif(name, page_number, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document images in GIF format to folder.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_images_extract_as_jpeg**
> AsposeResponse put_images_extract_as_jpeg(name, page_number, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document images in JPEG format to folder.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_images_extract_as_png**
> AsposeResponse put_images_extract_as_png(name, page_number, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document images in PNG format to folder.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_images_extract_as_tiff**
> AsposeResponse put_images_extract_as_tiff(name, page_number, width=width, height=height, storage=storage, folder=folder, dest_folder=dest_folder)

Extract document images in TIFF format to folder.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **dest_folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_import_fields_from_fdf_in_storage**
> AsposeResponse put_import_fields_from_fdf_in_storage(name, fdf_file_path, storage=storage, folder=folder)

Update fields from FDF file in storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **fdf_file_path** | **str**| The Fdf file path. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_import_fields_from_xfdf_in_storage**
> AsposeResponse put_import_fields_from_xfdf_in_storage(name, xfdf_file_path, storage=storage, folder=folder)

Update fields from XFDF file in storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **xfdf_file_path** | **str**| The XFDF file path. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_import_fields_from_xml_in_storage**
> AsposeResponse put_import_fields_from_xml_in_storage(name, xml_file_path, storage=storage, folder=folder)

Update fields from XML file in storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **xml_file_path** | **str**| Full source filename (ex. /folder1/folder2/template.xml) | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ink_annotation**
> InkAnnotationResponse put_ink_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document ink annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**InkAnnotation**](InkAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**InkAnnotationResponse**](InkAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_line_annotation**
> LineAnnotationResponse put_line_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document line annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**LineAnnotation**](LineAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**LineAnnotationResponse**](LineAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_link_annotation**
> LinkAnnotationResponse put_link_annotation(name, link_id, link, storage=storage, folder=folder)

Replace document page link annotations

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **link_id** | **str**| The link ID. | 
 **link** | [**LinkAnnotation**](LinkAnnotation.md)| Link annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**LinkAnnotationResponse**](LinkAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_list_box_field**
> ListBoxFieldResponse put_list_box_field(name, field_name, field, storage=storage, folder=folder)

Replace document listbox field

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name. | 
 **field** | [**ListBoxField**](ListBoxField.md)| The field. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ListBoxFieldResponse**](ListBoxFieldResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_markdown_in_storage_to_pdf**
> AsposeResponse put_markdown_in_storage_to_pdf(name, src_path, storage=storage, dst_folder=dst_folder)

Convert MD file (located on storage) to PDF format and upload resulting file to storage. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.md) | 
 **storage** | **str**| The document storage. | [optional] 
 **dst_folder** | **str**| The destination document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_merge_documents**
> DocumentResponse put_merge_documents(name, merge_documents, storage=storage, folder=folder)

Merge a list of documents.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Resulting document name. | 
 **merge_documents** | [**MergeDocuments**](MergeDocuments.md)| MergeDocuments with a list of documents. | 
 **storage** | **str**| Resulting document storage. | [optional] 
 **folder** | **str**| Resulting document folder. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_mht_in_storage_to_pdf**
> AsposeResponse put_mht_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)

Convert MHT file (located on storage) to PDF format and upload resulting file to storage. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.mht) | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_movie_annotation**
> MovieAnnotationResponse put_movie_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document movie annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**MovieAnnotation**](MovieAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**MovieAnnotationResponse**](MovieAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_page_add_stamp**
> AsposeResponse put_page_add_stamp(name, page_number, stamp, storage=storage, folder=folder)

Add page stamp.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **stamp** | [**Stamp**](Stamp.md)| Stamp with data. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_page_convert_to_bmp**
> AsposeResponse put_page_convert_to_bmp(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage, password=password)

Convert document page to bmp image and upload resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **out_path** | **str**| The out path of result image. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_page_convert_to_emf**
> AsposeResponse put_page_convert_to_emf(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage, password=password)

Convert document page to emf image and upload resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **out_path** | **str**| The out path of result image. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_page_convert_to_gif**
> AsposeResponse put_page_convert_to_gif(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage, password=password)

Convert document page to gif image and upload resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **out_path** | **str**| The out path of result image. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_page_convert_to_jpeg**
> AsposeResponse put_page_convert_to_jpeg(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage, password=password)

Convert document page to Jpeg image and upload resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **out_path** | **str**| The out path of result image. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_page_convert_to_png**
> AsposeResponse put_page_convert_to_png(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage, password=password)

Convert document page to png image and upload resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **out_path** | **str**| The out path of result image. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_page_convert_to_tiff**
> AsposeResponse put_page_convert_to_tiff(name, page_number, out_path, width=width, height=height, folder=folder, storage=storage, password=password)

Convert document page to Tiff image and upload resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **page_number** | **int**| The page number. | 
 **out_path** | **str**| The out path of result image. | 
 **width** | **int**| The converted image width. | [optional] [default to 0]
 **height** | **int**| The converted image height. | [optional] [default to 0]
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pcl_in_storage_to_pdf**
> AsposeResponse put_pcl_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)

Convert PCL file (located on storage) to PDF format and upload resulting file to storage. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.pcl) | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_a_in_storage_to_pdf**
> AsposeResponse put_pdf_a_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, dont_optimize=dont_optimize, storage=storage)

Convert PDFA file (located on storage) to PDF format and upload resulting file to storage. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.pdf) | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **dont_optimize** | **bool**| If set, document resources will not be optimized. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_doc**
> AsposeResponse put_pdf_in_request_to_doc(out_path, add_return_to_line_end=add_return_to_line_end, format=format, image_resolution_x=image_resolution_x, image_resolution_y=image_resolution_y, max_distance_between_text_lines=max_distance_between_text_lines, mode=mode, recognize_bullets=recognize_bullets, relative_horizontal_proximity=relative_horizontal_proximity, storage=storage, password=password, file=file)

Converts PDF document (in request content) to DOC format and uploads resulting file to storage.

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
 **password** | **str**| The password (Base64). | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_epub**
> AsposeResponse put_pdf_in_request_to_epub(out_path, content_recognition_mode=content_recognition_mode, storage=storage, file=file)

Converts PDF document (in request content) to EPUB format and uploads resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.epub) | 
 **content_recognition_mode** | **str**| Property tunes conversion for this or that desirable method of recognition of content. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_html**
> AsposeResponse put_pdf_in_request_to_html(out_path, additional_margin_width_in_points=additional_margin_width_in_points, compress_svg_graphics_if_any=compress_svg_graphics_if_any, convert_marked_content_to_layers=convert_marked_content_to_layers, default_font_name=default_font_name, document_type=document_type, fixed_layout=fixed_layout, image_resolution=image_resolution, minimal_line_width=minimal_line_width, prevent_glyphs_grouping=prevent_glyphs_grouping, split_css_into_pages=split_css_into_pages, split_into_pages=split_into_pages, use_z_order=use_z_order, antialiasing_processing=antialiasing_processing, css_class_names_prefix=css_class_names_prefix, explicit_list_of_saved_pages=explicit_list_of_saved_pages, font_encoding_strategy=font_encoding_strategy, font_saving_mode=font_saving_mode, html_markup_generation_mode=html_markup_generation_mode, letters_positioning_method=letters_positioning_method, pages_flow_type_depends_on_viewers_screen_size=pages_flow_type_depends_on_viewers_screen_size, parts_embedding_mode=parts_embedding_mode, raster_images_saving_mode=raster_images_saving_mode, remove_empty_areas_on_top_and_bottom=remove_empty_areas_on_top_and_bottom, save_shadowed_texts_as_transparent_texts=save_shadowed_texts_as_transparent_texts, save_transparent_texts=save_transparent_texts, special_folder_for_all_images=special_folder_for_all_images, special_folder_for_svg_images=special_folder_for_svg_images, try_save_text_underlining_and_strikeouting_in_css=try_save_text_underlining_and_strikeouting_in_css, storage=storage, flow_layout_paragraph_full_width=flow_layout_paragraph_full_width, output_format=output_format, file=file)

Converts PDF document (in request content) to Html format and uploads resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.html) | 
 **additional_margin_width_in_points** | **int**| Defines width of margin that will be forcibly left around that output HTML-areas. | [optional] 
 **compress_svg_graphics_if_any** | **bool**| The flag that indicates whether found SVG graphics(if any) will be compressed(zipped) into SVGZ format during saving. | [optional] 
 **convert_marked_content_to_layers** | **bool**| If attribute ConvertMarkedContentToLayers set to true then an all elements inside a PDF marked content (layer) will be put into an HTML div with &quot;data-pdflayer&quot; attribute specifying a layer name. This layer name will be extracted from optional properties of PDF marked content. If this attribute is false (by default) then no any layers will be created from PDF marked content. | [optional] 
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
 **css_class_names_prefix** | **str**| When PDFtoHTML converter generates result CSSs, CSS class names (something like &quot;.stl_01 {}&quot; ... &quot;.stl_NN {}) are generated and used in result CSS. This property allows forcibly set class name prefix. | [optional] 
 **explicit_list_of_saved_pages** | **list[int]**| With this property You can explicitely define what pages of document should be converted. Pages in this list must have 1-based numbers. I.e. valid numbers of pages must be taken from range (1...[NumberOfPagesInConvertedDocument]) Order of appearing of pages in this list does not affect their order in result HTML page(s) - in result pages allways will go in order in which they are present in source PDF. | [optional] 
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
 **flow_layout_paragraph_full_width** | **bool**| This attribute specifies full width paragraph text for Flow mode, FixedLayout &#x3D; false. | [optional] 
 **output_format** | **str**| This parameter determines the type of result. The zip archive will be uploaded into the storage if the parameter is &quot;Zip&quot; or missed (default). In case of the &quot;Folder&quot;, all resulting files and directories will be uploaded to the folder of the resulting HTML file. | [optional] [default to Zip]
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_mobi_xml**
> AsposeResponse put_pdf_in_request_to_mobi_xml(out_path, storage=storage, file=file)

Converts PDF document (in request content) to MOBIXML format and uploads resulting ZIP archive file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.mobixml) | 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_pdf_a**
> AsposeResponse put_pdf_in_request_to_pdf_a(out_path, type, storage=storage, password=password, file=file)

Converts PDF document (in request content) to PdfA format and uploads resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.pdf) | 
 **type** | **str**| Type of PdfA format. | 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_pptx**
> AsposeResponse put_pdf_in_request_to_pptx(out_path, separate_images=separate_images, slides_as_images=slides_as_images, storage=storage, password=password, file=file)

Converts PDF document (in request content) to PPTX format and uploads resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.pptx) | 
 **separate_images** | **bool**| Separate images. | [optional] 
 **slides_as_images** | **bool**| Slides as images. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_svg**
> AsposeResponse put_pdf_in_request_to_svg(out_path, storage=storage, password=password, file=file)

Converts PDF document (in request content) to SVG format and uploads resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.svg) | 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_te_x**
> AsposeResponse put_pdf_in_request_to_te_x(out_path, storage=storage, file=file)

Converts PDF document (in request content) to TeX format and uploads resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.tex) | 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_tiff**
> AsposeResponse put_pdf_in_request_to_tiff(out_path, brightness=brightness, compression=compression, color_depth=color_depth, left_margin=left_margin, right_margin=right_margin, top_margin=top_margin, bottom_margin=bottom_margin, orientation=orientation, skip_blank_pages=skip_blank_pages, width=width, height=height, x_resolution=x_resolution, y_resolution=y_resolution, page_index=page_index, page_count=page_count, storage=storage, file=file)

Converts PDF document (in request content) to TIFF format and uploads resulting file to storage.

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

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_xls**
> AsposeResponse put_pdf_in_request_to_xls(out_path, insert_blank_column_at_first=insert_blank_column_at_first, minimize_the_number_of_worksheets=minimize_the_number_of_worksheets, scale_factor=scale_factor, uniform_worksheets=uniform_worksheets, storage=storage, password=password, file=file)

Converts PDF document (in request content) to XLS format and uploads resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.xls) | 
 **insert_blank_column_at_first** | **bool**| Insert blank column at first | [optional] 
 **minimize_the_number_of_worksheets** | **bool**| Minimize the number of worksheets | [optional] 
 **scale_factor** | **float**| Scale factor (Obsolete) | [optional] 
 **uniform_worksheets** | **bool**| Uniform worksheets | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_xlsx**
> AsposeResponse put_pdf_in_request_to_xlsx(out_path, insert_blank_column_at_first=insert_blank_column_at_first, minimize_the_number_of_worksheets=minimize_the_number_of_worksheets, scale_factor=scale_factor, uniform_worksheets=uniform_worksheets, storage=storage, password=password, file=file)

Converts PDF document (in request content) to XLSX format and uploads resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.xlsx) | 
 **insert_blank_column_at_first** | **bool**| Insert blank column at first | [optional] 
 **minimize_the_number_of_worksheets** | **bool**| Minimize the number of worksheets | [optional] 
 **scale_factor** | **float**| Scale factor (Obsolete) | [optional] 
 **uniform_worksheets** | **bool**| Uniform worksheets | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_xml**
> AsposeResponse put_pdf_in_request_to_xml(out_path, storage=storage, file=file)

Converts PDF document (in request content) to XML format and uploads resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.xml) | 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_request_to_xps**
> AsposeResponse put_pdf_in_request_to_xps(out_path, storage=storage, file=file)

Converts PDF document (in request content) to XPS format and uploads resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.xps) | 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_doc**
> AsposeResponse put_pdf_in_storage_to_doc(name, out_path, add_return_to_line_end=add_return_to_line_end, format=format, image_resolution_x=image_resolution_x, image_resolution_y=image_resolution_y, max_distance_between_text_lines=max_distance_between_text_lines, mode=mode, recognize_bullets=recognize_bullets, relative_horizontal_proximity=relative_horizontal_proximity, folder=folder, storage=storage, password=password)

Converts PDF document (located on storage) to DOC format and uploads resulting file to storage.

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
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_epub**
> AsposeResponse put_pdf_in_storage_to_epub(name, out_path, content_recognition_mode=content_recognition_mode, folder=folder, storage=storage)

Converts PDF document (located on storage) to EPUB format and uploads resulting file to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.epub) | 
 **content_recognition_mode** | **str**| Property tunes conversion for this or that desirable method of recognition of content. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_html**
> AsposeResponse put_pdf_in_storage_to_html(name, out_path, additional_margin_width_in_points=additional_margin_width_in_points, compress_svg_graphics_if_any=compress_svg_graphics_if_any, convert_marked_content_to_layers=convert_marked_content_to_layers, default_font_name=default_font_name, document_type=document_type, fixed_layout=fixed_layout, image_resolution=image_resolution, minimal_line_width=minimal_line_width, prevent_glyphs_grouping=prevent_glyphs_grouping, split_css_into_pages=split_css_into_pages, split_into_pages=split_into_pages, use_z_order=use_z_order, antialiasing_processing=antialiasing_processing, css_class_names_prefix=css_class_names_prefix, explicit_list_of_saved_pages=explicit_list_of_saved_pages, font_encoding_strategy=font_encoding_strategy, font_saving_mode=font_saving_mode, html_markup_generation_mode=html_markup_generation_mode, letters_positioning_method=letters_positioning_method, pages_flow_type_depends_on_viewers_screen_size=pages_flow_type_depends_on_viewers_screen_size, parts_embedding_mode=parts_embedding_mode, raster_images_saving_mode=raster_images_saving_mode, remove_empty_areas_on_top_and_bottom=remove_empty_areas_on_top_and_bottom, save_shadowed_texts_as_transparent_texts=save_shadowed_texts_as_transparent_texts, save_transparent_texts=save_transparent_texts, special_folder_for_all_images=special_folder_for_all_images, special_folder_for_svg_images=special_folder_for_svg_images, try_save_text_underlining_and_strikeouting_in_css=try_save_text_underlining_and_strikeouting_in_css, folder=folder, storage=storage, flow_layout_paragraph_full_width=flow_layout_paragraph_full_width, output_format=output_format)

Converts PDF document (located on storage) to Html format and uploads resulting file to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.html) | 
 **additional_margin_width_in_points** | **int**| Defines width of margin that will be forcibly left around that output HTML-areas. | [optional] 
 **compress_svg_graphics_if_any** | **bool**| The flag that indicates whether found SVG graphics(if any) will be compressed(zipped) into SVGZ format during saving. | [optional] 
 **convert_marked_content_to_layers** | **bool**| If attribute ConvertMarkedContentToLayers set to true then an all elements inside a PDF marked content (layer) will be put into an HTML div with &quot;data-pdflayer&quot; attribute specifying a layer name. This layer name will be extracted from optional properties of PDF marked content. If this attribute is false (by default) then no any layers will be created from PDF marked content. | [optional] 
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
 **css_class_names_prefix** | **str**| When PDFtoHTML converter generates result CSSs, CSS class names (something like &quot;.stl_01 {}&quot; ... &quot;.stl_NN {}) are generated and used in result CSS. This property allows forcibly set class name prefix. | [optional] 
 **explicit_list_of_saved_pages** | **list[int]**| With this property You can explicitely define what pages of document should be converted. Pages in this list must have 1-based numbers. I.e. valid numbers of pages must be taken from range (1...[NumberOfPagesInConvertedDocument]) Order of appearing of pages in this list does not affect their order in result HTML page(s) - in result pages allways will go in order in which they are present in source PDF. | [optional] 
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
 **flow_layout_paragraph_full_width** | **bool**| This attribute specifies full width paragraph text for Flow mode, FixedLayout &#x3D; false. | [optional] 
 **output_format** | **str**| This parameter determines the type of result. The zip archive will be uploaded into the storage if the parameter is &quot;Zip&quot; or missed (default). In case of the &quot;Folder&quot;, all resulting files and directories will be uploaded to the folder of the resulting HTML file. | [optional] [default to Zip]

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_mobi_xml**
> AsposeResponse put_pdf_in_storage_to_mobi_xml(name, out_path, folder=folder, storage=storage)

Converts PDF document (located on storage) to MOBIXML format and uploads resulting ZIP archive file to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.mobixml) | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_pdf_a**
> AsposeResponse put_pdf_in_storage_to_pdf_a(name, out_path, type, folder=folder, storage=storage, password=password)

Converts PDF document (located on storage) to PdfA format and uploads resulting file to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.pdf) | 
 **type** | **str**| Type of PdfA format. | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_pptx**
> AsposeResponse put_pdf_in_storage_to_pptx(name, out_path, separate_images=separate_images, slides_as_images=slides_as_images, folder=folder, storage=storage, password=password)

Converts PDF document (located on storage) to PPTX format and uploads resulting file to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.pptx) | 
 **separate_images** | **bool**| Separate images. | [optional] 
 **slides_as_images** | **bool**| Slides as images. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| Base64 encoded password. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_svg**
> AsposeResponse put_pdf_in_storage_to_svg(name, out_path, folder=folder, storage=storage, password=password)

Converts PDF document (located on storage) to SVG format and uploads resulting file to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.svg) | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_te_x**
> AsposeResponse put_pdf_in_storage_to_te_x(name, out_path, folder=folder, storage=storage)

Converts PDF document (located on storage) to TeX format and uploads resulting file to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.tex) | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_tiff**
> AsposeResponse put_pdf_in_storage_to_tiff(name, out_path, brightness=brightness, compression=compression, color_depth=color_depth, left_margin=left_margin, right_margin=right_margin, top_margin=top_margin, bottom_margin=bottom_margin, orientation=orientation, skip_blank_pages=skip_blank_pages, width=width, height=height, x_resolution=x_resolution, y_resolution=y_resolution, page_index=page_index, page_count=page_count, folder=folder, storage=storage)

Converts PDF document (located on storage) to TIFF format and uploads resulting file to storage

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

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_xls**
> AsposeResponse put_pdf_in_storage_to_xls(name, out_path, insert_blank_column_at_first=insert_blank_column_at_first, minimize_the_number_of_worksheets=minimize_the_number_of_worksheets, scale_factor=scale_factor, uniform_worksheets=uniform_worksheets, folder=folder, storage=storage, password=password)

Converts PDF document (located on storage) to XLS format and uploads resulting file to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.xls) | 
 **insert_blank_column_at_first** | **bool**| Insert blank column at first | [optional] 
 **minimize_the_number_of_worksheets** | **bool**| Minimize the number of worksheets | [optional] 
 **scale_factor** | **float**| Scale factor (Obsolete) | [optional] 
 **uniform_worksheets** | **bool**| Uniform worksheets | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_xlsx**
> AsposeResponse put_pdf_in_storage_to_xlsx(name, out_path, insert_blank_column_at_first=insert_blank_column_at_first, minimize_the_number_of_worksheets=minimize_the_number_of_worksheets, scale_factor=scale_factor, uniform_worksheets=uniform_worksheets, folder=folder, storage=storage, password=password)

Converts PDF document (located on storage) to XLSX format and uploads resulting file to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.xlsx) | 
 **insert_blank_column_at_first** | **bool**| Insert blank column at first | [optional] 
 **minimize_the_number_of_worksheets** | **bool**| Minimize the number of worksheets | [optional] 
 **scale_factor** | **float**| Scale factor (Obsolete) | [optional] 
 **uniform_worksheets** | **bool**| Uniform worksheets | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_xml**
> AsposeResponse put_pdf_in_storage_to_xml(name, out_path, folder=folder, storage=storage)

Converts PDF document (located on storage) to XML format and uploads resulting file to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.xml) | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pdf_in_storage_to_xps**
> AsposeResponse put_pdf_in_storage_to_xps(name, out_path, folder=folder, storage=storage)

Converts PDF document (located on storage) to XPS format and uploads resulting file to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.xps) | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_poly_line_annotation**
> PolyLineAnnotationResponse put_poly_line_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document polyline annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**PolyLineAnnotation**](PolyLineAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**PolyLineAnnotationResponse**](PolyLineAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_polygon_annotation**
> PolygonAnnotationResponse put_polygon_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document polygon annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**PolygonAnnotation**](PolygonAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**PolygonAnnotationResponse**](PolygonAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_popup_annotation**
> PopupAnnotationResponse put_popup_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document popup annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**PopupAnnotation**](PopupAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**PopupAnnotationResponse**](PopupAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_privileges**
> AsposeResponse put_privileges(name, privileges, storage=storage, folder=folder)

Update privilege document.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **privileges** | [**DocumentPrivilege**](DocumentPrivilege.md)| Document privileges. DocumentPrivilege | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ps_in_storage_to_pdf**
> AsposeResponse put_ps_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)

Convert PS file (located on storage) to PDF format and upload resulting file to storage. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.ps) | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_radio_button_field**
> RadioButtonFieldResponse put_radio_button_field(name, field_name, field, storage=storage, folder=folder)

Replace document RadioButton field

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name. | 
 **field** | [**RadioButtonField**](RadioButtonField.md)| The field. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**RadioButtonFieldResponse**](RadioButtonFieldResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_redaction_annotation**
> RedactionAnnotationResponse put_redaction_annotation(name, annotation_id, annotation, storage=storage, folder=folder, apply=apply)

Replace document redaction annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**RedactionAnnotation**](RedactionAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **apply** | **bool**| Apply redaction immediately after adding. | [optional] [default to false]

### Return type

[**RedactionAnnotationResponse**](RedactionAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_replace_image**
> ImageResponse put_replace_image(name, image_id, image_file_path=image_file_path, storage=storage, folder=folder, image=image)

Replace document image.

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

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_replace_multiple_image**
> ImagesResponse put_replace_multiple_image(name, image_ids, image_file_path=image_file_path, storage=storage, folder=folder, image=image)

Replace document multiple image.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **image_ids** | **list[str]**| The image IDs. | 
 **image_file_path** | **str**| Path to image file if specified. Request content is used otherwise. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **image** | **file**| Image file. | [optional] 

### Return type

[**ImagesResponse**](ImagesResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_screen_annotation**
> ScreenAnnotationResponse put_screen_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document screen annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**ScreenAnnotation**](ScreenAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ScreenAnnotationResponse**](ScreenAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_screen_annotation_data_extract**
> AsposeResponse put_screen_annotation_data_extract(name, annotation_id, out_file_path, storage=storage, folder=folder)

Extract document screen annotation content to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **out_file_path** | **str**| The output file path. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_searchable_document**
> AsposeResponse put_searchable_document(name, storage=storage, folder=folder, lang=lang)

Create searchable PDF document. Generate OCR layer for images in input PDF document.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **lang** | **str**| language for OCR engine. Possible values: eng, ara, bel, ben, bul, ces, dan, deu, ell, fin, fra, heb, hin, ind, isl, ita, jpn, kor, nld, nor, pol, por, ron, rus, spa, swe, tha, tur, ukr, vie, chi_sim, chi_tra or thier combination e.g. eng,rus  | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_set_property**
> DocumentPropertyResponse put_set_property(name, property_name, value, storage=storage, folder=folder, password=password)

Add/update document property.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **property_name** | **str**| Property name. | 
 **value** | **str**| Property value. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **password** | **str**| The password (Base64). | [optional] 

### Return type

[**DocumentPropertyResponse**](DocumentPropertyResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_signature_field**
> SignatureFieldResponse put_signature_field(name, field_name, field, storage=storage, folder=folder)

Replace document signature field.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name. | 
 **field** | [**SignatureField**](SignatureField.md)| The field. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SignatureFieldResponse**](SignatureFieldResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sound_annotation**
> SoundAnnotationResponse put_sound_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document sound annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**SoundAnnotation**](SoundAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SoundAnnotationResponse**](SoundAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sound_annotation_data_extract**
> AsposeResponse put_sound_annotation_data_extract(name, annotation_id, out_file_path, storage=storage, folder=folder)

Extract document sound annotation content to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **out_file_path** | **str**| The output file path. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_square_annotation**
> SquareAnnotationResponse put_square_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document square annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**SquareAnnotation**](SquareAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SquareAnnotationResponse**](SquareAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_squiggly_annotation**
> SquigglyAnnotationResponse put_squiggly_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document squiggly annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**SquigglyAnnotation**](SquigglyAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**SquigglyAnnotationResponse**](SquigglyAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_stamp_annotation**
> StampAnnotationResponse put_stamp_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document stamp annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**StampAnnotation**](StampAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**StampAnnotationResponse**](StampAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_stamp_annotation_data_extract**
> AsposeResponse put_stamp_annotation_data_extract(name, annotation_id, out_file_path, storage=storage, folder=folder)

Extract document stamp annotation content to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **out_file_path** | **str**| The output file path. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_strike_out_annotation**
> StrikeOutAnnotationResponse put_strike_out_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document StrikeOut annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**StrikeOutAnnotation**](StrikeOutAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**StrikeOutAnnotationResponse**](StrikeOutAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_svg_in_storage_to_pdf**
> AsposeResponse put_svg_in_storage_to_pdf(name, src_path, adjust_page_size=adjust_page_size, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, dst_folder=dst_folder, storage=storage)

Convert SVG file (located on storage) to PDF format and upload resulting file to storage. 

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

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_table**
> AsposeResponse put_table(name, table_id, table, storage=storage, folder=folder)

Replace document page table.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **table_id** | **str**| The table ID. | 
 **table** | [**Table**](Table.md)| The table. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_te_x_in_storage_to_pdf**
> AsposeResponse put_te_x_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)

Convert TeX file (located on storage) to PDF format and upload resulting file to storage. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.tex) | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_text_annotation**
> TextAnnotationResponse put_text_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document text annotation

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

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_text_box_field**
> TextBoxFieldResponse put_text_box_field(name, field_name, field, storage=storage, folder=folder)

Replace document text box field

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The field name. | 
 **field** | [**TextBoxField**](TextBoxField.md)| The field. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TextBoxFieldResponse**](TextBoxFieldResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_underline_annotation**
> UnderlineAnnotationResponse put_underline_annotation(name, annotation_id, annotation, storage=storage, folder=folder)

Replace document underline annotation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **annotation_id** | **str**| The annotation ID. | 
 **annotation** | [**UnderlineAnnotation**](UnderlineAnnotation.md)| Annotation. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**UnderlineAnnotationResponse**](UnderlineAnnotationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_field**
> FieldResponse put_update_field(name, field_name, field, storage=storage, folder=folder)

Update field.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **field_name** | **str**| The name of a field to be updated. | 
 **field** | [**Field**](Field.md)| Field with the field data. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FieldResponse**](FieldResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_fields**
> FieldsResponse put_update_fields(name, fields, storage=storage, folder=folder)

Update fields.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **fields** | [**Fields**](Fields.md)| Fields with the fields data. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**FieldsResponse**](FieldsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_web_in_storage_to_pdf**
> AsposeResponse put_web_in_storage_to_pdf(name, url, height=height, width=width, is_landscape=is_landscape, margin_left=margin_left, margin_bottom=margin_bottom, margin_right=margin_right, margin_top=margin_top, dst_folder=dst_folder, storage=storage)

Convert web page to PDF format and upload resulting file to storage. 

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

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_xfa_pdf_in_request_to_acro_form**
> AsposeResponse put_xfa_pdf_in_request_to_acro_form(out_path, storage=storage, file=file)

Converts PDF document which contains XFA form (in request content) to PDF with AcroForm and uploads resulting file to storage.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.pdf) | 
 **storage** | **str**| The document storage. | [optional] 
 **file** | **file**| A file to be converted. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_xfa_pdf_in_storage_to_acro_form**
> AsposeResponse put_xfa_pdf_in_storage_to_acro_form(name, out_path, folder=folder, storage=storage)

Converts PDF document which contains XFA form (located on storage) to PDF with AcroForm and uploads resulting file to storage

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **out_path** | **str**| Full resulting filename (ex. /folder1/folder2/result.pdf) | 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_xml_in_storage_to_pdf**
> AsposeResponse put_xml_in_storage_to_pdf(name, src_path, xsl_file_path=xsl_file_path, dst_folder=dst_folder, storage=storage)

Convert XML file (located on storage) to PDF format and upload resulting file to storage. 

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

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_xps_in_storage_to_pdf**
> AsposeResponse put_xps_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)

Convert XPS file (located on storage) to PDF format and upload resulting file to storage. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.xps) | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_xsl_fo_in_storage_to_pdf**
> AsposeResponse put_xsl_fo_in_storage_to_pdf(name, src_path, dst_folder=dst_folder, storage=storage)

Convert XslFo file (located on storage) to PDF format and upload resulting file to storage. 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **src_path** | **str**| Full source filename (ex. /folder1/folder2/template.xpsfo) | 
 **dst_folder** | **str**| The destination document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_exists**
> StorageExist storage_exists(storage_name)

Check if storage exists

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | 

### Return type

[**StorageExist**](StorageExist.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> FilesUploadResult upload_file(path, file, storage_name=storage_name)

Upload file

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.              | 
 **file** | **file**| File to upload | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FilesUploadResult**](FilesUploadResult.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

