from configuration import *

file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

page_number = 1

annotation = asposepdfcloud.models.PolygonAnnotation()
annotation.name = 'Test Name'
annotation.rect = asposepdfcloud.models.Rectangle(
    llx=100, lly=100, urx=200, ury=200)
annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
annotation.rich_text = 'Rich Text'
annotation.subject = 'Subj'
annotation.z_index = 1
annotation.title = 'Title'
annotation.vertices = [
    asposepdfcloud.models.Point(10, 10),
    asposepdfcloud.models.Point(20, 10),
    asposepdfcloud.models.Point(10, 20),
    asposepdfcloud.models.Point(10, 10)
]

response = pdf_api.post_page_polygon_annotations(
    file_name, page_number,  [annotation], folder=temp_folder)

pprint(response)
