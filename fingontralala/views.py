from django.shortcuts import render


def index(requete):
    contexte = {}
    return render(requete, "base.html", contexte)

