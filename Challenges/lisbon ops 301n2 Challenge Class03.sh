#!/bin/bash 

# Script: lisbon-ops-301n2: Challenge Class03.
# Purpose: Prompt the user for directory and permissions input, navigate to said directory and print to the screen the contents with the new permissions. .
# Why: To guarantee that any file created in that directory has the permissions that it needs according to the person who created it.

#Prompting user for directory path (The -p option let's the script prompt the user with a message before reading input)
read -p "Enter directory path: " directory_path

#Prompting user for permissions

read -p "Enter permissions number (ex.777): " permissions

#Changing directory to the one specified by user
#In case the directory can't be found the script exits with a message and a general error

cd "$directory_path" ||{ echo "Directory not found"; exit 1; }

#Used the find command to search for file type of type "f" so that only normal files are changed and not directories

find . -type f -exec chmod "$permissions" {} +

#Outputting to the screen the actions of the script while changing the permissions of each file

find . -type f | while read -r file ; do 
    echo "Changing permissions for file: $file"
    chmod "$permissions" "$file"
    sleep 1
done

#Print to the screen the contents of the directory to show the changes to the permissions

echo "Directory Contents:"

ls -l

