from acroforms_helper import PdfAcroformsHelper, Config
from acroforms_add import PdfAcroformsAdd
from acroforms_get import PdfAcroformsGet
from acroforms_remove import PdfAcroformsDel
from acroforms_set import PdfAcroformsSetter
from acroforms_update import PdfAcroformsUpdate

if __name__ == "__main__":
	helper = PdfAcroformsHelper(Config.CREDENTIALS_FILE)

	add_filed = PdfAcroformsAdd(helper.pdf_api, helper)
	add_filed.addField(Config.PDF_DOCUMENT_NAME, Config.LOCAL_RESULT_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)

	del_fild =PdfAcroformsDel(helper.pdf_api, helper)
	del_fild.delField(Config.PDF_DOCUMENT_NAME, Config.LOCAL_RESULT_DOCUMENT_NAME, Config.FIELD_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)

	get_filed = PdfAcroformsGet(helper.pdf_api, helper)
	get_filed.getField(Config.PDF_DOCUMENT_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)

	set_fild = PdfAcroformsSetter(helper.pdf_api, helper)
	set_fild.setField(Config.PDF_DOCUMENT_NAME, Config.LOCAL_RESULT_DOCUMENT_NAME, Config.FIELD_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)

	upd_fild = PdfAcroformsUpdate(helper.pdf_api, helper)
	upd_fild.updField(Config.PDF_DOCUMENT_NAME, Config.LOCAL_RESULT_DOCUMENT_NAME, Config.FIELD_NAME, Config.LOCAL_FOLDER, Config.REMOTE_FOLDER)