from configuration import *
file_name = 'PdfWithAnnotations.pdf'
uploadFile(file_name)

parent_id = 'GI5TCMR3GE2TQLBSGM3CYMJYGUWDENRV'

annotation = asposepdfcloud.models.PopupAnnotation()
annotation.name = 'Name'
annotation.rect = asposepdfcloud.models.Rectangle(
    llx=100, lly=100, urx=200, ury=200)
annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
annotation.z_index = 1
annotation.modified = '02/02/2018 00:00:00.000 AM'

response = pdf_api.post_popup_annotation(
    file_name, parent_id, annotation, folder=temp_folder)

pprint(response)
