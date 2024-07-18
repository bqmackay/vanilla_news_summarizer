import openai
from bs4 import BeautifulSoup
import requests

# Set up news scraper
url = "https://www.nbcnews.com/business/consumer/paramount-merger-sparks-concern-movie-theater-owners-rcna160773"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

article_content = ""

articles = soup.find_all("div", class_='article-body__content')
for article in articles:
    paragraphs = article.find_all('p')
    for p in paragraphs:
        article_content += p.text

# Start tweet generator
client = openai.OpenAI()
response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages= [
        {
            'role':'system',
            'content': "Write a tweet describing the news story. No hashtags. Emojis should be added at the end."
        },
        {
            'role':'user',
            'content': f"Write a reader's digest version of this article: {article_content}"
        }
    ],
)

print(response.choices[0].message)
