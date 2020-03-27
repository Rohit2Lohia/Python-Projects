import requests
from django.shortcuts import render,redirect
#from bs4 import BeautifulSoup as BSoup
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

requests.packages.urllib3.disable_warnings()

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles': articles})
    # here 'articles' is  a dictonary of articles
    # to pass anything in a html we need to send it thorough a dictonarty variable
    # the name is not necessarily articles it can be anything.

def article_detail(request,slug):
    # return HttpResponse(slug) #this simply take the slug and print it out no matter what we click or url we hard_type
    # To get detailed individual response to any particular web page first we need to scarpe the database
    article = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method=='POST':
        form=forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            #save article to database and to auto config user we must
            # create an instance of the author before saving it.
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})

#
#
# def news_list(request):
#     headlines=Headline.objects.all()[::-1]
#     context = {
#         'object_list': headlines,
#     }
#     #....
#
# def scrape(request):
#     session = request.Session()
#     session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
#     url = "https://theonion.com"
#
#     content = session.get(url, verify=False).content
#     soup = BSoup(content, "html.parser")
#     News = soup.find_all('ul', {"class":"h_story normal"})
#
#
#     for article in News:
#         main = article.find_all('li')[0]
#         link = main['href']
#         image_src = str(main.find('img')['srcset']).split(" ")[-4]
# 		# title = main['title']
# 		new_headline = Headline()
# 		new_headline.title = title
# 		new_headline.url = link
# 		new_headline.image = image_src
# 		new_headline.save()
# 	return redirect("../")
