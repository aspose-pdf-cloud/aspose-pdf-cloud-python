from configuration import *
file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

page_number = 1

annotation = asposepdfcloud.models.InkAnnotation()
annotation.name = 'Name'
annotation.rect = asposepdfcloud.models.Rectangle(
    llx=100, lly=100, urx=200, ury=200)
annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
annotation.rich_text = 'Rich Text'
annotation.subject = 'Subj'
annotation.z_index = 1
annotation.title = 'Title'
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

response = pdf_api.post_page_ink_annotations(
    file_name, page_number,  [annotation], folder=temp_folder)
