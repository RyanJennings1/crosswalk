# Crosswalk
  Python program that uses [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Selenium](http://selenium-python.readthedocs.io/) to open up [crosswalk.com](http://www.crosswalk.com/newsletters/) and subscribe to all 186 newsletters

# How to Install
  1. Make sure you have [Python 2.7](https://www.python.org/downloads/) or higher version of Python 2.7 installed.
  2. Copy and paste the following for the installation:
      `# Crosswalk Installation
       git clone https://github.com/RyanJennings1/crosswalk $HOME/.crosswalk
       echo PATH="$HOME/.crosswalk:${PATH}" >> ~/.bashrc
       source ~/.bashrc
      `
  3. Now you can run the program like so:
     `$ crosswalk test@gmail.com`

# Usage
`crosswalk [parameter]

Parameters:
  [email]	- Email that is submitted after boxes checked.

Other Parameters:
  --help	- Display this menu.`

## Known problems
  [Using Firefox 53](https://github.com/mozilla/geckodriver/issues/659)

# Credits
[LazoCoder](https://github.com/LazoCoder/Pokemon-Terminal) for README.md structure and argument handlers in main.py
