from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from quotesapp.models import Quote
from quotesapp.templates.quotesapp.forms import QuoteForm


def get_quotes_on_page(page):
    per_page = 10
    paginator = Paginator(Quote.objects.all(), per_page)
    quotes_on_page = paginator.page(page)
    return quotes_on_page


def main(request, page=1):
    quotes_on_page = get_quotes_on_page(page)
    return render(request, 'quotesapp/index.html', context={'quotes': quotes_on_page})


def addQuote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotesapp:main')
        else:
            return render(request, 'quotesapp/addQuote.html', {'form': form})

    return render(request, 'quotesapp/addQuote.html', {'form': QuoteForm()})
