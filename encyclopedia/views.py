from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def showEntry(request, title):
    return render(request, "encyclopedia/showEntry.html", {
        "title": title
    })

