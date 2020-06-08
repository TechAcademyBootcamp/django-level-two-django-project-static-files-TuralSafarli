from django.shortcuts import render
import requests
import random


# Create your views here.
def random_news(request):
    news_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=dd5f84390b6e4218bf66116db5b25578'

    r = requests.get(news_url)

    total_news = r.json()['totalResults']

    news_number = random.randrange(0,total_news)

    title = r.json()['articles'][news_number]['title']
    author = r.json()['articles'][news_number]['author']
    content = r.json()['articles'][news_number]['content']
    image = r.json()['articles'][news_number]['urlToImage']
    published = r.json()['articles'][news_number]['publishedAt']

    context = {
        'title': title,
        'author': author,
        'content': content,
        'image': image,
        'published': published,
    }

    return render(request, 'news.html', context)