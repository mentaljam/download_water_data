# Download Water Data

Downloader for the [Global Surface Water](https://global-surface-water.appspot.com)
data of the Copernicus Programme.

It is based on the original downloadWaterData.py.

## Requirements

This tool runs on Windows/Mac/Unix and requires [Python](https://www.python.org) version 2 or 3.

## Usage

* Download the [latest](https://github.com/mentaljam/download_water_data/releases/latest)
release of the tool and unzip it somewhere
* Open a terminal or console
* Run the tool with `python download_water_data.py <arguments>`

## Arguments

Possible tool arguments and options can be listed with the `-h` option:

```
$ python download_water_data.py -h

usage: download_water_data.py [-h] [-v] [-d PATH] [-a] [DS [DS ...]]

Full Download Script for Global Surface Water Data.

positional arguments:
  DS                    one or more datasets names to download (occurrence,
                        change, seasonality, recurrence, transitions, extent),
                        use the "-a" option to download all the datasets

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d PATH, --directory PATH
                        destination directory where to download the data (by
                        default the current working directory is used)
  -a, --all             download all datasets (default is false)
```

## Examples

To download the **occurrence** and **change** datasets run

`python download_water_data.py occurrence change`

To download all the datasets run

`python download_water_data.py -a`

To change the destination directory add the `-d` option

`python download_water_data.py -a -d 'download/path'`
