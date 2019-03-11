 from configuration import *
 file_name = 'PdfWithAnnotations.pdf'
      uploadFile(file_name)


        annotation = asposepdfcloud.models.PopupAnnotation()
        annotation.name = 'Name Updated'
        annotation.rect = asposepdfcloud.models.Rectangle(llx=100, lly=100, urx=200, ury=200)
        annotation.flags = [asposepdfcloud.models.AnnotationFlags.DEFAULT]
        annotation.horizontal_alignment = asposepdfcloud.models.HorizontalAlignment.CENTER
        annotation.z_index = 1
        annotation.modified = '02/02/2018 00:00:00.000 AM'

        response_annotations = self.pdf_api.get_document_popup_annotations(file_name, folder=self.temp_folder)
        self.assertEqual(response_annotations.code, 200)
        annotation_id = response_annotations.annotations.list[0].id

        response = self.pdf_api.put_popup_annotation(file_name, annotation_id, annotation, folder=self.temp_folder)