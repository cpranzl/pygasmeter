#!/usr/bin/env python3

__author__ = "Christoph Pranzl"
__copyright__ = "Copyright 2022, Christoph Pranzl"
__credits__ = ["Christoph Pranzl"]
__license__ = "GPL-3.0"
__version__ = "0.0.1"
__maintainer__ = "Christoph Pranzl"
__email__ = "christoph.pranzl@pranzl.net"
__status__ = "prototype"

"""
SYNOPSIS
    pygasmeter [-i , --image ] [-d, --digits] [-v, --verbose]
               [-h,--help] [--version]
DESCRIPTION
    Detects and ocr's digits from pictures
EXAMPLES
    pygasmeter -i example.jpg -d
EXIT STATUS
    TODO: List exit codes
"""

import sys
import os
import traceback
import argparse
import time
import pytesseract
import cv2
from datetime import datetime


def main():

    global args

    image = cv2.imread(args.image)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    options = ''

    if args.digits:
        options = 'outputbase digits'

    text = pytesseract.image_to_string(rgb, config=options)
    print(text)


if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = argparse.ArgumentParser()
        parser.add_argument('-i',
                            '--image',
                            required=True,
                            help='path to input image to be ocrd')
        parser.add_argument('-d',
                            '--digits',
                            action='store_true',
                            help='wether or not *digits only* ocr will be \
                            performed')
        parser.add_argument('-v',
                            '--verbose',
                            action='store_true',
                            default=False,
                            help='increase verbose output')
        args = parser.parse_args()
        if args.verbose:
            print(datetime.utcnow().isoformat())
        main()
        if args.verbose:
            print(datetime.utcnow().isoformat())
        if args.verbose:
            print("TOTAL CALCULATION TIME IN MINUTES:")
        if args.verbose:
            print((time.time() - start_time) / 60.0)
        sys.exit(0)
    except KeyboardInterrupt as e:
        raise e
    except SystemExit as e:
        raise e
    except Exception as e:
        print('ERROR, UNEXPECTED EXCEPTION')
        print(str(e))
        traceback.print_exc()
        os._exit(1)
