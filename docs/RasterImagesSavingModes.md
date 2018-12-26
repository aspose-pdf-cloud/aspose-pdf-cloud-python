# RasterImagesSavingModes
Converted PDF can contain raster images(.png, *.jpeg etc.)
This enum defines methods of how raster images can be handled
during conversion of PDF to HTML
            

## Enum
Name | Type | Value | Description
------------ | ------------- | ------------- | -------------
**ASPNGIMAGESEMBEDDEDINTOSVG** | **str** | "AsPngImagesEmbeddedIntoSvg" | for each distinct raster file will be generated wrapper SVG image, and raster image will be embedded as Base64 encoded strings into that SVG image
**ASEXTERNALPNGFILESREFERENCEDVIASVG** | **str** | "AsExternalPngFilesReferencedViaSvg" | distinct raster images will be put apart as PNG files but will be referenced through wrapping SVG images, i.e. will be generated one PNG file and one SVG for each raster image, and each of such SVGs will contain links to relevant PNG file
**ASEMBEDDEDPARTSOFPNGPAGEBACKGROUND** | **str** | "AsEmbeddedPartsOfPngPageBackground" | Will be generated one big PNG background file for each result page. Raster images will be embedded into that file and rendered as regions of that image. No external PNG files for each image will be generated, only one PNG file per page will be present in conversion result set of files.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


