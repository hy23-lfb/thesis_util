#! python

"""
Script to create a single channel .npz files out of single channel .tif files.
Read the tif metadata to extract width, height, and the channels in each slice of the image.
The values are normalized between 0.0 and 1.0, and the npz files are stored in the same folder as the tif files are.

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

dst_filepath = os.path.join(args.file_path, 'npz_normalized_max')
os.makedirs(dst_filepath, exist_ok=True)

# list everything in the path; both directories and files.
dirlist = os.listdir(args.file_path)

# Of all the directories and files, filter only files
filelist = [file for file in dirlist if (os.path.isfile(os.path.join(args.file_path, file)))]

tif_file = [tif for tif in filelist if (os.path.isfile(os.path.join(args.file_path, tif)) and tif.endswith('.tif'))]
for file_idx in range(len(tif_file)):
    src = os.path.join(args.file_path, tif_file[file_idx])
    dst_file = tif_file[file_idx].replace('.tif', '.npz')
    dst = os.path.join(dst_filepath, dst_file)
    im = Image.open(src)
        
    # read tiff-file metadata
        
    '''
    below line of code works only for multichanneled images.
    i.e., no_of_channels exists.
    '''
    width, height   = im.size
    frames          = im.n_frames
    im_array        = np.zeros((height, width, frames))
        
    for slice_idx in range(frames):
        im.seek(slice_idx)
        im_array[:, :, slice_idx] = np.array(im)
    
    max_value = np.max(im_array)
    min_value = np.min(im_array)
    print("filename: {}".format(tif_file[file_idx]))
    print("max: {}".format(np.max(im_array)))
    print("min: {}".format(np.min(im_array)))
    print()
    np_array = im_array / max_value
    np.savez(dst, vol=np_array)