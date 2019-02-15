import os
from os.path import exists


def mk_upload_dir():
    here = os.path.abspath(os.path.dirname(__file__))
    upload_folder = os.path.join(here, '..\\uploads')
    if not exists(upload_folder):
        os.mkdir(upload_folder)
    return upload_folder


def mk_convert_dir():
    here = os.path.abspath(os.path.dirname(__file__))
    convert_folder = os.path.join(here, '..\\convert')
    if not exists(convert_folder):
        os.mkdir(convert_folder)
    return convert_folder
