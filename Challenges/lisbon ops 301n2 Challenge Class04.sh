#!/bin/bash

# Script: lisbon-ops-301n2: Challenge Class04.
# Purpose: Create a menu with various options that the user can use.
# Why: Have a script that can be run for people who don't know the specific commands for certain actions

clear
while true; do 
echo -e "\n"
echo "1. Hello World!"
echo "2. Ping Self."
echo "3. IP Info."
echo "4. Exit."
 
read -p "Please choose an option:" opt

    if [ "$option" == "1" ]; then 
        echo -e "\n"
        echo "Hello World!"

    elif [ "$option" == "2" ]; then
        ping -c 4 localhost

    elif [ "$option" == "3" ]; then
        echo -e "\n"
        ifconfig 

    elif [ "$option" == "4" ]; then
        echo "Exit Successful!"
        exit 0

    else 
        echo "Invalid Input!"
        exit 1
    fi
done
