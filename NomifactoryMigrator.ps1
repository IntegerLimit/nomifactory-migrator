#Nomifactory or Nomifactory CEu Migrate Script
#This script will help move important folders from one instance of the pack to another, saving you time!
#Original Author: capSAR273, updated author, IntegerLimit, if you have any questions or issues you can contact me on GitHub (Or on the Nomifactory Discord)!

Write-Host "Before you continue, make sure you have imported the new instance in your preferred launcher from CurseForge, or a zip file, first!"

$oldPath = Read-Host -Prompt "Enter the path to the old version's minecraft folder."
$newPath = Read-Host -Prompt "Enter the path to the new version's minecraft folder."

Write-Host "Copying Files..."

#This will take the important folders/files recommended on the Omnifactory GitHub and copy them to the new instance folder.
Copy-Item $oldPath\saves -Destination $newPath -Recurse
Copy-Item $oldPath\resourcepacks -Destination $newPath -Recurse
Copy-Item $oldPath\options.txt -Destination $newPath -Recurse
Copy-Item $oldPath\journeymap -Destination $newPath -Recurse
Copy-Item $oldPath\visualores -Destination $newPath -Recurse
Copy-Item $oldPath\hei_bookmarks.ini -Destination $newPath -Recurse

Write-Host "Copy Complete!"
