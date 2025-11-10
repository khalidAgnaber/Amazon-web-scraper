import requests
from bs4 import BeautifulSoup

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
  'Accept-Language': 'en-US,en;q=0.5'
}

def get_product_details(product_url: str) ->dict:
    # Create an empty dictionary to store product details
    product_details = {}

    # get product page content and create soup object
    page = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(page.content, features ='lxml')

    # Scrape the product details
    try:
        # We use the .find() method to find a span element. Then pass the productTitle id in a dictionary called
        # attrs that accepts the attributes. The .get_text() method returns the text in a string format.
        # The .strip() method is used to remove any extra leading and trailing whitespaces.
        title = soup.find('span', attrs={'id': 'productTitle'}).get_text().strip()

        # Same for price
        extracted_price = soup.find('span', attrs={'class': 'a-price-whole'}).get_text().strip()
        extrancted_decimal= soup.find('span', attrs={'class': 'a-price-fraction'}).get_text().strip()

        price = '$' + extracted_price + extrancted_decimal

        # Adding it to the product details dictionary
        product_details['title'] = title
        product_details['price'] = price
        product_details['product_url'] = product_url

        # Return the product details dictionary
        return product_details
    
    except Exception as e:
        print('Could not fetch product details')
        print(f'Failed with exception: {e}')
    
product_url = input('Enter product url: ')
product_details = get_product_details(product_url)

print(product_details)






