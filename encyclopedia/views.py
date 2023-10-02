from django.shortcuts import render, redirect
from django import forms
import markdown2
from . import util

def index(request):
    if request.method == "POST":
        searched = request.POST['q']
        if checkEntry(searched) != 'Requested page was not found':
            return redirect("/" + searched)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def showEntry(request, title):
    html = checkEntry(title)
    return render(request, "encyclopedia/showEntry.html", {
        "html": html
        })
    
def checkEntry(title):
    markdownContent = util.get_entry(title)
    if markdownContent != None:
        html = markdown2.markdown(markdownContent)
        return html
    else:
        html = "Requested page was not found"
        return html



    


