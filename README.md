# pycrawler

## Requirements

- Python 3.6
- pip3
- pipenv

## Configuring your environment

Install the project dependencies:
```
pipenv install --three
```

Enable pipenv environment:
```
pipenv shell
```

## Running

Make sure to have the correct configuration within **config.cfg** file

Run in single command mode:
```
python crawler.py -c subreddit1;subreddit2;subredditN
```

Run in bot mode:
```
python crawler.py -b
```
