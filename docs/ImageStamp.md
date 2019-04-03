# ImageStamp
Represents Pdf stamps.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) | Link to the document. | [optional] 
**background** | **bool** | Sets or gets a bool value that indicates the content is stamped as background. If the value is true, the stamp content is layed at the bottom. By defalt, the value is false, the stamp content is layed at the top. | [optional] 
**bottom_margin** | **float** | Gets or sets bottom margin of stamp. | [optional] 
**horizontal_alignment** | [**HorizontalAlignment**](HorizontalAlignment.md) | Gets or sets Horizontal alignment of stamp on the page.  | [optional] 
**left_margin** | **float** | Gets or sets left margin of stamp. | [optional] 
**opacity** | **float** | Gets or sets a value to indicate the stamp opacity. The value is from 0.0 to 1.0. By default the value is 1.0. | [optional] 
**right_margin** | **float** | Gets or sets right margin of stamp. | [optional] 
**rotate** | [**Rotation**](Rotation.md) | Sets or gets the rotation of stamp content according  values. Note. This property is for set angles which are multiples of 90 degrees (0, 90, 180, 270 degrees). To set arbitrary angle use RotateAngle property.  If angle set by ArbitraryAngle is not multiple of 90 then Rotate property returns Rotation.None. | [optional] 
**rotate_angle** | **float** | Gets or sets rotate angle of stamp in degrees. This property allows to set arbitrary rotate angle.  | [optional] 
**top_margin** | **float** | Gets or sets top margin of stamp. | [optional] 
**vertical_alignment** | [**VerticalAlignment**](VerticalAlignment.md) | Gets or sets vertical alignment of stamp on page. | [optional] 
**x_indent** | **float** | Horizontal stamp coordinate, starting from the left. | [optional] 
**y_indent** | **float** | Vertical stamp coordinate, starting from the bottom. | [optional] 
**zoom** | **float** | Zooming factor of the stamp. Allows to scale stamp. | [optional] 
**file_name** | **str** | Gets or sets the file name. | [optional] 
**width** | **float** | Gets or sets image width. Setting this property allos to scal image horizontally. | [optional] 
**height** | **float** | Gets or sets image height. Setting this image allows to scale image vertically. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


