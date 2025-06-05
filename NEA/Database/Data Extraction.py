import requests 
from bs4 import BeautifulSoup
import csv


#Adding a user agent specific to our device
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edge/134.0.0.0"}
#Specifying the website that we want to search from
URL = "https://www.chainreactioncycles.com/bike-parts/frames-and-forks"
#Sending a HTTP request to the specified URL and save the response from the server in an object called r
r = requests.get(url=URL, headers=headers)

#Creating a beautiful soup object
soup = BeautifulSoup(r.content, 'html5lib')
#Prints a visual reprsentation of the tree created from the HTML content
print(soup.prettify()[:500])

#Searches the html content stored in the soup object which we created, specifically searches for all div elemtnts that have the class product title
products = soup.find_all('div', class_='product-tile')

#Defining the filename and opening CSV file in write mode
filename = 'forksframes.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    #Create a CSV DictWriter to write data into CSV
    fieldnames = ['product_name', 'brand', 'product_size', 'image_url', 'product_price', 'product_link']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()



#For loop that iterates over each product block
for product in products:
   #Product name
    product_name_tag = product.find('span', class_='productdescriptionname')
    product_name = product_name_tag.text.strip() if product_name_tag else 'N/A'
   
   #Product brand
    brand_tag = product.find('span', class_='brandWrapTitle')
    brand =

   #Product size
    product_size_tag = product.find('span', class_='sizeDetail')
    product_size = 

    #Product image
    image_url_tag = product.find('img', class_='rtimg.MainImage.image-responsive')
    image_url = 

    #Product price
    product_price_tag = product.find('span', class_='CurrencySizeLarge.curprice')
    product_price = 

    #Product link
    product_link_tag = product.find('a', href=True)
    product_link = 

#name, brand, subCategory,colour,imagure url, price, targetUrl 
    
#Appending the data we have found to a csv file
    writer.writenow({
        'product_name': product_name,
        'brand': brand,
        'product_size': product_size,
        'image_url': image_url,
        'product_price': product_price,
        'product_link': product_link
    })
    