from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Article
# Create your views here


def accueil_blog(requete):
    return render(
        requete,
        "blog/accueil.html",
        {"articles": Article.objects.all().order_by("-date_publication")},
    )


def article(requete, cle_primaire):
    objet_article = get_object_or_404(Article, pk=cle_primaire)
    return render(requete, "blog/article.html", {"article": objet_article})
