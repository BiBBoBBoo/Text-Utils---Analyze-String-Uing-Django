from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = (request.POST.get('text', 'default'))
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps = (request.POST.get('fullcaps', 'off'))
    newlineremover = (request.POST.get('newlineremover', 'off'))
    spaceremover = (request.POST.get('spaceremover', 'off'))
    countchar = (request.POST.get('countchar', 'off'))

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose': 'Punctuation removed', 'analysed_text': analysed}
        djtext = analysed

    if fullcaps == "on":
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        params = {'purpose': 'Convert all to capital', 'analysed_text': analysed}
        djtext = analysed

    if newlineremover == "on":
        analysed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analysed = analysed + char
        params = {'purpose': 'Removed new line', 'analysed_text': analysed}
        djtext = analysed

    if spaceremover == "on":
        analysed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analysed = analysed + char
        params = {'purpose': 'Extra Spaces Removed', 'analysed_text': analysed}
        djtext = analysed

    if countchar == 'on':
        analysed = len(djtext)
        params = {'purpose': 'The number of character in your string is', 'analysed_text': analysed}

    if removepunc == 'off' and fullcaps == "off" and newlineremover == "off" and spaceremover == "on":
        return HttpResponse("Please select the operation and try again !!")

    else:
        return render(request, 'analyze.html', params)

