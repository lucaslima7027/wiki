from django.shortcuts import render
import markdown2
from . import util

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def showEntry(request, title):
    markdownContent = util.get_entry(title)

    if markdownContent != None:
        html = markdown2.markdown(markdownContent)
        return render(request, "encyclopedia/showEntry.html", {
        "html": html
        })
    else:
        html = "Requested page was not found"
        return render(request, "encyclopedia/showEntry.html", {
        "html": html
        })

