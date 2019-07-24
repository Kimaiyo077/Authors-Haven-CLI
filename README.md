# Authors-Haven-CLI
[![Build Status](https://travis-ci.org/Kimaiyo077/Authors-Haven-CLI.svg?branch=develop)](https://travis-ci.org/Kimaiyo077/Authors-Haven-CLI)

# How to install
1. Clone this repository on your local machine.
2. Navigate to the main directory and run `pip install --editable .`
3. You can now run the commands

# Available commands
1. `ah --help` - get help information for the main command.
2. `ah view --help` - get help information for sub-command view.
3. `ah list --help` - get help information for sub-command list.
4. `ah view <article_slug>` - get a single article from the database and display it.
    Note: `responsive-images` is the slug of an article that already exists. Feel free to use it as an example
5. `ah view --save <article_slug>` - get a single article and save it in a docs folder as a json file.
6. `ah list` - get all articles. Limit is default to two articles.
7. `ah list --limit <int>` - set the limit of how many articles can be viewed.
8. `ah list --search <author_name>` - Allows user to search article with the author name.
    Note: `kimaiyo` is the name of one of the authors. Feel free to use it as an example

N.B. - you can use all options at the same time, for example, `ah list --limit 10 --search kimaiyo` will return the first ten articles written by the author Kimaiyo.
