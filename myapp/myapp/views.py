from django.shortcuts import render, redirect


def home(request):
    return render(request, './base.html')


def login(request):
    return render(request, './log-in.html')
