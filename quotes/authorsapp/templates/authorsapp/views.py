from django.shortcuts import render, redirect
from authorsapp.templates.authorsapp.forms import AuthorForm


def main(request):
    return render(request, 'authorsapp/index.html')


def addAuthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authorsapp:main')
        else:
            return render(request, 'authorsapp/addAuthor.html', {'form': form})

    return render(request, 'authorsapp/addAuthor.html', {'form': AuthorForm()})
