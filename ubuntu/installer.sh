#!/bin/bash

# # Install Dependencies (main)
sudo apt update && sudo apt upgrade -y
sudo apt install wget nano git python3 python3-pip -y

# # Cloning the repo
git clone "https://github.com/hirusha-adi/GifGang.git"
cd GifGang

# # Install Dependencies (required by gifgang)
pip3 install -r ./requirements.txt

# Delete files if not exist
read -p "[?] Remove other files [y/n]:" remove_other_files
if [ $remove_other_files == "y" ]; then
    echo "[+] Removing other files"
    declare -a FilesList=(
        ".gitignore",
        "CHANGELOG.md",
        "CREDITS.md",
        "PRIVACY-POLICY.md",
        "README.md",
        "TODO.md",
        "requirements.txt"
    )
    for filename in "${FilesList[@]}"; do
        rm -f $filename
        echo "[+] Removed" $filename
    done
else
    echo "[-] Not removing other files"
fi

# Clear out
echo "[*] Waiting 2 seconds"
sleep 2s

clear

# because `utls.py` as a check for the database files
# if not exits, will grab them from github repo manually
cd ./web
python3 ./utils.py

# Prompt main 2 database files for user to edit if needed
ehco "[*] Edit config.json (Web Server Settings)"
sleep 2s
nano ./database/config.json
clear

ehco "[*] Edit important.json (Main Backend Settings)"
sleep 2s
nano ./database/important.json
clear

echo "[+] Database checks complete"

cd ..
