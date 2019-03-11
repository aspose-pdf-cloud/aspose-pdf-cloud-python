from configuration import *

file_name = 'PdfWithScreenAnnotations.pdf'
uploadFile(file_name)

attachment_file = 'ScreenMovie.swf'
uploadFile(attachment_file)

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

response_annotations = pdf_api.get_document_screen_annotations(
    file_name, folder=temp_folder)
annotation_id = response_annotations.annotations.list[0].id

response = self.pdf_api.put_screen_annotation(
    file_name, annotation_id, annotation, folder=temp_folder)

pprint(response)