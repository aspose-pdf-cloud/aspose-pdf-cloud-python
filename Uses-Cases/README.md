#### Annotations
- **[Annotations/annotations_launch.py](Annotations/annotations_launch.py)** – Orchestrates PDF annotation operations: adding, getting, modifying, and deleting text, highlight, underline, strikeout, and free text annotations.
  ```bash
  python Uses-Cases/Annotations/annotations_launch.py
  ```
- *[Annotations/annotations_helper.py](Annotations/annotations_helper.py)* – Provides configuration, API client initialization, and helper methods for PDF annotation tasks.
- *[Annotations/delete_page_annotations.py](Annotations/delete_page_annotations.py)* – Deletes all annotations from a specific page in a PDF document.
- *[Annotations/delete_text_annotation.py](Annotations/delete_text_annotation.py)* – Deletes a specific text annotation and its associated popup from a PDF.
- *[Annotations/get_annotation_by_id.py](Annotations/get_annotation_by_id.py)* – Retrieves a specific annotation by its ID from a PDF document.
- *[Annotations/get_annotations.py](Annotations/get_annotations.py)* – Retrieves all annotations from a specific page in a PDF document.
- *[Annotations/new_highlight_annotation.py](Annotations/new_highlight_annotation.py)* – Adds a new highlight annotation to a PDF document page.
- *[Annotations/new_strikeout_annotation.py](Annotations/new_strikeout_annotation.py)* – Adds a new strikeout annotation to a PDF document page.
- *[Annotations/new_text_annotation.py](Annotations/new_text_annotation.py)* – Adds a new free text annotation to a PDF document page.
- *[Annotations/new_underline_annotation.py](Annotations/new_underline_annotation.py)* – Adds a new underline annotation to a PDF document page.
- *[Annotations/replace_annotation.py](Annotations/replace_annotation.py)* – Modifies the content and properties of an existing text annotation.

#### Attachments
- **[Attachments/add/appendAttachments.py](Attachments/add/appendAttachments.py)** – Appends a new file attachment to a PDF document.
  ```bash
  python Uses-Cases/Attachments/add/appendAttachments.py
  ```
- **[Attachments/get/getAttachmentAndSave.py](Attachments/get/getAttachmentAndSave.py)** – Retrieves and downloads a specific attachment from a PDF document to a local file.
  ```bash
  python Uses-Cases/Attachments/get/getAttachmentAndSave.py
  ```

#### Bookmarks
- **[Bookmarks/add/appendBookmarks.py](Bookmarks/add/appendBookmarks.py)** – Appends a new bookmark link to a specific page in a PDF document.
  ```bash
  python Uses-Cases/Bookmarks/add/appendBookmarks.py
  ```
- **[Bookmarks/get/getBookmarkByPathAndShow.py](Bookmarks/get/getBookmarkByPathAndShow.py)** – Retrieves and displays a specific bookmark using its path.
  ```bash
  python Uses-Cases/Bookmarks/get/getBookmarkByPathAndShow.py
  ```
- **[Bookmarks/get/getBookmarksAndShow.py](Bookmarks/get/getBookmarksAndShow.py)** – Retrieves and displays all bookmarks in a PDF document.
  ```bash
  python Uses-Cases/Bookmarks/get/getBookmarksAndShow.py
  ```
- **[Bookmarks/remove/removeBookmark.py](Bookmarks/remove/removeBookmark.py)** – Removes a specific bookmark from a PDF document using its path.
  ```bash
  python Uses-Cases/Bookmarks/remove/removeBookmark.py
  ```
- **[Bookmarks/replace/replaceBookmark.py](Bookmarks/replace/replaceBookmark.py)** – Replaces the title and properties of an existing bookmark.
  ```bash
  python Uses-Cases/Bookmarks/replace/replaceBookmark.py
  ```

#### ChangeLayout
- **[ChangeLayout/change_layout_launch.py](ChangeLayout/change_layout_launch.py)** – Orchestrates PDF layout operations: rotating, resizing, and cropping pages.
  ```bash
  python Uses-Cases/ChangeLayout/change_layout_launch.py
  ```
