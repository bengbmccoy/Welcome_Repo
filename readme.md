***README***

***Welcome to Ben McCoy's online Guthub RenewEconomy Scrape repo!***

In this repo is my project involving scraping, storing and ranking RenewEconomy articles as HTML files along with some metadata such as author and date scraped. These articles will be used as data for future analysis. The idea will be to perform some kind of statistical analysis on the articles but exactly how this is works is to be decided.

Currently there are 6 items within this online repo:
- readme.md - This file.
- .gitignore - ignores all .html files and the bash file
- url_database.csv - Stores urls (and meta data) that has been saved.
- pages_ - where the HTML files are stored.
- renewecon_scrape.py - script that accesses new articles and saves them as html files in the pages_ directory.
- renewecon_rank.py - script that saves the rank of an article using command line arguments as input.


I hope you enjoy your time in the repo.

Regards,

Ben

LinkedIn: [Ben McCoy](https://www.linkedin.com/in/benjamin-mccoy-68005b125/)

**Decision Log:**

20190212 - Decided to perform ranking of articles through a seperate script called renewecon_rank. This will be easier than collecting user input in the renewecon_read script.
