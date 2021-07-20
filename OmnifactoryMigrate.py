#Omnifactory Migrate Script
#This script will help move important folders from one instance of the pack to another, saving you time!
#Author: capSAR273, if you have any questions or issues you can contact me on GitHub (Or on the Omnifactory Discord)!
import os
from os import path
import shutil

print("Before you continue, make sure you have imported the new instance in MultiMC from the zip file first!\n")

old_path=input("Enter the path to the old version's minecraft folder.\n")
new_path=input("Enter the path to the new version's minecraft folder.\n")


#This will take the important folders/files recommended on the Omnifactory GitHub and copy them to the new instance folder.
def copyFiles(old_path,new_path):
    shutil.rmtree(os.path.join(new_path,'saves'))
    shutil.copytree(os.path.join(old_path,'saves'), os.path.join(new_path,'saves'))
    
    shutil.rmtree(os.path.join(new_path,'resourcepacks'))
    shutil.copytree(os.path.join(old_path,'resourcepacks'), os.path.join(new_path,'resourcepacks'))
    
    os.remove(os.path.join(new_path,'options.txt'))
    shutil.copyfile(os.path.join(old_path,'options.txt'), os.path.join(new_path,'options.txt'))
    
    shutil.rmtree(os.path.join(new_path,'journeymap'))
    shutil.copytree(os.path.join(old_path,'journeymap'), os.path.join(new_path,'journeymap'))
    
    os.remove(os.path.join(new_path,'config','jei','bookmarks.ini'))
    shutil.copyfile(os.path.join(old_path,'config','jei','bookmarks.ini'), os.path.join(new_path,'config','jei','bookmarks.ini'))

print("Copying Files...\n")
copyFiles(old_path,new_path)
print("Copy Complete!\n")
