from configuration import *

response =pdf_api.get_document_annotations("PdfWithAnnotations.pdf")
pprint(response)
