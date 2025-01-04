from django.shortcuts import render, get_object_or_404
from .models import Article

# Object for home
def Home(request) :
    list_articles = Article.objects.all()
    context       = {"liste_articles" : list_articles}
    return render(request, "index.html", context)
 
 # Object for details page
def detail(request, id) :
    article = get_object_or_404(Article, id=id)
    Category= article.Category
    article_en_relation = Article.objects.filter(Category=Category)[:5]
    return render(request, 'detail.html', {'article':article, 'aer':article_en_relation})

# Object for search
def search(request):
    query = request.GET["article"]
    list_article = Article.objects.filter(title__contains=query)
    return render(request, "search.html",{"list_article":list_article})

