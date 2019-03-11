from configuration import *

file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

response_annotations = pdf_api.get_document_polygon_annotations(
    file_name, folder=temp_folder)
annotation_id = response_annotations.annotations.list[0].id

response = pdf_api.get_polygon_annotation(
    file_name, annotation_id, folder=temp_folder)

pprint(response)
