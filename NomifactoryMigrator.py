#!/usr/bin/env python3
#Nomifactory or Nomifactory CEu Migrate Script
#This script will help move important folders from one instance of the pack to another, saving you time!
#Original Author: capSAR273, updated author, IntegerLimit, if you have any questions or issues you can contact me on GitHub (Or on the Nomifactory Discord)!
import os
from os import path
import shutil

print("Before you continue, make sure you have imported the new instance in your preffered launcher from CurseForge, or a zip file, first!\n")

old_path=os.path.expanduser(input("Enter the path to the old version's minecraft folder.\n"))
new_path=os.path.expanduser(input("Enter the path to the new version's minecraft folder.\n"))


#This will take the important folders/files recommended on the Nomifactory GitHub and copy them to the new instance folder.
def copyFiles(old_path,new_path):
    if os.path.exists(os.path.join(new_path,'saves')):
        shutil.rmtree(os.path.join(new_path,'saves'))
    shutil.copytree(os.path.join(old_path,'saves'), os.path.join(new_path,'saves'))
    
    if os.path.exists(os.path.join(new_path,'resourcepacks')):
        shutil.rmtree(os.path.join(new_path,'resourcepacks'))
    shutil.copytree(os.path.join(old_path,'resourcepacks'), os.path.join(new_path,'resourcepacks'))
    
    shutil.copyfile(os.path.join(old_path,'options.txt'), os.path.join(new_path,'options.txt'))
    
    if os.path.exists(os.path.join(new_path,'journeymap')):
        shutil.rmtree(os.path.join(new_path,'journeymap'))
    shutil.copytree(os.path.join(old_path,'journeymap'), os.path.join(new_path,'journeymap'))
    
    shutil.copyfile(os.path.join(old_path,'hei_bookmarks.ini'), os.path.join(new_path,'hei_bookmarks.ini'))

print("Copying Files...\n")
copyFiles(old_path,new_path)
print("Copy Complete!\n")
