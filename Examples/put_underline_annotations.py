from configuration import *
file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

annotation = asposepdfcloud.models.UnderlineAnnotation()
annotation.name = 'Name Updated'
annotation.rect = asposepdfcloud.models.Rectangle(
    llx=100, lly=100, urx=200, ury=200)
annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
annotation.rich_text = 'Text Updated'
annotation.subject = 'Subj Updated'
annotation.z_index = 1
annotation.title = 'Title Updated'
annotation.quad_points = [
    asposepdfcloud.models.Point(10, 10),
    asposepdfcloud.models.Point(20, 10),
    asposepdfcloud.models.Point(10, 20),
    asposepdfcloud.models.Point(10, 10)
]
annotation.modified = '02/02/2018 00:00:00.000 AM'

response_annotations = pdf_api.get_document_underline_annotations(
    file_name, folder=temp_folder)
annotation_id = response_annotations.annotations.list[0].id

response = pdf_api.put_underline_annotation(
    file_name, annotation_id, annotation, folder=temp_folder)
pprint(response)