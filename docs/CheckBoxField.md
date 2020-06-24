# CheckBoxField
Provides CheckBoxField.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) | Link to the document. | [optional] 
**partial_name** | **str** | Field name. | [optional] 
**full_name** | **str** | Full Field name. | [optional] 
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
**allowed_states** | **list[str]** | Returns list of allowed states. | [optional] 
**style** | [**BoxStyle**](BoxStyle.md) | Gets or sets style of check box. | [optional] 
**active_state** | **str** | Gets or sets current annotation appearance state. | [optional] 
**checked** | **bool** | Gets or sets state of check box. | 
**export_value** | **str** | Gets or sets export value of CheckBox field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