- *[ChangeLayout/change_layout_helper.py](ChangeLayout/change_layout_helper.py)* – Provides configuration, API client initialization, and helper methods for PDF layout change tasks.
- *[ChangeLayout/crop_document_page.py](ChangeLayout/crop_document_page.py)* – Crops a specific page in a PDF document to a defined rectangle.
- *[ChangeLayout/resize_document_all_pages.py](ChangeLayout/resize_document_all_pages.py)* – Resizes all pages in a PDF document by converting to HTML and back.
- *[ChangeLayout/rotate_documents_pages.py](ChangeLayout/rotate_documents_pages.py)* – Rotates a specified range of pages in a PDF document.

#### Compares
- **[Compares/compares_launch.py](Compares/compares_launch.py)** – Compares two PDF documents and highlights the differences.
  ```bash
  python Uses-Cases/Compares/compares_launch.py
  ```
- *[Compares/compare_pdf_documents.py](Compares/compare_pdf_documents.py)* – Performs the core comparison operation between two PDF documents.
- *[Compares/compares_helper.py](Compares/compares_helper.py)* – Provides configuration, API client initialization, and helper methods for PDF comparison tasks.

#### CompressDocument
- **[CompressDocument/compressPdf.py](CompressDocument/compressPdf.py)** – Compresses a PDF document by optimizing images and removing unused objects.
  ```bash
  python Uses-Cases/CompressDocument/compressPdf.py
  ```

#### CreateDocument
- **[CreateDocument/createPdf.py](CreateDocument/createPdf.py)** – Creates a new PDF document with customizable page properties, display settings, and metadata.
  ```bash
  python Uses-Cases/CreateDocument/createPdf.py
  ```
- **[CreateDocument/createPdfSimple.py](CreateDocument/createPdfSimple.py)** – Creates a simple, empty PDF document.
  ```bash
  python Uses-Cases/CreateDocument/createPdfSimple.py
  ```

#### EncryptDecrypt
- **[EncryptDecrypt/decryptDocument.py](EncryptDecrypt/decryptDocument.py)** – Decrypts a password-protected PDF document.
  ```bash
  python Uses-Cases/EncryptDecrypt/decryptDocument.py
  ```
- **[EncryptDecrypt/encryptDocument.py](EncryptDecrypt/encryptDocument.py)** – Encrypts a PDF document with user and owner passwords using a specified algorithm.
  ```bash
  python Uses-Cases/EncryptDecrypt/encryptDocument.py
  ```

#### Links
- **[Links/add/appendLink.py](Links/add/appendLink.py)** – Appends a new hyperlink annotation to a specific page in a PDF document.
  ```bash
  python Uses-Cases/Links/add/appendLink.py
  ```
- **[Links/get/getLinksAndShow.py](Links/get/getLinksAndShow.py)** – Retrieves and displays all hyperlink annotations on a specific PDF page.
  ```bash
  python Uses-Cases/Links/get/getLinksAndShow.py
  ```
- **[Links/remove/removeLink.py](Links/remove/removeLink.py)** – Removes a specific hyperlink annotation by its ID from a PDF document.
  ```bash
  python Uses-Cases/Links/remove/removeLink.py
  ```
- **[Links/replace/replaceLink.py](Links/replace/replaceLink.py)** – Replaces the target URL of an existing hyperlink annotation.
  ```bash
  python Uses-Cases/Links/replace/replaceLink.py
  ```

#### Pages
- **[Pages/add/appendNewPage.py](Pages/add/appendNewPage.py)** – Adds a new page to the end of a PDF document.
  ```bash
  python Uses-Cases/Pages/add/appendNewPage.py
  ```
- **[Pages/get/getPageInfoAndSavePng.py](Pages/get/getPageInfoAndSavePng.py)** – Retrieves page information and saves a specific page as a PNG image.
  ```bash
  python Uses-Cases/Pages/get/getPageInfoAndSavePng.py
  ```
- **[Pages/move/movePageNewPosition.py](Pages/move/movePageNewPosition.py)** – Moves a page to a new position within the PDF document.
  ```bash
  python Uses-Cases/Pages/move/movePageNewPosition.py
  ```
- **[Pages/remove/removePage.py](Pages/remove/removePage.py)** – Deletes a specific page from a PDF document.
  ```bash
  python Uses-Cases/Pages/remove/removePage.py
  ```
- **[Pages/stamp/pageAppendTextStamp.py](Pages/stamp/pageAppendTextStamp.py)** – Adds a text stamp to a specific page in a PDF document.
  ```bash
  python Uses-Cases/Pages/stamp/pageAppendTextStamp.py
  ```
