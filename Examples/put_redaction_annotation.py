from configuration import *
file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

page_number = 1

annotation = asposepdfcloud.models.RedactionAnnotation()
annotation.name = 'Test Name Updated'
annotation.rect = asposepdfcloud.models.Rectangle(
    llx=100, lly=100, urx=200, ury=200)
annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
annotation.z_index = 1
annotation.quad_point = [
    asposepdfcloud.models.Point(10, 40),
    asposepdfcloud.models.Point(30, 40)
]
annotation.modified = '01/01/2018 12:01:02.000 AM'

response = pdf_api.post_page_redaction_annotations(
    file_name, page_number, [annotation], folder=temp_folder)

response_annotations = pdf_api.get_document_redaction_annotations(
    file_name, folder=temp_folder)
annotation_id = response_annotations.annotations.list[0].id

response = pdf_api.put_redaction_annotation(
    file_name, annotation_id, annotation, folder=temp_folder)
pprint(response)
