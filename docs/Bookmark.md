# Bookmark
Provides link to bookmark.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) | Link to the document. | [optional] 
**title** | **str** | Get the Title; | [optional] 
**italic** | **bool** | Is bookmark italic. | [optional] 
**bold** | **bool** | Is bookmark bold. | [optional] 
**color** | [**Color**](Color.md) | Get the color | [optional] 
**action** | **str** | Gets or sets the action bound with the bookmark. If PageNumber is presented the action can not be specified. The action type includes: &quot;GoTo&quot;, &quot;GoToR&quot;, &quot;Launch&quot;, &quot;Named&quot;. | [optional] 
**level** | **int** | Gets or sets bookmark&#39;s hierarchy level. | [optional] 
**destination** | **str** | Gets or sets bookmark&#39;s destination page. Required if action is set as string.Empty. | [optional] 
**page_display** | **str** | Gets or sets the type of display bookmark&#39;s destination page. | [optional] 
**page_display_bottom** | **int** | Gets or sets the bottom coordinate of page display. | [optional] 
**page_display_left** | **int** | Gets or sets the left coordinate of page display. | [optional] 
**page_display_right** | **int** | Gets or sets the right coordinate of page display. | [optional] 
**page_display_top** | **int** | Gets or sets the top coordinate of page display. | [optional] 
**page_display_zoom** | **int** | Gets or sets the zoom factor of page display. | [optional] 
**page_number** | **int** | Gets or sets the number of bookmark&#39;s destination page.  | [optional] 
**remote_file** | **str** | Gets or sets the file (path) which is required for &quot;GoToR&quot; action of bookmark. | [optional] 
**bookmarks** | [**Bookmarks**](Bookmarks.md) | The children bookmarks. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


