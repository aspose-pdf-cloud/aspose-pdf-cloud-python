from configuration import *

file_name = 'PdfWithScreenAnnotations.pdf'
uploadFile(file_name)

attachment_file = 'ScreenMovie.swf'
uploadFile(attachment_file)

page_number = 1

annotation = asposepdfcloud.models.ScreenAnnotation()
annotation.name = 'Test Name'
annotation.rect = asposepdfcloud.models.Rectangle(
    llx=100, lly=100, urx=200, ury=200)
annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
annotation.z_index = 1
annotation.title = 'Title'
annotation.modified = '01/01/2018 12:00:00.000 AM'
annotation.file_path = temp_folder + '/' + attachment_file

response = pdf_api.post_page_screen_annotations(
    file_name, page_number, [annotation], folder=temp_folder)

pprint(response)
