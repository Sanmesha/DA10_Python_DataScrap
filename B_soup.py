import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

q_url = "https://books.toscrape.com/" 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

book_titles = []  
for page in range(1, 51):
    url = q_url.format(page)
    response = rq.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        books = soup.find_all('h3')
        for book in books:
            title = book.a['title']
            book_titles.append(title)

books_df = pd.DataFrame(book_titles, columns=['Book Title'])

output_file = 'books_list.csv'
books_df.to_csv(output_file, index=False)

print(f"Scraped {len(book_titles)} book titles and saved to {output_file}")
