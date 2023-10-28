# Metadata_deleter

Simple console app for simple users :sunglasses:


## Run as a python script

```sh
git clone https://github.com/practicesavedtheworld/metadata_deleter.git
```
```sh
cd metadata_deleter
```
```sh
poetry install
```
```sh
python3 metadata_deleter
```

## Restrictions


At this moment supports formats:


    "rgb",
    "gif",
    "pbm",
    "pgm",
    "ppm",
    "tiff",
    "rast",
    "xbm",
    "jpeg",
    "bmp",
    "png",
    "webp",
    "exr",
    "svg",
    "docx"

## Which commands is available now ?

|  COMMAND | ACTION |
| ----------- | ----------- |
| change <br> -c | Change mod. Set value to on of a metadata field  |
| delete <br> -d  | Removes all found file metadata. |
| metadata <br> -m | Presenting list of metadata field related to file  |
| metadata-detailed <br> -md  | Presenting metadata like filed - value object. For e.g. <br> M_field1      M_value1 <br> M_field2      M_value2 |
| save  <br> -s | Save the file after metadata changing/deleting   |



