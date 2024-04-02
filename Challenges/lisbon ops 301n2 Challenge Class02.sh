#!/bin/bash 

# Script: lisbon-ops-301n2: Challenge Class02.
# Purpose: Append time and date.
# Why: To know at what time the file was copied.


# Storing the date and time inside variables

year=$(date +%y)
month=$(date +%m)
day=$(date +%d)
time=$(date +%T)

# Copying the file to current directory and appending date and time

cp /var/log/lastlog ./laslog$year$month$day$time