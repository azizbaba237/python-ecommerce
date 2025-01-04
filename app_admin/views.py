from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from blog.models import Article
from blog.forms import ArticleForm

# Render views
def dashboard(request):
    return render(request, 'db.html')

# Show article 
@login_required
def user_articles(request):
    has_perm = False
    if request.user.has_perm("blog.delete_article"):
        has_perm = True
        
    list_articles = Article.objects.filter(user=request.user)
    return render(request, 'my-articles.html', {'list_articles':list_articles, "has_perm":has_perm})

# Add article class 
class AddArticle(LoginRequiredMixin,CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "add-article.html"
    success_url = "my-articles"
# Pour savoir qui a publiblier 
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
# Edit article 
class UpdateArticle(LoginRequiredMixin,UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'app_admin/article_form.html'
    
# Delete article  
class DeleteArticle(DeleteView):
    model = Article
    template_name = "blog/article_confirm_delete.html"
    success_url = "/my-admin/my-articles"
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('blog.delete_artccle'):
            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)
    