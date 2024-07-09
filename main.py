import openai
from bs4 import BeautifulSoup
import requests

url = "https://www.nbcnews.com/business/consumer/paramount-merger-sparks-concern-movie-theater-owners-rcna160773"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

article_content = ""

articles = soup.find_all("div", class_='article-body__content')
for article in articles:
    paragraphs = article.find_all('p')
    for p in paragraphs:
        article_content += p.text

print(article_content)

client = openai.OpenAI()
response = client.chat.completions.create(
    messages= [
        {
            'role':'system',
            'content': "Write a tweet describing the news story. No hashtags. Emojis should be added at the end."
        },
        {
            'role':'user',
            'content': f"Article: {article_content}"
        }
    ],
    model="gpt-3.5-turbo-0125"
)

print(response.choices[0].message)

# class: article-body__content

