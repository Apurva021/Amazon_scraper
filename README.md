# Amazon_scraper
In this project I have created a web scraper using python which will take the url of the product the user is interested in as input and then fetch the details like: the name of the product, whether the product is currently available and the price of the product. The script will also take as input the desired price of the product and the email id of the user. If the actual price of the product is less than or equal to the desired price than the user will receive an email allowing him to purchase the product at his desired price.
This script uses the following libraries in python:
1.	Beautiful Soup
2.	Selenium
3.	Os
4.	Time
5.	Smtplib

After the above details are taken as input, I have used the selenium library to fetch the html script of the page and then I have used the Beautiful Soup library to parse the html script of the page. After the html script is parsed, we can use it to fetch important details from the web page like name of the product, its availability and price.

The remove_non_ascii function is used to remove non ascii characters like the rupee symbol from the string.
The get_price() function takes the html body of the page as argument and then fetches the price of the product of the page.
The get_name() function takes the html body of the page as argument and then fetches the name of the product from the page
The is_available() function takes the html body as parameter and checks if the product is available or not.

If the product is not available the program will complete its execution after printing that product not available. If the product is available and its price is less than the desired price than a mail will be sent to the user that the product can now be purchased. But if the price is greater than the desired price than program will re-execute after 20 seconds to check the price again.
