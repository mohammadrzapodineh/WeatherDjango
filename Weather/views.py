from django.shortcuts import render


def weather(reuqest):
    return render(reuqest, 'home_page.html')