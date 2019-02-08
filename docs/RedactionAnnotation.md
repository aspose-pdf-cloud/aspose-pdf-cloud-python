# RedactionAnnotation
Provides RedactionAnnotation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) | Link to the document. | [optional] 
**color** | [**Color**](Color.md) | Color of the annotation. | [optional] 
**contents** | **str** | Get the annotation content. | [optional] 
**modified** | **str** | The date and time when the annotation was last modified. | [optional] 
**id** | **str** | Gets ID of the annotation. | [optional] 
**flags** | [**list[AnnotationFlags]**](AnnotationFlags.md) | Gets Flags of the annotation. | [optional] 
**name** | **str** | Gets Name of the annotation. | [optional] 
**rect** | [**Rectangle**](Rectangle.md) | Gets Rect of the annotation. | [optional] 
**page_index** | **int** | Gets PageIndex of the annotation. | [optional] 
**z_index** | **int** | Gets ZIndex of the annotation. | [optional] 
**horizontal_alignment** | [**HorizontalAlignment**](HorizontalAlignment.md) | Gets HorizontalAlignment of the annotation. | [optional] 
**vertical_alignment** | [**VerticalAlignment**](VerticalAlignment.md) | Gets VerticalAlignment of the annotation. | [optional] 
**quad_point** | [**list[Point]**](Point.md) | An array of 8xN numbers specifying the coordinates of content region that is intended to be removed.  | [optional] 
**fill_color** | [**Color**](Color.md) | Gets or sets color to fill annotation. | [optional] 
**border_color** | [**Color**](Color.md) | Gets or sets color of border which is drawn when redaction is not active. | [optional] 
**overlay_text** | **str** | Text to print on redact annotation. | [optional] 
**repeat** | **bool** | If true overlay text will be repated on the annotation.  | [optional] 
**text_alignment** | [**HorizontalAlignment**](HorizontalAlignment.md) | Gets or sets. Alignment of Overlay Text. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


