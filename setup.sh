#!/bin/bash

sudo apt-get update 
sudo apt-get upgrade
sudo apt-get install python3-picamera -y

# For PIL images to show() (debugging)
sudo apt install imagemagick
