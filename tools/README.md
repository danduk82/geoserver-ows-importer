# OWS importer script from fis-broker to geoserver

## install the dependencies:


```shell
cd tools/
pip install poetry
poetry install
```

## Create a new config file

Copy `config.ini` and adapt your file

```shell
cp config.ini /some/other/file.ini
# then adapt it 
```

Then run the script with that config file using the `-c <filename>` syntax

```shell
python Main.py -c /some/other/file.ini
# then adapt it 
```


## Windows users attention

Please ensure that your SLD file paths are written with double `\` characters like e.g. `"file" = "U:\\some\\path\\to\\file.sld"`
