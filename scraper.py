from mechanize import Browser
from bs4 import BeautifulSoup as BS

websiteLink = "http://www.amazon.in"

def print_product_details(soup):
  productName="" 
  for product in soup.find_all('a', class_="s-access-detail-page"):
    #print (product.prettify()) 
    #printing product name and url
    #print "Product Name : " + product["title"]
    #print "Product Url : " + product["href"]
    #print "======================="
    productName= productName+","+product["title"]
  return productName

def get_next_link(soup):
  nextlink = soup.find(id="pagnNextLink")
  return websiteLink+nextlink["href"]

br = Browser()
 
# Browser options
# Ignore robots.txt. Do not do this without thought and consideration.
br.set_handle_robots(False)
 
# Don't add Referer (sic) header
br.set_handle_referer(False)
 
# Don't handle Refresh redirections
br.set_handle_refresh(False)
 
#Setting the user agent as firefox
br.addheaders = [('User-agent', 'Firefox')]
 
br.open(websiteLink)
br.select_form(name="site-search")
br['field-keywords'] = "Blackberry"
br.submit()
 
#Getting the response in beautifulsoup
soup = BS(br.response().read())
productName = print_product_details(soup)
print "Page 1: "+productName
nextlink = get_next_link(soup)
print nextlink

br.open(nextlink)
soup=""
soup = BS(br.response().read())
productName = print_product_details(soup)
print "Page 2: "+productName
nextlink = get_next_link(soup)
print nextlink


