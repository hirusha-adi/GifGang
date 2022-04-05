## GifGang

# What is this?

This is a website with both SFW and NSFW GIF's and Images (Some redirecting to Videos in thier original website). This website does NOT own any media displayed. All the media are taken/requested/scraped from many services and the service name is mentioned above every image set to give credit. ( You can call this a lightweight yet modern and powerful wrapper for many websites with media. )

# Image Showcase

- [ ] Add images

# Installation Guide

NOTE: You do not need to install this in order to use this web app. You can [cick here](http://gifgang.net) to try out the publicly hosted version. Following the steps below will lead you to hosting your own instance of this website.

### Ubuntu & Debian

run the commands below

```bash
wget "script.url.goes.here"
chmod +x debian_installer.sh
./debian_installer.sh
```

### Arch Linux

run the commands below

```bash
wget "script.url.goes.here"
chmod +x arch_installer.sh
./arch_installer.sh
```

### I have an error while Installation. What should I do?

1) Check if your issue in this list of most commonly encountable error list (Click to open the guide to fixing it) or use your common sense:
    - Sample
    - Sample 2

2) Enable the developer-mode
    1) Stop the program if it is already running
    2) Open the `./database/config.json` file and set `"dev_mode"` to true.
         - ```json "dev_mode": true```
    3) Save the file
    4) Restart the application
3) Re-create the issue.
4) Copy the log displayed in the console
5) [Open an Issue](https://github.com/hirusha-adi/GifGang/issues/new/choose) with the copied log


# :)

- Starring this project will support me!
- Make sure to [open an Issue](https://github.com/hirusha-adi/GifGang/issues/new/choose) if something is wrong or if you want to request a new feature in the future version
- If you are interested in adding your code to this project, feel free to [open a pull request](https://github.com/hirusha-adi/GifGang/compare) anytime!

# APIs Used
The list of servcies that are wrapped by this project

## SFW
  - [GIPHY](https://developers.giphy.com/)
  - [Picsum](https://picsum.photos/)
  - [Tenor](https://tenor.com/gifapi/documentation)
  - [TheCatAPI](https://thecatapi.com/)
  - [DogAPI (DogCEO)](https://dog.ceo/dog-api/)
  - [Unsplash](https://unsplash.com/developers) - Incomplete ( Difficulties of getting a token )
  - [Imgur](https://api.imgur.com/) - Incomplete ( Difficulties with bad URLs returned from the API )
## NSFW
  - [EPORNER](https://www.eporner.com/api/v2/)
  - [RedTube](https://api.redtube.com/)
  - [l0calserve4](https://api.l0calserve4.ml/hmtai/)
## Used for both
  - [Nekos.Life](https://nekos.life/)
  
  
# NOTE

I am not responsible for any bad that happens with this website and i dont promote or encourage the usage of `/adult/*` routes for anyone. Anyone who is under the age of 18 should NOT visit these NSFW endpoints

# For any issue, make sure to contact me

- Discord: `ZeaCeR#5641`
- Email: `zesta5j7k@gmail.com`


