# Self created file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # POST the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newline = request.POST.get('newlineremover', 'off')
    removespace = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    print(newline)
    print(djtext)
    analyzed_text = djtext
    punctuations = '''<>\,.?/{}[];:!*@#$%^()-_+=~`'"|&'''
    analyzed = ""
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # analyze the text
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Capitialized Text', 'analyzed_text': analyzed}
        djtext=analyzed
    #    return render(request, 'analyze.html', params)

    if newline == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed += char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if removespace == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        djtext=analyzed
        return render(request, 'analyze.html', params)

    if charcount == 'on':
        analyzed = ""
        c = 0;
        for char in djtext:
            c += 1
        params = {'purpose': 'Character Count', 'analyzed_text': c}
        return render(request, 'analyze.html', params)

    if removepunc!= 'on' and fullcaps!= 'on' and newline!= 'on' and removespace!= 'on' and charcount!= 'on' :
        return render(request,'error.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request,'contact.html')
