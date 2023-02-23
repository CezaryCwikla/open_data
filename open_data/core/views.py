from django.shortcuts import render


def about(request):
    return render(request, 'core/about.html', {'title': 'O mieście'})


def home_search(request):
    return render(request, 'core/home-search.html', {'title': 'Otwarte dane'})
