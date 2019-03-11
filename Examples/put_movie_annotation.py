from configuration import *

file_name = 'PdfWithAnnotations1.pdf'
uploadFile(file_name)

attachment_file = '4pages.pdf'
uploadFile(attachment_file)

annotation = asposepdfcloud.models.MovieAnnotation()
annotation.name = 'Test Name'
annotation.rect = asposepdfcloud.models.Rectangle(
    llx=100, lly=100, urx=200, ury=200)
annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
annotation.z_index = 1
annotation.modified = '01/01/2018 12:00:00.000 AM'
annotation.file_path = temp_folder + '/' + attachment_file

response_annotations = pdf_api.get_document_movie_annotations(
    file_name, folder=temp_folder)
annotation_id = response_annotations.annotations.list[0].id

response = pdf_api.put_movie_annotation(
    file_name, annotation_id, annotation, folder=temp_folder)
pprint(response)
