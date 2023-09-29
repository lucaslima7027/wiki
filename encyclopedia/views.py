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
    html = markdown2.markdown(markdownContent)
    return render(request, "encyclopedia/showEntry.html", {
        "html": html
    })

