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
