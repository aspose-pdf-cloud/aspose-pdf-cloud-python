# DocRecognitionMode
Allows to control how a PDF document is converted into a word processing document.

## Enum
Name | Type | Value | Description
------------ | ------------- | ------------- | -------------
**TEXTBOX** | **str** | "Textbox" | This mode is fast and good for maximally preserving original look of the PDF file, but editability of the resulting document could be limited.Every visually grouped block of text int the original PDF file is converted into a textbox in the resulting document. This achieves maximal resemblance of the output document to the original PDF file. The output document will look good, but it will consist entirely of textboxes and it could makes further editing of the document in Microsoft Word quite hard.This is the default mode.
**FLOW** | **str** | "Flow" | Full recognition mode, the engine performs grouping and multi-level analysis to restore the original document author's intent and produce a maximally editable document. The downside is that the output document might look different from the original PDF file.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


