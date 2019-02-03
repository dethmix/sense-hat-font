# sense-hat-font
Create own png asset file for sense-hat library.

Better to use python3 for executing to get less issues with Unicode errors.

Font PTMono was found inside /Library/Fonts on MacOs. Also can be found at https://fonts.google.com/specimen/PT+Mono

Script will generate two files sense_hat_text.png and sense_hat_text.txt which should be used instead of default asset files provided by sense-hat library. Also you will need to increase size of pixel block used for 1 symbol from 40 pixels to 48, because generated image has 1 pixel space between symbols(original image doesn't have it).

Initially script was created to add support of cyrillic symbols.

Link to original sense-hat lib https://github.com/RPi-Distro/python-sense-hat
