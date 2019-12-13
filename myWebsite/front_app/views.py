# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Prix journalier des fruits et légumes</h1>
        <p>Alors combien ça coûte ?</p>
    """)

def fruit(request, fruit):
    return render(request, 'front_app/fruit.html', {'fruit': fruit})
#
# def fruit(request):
#     HttpResponse("""
#         <p>fruit 1</p>
#         <p>fruit 2</p>
#     """)
