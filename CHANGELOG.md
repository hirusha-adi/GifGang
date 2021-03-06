# 1.6

- Final Version
- Stable discord bot
- Stable web-application / web-server
- Uses MongoDB to store torrents (has a json that is easily importable with over 625 torrents)
- Admin Panel is stable
- Most parts are customizable using the Admin Settings
- All main and important settings are stored in JSON for easy customization from the user's end
- It took me 2.5 months to come here. (I coded while working on other projects and managing with my school studies)

# 1.5

- First ready to deploy version with Torrents Support
- Has a fully featured discord bot with custom help for every command
- Wrote [documentation in gitbook](https://hirusha-adikari.gitbook.io/gifgang/)
- backend bug fixes of `/torrents/*`
- Added Pagination for torrents with `flask-pagination`

# 1.4

- Download torrents with the stored Magnet-URLs in MongoDB
- get torrents list by filtering from uploaded channel name
- New search pages for every service
- backend bug fixes
- redirect to login page if wrong login information is providied instead of the debug mode taking over
- completed adding all image URLs for [NSFW Categories List](https://github.com/hirusha-adi/GifGang/issues/8) - Thank you OLIVER!

# 1.3

- Better route management, Clean Code
- backend Bug Fixes
- search bar color fix
- New pin added at first position in the Pinned List in both SFW and NSFW that will redirect to `/links`

# v1.2

## Whats new?

1. Website Only (`./web/*`)
2. Manage all settings stored in json files with the admin settings page `/admin/settings` (Also has a very nice mobile UI)
   3, Default Dark Mode
3. Color theme changes - [New Color Pallete](https://www.color-hex.com/color-palette/97670)
4. THE DARK MODE IS ADDED ONLY TO PLUBLICLY AVAILABLE ROUTES. ALL ADMIN ROUTES WILL BE STICKING WITH THIER ORIGINAL THEMES

## Bugs

1. Bad text color and background color in Search bar (input-field)

# v1.1

1.  Website Only
2.  Display the current request count given to the web app at the bottom
3.  added META tags for the website
4.  Log to file

```
[time] (IP-Address) - /webpage - "User Agent (Browser Info)"
```

```
[2022-04-24 21:25:41.526415] (127.0.0.1) - /about - "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
```

5.  Better Code. Manage services with functions outside from the main file (in `services.*`)
6.  Change in privacy policy for better protection of users
7.  Secure Admin Login System and an Admin Dashboard `/admin`

# v1.0

1. Website Only
2. Has a fully functional website for both SFW and NSFW content4
