# ComboBoxField
Provides ComboBoxField.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) | Link to the document. | [optional] 
**partial_name** | **str** | Field name. | [optional] 
**rect** | [**Rectangle**](Rectangle.md) | Field rectangle. | [optional] 
**value** | **str** | Field value. | [optional] 
**page_index** | **int** | Page index. | 
**height** | **float** | Gets or sets height of the field. | [optional] 
**width** | **float** | Gets or sets width of the field. | [optional] 
**z_index** | **int** | Z index. | [optional] 
**is_group** | **bool** | Is group. | [optional] 
**parent** | [**FormField**](FormField.md) | Gets field parent. | [optional] 
**is_shared_field** | **bool** | Property for Generator support. Used when field is added to header or footer. If true, this field will created once and it&#39;s appearance will be visible on all pages of the document. If false, separated field will be created for every document page. | [optional] 
**flags** | [**list[AnnotationFlags]**](AnnotationFlags.md) | Gets Flags of the field. | [optional] 
**color** | [**Color**](Color.md) | Color of the annotation. | [optional] 
**contents** | **str** | Get the field content. | [optional] 
**margin** | [**MarginInfo**](MarginInfo.md) | Gets or sets a outer margin for paragraph (for pdf generation) | [optional] 
**highlighting** | [**LinkHighlightingMode**](LinkHighlightingMode.md) | Field highlighting mode. | [optional] 
**horizontal_alignment** | [**HorizontalAlignment**](HorizontalAlignment.md) | Gets HorizontalAlignment of the field. | [optional] 
**vertical_alignment** | [**VerticalAlignment**](VerticalAlignment.md) | Gets VerticalAlignment of the field. | [optional] 
**border** | [**Border**](Border.md) | Gets or sets annotation border characteristics. | [optional] 
**multi_select** | **bool** | Gets or sets multiselection flag. | [optional] 
**selected** | **int** | Gets or sets index of selected item. Numbering of items is started from 1. | [optional] 
**options** | [**list[Option]**](Option.md) | Gets collection of options of the combobox. | [optional] 
**active_state** | **str** | Gets or sets current annotation appearance state. | [optional] 
**editable** | **bool** | Gets or sets editable status of the field. | [optional] 
**spell_check** | **bool** | Gets or sets spellchaeck activiity status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


