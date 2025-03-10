## Resources

[Zilliow](https://appbrewery.github.io/Zillow-Clone/)

[Docs](https://docs.google.com/forms/u/0/?pli=1)

[Zillow](https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D)

[Workplace](https://workplace.stackexchange.com/questions/93696/is-it-unethical-for-me-to-not-tell-my-employer-i-ve-automated-my-job)

[Reddit](https://www.reddit.com/r/Python/comments/8uxifv/has_anyone_automated_their_job_completely/?rdt=49333)

Web Scraping and Data Entry Capstone Project Requirements
As we get closer to the latter part of the course, and as you build up your skills every day, the challenges are going to become more life-like and more challenging. As a developer, you will spend most of your time figuring out how to do things using Google and StackOverflow. It's rare that I come across a new project and already know exactly what code I need to write.

In this capstone project, you will need to apply everything you've learnt about website and web scraping with Beautiful Soup and Selenium to complete the project and fulfil the project requirements. You might also need to do your own research and revision to complete the task.

Set up your own Google Form
First, you need to create a new form in Google Forms.

1. Go to https://docs.google.com/forms/ and create your own form:


2. Add 3 questions to the form, make all questions "short-answer":


3. Click send and copy the link address of the form. You will need to use this in your program.




Go to our Zillow-Clone Website
4. Go to https://appbrewery.github.io/Zillow-Clone/ and see how the website is structured. This is where you'll be scraping the data from:


BeautifulSoup Requirements
Use BeautifulSoup/Requests to scrape all the listings from the Zillow-Clone web address (Step 4 above).



Create a list of links for all the listings you scraped. e.g.



Create a list of prices for all the listings you scraped. e.g.

Clean up the strings, by removing any "+" symbols and other information so that you are only left with a dollar price. The price should look like "$1,234" instead of "$1,234+ /mo"



Create a list of addresses for all the listings you scraped. e.g.


Clean up the address data as well. Remove any newlines, pipe symbols |, and unnecessary whitespace.



Selenium Requirements


Use Selenium to fill in the form you created (step 1,2,3 above). Each listing should have its price/address/link added to the form. You will need to fill in a new form for each new listing. e.g.


Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the responses to the Google Form. You should end up with a spreadsheet with all the details from the properties.


Objective 🎯
You should end up with a spreadsheet that looks something like this.

Hints & Solution
Hint 1
Remember to provide your user agent and accepted languages via a header. We've discussed this in the Amazon Price Scraping project in day 47.



Hint 2:
The address data can be quite messy:


There's many ways you can clean this up. One way is to use Python's .replace() and .strip() methods to remove the newlines, whitespace and pipe symbols.



Hint 3
The price for listings with multiple properties have different text from listings with a single property only. A property with a single listing will have a price of $1,234/mo or $1,234+/mo, but a listing with multiple properties will have the number of bedrooms in the price $1,234+ 1bd. Try to clean up this data as well.



Partial Solution
If you got stuck on the data cleaning and BeautifulSoup, you can look at the solution to the first part of the capstone project here: https://gist.github.com/TheMuellenator/7e45f9b977e90419146c4a2ee1713087



Complete Solution
Here's the complete solution that includes both BeautifulSoup and Selenium:

https://gist.github.com/TheMuellenator/1318b1084a74e9b559f9820438b4a931




