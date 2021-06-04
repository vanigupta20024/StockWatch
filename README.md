# StockWatch
<p align="center">
  <img width="200" height="200" src="https://github.com/vanigupta20024/StockWatch/blob/master/Readme_images/logo.ico">
</p>

Website for viewing stock data or related information in real time. There could be a delay of 1 minute (local caching) since updating it every second will have a huge load on backend (in free services). Daily top losing and gainer stocks can be visible along with tick data. Most graphs have a live tick data with more than 10 thousand points.

#### Website:
Live project deployed to heroku: [StockWatch](https://stockwatch-app.herokuapp.com/)

#### Tech stack:
![Django](https://img.shields.io/badge/-Django-red)
![Python](https://img.shields.io/badge/-Python%20-blueviolet)
![JavaScript](https://img.shields.io/badge/-JavaScript-brightgreen)
![JQuery](https://img.shields.io/badge/-JQuery-yellow)
![Ajax](https://img.shields.io/badge/-Ajax-blue)
![HTML](https://img.shields.io/badge/-HTML-lightgrey)
![CSS](https://img.shields.io/badge/-CSS-9fc)
![Bootstrap](https://img.shields.io/badge/-Bootstrap-orange)

#### How to run:
- Download the project to your local system or fork the project and clone it
- cd into the project directory: `cd StockWatch`
- Install the requirements: `pip install -r requirements.txt`
- Run the server: `python manage.py runserver`
- Run the custom management command for updating data: `python manage.py create_json`
- Open your web browser and go to: `http://127.0.0.1:8000/stockwatch/about` or `http://127.0.0.1:8000/`

#### Screenshots:

#### Landing Page:
Basic landing page with minimal functionality
![Landing](https://github.com/vanigupta20024/StockWatch/blob/master/Readme_images/landing_page.PNG)


#### Listing Page: 
Lists most viewed indices, top gainers of the day, top losers of the day and an option to search through thousands of company listings.
![Listing](https://github.com/vanigupta20024/StockWatch/blob/master/Readme_images/listing.jpg)

#### Stock Info:
Financial information and metadata/company specific data related to a particular stock with graph and tick points.
![Info](https://github.com/vanigupta20024/StockWatch/blob/master/Readme_images/info_page.PNG)

Special mentions: [Aakash Dinkar](https://github.com/aakashdinkar)
