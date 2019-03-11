from configuration import *

file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

text_style = asposepdfcloud.models.TextStyle(font_size=12, font='Arial',
                                             foreground_color=asposepdfcloud.models.Color(
                                                 a=0xFF, r=0, g=0xFF, b=0),
                                             background_color=asposepdfcloud.models.Color(a=0xFF, r=0xFF, g=0, b=0))

annotation = asposepdfcloud.models.FreeTextAnnotation()
annotation.name = 'Test Free Text'
annotation.text_style = text_style
annotation.rect = asposepdfcloud.models.Rectangle(
    llx=100, lly=100, urx=200, ury=200)
annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
annotation.intent = asposepdfcloud.models.FreeTextIntent.FREETEXTTYPEWRITER
annotation.rich_text = 'Rich Text'
annotation.subject = 'Text Box Subj'
annotation.z_index = 1
annotation.justification = asposepdfcloud.models.Justification.CENTER
annotation.title = 'Title'

response_annotations = pdf_api.get_document_free_text_annotations(
    file_name, folder=temp_folder)
annotation_id = response_annotations.annotations.list[0].id

response = pdf_api.put_free_text_annotation(
    file_name, annotation_id, annotation, folder=temp_folder)

pprint(response)
