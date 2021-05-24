# YoutubeAPI
Some experiments on Youtube API : https://developers.google.com/youtube/v3/


## How to Run in Mac :

Create Python environment using : ```python3 -m venv env```
Activate environment using : ```source env/bin/activate```
Install all dependencies : ```pip install -r requirements.txt```
Execute test suite : ```python src/test_runner.py```
Execute Youtube Task : ```python src/youtubeTask.py```

## Dependencies and libraries used
1. isodate : to transfer youtube's duration to timedelta
2. tableprint : to print video details in cosole as a table
3. xlsxwriter : to make table in excel file
4. requests : to call YouTube API

# Tests
Tests written using unittest library of Python

# CI
Used GitHub actions that triggers on push of all branches and on pull request on main branch

## Deployment details
Uploaded in GitHub and run in local

## Sample playlist link
www.youtube.com/watch?v=g4Fny0Zz5j8&list=PLkcctaU57y5ctgdK18QBThxJ8G4mB9q-u