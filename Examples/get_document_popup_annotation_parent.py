from configuration import *
file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

parent_id = 'GI5TAOZRGU3CYNZSGEWDCNZWFQ3TGOI'

response = pdf_api.get_document_popup_annotations_by_parent(
    file_name, parent_id, folder=temp_folder)

pprint(response)
