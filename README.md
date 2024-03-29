<img src="./img/xcorebot_logo.png">

Developed by **Antonio Finocchiaro** and **Salvatore Alfio Sambataro**, this project is part of the **Quality Development** course at the University of Catania.

## Project Goal
This project involves the creation of a Telegram Bot aimed at delivering users the most recent music releases from the metal music scene.
Users have the option to access this information using two distinct commands.
They can choose to retrieve all the latest releases or specify a subset based on their preferences.

## Technologies used
<ul>
<li> <strong>Web Scraping</strong>: <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup</a>
<li> <strong>Parallel Tasks</strong>: <a href="https://docs.python.org/3/library/concurrent.futures.html">Concurrent Futures</a></li>
<li> <strong>Telegram API</strong>: <a href="https://core.telegram.org/bots/api">Telegram</a></li>
</ul>

## Project Structure
<img src="./img/xcorebot_pipe.png" width="60%">

## How to execute the project
To execute the Telegram Bot, you need to follow some steps.
### Install requirements
Install the libraries needed first.
Use pip or pip3 to install the dev requirements for the software usage and testing:

Source code requirements: 
```bash
pip3 install -r requirements.txt
```

Testing code requirements: 
```bash
pip3 install -r requirements_dev.txt
```

### Start project
Execute <code>python3 coreRadioBot.py</code> in the /src folder.

To run this code, you need the Telegram Bot Token, stored within `token_config.yaml` in /src. 
It is hidden for security purpose, contact the authors to receive it and follow the instructions within `config.py`.

To interact with the Bot:

<ul>
  <li>Open Telegram.</li>
  <li>Search <em>xCoreBot</em> and start a conversation.</li>
  <li>Digit <code>/help</code> to obtain information about its usage.</li>
</ul>

### Software Testing

Run the following command in the main directory to obtain a HTML report about the Pytest Coverage!

```bash
$ pytest --cov ./src ./tests --cov-report=html
```

