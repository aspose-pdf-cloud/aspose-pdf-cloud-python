from configuration import *
file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

response_annotations = pdf_api.get_document_file_attachment_annotations(
    file_name, folder=temp_folder)
annotation_id = response_annotations.annotations.list[0].id

response = pdf_api.get_file_attachment_annotation_data(
    file_name, annotation_id, folder=temp_folder)

pprint(response)