- **[Pages/wordsCount/wordsCountOnPages.py](Pages/wordsCount/wordsCountOnPages.py)** – Retrieves the word count for each page in a PDF document.
  ```bash
  python Uses-Cases/Pages/wordsCount/wordsCountOnPages.py
  ```

#### Parser
- **[Parser/parser_launch.py](Parser/parser_launch.py)** – Orchestrates PDF parsing operations to extract form data, images, tables, and text boxes.
  ```bash
  python Uses-Cases/Parser/parser_launch.py
  ```
- *[Parser/get_fdf.py](Parser/get_fdf.py)* – Extracts PDF form field data and exports it to an FDF file.
- *[Parser/get_images.py](Parser/get_images.py)* – Extracts images from a specific page in a PDF document.
- *[Parser/get_tables.py](Parser/get_tables.py)* – Extracts tables from a PDF document.
- *[Parser/get_textboxes.py](Parser/get_textboxes.py)* – Extracts text box fields from a PDF document.
- *[Parser/get_xml.py](Parser/get_xml.py)* – Extracts PDF form field data and exports it to an XML file.
- *[Parser/paresr_helpers.py](Parser/paresr_helpers.py)* – Provides configuration, API client initialization, and helper methods for PDF parsing tasks.

#### Signatures
- **[Signatures/addDocumentSignature.py](Signatures/addDocumentSignature.py)** – Appends a new digital signature field to a PDF document.
  ```bash
  python Uses-Cases/Signatures/addDocumentSignature.py
  ```
- **[Signatures/getDocumentSignatures.py](Signatures/getDocumentSignatures.py)** – Retrieves and displays all signature fields in a PDF document.
  ```bash
  python Uses-Cases/Signatures/getDocumentSignatures.py
  ```
- **[Signatures/replaceDocumentSignature.py](Signatures/replaceDocumentSignature.py)** – Replaces an existing digital signature in a PDF document.
  ```bash
  python Uses-Cases/Signatures/replaceDocumentSignature.py
  ```
- **[Signatures/verifySignature.py](Signatures/verifySignature.py)** – Verifies the validity of a specific digital signature in a PDF document.
  ```bash
  python Uses-Cases/Signatures/verifySignature.py
  ```

#### Split
- **[Split/splitPages.py](Split/splitPages.py)** – Splits a PDF document into individual pages, each saved as a separate file.
  ```bash
  python Uses-Cases/Split/splitPages.py
  ```
- **[Split/splitRanges.py](Split/splitRanges.py)** – Splits a PDF document into multiple files based on specified page ranges.
  ```bash
  python Uses-Cases/Split/splitRanges.py
  ```

#### Stamps
- **[Stamps/add/appendStamps.py](Stamps/add/appendStamps.py)** – Appends text and image stamps to a PDF document.
  ```bash
  python Uses-Cases/Stamps/add/appendStamps.py
  ```
- **[Stamps/remove/removeStamps.py](Stamps/remove/removeStamps.py)** – Removes stamps from a specific page and by ID from a PDF document.
  ```bash
  python Uses-Cases/Stamps/remove/removeStamps.py
  ```

#### Tables
- **[Tables/add/appendTable.py](Tables/add/appendTable.py)** – Appends a new table to a specific page in a PDF document.
  ```bash
  python Uses-Cases/Tables/add/appendTable.py
  ```
- **[Tables/get/getTablesAndShow.py](Tables/get/getTablesAndShow.py)** – Retrieves and displays all tables in a PDF document.
  ```bash
  python Uses-Cases/Tables/get/getTablesAndShow.py
  ```
- **[Tables/remove/removeTables.py](Tables/remove/removeTables.py)** – Deletes a specific table and all tables on a page from a PDF document.
  ```bash
  python Uses-Cases/Tables/remove/removeTables.py
  ```
- **[Tables/replace/replaceTable.py](Tables/replace/replaceTable.py)** – Replaces an existing table in a PDF document with a new one.
  ```bash
  python Uses-Cases/Tables/replace/replaceTable.py
  ```

#### Texts
- **[Texts/replace/replaceTexts.py](Texts/replace/replaceTexts.py)** – Replaces text either across an entire PDF document or on a specific page.
  ```bash
  python Uses-Cases/Texts/replace/replaceTexts.py
  ```