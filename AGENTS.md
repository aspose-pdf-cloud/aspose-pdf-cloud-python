# Aspose.PDF Cloud SDK for Python — Agent Analysis

> **Repository:** [aspose-pdf-cloud/aspose-pdf-cloud-python](https://github.com/aspose-pdf-cloud/aspose-pdf-cloud-python)  
> **Version:** 26.7.0 | **Package:** `asposepdfcloud`  
> **License:** MIT | **Python Version:** 2.7 and 3.4+  
> **API Version:** v3.0

---

## 1. Repository Overview

The **Aspose.PDF Cloud SDK for Python** is a generated REST API client that wraps the Aspose.PDF Cloud API v3.0. It enables Python applications to perform a wide range of PDF document processing operations — creation, manipulation, conversion, and rendering — entirely in the cloud.

The SDK follows a **Python package structure** (`asposepdfcloud/`) with separate sub-packages for the API client, models, and supporting classes. All models reside in `asposepdfcloud/models/`, the API surface is in `asposepdfcloud/apis/`, and supporting utilities are at the package root level.

---

## 2. Architecture & Core Components

### 2.1 Package Structure

```
asposepdfcloud/
├── __init__.py                 # Package exports, imports all models + PdfApi + ApiClient
├── api_client.py               # ApiClient — HTTP client, OAuth2 auth, request building (710 lines)
├── configuration.py            # Configuration singleton (host, access_token, logging, SSL, proxy)
├── rest.py                     # RESTClientObject, ApiException, RESTResponse (343 lines)
├── apis/
│   └── pdf_api.py              # PdfApi — all REST endpoint methods (~2.2 MB)
└── models/
    ├── __init__.py             # Model imports (326 lines, all 294 model classes)
    ├── aspose_response.py      # Base response type
    └── {292 model files}       # One file per PDF concept
├── test/
│   ├── __init__.py
│   └── pdf_test.py             # Unit test file
├── test_data/                  # PDF fixture files (4pages.pdf, 4pagesEncrypted.pdf, etc.)
├── Uses-Cases/                 # Runnable domain-specific examples
│   ├── README.md               # Index of all use cases
│   ├── Annotations/
│   ├── Attachments/
│   ├── Bookmarks/
│   ├── ChangeLayout/
│   ├── Compares/
│   ├── CompressDocument/
│   ├── CreateDocument/
│   ├── EncryptDecrypt/
│   ├── HeaderFooter/
│   ├── Links/
│   ├── Pages/
│   ├── Parser/
│   ├── Signatures/
│   ├── Split/
│   ├── Stamps/
│   ├── Tables/
│   └── Texts/
├── settings/
│   └── credentials.json        # API credentials template
├── docs/                       # Markdown API documentation
├── setup.py                    # Package definition
├── requirements.txt            # Runtime dependencies
└── README.md                   # Usage examples and overview
```

### 2.2 Core Files

| File | Purpose |
|------|---------|
| **`asposepdfcloud/apis/pdf_api.py`** | `PdfApi` — the main API surface with all REST endpoint methods (~2.2 MB) |
| **`asposepdfcloud/api_client.py`** | `ApiClient` — handles HTTP requests, OAuth2 client credentials flow, serialization/deserialization, multipart upload. Constructor: `ApiClient(client_secret, client_id, host=None, self_host=False)` |
| **`asposepdfcloud/configuration.py`** | `Configuration` — singleton class (decorated with `@singleton`) holding `host`, `access_token`, `verify_ssl`, `proxy`, `logger` settings |
| **`asposepdfcloud/rest.py`** | `RESTClientObject` — low-level HTTP transport using `urllib3`, `RESTResponse` wrapper, `ApiException` class |
| **`asposepdfcloud/__init__.py`** | Package entry point importing all 294 model classes, `PdfApi`, `ApiClient`, and `Configuration` |

### 2.3 Key Architectural Decisions

- **urllib3 HTTP client**: The SDK uses `urllib3` for all HTTP communication — lightweight, no external HTTP library like `requests`
- **Singleton Configuration**: `Configuration` is decorated with a custom `@singleton` decorator, ensuring a single shared instance across the SDK
- **Kwargs-based API**: All API methods accept `**kwargs` for optional parameters, providing flexibility and Pythonic usage
- **Dual Python 2/3 support**: Uses the `six` compatibility library for Python 2 and 3 interoperability
- **Self-host support**: Pass `self_host=True` and custom `host` URL to `ApiClient` constructor to skip OAuth2 authentication

---

## 3. Data Model Organization

### 3.1 Model Files (294 files)

All models are in `asposepdfcloud/models/`, organized by PDF concept:

| Category | Example Files |
|----------|---------------|
| **Annotations** | `annotation.py`, `annotation_info.py`, `annotation_type.py`, `annotation_flags.py`, `annotation_state.py`, `caret_annotation.py`, `circle_annotation.py`, `file_attachment_annotation.py`, `free_text_annotation.py`, `highlight_annotation.py`, `ink_annotation.py`, `line_annotation.py`, `link_annotation.py`, `movie_annotation.py`, `polygon_annotation.py`, `poly_line_annotation.py`, `popup_annotation.py`, `redaction_annotation.py`, `screen_annotation.py`, `sound_annotation.py`, `square_annotation.py`, `squiggly_annotation.py`, `stamp_annotation.py`, `strike_out_annotation.py`, `text_annotation.py`, `underline_annotation.py` |
| **Form Fields** | `field.py`, `field_type.py`, `form_field.py`, `check_box_field.py`, `combo_box_field.py`, `list_box_field.py`, `radio_button_field.py`, `text_box_field.py`, `signature_field.py`, `choice_field.py` |
| **Document** | `document.py`, `document_config.py`, `document_property.py`, `document_properties.py`, `display_properties.py`, `document_privilege.py`, `document_layers.py`, `xmp_metadata.py` |
| **Pages** | `page.py`, `pages.py`, `page_layout.py`, `page_mode.py`, `page_range.py`, `page_word_count.py`, `word_count.py` |
| **Stamps** | `stamp.py`, `stamp_base.py`, `image_stamp.py`, `text_stamp.py`, `page_number_stamp.py`, `pdf_page_stamp.py`, `image_stamp_page_specified.py`, `text_stamp_page_specified.py`, `stamp_info.py`, `stamp_type.py`, `stamp_icon.py` |
| **Headers/Footers** | `image_header.py`, `image_footer.py`, `text_header.py`, `text_footer.py` |
| **Tables** | `table.py`, `table_broken.py`, `row.py`, `cell.py`, `table_recognized.py`, `row_recognized.py`, `cell_recognized.py` |
| **Conversions** | `doc_format.py`, `html_document_type.py`, `epub_recognition_mode.py`, `color_depth.py`, `compression_type.py`, `output_format.py` |
| **Storage** | `file_version.py`, `file_versions.py`, `files_list.py`, `files_upload_result.py`, `disc_usage.py`, `object_exist.py`, `storage_exist.py`, `storage_file.py` |
| **Signatures** | `signature.py`, `signature_field.py`, `signature_type.py`, `signature_custom_appearance.py`, `timestamp_settings.py`, `signature_verify_response.py` |
| **Primitives** | `color.py`, `point.py`, `rectangle.py`, `dash.py`, `border.py`, `border_info.py`, `margin_info.py`, `graph_info.py`, `link.py`, `link_element.py`, `position.py`, `segment.py`, `text_state.py`, `text_style.py`, `text_line.py`, `text_rect.py` |
| **Enums** | `annotation_type.py`, `border_style.py`, `border_effect.py`, `cap_style.py`, `direction.py`, `font_styles.py`, `horizontal_alignment.py`, `justification.py`, `line_ending.py`, `line_spacing.py`, `crypto_algorithm.py`, `permissions_flags.py`, `shape_type.py`, `wrap_mode.py`, `stamp_type.py`, `file_icon.py`, `sound_encoding.py`, `sound_icon.py` |

### 3.2 Response Type Naming Convention

- **Single entity:** `{Entity}Response` — e.g., `DocumentResponse`, `BookmarkResponse`, `CircleAnnotationResponse`
- **Collection:** `{Entity}sResponse` or `{Entity}esResponse` — e.g., `BookmarksResponse`, `CircleAnnotationsResponse`, `FieldsResponse`, `ImagesResponse`
- **Base:** `AsposeResponse` with `Code` (int) and `Status` (string)

---

## 4. API Capabilities

### 4.1 Document Operations

| Method | Description |
|--------|-------------|
| `get_document` | Read document info |
| `put_create_document` | Create empty document |
| `post_create_document` | Create document with config |
| `post_optimize_document` | Optimize document (compress images, remove unused objects, unembed fonts) |
| `post_split_document` | Split document into pages |
| `post_split_range_pdf_document` | Split by page ranges |
| `post_organize_document` | Reorder pages |
| `post_organize_documents` | Organize pages from multiple documents |
| `post_merge_documents` | Merge multiple documents |

### 4.2 Page Operations

| Method | Description |
|--------|-------------|
| `get_page` | Read page info |
| `post_page` | Add new page |
| `delete_page` | Delete page by number |
| `post_move_page` | Move page to new position |
| `post_document_pages_rotate` | Rotate pages by angle |
| `post_document_pages_resize` | Resize pages |
| `post_document_pages_crop` | Crop pages |
| `get_page_convert_to_tiff` / `put_page_convert_to_tiff` | Convert page to TIFF |
| `get_page_convert_to_jpeg` / `put_page_convert_to_jpeg` | Convert page to JPEG |
| `get_page_convert_to_png` / `put_page_convert_to_png` | Convert page to PNG |
| `get_page_convert_to_emf` / `put_page_convert_to_emf` | Convert page to EMF |
| `get_page_convert_to_bmp` / `put_page_convert_to_bmp` | Convert page to BMP |
| `get_page_convert_to_gif` / `put_page_convert_to_gif` | Convert page to GIF |
| `post_page_image_stamps` | Add image stamp to page |
| `post_page_text_stamps` | Add text stamp to page |
| `post_page_pdf_page_stamps` | Add PDF page stamp to page |
| `post_page_page_number_stamps` | Add page number stamp |

### 4.3 Annotations (15+ Types)

Each annotation type supports full CRUD operations:

| Operation | Pattern |
|-----------|---------|
| **Get all** | `get_document_{type}_annotations(name, ...)` |
| **Get by page** | `get_page_{type}_annotations(name, page_number, ...)` |
| **Get by ID** | `get_{type}_annotation(name, annotation_id, ...)` |
| **Create** | `post_page_{type}_annotations(name, page_number, annotation, ...)` |
| **Update** | `put_{type}_annotation(name, annotation_id, annotation, ...)` |
| **Delete** | `delete_annotation(name, annotation_id, ...)` |

Supported annotation types: Caret, Circle, FileAttachment, FreeText, Highlight, Ink, Line, Link, Movie, Polygon, PolyLine, Popup, Redaction, Screen, Sound, Square, Squiggly, Stamp, StrikeOut, Text, Underline.

### 4.4 Form Fields (8 Types)

| Field Type | Operations |
|------------|------------|
| CheckBox, ComboBox, ListBox, RadioButton, TextBox, Signature | Get document fields, get page fields, get by name, create, update, delete |
| General | `get_fields`, `put_update_fields`, `post_flatten_document` |
| Import/Export | XML, FDF, XFDF formats (GET and PUT for each) |

### 4.5 Bookmarks

| Method | Description |
|--------|-------------|
| `get_document_bookmarks` | Get bookmark tree |
| `get_bookmarks` | Get bookmarks at path |
| `get_bookmark` | Get single bookmark |
| `post_bookmark` | Add bookmark |
| `put_bookmark` | Update bookmark |
| `delete_bookmark` | Delete bookmark |
| `delete_document_bookmarks` | Delete all bookmarks |

### 4.6 Conversions

**PDF → Other formats:**
DOC, DOCX, EPUB, Excel (XLS/XLSX), HTML, MobiXML, PDF/A, PPTX, SVG, TEX, TIFF, XLS, XML, XPS, and more.

**Other formats → PDF:**
APS, BMP, EPUB, GIF, HTML, JPEG, Markdown, MHTML, PCL, PNG, PS, SVG, TeX, Web, XML, XPS, XSL FO, images.

**Pattern:** `get_{format}_in_storage_to_pdf` / `put_{format}_in_storage_to_pdf` for each source format.

### 4.7 Storage & File Management

| Method | Description |
|--------|-------------|
| `upload_file` | Upload file to cloud storage |
| `download_file` | Download file from cloud storage |
| `copy_file` / `move_file` / `delete_file` | File operations |
| `create_folder` / `copy_folder` / `move_folder` / `delete_folder` | Folder operations |
| `get_files_list` | List files in folder |
| `get_disc_usage` | Get storage usage |
| `object_exists` / `storage_exists` | Check existence |
| `get_file_versions` | List file versions |

### 4.8 Other Features

| Feature | Key Methods |
|---------|-------------|
| **Text** | `get_text`, `get_page_text`, `put_add_text` |
| **Images** | `get_images`, `get_image`, `delete_image`, `post_insert_image` |
| **Links** | `get_page_link_annotations`, `post_page_link_annotations`, `put_link_annotation`, `delete_link_annotation` |
| **Stamps** | `get_document_stamps`, `post_page_text_stamps`, `post_page_image_stamps`, `delete_stamp` |
| **Tables** | `get_document_tables`, `post_page_tables`, `put_table`, `delete_table` |
| **Watermarks** | Via image stamps |
| **Headers/Footers** | Via text/image stamps |
| **Encryption** | `put_encrypt_document`, `put_decrypt_document`, `put_change_password_document` |
| **Properties** | `get_document_properties`, `put_set_property`, `delete_property` |
| **XMP Metadata** | `get_xmp_metadata_json`, `get_xmp_metadata_xml`, `post_xmp_metadata` |
| **Layers** | `get_document_layers`, `delete_document_layer` |
| **Compare** | `post_compare_document` |
| **Privileges** | `put_privileges` |
| **OCR** | `put_searchable_document` |

---

## 5. Testing Infrastructure

### 5.1 Test File (`test/pdf_test.py`)

- Single test file containing all unit tests
- Reads credentials from `settings/credentials.json`
- Uses `ApiClient` with credentials from JSON config
- Provides `upload_file(name)` helper for pre-uploading test files
- Supports both public cloud and self-hosted modes

### 5.2 Credentials Format (`settings/credentials.json`)

```json
{
    "client_secret": "YOUR_CLIENT_SECRET",
    "client_id": "YOUR_CLIENT_ID",
    "api_url": "https://api.aspose.cloud/v3.0",
    "self_host": false
}
```

### 5.3 Test Pattern

```python
import asposepdfcloud
from asposepdfcloud import PdfApi, ApiClient

config = asposepdfcloud.configuration.Configuration()
with open('settings/credentials.json') as f:
    creds = json.load(f)

api_client = ApiClient(creds['client_secret'], creds['client_id'],
                       creds.get('api_url'), creds.get('self_host', False))
pdf_api = PdfApi(api_client)

response = pdf_api.get_page_annotations(file_name, page_number, folder=temp_folder)
print(response.code)
```

### 5.4 Test Fixtures

Test fixture PDF files are located in `test_data/`:
- `4pages.pdf`, `4pagesEncrypted.pdf`, `4pagesPdfA.pdf` — multi-page documents
- `33226.p12` — certificate for digital signatures
- `33539.jpg`, `44781.jpg` — image files
- `5pages.aps`, `5pages.pdf` — additional documents
- `adbe.x509.rsa_sha1.valid.pdf` — signed PDF

### 5.5 Running Tests

```bash
python -m pytest test/
```

---

## 6. Use Cases (`Uses-Cases/`)

The `Uses-Cases/` directory contains **domain-specific, runnable Python examples** organized by domain.

### 6.1 Directory Structure

Each domain directory contains py files with standalone entry points:

```
Uses-Cases/{domain}/
├── add/                        # Group folder (optional)
│   └── somefile.py             # Individual files (optional)       
├── anotherfile.py              # Individual files (optional)
```

### 6.2 README.md Format

The `Uses-Cases/README.md` file serves as the **index and documentation** for all use case domains. It follows a strict format:

```markdown
#### {domain}
- **[{domain}/{path to main file}.py]({domain}/{path to main file}.py)** – Description of the main entry file containing top level statements.
  ```bash
  python Uses-Cases/{domain}/{path to main file}.py
  ```
- *[{domain}/{path to operation file}.py]({domain}/{path to operation file}.py)* – Description of the operation containing only classes declarations.
```

**Formatting Rules:**

| Element | Rule |
|---------|------|
| **Section header** | `#### {domain}` — level-4 heading, PascalCase |
| **Main files** | Listed first, bold (`**`), includes `python` run command in a code block |
| **Operation files** | Listed after main files, italic (`*`), one per line |
| **File links** | Relative paths from `Uses-Cases/` directory |
| **Descriptions** | Present tense, action-oriented (e.g., "Adds", "Retrieves", "Deletes") |
| **Blank lines** | One blank line between sections |

### Example

```markdown
#### Compares
- **[Compares/compares_launch.py](Compares/compares_launch.py)** – Compares two PDF documents and highlights the differences.
  ```bash
  python Uses-Cases/Compares/compares_launch.py
  ```
- *[Compares/compare_pdf_documents.py](Compares/compare_pdf_documents.py)* – Performs the core comparison operation between two PDF documents.
- *[Compares/compares_helper.py](Compares/compares_helper.py)* – Provides configuration, API client initialization, and helper methods for PDF comparison tasks.
```

### 6.3 File Inclusion/Exclusion Rules

When generating or updating `Uses-Cases/README.md`, the following rules determine which files are included:

#### Included Files

| File Pattern | Reason | Example |
|-------------|--------|---------|
| `*{main}.py` (main files) | py files that contains top level statements | `addDocumentSignature.py`, `replaceDocumentSignature.py` |
| `*{operation}.py` (operation files) | py files that contains only class declarations | `comparePdfDocuments.py` |

#### Excluded Files

| File Pattern | Reason | Example |
|-------------|--------|---------|
| **Non-`.py` files** | Only py source files are documented | `*.md`, `*.json`, `*.pdf` |
| `*.py` (helper files) | Shared utilities (API init, file upload/download) | `comparesHelper.py` |
| `*.py` (data files)| Test data files (Initialization of complex data) | `fields.py` |
| **Files outside `UsesCases/`** | README only covers the `UsesCases/` directory | Root-level `*.py` files |
| **Hidden files/directories** | Not user-facing | `.DS_Store`, `.gitkeep` |

#### Ordering Rules

1. **Domains** are listed in **alphabetical order** by directory name.
2. **Within a domain**, files are ordered as:
   - `{main}.py` (first, bold)
   - All remaining `*.py` files in **alphabetical order** (italic)

---

## 7. Design Patterns & Conventions

### 7.1 Code Generation

The SDK is **auto-generated** from the OpenAPI specification. Evidence:
- `.swagger-codegen-ignore` file present
- Consistent, repetitive method structure across all API methods
- Uniform model structure across all 294 model files
- Predictable naming patterns: `get_{entity}`, `post_{entity}`, `put_{entity}`, `delete_{entity}`

### 7.2 Key Conventions

| Convention | Description |
|------------|-------------|
| **Python package** | `asposepdfcloud` — single top-level package |
| **Sub-packages** | `apis/` for `PdfApi`, `models/` for all model classes |
| **Snake_case API** | All API methods use snake_case: `get_page_annotations`, `put_create_document` |
| **MIT license header** | Every Python file starts with the same copyright block |
| **Kwargs for options** | Optional parameters passed as `**kwargs` to all API methods |
| **Callback support** | Each API method supports async callback via `callback` kwarg |
| **Self-host support** | `ApiClient(secret, id, host_url, self_host=True)` skips OAuth2 |
| **Singleton config** | `Configuration` class decorated with `@singleton` |
| **Dual Python 2/3** | Uses `six` compatibility library for cross-version support |

### 7.3 Configuration Pattern

```python
import asposepdfcloud
from asposepdfcloud import ApiClient, PdfApi

# Public cloud
api_client = ApiClient('YOUR_CLIENT_SECRET', 'YOUR_CLIENT_ID')

# Self-hosted
api_client = ApiClient('', '', 'https://self-hosted-api.example.com', True)

# Instantiate API
pdf_api = PdfApi(api_client)
```

### 7.4 Error Handling

```python
from asposepdfcloud.rest import ApiException

try:
    result = pdf_api.get_page_annotations(file_name, page_number, folder=temp_folder)
except ApiException as e:
    # e.status      — HTTP status code
    # e.reason      — HTTP reason phrase
    # e.body        — raw response body
    # e.headers     — response headers
    print(f"Error {e.status}: {e.reason}")
```

---

## 8. Dependencies & Build

### 8.1 Dependencies

| Dependency | Version | Purpose |
|------------|---------|---------|
| `urllib3` | >= 1.15 | HTTP client library |
| `six` | >= 1.10 | Python 2/3 compatibility |
| `certifi` | >= 14.05.14 | SSL certificate bundle |
| `python-dateutil` | >= 2.5.3 | Date/time parsing |
| `setuptools` | >= 21.0.0 | Package installation |

### 8.2 Installation

```bash
pip install asposepdfcloud
```

Or from source:

```bash
python setup.py install
```

---

## 9. Documentation

The `docs/` directory contains **Markdown files** with API reference documentation:

- `PdfApi.md` — Full API method reference
- `{Model}.md` — One file per model type (e.g., `Document.md`, `Annotation.md`, `Bookmark.md`)
- `{Response}.md` — One file per response type (e.g., `DocumentResponse.md`, `AnnotationsResponse.md`)

---

