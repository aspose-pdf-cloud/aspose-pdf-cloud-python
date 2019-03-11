from configuration import *

file_name = 'PdfWithScreenAnnotations.pdf'
uploadFile(file_name)
response_annotations =pdf_api.get_document_screen_annotations(file_name, folder=temp_folder)
annotation_id = response_annotations.annotations.list[0].id
response = pdf_api.put_screen_annotation_data_extract(
    file_name, annotation_id, folder=temp_folder)

pprint(response)
