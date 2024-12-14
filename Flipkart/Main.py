from Utils.extracthtml import getHtml
import pandas as pd

fetch_url = 'https://www.flipkart.com/search?q=macbook&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

fetch_header = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}

if __name__ == "__main__":
    fetched_data = getHtml(websiteurl=fetch_url, showbrowser=False, screenshotname='LAPTOP')

    product_items = []

    for item in fetched_data.css('div[class*="tUxRFH"]'):
       
        product_image = item.css_first('img[loading="eager"]')
        if product_image:
            image_info = {
                'Src': product_image.attrs.get('src', ''),
                'Alt': product_image.attrs.get('alt', '')
            }
        else:
            image_info = {'Src': None, 'Alt': None}

        
        product_name = item.css_first('div[class*="KzDlHZ"]')
        product_name = product_name.text() if product_name else None

        
        product_rating = item.css_first('span > div[class*="XQDdHH"]')
        product_rating = product_rating.text() if product_rating else None

        
        rating_review_count = item.css_first('span[class*="Wphh3N"]')
        rating_review_count = rating_review_count.text() if rating_review_count else None

        
        product_details = item.css_first('ul[class*="G4BRas"]')
        product_details = product_details.text() if product_details else None

       
        original_price = item.css_first('div[class*="Nx9bqj"]')
        original_price = original_price.text() if original_price else None

        
        before_discount = item.css_first('div[class*="yRaY8j"]')
        discount_info = before_discount.text() if before_discount else None

        discount_percent = item.css_first('div[class*="UkUFwK"]')
        discount_value = discount_percent.text() if discount_percent else None

        #
        product_dict = {
            'Product Name': product_name,
            'BeforeDiscount': discount_info,
            '%Discount': discount_value,
            'Price': original_price,
            'Product Detail': product_details,
            'Rating': product_rating,
            'Number of rating and review': rating_review_count,
            'Image': image_info
        }

        product_items.append(product_dict)

   
    product_dataframe = pd.DataFrame(product_items)
    product_dataframe.to_csv('FlipkartData.csv', index=False)
