# SignatureCustomAppearance
An abstract class which represents signature custom appearance object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**font_family_name** | **str** | Gets/sets font family name. It should be existed in the document. Default value: Arial. | [optional] 
**font_size** | **float** | Gets/sets font size. Default value: 10. | [optional] 
**rotation** | [**Rotation**](Rotation.md) | Gets or sets signature rotation. | 
**show_contact_info** | **bool** | Gets/sets contact info visibility. Default value: true. | 
**show_reason** | **bool** | Gets/sets reason visibility. Default value: true. | 
**show_location** | **bool** | Gets/sets location visibility. Default value: true. | 
**contact_info_label** | **str** | Gets/sets contact info label. Default value: &quot;Contact&quot;. | [optional] 
**reason_label** | **str** | Gets/sets reason label. Default value: &quot;Reason&quot;. | [optional] 
**location_label** | **str** | Gets/sets location label. Default value: &quot;Location&quot;. | [optional] 
**digital_signed_label** | **str** | Gets/sets digital signed label. Default value: &quot;Digitally signed by&quot;. | [optional] 
**date_signed_at_label** | **str** | Gets/sets date signed label. Default value: &quot;Date&quot;. | [optional] 
**date_time_local_format** | **str** | Gets/sets datetime local format. Default value: &quot;yyyy.MM.dd HH:mm:ss zzz&quot;. | [optional] 
**date_time_format** | **str** | Gets/sets datetime format. Default value: &quot;yyyy.MM.dd HH:mm:ss&quot;. | [optional] 
**background_color** | [**Color**](Color.md) | Gets/sets background color. | [optional] 
**foreground_color** | [**Color**](Color.md) | Gets/sets foreground color. | [optional] 
**use_digital_subject_format** | **bool** | Gets/sets subject format usage. | 
**digital_subject_format** | [**list[SignatureSubjectNameElements]**](SignatureSubjectNameElements.md) | Gets/sets subject format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


