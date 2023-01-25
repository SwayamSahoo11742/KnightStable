![banner](https://user-images.githubusercontent.com/117121187/210261879-313142b4-728e-4ef2-916d-abfac24c4047.jpg)
![GitHub repo size](https://img.shields.io/github/repo-size/SwayamSahoo11742/KnightStable) ![GitHub last commit](https://img.shields.io/github/last-commit/SwayamSahoo11742/KnightStable)

KnightStable is a chess website where users can look at previous games, openings, recent news as well as play against others


Link: https://764f-108-7-187-149.ngrok.io      

**note: This site's url changes every ~24-48hrs and this website is NOT meant to be used on a small device such as a phone. For more info, check the Notes section**
<br>
<br>

![ks](https://user-images.githubusercontent.com/117121187/210262413-05c97721-5fc1-48c8-866b-4b9651ebc9e1.gif)

# Installation
### Step 1 - Clone the Project
Run the following command
```
git clone https://github.com/SwayamSahoo11742/KnightStable.git
```
### Step 2 - Install everything in requirements.txt using the following command:
****Make sure you are in knightstable folder**
```
pip install -r requirements.txt
```

### Step 3 - Setting up the databases.

Run `database.py` in the staticHelpers directory to create the databases:
```
python database.py
```
****The openings and games databases will be empty at this stage and unfortunately, the games database cannot be filled, however if you want the opening database, simply run `web_scraper.py` in staticHelpers**

### Step 4 - setting authtoken with ngrok

Create an ngrok account at this [link](https://ngrok.com/) and go to their [dashboard](https://dashboard.ngrok.com/get-started/setup) to follow instructions on how to set up an authtoken


### Step 5 - Running the website

After setting up your authtoken, to run the website, open the knightstable terminal and run the following commands:
```
set FLASK_APP=__init__.py
```
```
flask run
```
It should be running in port 5000, so now you can open cmd as an administrator and run `ngrok http 5000` and the link to your website will be in the ngrok terminal. You do not have to use the randomly generated link by ngrok, you can use a domain name, but for that you will need to buy ngrok premiun which is quite expensive.

****You will have to do this step each time you reset your server.**

# Features
- ### Look at the games of others
  - Learn from higher level plays, or have a look at how lower level play is

- ### Search for fun openings
  - Whether it be the famous Sicillian, or obsecure Flick Knife Attack, we have it 

- ### Look at recent, world-wide, chess events
  - Maybe you can go to one

- ### Play against other players
  - And climb the rating ladder

# Images
  - ### Homepage
  <img width="950" alt="Screenshot_20221227_110428" src="https://user-images.githubusercontent.com/117121187/210263823-88472bee-b7c0-4617-9049-56307a9ca934.png">
  
  <img width="953" alt="Screenshot_20221227_110458" src="https://user-images.githubusercontent.com/117121187/210263866-35831c41-737b-44d2-8a2a-216740a6960d.png">
  
  - ### Search Page
    <img width="950" alt="Screenshot_20221227_110524" src="https://user-images.githubusercontent.com/117121187/210263902-58abbad6-f71f-42d1-98de-7ea3dd20e705.png">
  
  - ### Opening Search Page
    <img width="949" alt="image" src="https://user-images.githubusercontent.com/117121187/211160731-4f03652b-e1be-4be9-a6a7-0411768ec9bf.png">
  
  - ### Play page
    <img width="949" alt="image" src="https://user-images.githubusercontent.com/117121187/211160887-a6f8aef2-7533-4a45-8bbc-919bbb07f950.png">
  
  - ### Game page
    <img width="951" alt="Screenshot_20221227_110728" src="https://user-images.githubusercontent.com/117121187/210263981-8aab3ea9-f391-4a32-aeca-0e4499f12f1a.png">
  
  - ### **Many more pages that cannot be displayed to keep this concise, can be viewed in the link above
# Languages/tools used
- ### Backend
  - Python
  - Sqlite3 (Development Database)
  - PostgreSQL (Production Database)
  

- ### Frontend
  - JavaScript
  - HTML5
  - CSS
  
- ### Tools and Modules
    ### Backend
    - Flask
    - SocketIO
    - Pyscopg2
    - BeautifulSoup4
    - Selenium
    
    ### Frontend
    - Chart.js
    - chessboard.js
    - chess.js
    - Bootstrap5
    - Jinja2


# Notes
- Due to the lack of visits, from both me and others, the product is not publicly accessible as it is not worth the cost to keep it running. Instead, the development version of this is ran on my local system since the traffic will not be high.

- This app is using **Ngrok** to run and forward an SSH tunnel to my localhost. 

- The url is different every day or so because ngrok's free plan does not allow for a domain name. That being said, because there is no limit on the session duration, I will try to keep it on as much as possible but it will have to restart with a new url every other day or so. 

- The production version repository of this project is at this [link](https://github.com/SwayamSahoo11742/KnightStable-product) 

<br>

# Test Contributors
Jake Pisanwarakul

# Developer
Swayam Sahoo

Email: swayamsa01@gmail.com
