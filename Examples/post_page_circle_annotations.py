from configuration import *

file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

page_number = 1

annotation = asposepdfcloud.models.CircleAnnotation()
annotation.name = 'Test Name'
annotation.rect = asposepdfcloud.models.Rectangle(
    llx=100, lly=100, urx=200, ury=200)
annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
annotation.rich_text = 'Rich Text'
annotation.subject = 'Subj'
annotation.z_index = 1
annotation.title = 'Title'

response =pdf_api.post_page_circle_annotations(
    file_name, page_number,  [annotation], folder=temp_folder)
