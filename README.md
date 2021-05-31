# YoutubeAPI
Some experiments on Youtube API : https://developers.google.com/youtube/v3/


## How to Run in Mac :

1. Create Python environment using : ```python3 -m venv env```
2. Activate environment using : ```source env/bin/activate```
3. Install all dependencies : ```pip install -r requirements.txt```
4. Open bash_profile file in VS Code : ``` code ~/.bash_profile```
5. Add your API key : ```export YOUTUBE_API_KEY="YOUR KEY"```
6. Execute test suite : ```python src/test_runner.py```
7. Execute Youtube Task : ```python src/youtubeTask.py```

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

## Sample playlist links
8 videos in playlist : PLkcctaU57y5ctgdK18QBThxJ8G4mB9q-u