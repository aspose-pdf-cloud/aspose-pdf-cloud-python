from configuration import *
file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

page_number = 1

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

response = pdf_api.post_page_text_annotations(
    file_name, page_number,  [annotation], folder=temp_folder)

pprint(response)
