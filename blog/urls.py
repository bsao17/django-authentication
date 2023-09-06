from django.urls import path
from . import views
from .views import Author

urlpatterns = [
    path("article-<int:article_id>", Author.as_view, name="articles")
]