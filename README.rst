Download Water Data
===================

Downloader for the `Global Surface Water`_ data of the Copernicus Programme.

It is based on the original downloadWaterData.py.

.. image:: https://img.shields.io/pypi/pyversions/download_water_data.svg
    :target: https://pypi.python.org/pypi/download-water-data

.. image:: https://img.shields.io/pypi/v/download-water-data.svg
    :target: https://pypi.python.org/pypi/download-water-data

.. image:: https://img.shields.io/github/issues/mentaljam/download_water_data.svg
    :target: https://github.com/mentaljam/download_water_data/issues

Requirements
------------

This tool runs on Windows/Mac/Unix and requires `Python`_ version 2 or 3.

Usage
-----

**Install with** `pip`_

- Install the tool with ``python -m pip install download_water_data``
- Run the tool with ``python -m download_water_data <arguments>`` or just
  ``download_water_data <arguments>`` if the Python Scripts directory is in your system ``PATH``

**Download without installing**

-  Download the `latest`_ ``download_water_data.pyz`` file
-  Open a terminal or console
-  Run the tool with ``python download_water_data.pyz <arguments>``

To **interrupt** tool execution press ``Ctrl+C``.

Arguments
---------

Possible tool arguments and options can be listed with the ``-h`` option:

::

    $ download_water_data -h

    usage: download_water_data [-h] [-v] [-d PATH] [-r {1_0,1_1,1_1_2019,1_3_2020,1_4_2021}] [-a] [-f] [DS ...]

    Full Download Script for Global Surface Water Data.

    positional arguments:
      DS                    one or more datasets names to download (occurrence,
                            change, seasonality, recurrence, transitions, extent),
                            use the "-a" option to download all the datasets

    options:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      -d PATH, --directory PATH
                            destination directory where to download the data (by
                            default the current working directory is used)
      -r {1_0,1_1,1_1_2019,1_3_2020,1_4_2021}, --revision {1_0,1_1,1_1_2019,1_3_2020,1_4_2021}
                            data revision (default is 1_4_2021)
      -a, --all             download all datasets (default is false)
      -f, --force           rewrite existing files (default is false)

Examples
--------

To download the **occurrence** and **change** datasets run

``download_water_data occurrence change``

To download all the datasets run

``download_water_data -a``

To change the destination directory add the ``-d`` option

``download_water_data -a -d 'download/path'``

.. _Global Surface Water: https://global-surface-water.appspot.com
.. _Python: https://www.python.org
.. _pip: https://pip.pypa.io/en/stable
.. _latest: https://github.com/mentaljam/download_water_data/releases/latest
