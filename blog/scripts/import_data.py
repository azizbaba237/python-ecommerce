from blog.models import Article
def run():
    for i in range(11,15):
        article = Article()
        article.title = "Article N° #%d" %i
        article.des   = "Description article N° #%d" %i
        article.image = "http://default"
        article.save()
print("Operation reussie ")