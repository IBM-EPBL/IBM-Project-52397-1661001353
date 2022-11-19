from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/india')
def india():
    newsapi = NewsApiClient(api_key = "faeeea5c0d764c4faa9a2bcbd4af3ca3")
    topheadlinesindia= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=in")
    articles =topheadlinesindia['articles']

    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist1=zip(news,desc,img)
    return render_template ("india.html", context = mylist1)

@app.route('/southkorea')
def southkorea():
    newsapi = NewsApiClient(api_key = "faeeea5c0d764c4faa9a2bcbd4af3ca3")
    topheadlinessouthkorea = newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=kr")
    articles = topheadlinessouthkorea['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist2=zip(news,desc,img)
    return render_template ("southkorea.html", context = mylist2)

@app.route('/thailand')
def thailand():
    newsapi = NewsApiClient(api_key = "faeeea5c0d764c4faa9a2bcbd4af3ca3")
    topheadlinesthailand= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=th")
    articles = topheadlinesthailand['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist3 =zip(news,desc,img)
    return render_template ("thailand.html", context = mylist3)

@app.route('/unitedkingdom')
def unitedkingdom():
    newsapi = NewsApiClient(api_key = "faeeea5c0d764c4faa9a2bcbd4af3ca3")
    topheadlinesuk= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=gb")
    articles =topheadlinesuk['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist4 =zip(news,desc,img)
    return render_template ("unitedkingdom.html", context = mylist4)
    
@app.route('/ukrane')
def ukrane():
    newsapi = NewsApiClient(api_key = "faeeea5c0d764c4faa9a2bcbd4af3ca3")
    topheadlinesukrane= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=ua")
    articles =topheadlinesukrane['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist5 =zip(news,desc,img)
    return render_template ("ukrane.html", context = mylist5)
    
@app.route('/russia')
def russia():
    newsapi = NewsApiClient(api_key = "faeeea5c0d764c4faa9a2bcbd4af3ca3")
    topheadlinesrussia= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=ru")
    articles =topheadlinesrussia['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist6 =zip(news,desc,img)
    return render_template ("russia.html", context = mylist6)

@app.route('/tiwan')
def tiwan():
    newsapi = NewsApiClient(api_key = "faeeea5c0d764c4faa9a2bcbd4af3ca3")
    topheadlinestiwan= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=tw")
    articles =topheadlinestiwan['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist7 =zip(news,desc,img)
    return render_template ("tiwan.html", context = mylist7)
   
@app.route('/france')
def france():
    newsapi = NewsApiClient(api_key = "faeeea5c0d764c4faa9a2bcbd4af3ca3")
    topheadlinesfrance= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=fr")
    articles =topheadlinesfrance['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist8 =zip(news,desc,img)
    return render_template ("france.html", context = mylist8)
   
@app.route('/germany')
def germany():
    newsapi = NewsApiClient(api_key = "faeeea5c0d764c4faa9a2bcbd4af3ca3")
    topheadlinesgermany= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=de")
    articles =topheadlinesgermany['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist9 =zip(news,desc,img)
    return render_template ("germany.html", context = mylist9)
    
@app.route('/china')
def china():
    newsapi = NewsApiClient(api_key = "faeeea5c0d764c4faa9a2bcbd4af3ca3")
    topheadlineschina = newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=cn")
    articles = topheadlineschina['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist10 =zip(news,desc,img)
    return render_template ("china.html", context = mylist10)

if __name__ == "__main__":
    app.run(debug = True)
