from django.shortcuts import render, redirect
from django import forms
import markdown2
from . import util

class newPageForm(forms.Form):
    title = forms.CharField(label="title")
    mdContent = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), label="mdContent")

def index(request):
    if request.method == "POST":
        searched = request.POST['q']
        if checkEntry(searched) != 'Requested page was not found':
            return redirect("/" + searched)
        
        else:
           searchResults = []
           for entry in util.list_entries():
               if searched in util.get_entry(entry):
                   searchResults.append(entry)
           return render(request, "encyclopedia/search.html", {
               "searchResults": searchResults,
               'searched': searched} )

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def showEntry(request, title):
    html = checkEntry(title)
    return render(request, "encyclopedia/showEntry.html", {
        "html": html
        })

def newPage(request):
    if request.method == "POST":
        form = newPageForm(request.POST)
        if form.is_valid():
            newTitle = form.cleaned_data["title"]
            newContent = form.cleaned_data["mdContent"]
            if util.get_entry(newTitle) == None:
                util.save_entry(newTitle, newContent)
                return redirect("/" + newTitle)
            
            else:
                errorMessage = "<h1>This title already exists</h1>"
                return render(request, "encyclopedia/newPage.html", {
                    "errorMessage": errorMessage
                })


    return render(request, "encyclopedia/newPage.html", {
        "form": newPageForm()
    })
    
    
def checkEntry(title):
    markdownContent = util.get_entry(title)
    if markdownContent != None:
        html = markdown2.markdown(markdownContent)
        return html
    else:
        html = "Requested page was not found"
        return html



    


