#!/bin/bash

echo "Checking Package..."
sleep 2

bin=$PREFIX/bin
echo -e "\033[1;97mUpdating Packages!"
pkg update && pkg upgrade -y

# Git পরীক্ষা ও ইনস্টল
if command -v git &> /dev/null; then 
  echo -e "\u001b[32mGit is already installed!"
else 
  echo -e "\u001b[31mInstalling git!"
  pkg install git -y
  echo -e "\u001b[32mDone installing git!"
fi

# Python পরীক্ষা ও ইনস্টল
if command -v python &> /dev/null; then 
  echo -e "\u001b[32mPython is already installed!"
else 
  echo -e "\u001b[31mInstalling python!"
  pkg install python -y
  echo -e "\u001b[32mDone installing python!"
fi

# Bash পরীক্ষা ও ইনস্টল
if command -v bash &> /dev/null; then 
  echo -e "\u001b[32mBash is already installed!"
else 
  echo -e "\u001b[31mInstalling bash!"
  pkg install bash -y
  echo -e "\u001b[32mDone installing bash!"
fi

echo -e "\u001b[32mInstalling required Pip modules..."
sleep 2

# প্রয়োজনীয় পাইথন প্যাকেজ ইনস্টল
pip install --upgrade pip
pip install colorama requests phonenumbers instaloader

echo -e "\u001b[32mDone installing pip packages!"
echo -e "Running Tools..."
sleep 2

python owlsint.py
