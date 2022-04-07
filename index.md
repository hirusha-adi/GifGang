## GifGang

# What is this?

This is a website with both SFW and NSFW GIF's and Images (Some redirecting to Videos in thier original website). This website does NOT own any media displayed. All the media are taken/requested/scraped from many services and the service name is mentioned above every image set to give credit. ( You can call this a lightweight yet modern and powerful wrapper for many websites with media. )

# Installation Guide

NOTE: You do not need to install this in order to use this web app. You can [cick here](http://gifgang.net) to try out the publicly hosted version. Following the steps below will lead you to hosting your own instance of this website.

### Ubuntu & Debian

run the commands below

```bash
sudo apt update && sudo apt install wget -y && wget "https://raw.githubusercontent.com/hirusha-adi/GifGang/installer/ubuntu/installer.sh" && chmod +x installer.sh && ./installer.sh
```

### Arch Linux

run the commands below

```bash
sudo pacman -Syy wget --noconfirm && wget "https://raw.githubusercontent.com/hirusha-adi/GifGang/installer/arch/installer.sh" && chmod +x installer.sh && ./installer.sh
```

### I have an error while Installation. What should I do?

1. Check if your issue in this list of most commonly encountable error list (Click to open the guide to fixing it) or use your common sense:

   - [pip3 command not found](https://exerror.com/sudo-pip3-command-not-found/)
   - [python3 command not found](https://stackoverflow.com/questions/40914108/bash-python3-command-not-found-windows-discord-py)

<br>

2. Enable the developer-mode
   1. Stop the program if it is already running
   2. Open the `./database/config.json` file and set `"dev_mode"` to true.
      - `json "dev_mode": true`
   3. Save the file
   4. Restart the application
3. Re-create the issue.
4. Copy the log displayed in the console
5. [Open an Issue](https://github.com/hirusha-adi/GifGang/issues/new/choose) with the copied log

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

# Image Showcase
- ### `/`
![Screenshot_20220407_104601](https://user-images.githubusercontent.com/36286877/162125258-03d11344-d5c1-4792-8c03-0f2ee3b8886b.png)

- ### `/pins`
![Screenshot_20220407_104750](https://user-images.githubusercontent.com/36286877/162125472-3ae6266d-57bc-449a-acab-b65bb730ddef.png)

- ### `/restricted`
![Screenshot_20220407_104945](https://user-images.githubusercontent.com/36286877/162125666-ee7b7a5b-2036-4509-9d83-ec2531c22602.png)

- ### `/adult`
![Screenshot_20220407_110741 (1)](https://user-images.githubusercontent.com/36286877/162129428-1ea7eff8-7e0e-400d-9b94-5b226294b3dd.png)

- ### `/adult/categories`
![unknown (1) (1)](https://user-images.githubusercontent.com/36286877/162131286-6120d255-d3d9-4173-bf76-0fb696c35dcd.png)




