from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def word(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 1

    context = {
        'attempts' : request.session['attempts'],
        'randomWord' : get_random_string(length=16)
    }

    print(f'\n {context["attempts"]} \n')

    return render(request, 'word.html', context)

def generateWord(request):
    request.session['attempts'] += 1

    return redirect('/word')

def reset(request):
    request.session.pop('attempts')

    return redirect('/word')