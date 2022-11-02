# Import the json library
import os
import json

data_file_path_nt = """{
    "img_list": "I:\\\\00.masterarbeit_dataset\\\\janelia_nt_2.txt",
    "val_list": "",
    "atlas": "I:\\\\00.masterarbeit_dataset\\\\00.atlas\\\\np-scaled-channel\\\\npz\\\\np_atlas_scaled.npz",
    "model_dir": "I:\\\\03.masterarbeit_out\\\\janelia_cascade_iter2_pc161_ncc","""

data_file_path_posix = """{
    "img_list": "/work/scratch/yogeshappa/00.masterarbeit_dataset/janelia_posix_2.txt",
    "val_list": "",
    "atlas": "/work/scratch/yogeshappa/00.masterarbeit_dataset/00.atlas/np-scaled-channel/npz/np_atlas_scaled.npz",
    "model_dir": "/work/scratch/yogeshappa/03.masterarbeit_out/janelia_cascade_iter2_condor_ncc","""

data_parameters = """
    "epochs": 30,
    "steps_per_epoch": 594,
    "gpu": 0,
    "batch_size": 1,
    "initial_epoch": 0,
    "int_steps": 0,
    "int_downsize": 2,
    "kl_lambda": 10,
    "image_sigma": 1.0,
    "image_loss": "ncc",
    "lr": 1e-3,
    "enc": [16, 32, 32, 32, 32, 32],
    "dec": [32, 32, 32, 32, 32, 32, 32, 16, 16],
    "max_pool": [[2,2,1], [2,2,1], [2,2,2], [2,2,2], [2,2,2], [2,2,2]],
    "multichannel": false,
    "use_probs": false,
    "bidir": false,
    "lambda_weight": 25,
    "img_prefix": "",
    "img_suffix": "",
    "load_weights": "",
    "use_validation": false,
    "n_gradients": 18,
    "_comment": ""
}
"""


# Writing to sample.json
#with open("/home/students/yogeshappa/repo_util/Masterarbeit_Util/src/00.config_vanilla/config_itr2_janelia_condor_ncc.json", "w") as outfile:
#    outfile.write(data_file_path_posix)
#    outfile.write(data_parameters)

with open("/home/students/yogeshappa/repo_util/Masterarbeit_Util/src/00.config_vanilla/config_itr2_janelia_pc161_ncc.json", "w") as outfile:
    outfile.write(data_file_path_nt)
    outfile.write(data_parameters)