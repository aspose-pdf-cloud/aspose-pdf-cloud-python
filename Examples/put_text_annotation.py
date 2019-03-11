from configuration import *
file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

annotation = asposepdfcloud.models.TextAnnotation()
annotation.name = 'Test Free Text'
annotation.rect = asposepdfcloud.models.Rectangle(
    llx=100, lly=100, urx=200, ury=200)
annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
annotation.rich_text = 'Rich Text'
annotation.subject = 'Text Box Subj'
annotation.z_index = 1
annotation.title = 'Title'
annotation.state = asposepdfcloud.models.AnnotationState.UNDEFINED

response_annotations = pdf_api.get_document_text_annotations(
    file_name, folder=temp_folder)
annotation_id = response_annotations.annotations.list[0].id

response = pdf_api.put_text_annotation(
    file_name, annotation_id, annotation, folder=temp_folder)

pprint(response)
