
# Python Internship Projects

Projects I built during my Python programming internship at InternCircle (November 2026).

## Projects

### 1. Calculator and Unit Converter
A menu-driven command-line program that keeps running until the user quits.

- Calculator: addition, subtraction, multiplication, division
- Unit converter: km/miles, Celsius/Fahrenheit, kg/pounds
- Currency converter: INR to USD, EUR, GBP and back (fixed sample rates)
- Input is checked with while loops, so wrong input does not crash the program

**How to run:**
        python project1-calculator/convertocalc.py

Requires Python 3.10 or newer.

### 2. Number Guessing Game and Word Counter
A menu-driven program with two tools.

- Guessing game: the computer picks a number from 1 to 100, the player has 7 tries and gets higher/lower hints
- Word counter: reads a text file and shows total words, unique words and the top 10 most common words

**How to run:**

    python project2-game-and-counter/game-and-counter.py
    
    ### 3. Personal Expense Tracker with CSV
A menu-driven program that saves expenses to a CSV file, so they stay after the program is closed.

- Add an expense (date, category, description, amount) with input validation
- View all expenses with a total
- Filter by category, month or minimum amount
- Category summary: count and total per category, plus the highest spending category

**How to run:**

    python project3-expense-tracker/expense_tracker.py

### 3. Personal Expense Tracker with CSV
A menu-driven program that saves expenses to a CSV file, so they stay after the program is closed.

- Add an expense (date, category, description, amount) with input validation
- View all expenses with a total
- Filter by category, month or minimum amount
- Category summary: count and total per category, plus the highest spending category

**How to run:**

    python project3-expense-tracker/expense_tracker.py

Sample data is in `expenses.csv` (made-up data). 

# Project 4: Web Scraper for Quotes

## Description
This project is a simple Python web scraper that collects quotes from a website using Requests and BeautifulSoup.

## Features
- Extracts at least 20 quotes.
- Collects quote text, author names, and tags.
- Saves the extracted data in JSON format.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- JSON

## Website Used
https://quotes.toscrape.com/

## Output
The scraped data is saved in `quotes.json`.

## How to Run
```bash
pip install requests beautifulsoup4
python web_scraper.py
```

### 5. Weather App with Live OpenWeather API
A command-line app that shows the current temperature, humidity, wind and a short forecast for any city using the OpenWeather API.

**Setup:**
1. Get a free API key from openweathermap.org
2. Install requests: `pip install requests`
3. Create a `.env` file in the project folder with this line (see `.env.example`):

       API_KEY=your_key_here

**How to run:**

    python project5-weather-app/weather_app.py

The API key is read from `.env`, which is not uploaded to GitHub.

## Author
Vaibhav kumar 
