from configuration import *

file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

annotation = asposepdfcloud.models.LineAnnotation()
annotation.name = 'Test Name Updated'
annotation.rect = asposepdfcloud.models.Rectangle(
    llx=100, lly=100, urx=200, ury=200)
annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
annotation.rich_text = 'Rich Text Updated'
annotation.subject = 'Subj Updated'
annotation.z_index = 1
annotation.starting = asposepdfcloud.models.Point(10, 10)
annotation.ending = asposepdfcloud.models.Point(100, 100)

response_annotations = pdf_api.get_document_line_annotations(
    file_name, folder=temp_folder)
annotation_id = response_annotations.annotations.list[0].id

response = pdf_api.put_line_annotation(
    file_name, annotation_id, annotation, folder=temp_folder)

pprint(response)
