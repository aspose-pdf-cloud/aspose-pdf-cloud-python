# OptimizeOptions
Represents Pdf optimize options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_reuse_page_content** | **bool** | If true page contents will be reused when document is optimized for equal pages. | [optional] 
**compress_images** | **bool** | If this flag is set to true images will be compressed in the document. Compression level is specified with ImageQuality property. | [optional] 
**image_quality** | **int** | Specifies level of image compression when CompressImages flag is used. | [optional] 
**link_duplcate_streams** | **bool** | If this flag is set to true, Resource streams will be analyzed. If duplicate streams are found (i.e. if stream contents is equal), then thees streams will be stored as one object.  This allows to decrease document size in some cases (for example, when same document was concatenated multiple times). | [optional] 
**remove_unused_objects** | **bool** | If this flag is set to true, all document objects will be checked and unused objects (i.e. objects which does not have any reference) are removed from document. | [optional] 
**remove_unused_streams** | **bool** | If this flag set to true, every resource is checked on it&#39;s usage. If resource is never used, then resources is removed. This may decrease document size for example when pages were extracted from document.  | [optional] 
**unembed_fonts** | **bool** | Make fonts not embedded if set to true.  | [optional] 
**resize_images** | **bool** | If this flag set to true and CompressImages is true images will be resized if image resolution is greater then specified MaxResolution parameter. | [optional] 
**max_resolution** | **int** | Specifies maximum resolution of images. If image has higher resolution it will be scaled. | [optional] 
**subset_fonts** | **bool** | Fonts will be converted into subsets if set to true. | [optional] 
**remove_private_info** | **bool** | Remove private information (page piece info). | [optional] 
**image_encoding** | [**ImageEncoding**](ImageEncoding.md) | Image encode which will be used. | [optional] 
**image_compression_version** | [**ImageCompressionVersion**](ImageCompressionVersion.md) | Version of compression algorithm. Possible values are: &quot;Standard&quot; - standard compression, &quot;Fast&quot; - fast (improved compression which is faster then standard but may be applicable not for all images), &quot;Mixed&quot; - mixed (standard compression is applied to images which can not be compressed by  faster algorithm, this may give best compression but more slow then &quot;Fast&quot; algorithm. Version &quot;Fast&quot; is not applicable for resizing images (standard method will be used). Default is &quot;Standard&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


