import os
from time import sleep

# Install and Setup MongoDB
# --------------------------------------------

os.system(
    "sudo pacman -Syyu mongodb python python-pip nano git certbot nginx --noconfirm")
os.system("sudo systemctl enable mongodb --now")

print("! Change\n\tfrom: bind_ip = 127.0.0.1\n\tto: bind_ip = 0.0.0.0")
sleep(3)

os.system("sudo nano /etc/mongodb.conf")
os.system("sudo systemctl restart mongodb")

print("""
! Opening MongoDB Shell,
  run the commands below
1.  use admin
2.  db.createUser(
        {
            user: "AdminUserName",
            pwd: "SuperSecretPassword",
            roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
        }
    )
Refer the documentaion for additional information:
    https://hirusha-adikari.gitbook.io/gifgang/discord-bot/installation
      """)

print("! Change\n\tfrom: authorization: disabled\n\tto: authorization: enabled")
sleep(3)

os.system("sudo nano /etc/mongodb.conf")
os.system("sudo systemctl restart mongodb")

# Install and Setup GifGang
# --------------------------------------------

os.system("mkdir /GifGang && cd /GifGang")
os.system('git clone "https://github.com/hirusha-adi/GifGang.git" && cd ./Gifang')
os.system("python -m pip install -r requirements.txt")

print("! Change the main configuration file to your needs")
sleep(3)
os.system("nano ./database/config.json")

print("! Change the admin settings file")
sleep(3)
os.system("nano ./database/admin/settings.json")

os.system("python gifgang.net &")
os.system("bg")
os.system("disown -h")

sleep(5)

os.system("python discord-bot.py &")
os.system("bg")
os.system("disown -h")


# Setup Ngrok for SSL and setup SSL
# --------------------------------------------

domain_name = input("Enter your domain name> ")

os.system("sudo systemctl enable nginx --now")
os.system("sudo systemctl start nginx")
os.system("")

with open("/etc/nginx/sites-enabled/default", "w") as file:
    file.write("""server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name """ + domain_name + """;

        location / {
                proxy_pass http://localhost:8080;
        }
}""")
os.system("nginx -t")
os.system("nginx -s reload")


os.system("systemctl stop nginx")
os.system(
    f"certbot certonly --standalone --agree-tos -d {domain_name},www.{domain_name}")

with open("/etc/nginx/sites-enabled/default", "w") as file:
    file.write("""server {
  listen 80 default_server;
  listen [::]:80 default_server;

  location / {
    return 301 https://$host$request_uri;
  }
}

server {
  listen 443 ssl;
  listen [::]:443 ssl;
  ssl_certificate     /etc/letsencrypt/live/""" + domain_name + """/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/""" + domain_name + """/privkey.pem;

  location / {
    proxy_pass http://localhost:8080;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Protocol $scheme;
    proxy_set_header X-Forwarded-Host $http_host;
  }
}""")

os.system("systemctl start nginx")
os.system("nginx -t")
os.system("nginx -s reload")
