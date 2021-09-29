import requests 
import json
from django.shortcuts import render
from hunspell import Hunspell

h = Hunspell()
h.suggest('spookie')

def index(request):
    result = request.GET.dict()
    ##word_text=(result)
    #word_text = list(result.values())[0]
    word_text= "helo"
    word_list= h.suggest(word_text)
    data ={'output': word_list}
    return render(request, "main/index.html",data)


# #Create your views here.
# def index(request):
#     ## Get url parameters "enter_text"
#     result = request.GET.dict()
#     ## If not available start with default parameters
#     res = not bool(result)
#     if res==True :
#         result = {'enter_text': 'default'}
#         word_text=(result['enter_text'])
#         word_list=h.suggest(word_text)
#         data ={'output': word_list}
#         ## Else enter your word of choice
#     else:
#         word_text=(result['enter_text'])
#         ##word_text= "helo"
#         word_list= h.suggest(word_text)
#         data ={'output': word_list}
#     return render(request, "main/index.html",data)


