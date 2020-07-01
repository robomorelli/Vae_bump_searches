

import pandas as pd
import numpy as np
import uproot
import os
from config import *
from utils import *


data_kind = 'background' #Only for backrdound, don't need to merge signal

def main(depth):

    if data_kind not in ['signal', 'background']:
        raise Exception('i can t infer the data to process, please define the data_kind: background or sig')

    if data_kind == 'background':
        print('"\x1b[31m\"merging the files "\x1b[0m"')
        path_in = splitted_numpy_bkg + depth
        path_out = numpy_bkg  + depth

        if os.path.exists(path_out):
            print('folder already existing...saving {}'.format(data_kind))
        else:
            try:
                os.makedirs(path_out)
            except:
                print('failing to create output folder')
        concatenate_file(path_in, path_out, data_kind)

    elif data_kind == 'signal':
        print('"\x1b[31m\"merging the files "\x1b[0m"')
        path_in = splitted_numpy_sig + depth
        path_out = numpy_sig  + depth
        if os.path.exists(path):
            print('folder already existing...saving {}'.format(data_kind))
        else:
            try:
                os.makedirs(path)
            except:
                print('failing to create output folder')

        concatenate_file(path_in, path_out, data_kind)


if __name__ == "__main__":

    depth=''

    if depth in ['preselection', 'middle']:
        print(depth)
    else:
        print('no depth selection')

    main(depth)
