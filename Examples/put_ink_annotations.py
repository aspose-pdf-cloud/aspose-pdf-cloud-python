from configuration import *

file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

annotation = asposepdfcloud.models.InkAnnotation()
annotation.name = 'Name Updated'
annotation.rect = asposepdfcloud.models.Rectangle(
    llx=100, lly=100, urx=200, ury=200)
annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
annotation.rich_text = 'Text Updated'
annotation.subject = 'Subj Updated'
annotation.z_index = 1
annotation.title = 'Title Updated'
annotation.ink_list = [
    [
        asposepdfcloud.models.Point(10, 40),
        asposepdfcloud.models.Point(30, 40),
    ],
    [
        asposepdfcloud.models.Point(10, 20),
        asposepdfcloud.models.Point(20, 20),
        asposepdfcloud.models.Point(30, 20),
    ]
]
annotation.cap_style = asposepdfcloud.models.CapStyle.ROUNDED
annotation.modified = '02/02/2018 00:00:00.000 AM'

response_annotations = pdf_api.get_document_ink_annotations(
    file_name, folder=temp_folder)
annotation_id = response_annotations.annotations.list[0].id

response = pdf_api.put_ink_annotation(
    file_name, annotation_id, annotation, folder=temp_folder)

pprint(response)
