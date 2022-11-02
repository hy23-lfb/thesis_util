#! python

"""
Script to create multichanneled .npz files out of multichanneled .tif files.
Read the tif metadata to extract width, height, and the channels in each slice of the image.
The values are normalized to values between 0.0 and 1.0, and the npz files are stored in the same folder as the tif files are.

Parameters:
    file_path <str>: Is a directory.
    
Author: Harsha Yogeshappa, M.Sc

"""
import os
import argparse
import numpy as np
from PIL import Image


# parse the commandline
parser = argparse.ArgumentParser()
parser.add_argument('--file-path', type=str, required=True, help='root directory that holds folders containing tif files.')
args = parser.parse_args()

# list everything in the path; both directories and files.
dirlist = os.listdir(args.file_path)

# Of all the directories and files, filter only directories
folders = [file for file in dirlist if (os.path.isdir(os.path.join(args.file_path, file)))]

for f in folders:
    '''
    f are only directories
    '''
    src_file_path = os.path.join(args.file_path, f)
    sub_dirlist = os.listdir(src_file_path)
    
    # list of tif files in the src_file_path
    tif_file = [tif for tif in sub_dirlist if (os.path.isfile(os.path.join(src_file_path, tif)) and tif.endswith('.tif'))]
    for file_idx in range(len(tif_file)):
        src = os.path.join(src_file_path, tif_file[file_idx])
        dst = src.replace('.tif', '.npz')
        im = Image.open(src)
        
        # read tiff-file metadata
        
        '''
        below line of code works only for multichanneled images.
        i.e., no_of_channels exists.
        '''
        height, width, no_of_channels   = np.shape(im)
        frames                          = im.n_frames
        im_array                        = np.zeros((height, width, no_of_channels, frames))
        
        for slice_idx in range(frames):
            im.seek(slice_idx)
            im_array[:,:,:, slice_idx] = np.array(im)
        print("max: {}".format(max(im_array)))
        print("min: {}".format(min(im_array)))
        print()
        np_array = im_array / 255.0
        np.savez(dst, vol=np_array)