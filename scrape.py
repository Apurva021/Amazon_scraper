from bs4 import BeautifulSoup
import time
import os
import smtplib
from selenium import webdriver


#functions
#this function is used to remove all the non ascii characters so they dont cause problem while parsing
def remove_non_ascii(text):
	return ''.join([i if ord(i) < 128 else '' for i in text])

#this function will fetch the price of the product
def get_price(body):
	span=body.find("span",id="priceblock_ourprice")
	price=span.text
	price=price.replace(',','')
	price=remove_non_ascii(price)
	#price=remove_non_ascii(span.text)	
	print('Price:'+price)
	return price

#this function will check whether the product is in stock or not
def is_available(body):
	span=body.find("span",{'class':'a-size-medium a-color-success'})
	if span==None:
		return False
	return True

#this function will be used to fetch the name of product
def get_name(body):
	span=body.find("span", id="productTitle")
	name=span.text
	name=name.replace('\n','')
	return name	

#the email-id and password are stored as environment variables
#this is done so that we dont need to write the sensitive information in our code
EMAIL_ID=os.environ.get('EMAIL_ID')
EMAIL_PASS=os.environ.get('EMAIL_PASS')


#right now the url is static
#later we will take the url as an input from the user
#example of available url
#url='https://www.amazon.in/Philips-BT1212-Beard-Trimmer-Green/dp/B0744L38KK/ref=sr_1_2?crid=CNCFP1RTI561&dchild=1&keywords=philips+trimmers&qid=1597664820&sprefix=philips%2Caps%2C358&sr=8-2'

#example of unavailble url
#url='https://www.amazon.in/Havells-BT5171C-Quick-Charging-Trimmer/dp/B07SP4PKXX/ref=sr_1_18?dchild=1&keywords=trimmer&qid=1597725694&sr=8-18'

#taking url as input
url=input("Enter the url of the product page on Amazon:\n")

#taking the desired price as input
desired_price=input("Enter your desired price:\n")

#taking the user email-id as input
receiver_email=input("Enter your email-id:\n")


while True:
	browser=webdriver.Firefox()
	browser.get(url)
	time.sleep(5)
	page=browser.page_source
	soup=BeautifulSoup(page,'html.parser')
	product_name=get_name(soup)
	inStock=is_available(soup)
	if not inStock:
		print('Product not available')
		browser.close()
		continue
	print('Product is available')
	price=get_price(soup)
	browser.close()
	if float(price)<float(desired_price):
		print('Sending mail')
		#code for sending mail
		with smtplib.SMTP('smtp.gmail.com',587) as smtp:
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo
			smtp.login(EMAIL_ID,EMAIL_PASS)
			subject='Amazon Product available'
			body=str(product_name)+' is now available at price '+str(price)+' at the following url:\n'+url
			message=f'Subject: {subject}\n\n{body}'
			smtp.sendmail(EMAIL_ID,receiver_email,message)
			smtp.quit()
			print('Mail sent')
		break

	#the price and availablilty is fetched every 20 seconds
	time.sleep(20)

