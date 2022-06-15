#!/usr/bin/env python3

import os 
import zipfile

def zipdir(dirpath, zipfileobj):
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            print(os.path.join(root,file))
            zipfileobj.write(os.path.join(root, file))
    return None

def main():
    """called at runtime"""
    # ask ths user for the directory to be archived
    dirpath = input("What directory are we archiving today? ")

    ## If the directory exists, then we can begin archiving it
    if os.path.isdir(dirpath):
        zippedfn = input("What should we call the finished archive? ")
        ## zippedfn is the zipped file for the archive
        with zipfile.ZipFile(zippedfn, "w", zipfile.ZIP_DEFLATED) as zipfileobj:
            # create a zip file object -- we are making a new zip file
            zipdir(dirpath, zipfileobj) # call to our function
    else:
        print("Run the script again when you have a valid directory to zip.")

# this line calls our main function
main()
