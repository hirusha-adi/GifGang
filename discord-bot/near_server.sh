#!/bin/bash
echo "Starting to restart servcies"

# Main Stuff - Requested by NoPE
# -----------------------
# LavaLink Server
cd ~/NearBot/LavaLink/
java -jar ./Lavalink.jar &
disown -h

# Near Bot
cd ~/NearBot/Near/
python3 nearbot.py &
disown -h

# NSFW Discord Bot
cd ~/AnimeBot/NSFW-Discord-Bot/
python3 nsfwdiscordbot.py &
disown -h

# Cats Discord Bot
cd ~/Cats/Cats/
python3 discordbot.py &
disown -h

# Cats Website
cd ~/Cats/Cats/web
python3 server.py &
disown -h

# My Stuff
# -----------------------
# Dogs Website
cd ~/ZeaCeR/Dogs/Dogs/
python3 app.py &
disown -h

# Fake Information
cd ~/ZeaCeR/Fake-Information-Webpage/
python3 fake.py &
disown -h

# Covid Dashboard - Sri Lanka
cd ~/ZeaCeR/Sri-Lanka-Covid-19-Dashboard/
python3 covid.py &
disown -h

# NSFW Memes Website
cd ~/ZeaCeR/NSFW-Memes-Website
python3 server.py &
disown -h

# The Jokes Webite
cd ~/ZeaCeR/TheJokeAPI/
python3 app.py &
disown -h

# Password Stats Checker
cd ~/ZeaCeR/Password-Check/
python3 start.py &
disown -h

# RIS Logo Generator
cd ~/ZeaCeR/Whatsapp-Group-Logo-Creator-RIS/
python3 server.py &
disown -h
