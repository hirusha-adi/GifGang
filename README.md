# GifGang

Important Links

- [GifGang (Main Deployment)](https://gifgang.net/links)
- [GifGang Info Website](https://hirusha-adi.github.io/GifGang/)
- [GifGang Module](https://github.com/hirusha-adi/GifGang/tree/module)
- [GifGang Intsaller Scripts](https://github.com/hirusha-adi/GifGang/tree/installer)

<br>

# Current Versions

## Website: `v1.4`

## Discord Bot: `v1.0`

## Module: `v1.1`

<br>
<br>

# SETUP

# Setting up MongoDB

- ## Install

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install mongodb -y
sudo systemctl enable mongodb --now
```

- ## Setup - Part 1

1. Run this command and open the config file

```bash
sudo nano /etc/mongodb.conf
```

2. Change `bind_ip` from `127.0.0.1` to `0.0.0.0`

```
bind_ip = 0.0.0.0
```

3. run this command to restart mongo

```bash
sudo systemctl restart mongodb
```

- ## Setup - Part 2

1. Create a new user

```
mongo
use admin
```

```
db.createUser(
{
user: "AdminUserName",
pwd: "SuperSecretPassword",
roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
}
)
```

2. Make login required

```
sudo nano /etc/mongodb.conf
```

```
authorization: enabled
```

```
sudo systemctl restart mongod
```

- ## Setup - Part 2

1. Create a Database named `GifGang`
2. Create a collection named `torrents`

---

You can now connect to the mongodb database with MongoDB Compass

---

# Other - MongoDB

- ## Management

```bash
sudo systemctl status mongodb
```

```bash
sudo systemctl stop mongodb
```

```bash
sudo systemctl restart mongodb
```

```bash
sudo systemctl enable mongodb --now
```

```bash
sudo systemctl disable mongodb
```

# Setting up NGINX

- `gifgang.net` is the domain name

1. Install nginx

```bash
apt install nginx
systemctl enable nginx --now
systemctl start nginx
```

2. Edit the default config file for the first time before setting up SSL

```bash
nano /etc/nginx/sites-enabled/default
```

```nginx
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name gifgang.net;

        location / {
                proxy_pass http://localhost:8080;
        }
}
```

3. Load the new config and stop nginx to get the SSL certificate

```bash
nginx -t
nginx -s reload
sudo apt install certbot -y
systemctl stop nginx
certbot certonly --standalone --agree-tos -d gifgang.net,www.gifgang.net
```

4. Edit the default config file for the second time with new SSL settings

```bash
nano /etc/nginx/sites-enabled/default
```

```nginx
server {
  listen 80 default_server;
  listen [::]:80 default_server;

  location / {
    return 301 https://$host$request_uri;
  }
}

server {
  listen 443 ssl;
  listen [::]:443 ssl;
  ssl_certificate     /etc/letsencrypt/live/gifgang.net/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/gifgang.net/privkey.pem;

  location / {
    proxy_pass http://localhost:8080;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Protocol $scheme;
    proxy_set_header X-Forwarded-Host $http_host;
  }
}
```

5. Restart nginx

```bash
systemctl start nginx
nginx -t
nginx -s reload
```

You can now load the website with SSL
