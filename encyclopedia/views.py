from django.shortcuts import render, redirect
from django import forms
import markdown2
from . import util
import random

class newPageForm(forms.Form):
    Title = forms.CharField(label="Title")
    mdContent = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), label="Content")

class editEntryForm(forms.Form):
    entryContent = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), label="Content")

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
        "html": html,
        "title": title,
        })

def newPage(request):
    errorMessage = ""
    if request.method == "POST":
        form = newPageForm(request.POST)
        if form.is_valid():
            newTitle = form.cleaned_data["Title"]
            newContent = form.cleaned_data["mdContent"]
            if util.get_entry(newTitle) == None:
                content = f"# {newTitle}\n{newContent}"
                util.save_entry(newTitle, content)
                return redirect("/" + newTitle)
            
            else:
                errorMessage = "<h2>This title already exists</h2>"
                return render(request, "encyclopedia/newPage.html", {
                    "errorMessage": errorMessage,
                    "form": form
                })


    return render(request, "encyclopedia/newPage.html", {
        "form": newPageForm()
    })

def randomPage(request):
    ramdomEntry = random.choice(util.list_entries())
    return redirect("/" + ramdomEntry)

def editEntry(request, title):
    if request.method == "POST":
        editedForm = editEntryForm(request.POST)
        if editedForm.is_valid():
            editedContent = editedForm.cleaned_data["entryContent"]
            util.save_entry(title, editedContent)
            return redirect("/" + title)

    mdToEdit = util.get_entry(title)
    editForm = editEntryForm({'entryContent': mdToEdit})
    return render(request, "encyclopedia/editEntry.html", {
        "form": editForm
        })
    
def checkEntry(title):
    markdownContent = util.get_entry(title)
    if markdownContent != None:
        html = markdown2.markdown(markdownContent)
        return html
    else:
        html = "Requested page was not found"
        return html



    


