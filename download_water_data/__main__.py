#!/usr/bin/env python

'''Downloader for the Global Surface Water Data of the Copernicus Programme:
https://global-surface-water.appspot.com/download

Based on the original downloadWaterData.py'''

__author__ = 'Petr Tsymbarovich'
__email__ = 'petr@tsymbarovich.ru'
__license__ = 'MIT'
__version__ = '0.3.0'

import sys
import signal
import os
import argparse
if sys.version_info.major == 2:
    # Python 2
    from urllib import urlretrieve
    from urllib2 import HTTPError
else:
    # Python 3
    from urllib.request import urlretrieve
    from urllib.error import HTTPError


KNOWN_DATASETS = ['occurrence', 'change', 'seasonality', 'recurrence', 'transitions', 'extent']
REVISIONS = ['1_0', '1_1', '1_1_2019']
_GLOBALS = {}


def templates(revision):
    '''Configure URL and file templates'''

    v10, v11, v11_2019 = REVISIONS
    url_tmpl  = 'http://storage.googleapis.com/global-surface-water/downloads'
    file_tmpl = '{ds}_{lon}_{lat}'
    if revision == v10:
        padding   = 15
    elif revision == v11:
        url_tmpl  += '2'
        file_tmpl += '_v' + v11
        padding   = 20
    elif revision == v11_2019:
        url_tmpl  += '2019v2'
        file_tmpl += 'v' + v11_2019
        padding   = 24
    url_tmpl  += '/{ds}/{file}'
    file_tmpl += '.tif'
    return (url_tmpl, file_tmpl, padding)


def sigint_handler(signum, frame):
    '''Handler for interruption signal (Ctrl+C).'''

    print('\ninterrupted by user')
    part_file = _GLOBALS['part_file']
    if os.path.exists(part_file):
        os.remove(part_file)
    sys.exit(0)


def main():
    '''The main function.'''

    # register sigint handler
    signal.signal(signal.SIGINT, sigint_handler)

    # parse command line arguments
    parser = argparse.ArgumentParser(
        description='Full Download Script for Global Surface Water Data.')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument(
        'datasets', metavar='DS', type=str, nargs='*',
        help='one or more datasets names to download ({}), use the "-a" option to download \
all the datasets'.format(', '.join(KNOWN_DATASETS)))
    parser.add_argument(
        '-d', '--directory', metavar='PATH', type=str, default=os.getcwd(),
        help='destination directory where to download the data \
(by default the current working directory is used)')
    parser.add_argument(
        '-r', '--revision', choices=REVISIONS, default=REVISIONS[2],
        help='data revision (default is 1_1_2019)')
    parser.add_argument(
        '-a', '--all', action='store_true', default=False,
        help='download all datasets (default is false)')
    parser.add_argument(
        '-f', '--force', action='store_true', default=False,
        help='rewrite existing files (default is false)')
    args = parser.parse_args()

    # check parsed arguments
    if args.datasets:
        known_ds = set(KNOWN_DATASETS)
        for ds_name in args.datasets:
            if not ds_name in known_ds:
                sys.stderr.write('error: unknown dataset name "{}"\n'.format(ds_name))
                sys.exit(1)
        if args.all:
            print('warning: both dataset names and the option "-a" were provided - \
ignoring datasets names and downloading all')
            args.datasets = KNOWN_DATASETS
    elif args.all:
        print('downloading all datasets')
        args.datasets = KNOWN_DATASETS
    else:
        sys.stderr.write('error: nothing to download - provide datasets names or \
use the "-a" option to download all the datasets, for more information run with the "-h" option\n')
        sys.exit(2)

    # check output dir
    args.directory = os.path.normpath(args.directory)
    if not os.path.isdir(args.directory):
        print('Creating destination directory "{}"'.format(args.directory))
        os.makedirs(args.directory)
    else:
        print('Using destination directory "{}"'.format(args.directory))

    # preparing coordinate suffixes
    lons = [str(w) + 'W' for w in range(180, 0, -10)]
    lons.extend([str(e) + 'E' for e in range(0, 180, 10)])
    lats = [str(s) + 'S' for s in range(50, 0, -10)]
    lats.extend([str(n) + 'N' for n in range(0, 90, 10)])
    files_count = len(lons) * len(lats)
    padding = len(str(files_count))

    # configure templates
    url_tmpl, file_tmpl, filename_padding = templates(args.revision)

    # downloading datasets
    skip = not args.force
    for ds_name in args.datasets:
        print('downloading ' + ds_name)
        ds_dir = os.path.join(args.directory, ds_name)
        if not os.path.isdir(ds_dir):
            os.makedirs(ds_dir)
        counter = 1
        padding2 = len(ds_name) + filename_padding
        for lon in lons:
            for lat in lats:
                filename = file_tmpl.format(ds=ds_name, lon=lon, lat=lat)
                filepath = os.path.join(ds_dir, filename)
                sys.stdout.write('{i: >{pad}}/{c} {name: <{pad2}}'
                                 .format(i=counter, c=files_count, pad=padding,
                                         name=filename, pad2=padding2))
                sys.stdout.flush()
                if skip and os.path.exists(filepath):
                    print('already exists, skipping')
                else:
                    url = url_tmpl.format(ds=ds_name, file=filename)
                    try:
                        part_file = filepath + '.part'
                        _GLOBALS['part_file'] = part_file
                        urlretrieve(url, part_file)
                        os.rename(part_file, filepath)
                        print('ok')
                    except HTTPError as err:
                        print(filename + ' - ' + str(err))
                counter += 1
    print('finished')


if __name__ == "__main__":
    main()
