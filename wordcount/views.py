from django.http import HttpResponse
from django.shortcuts import render
import operator
#import operator ==>> sorted(dict.items(), key=operator.itemgetter(1), reverse = True)

def homepage(request):
	return render(request, 'home.html', {'myname':'choulla mohammed'})
	
def count(request):
	fulltext = request.GET['fulltext']
	splited_fulltext = fulltext.split(' ')
	dict = {}

	for word in splited_fulltext:
		if word in dict:
			dict[word] += 1
		else:
			dict[word] = 1

	sortedword = sorted(dict.items(), key=operator.itemgetter(1), reverse = True)

	return render(request, 'count.html',{'fulltext':fulltext,'fulltextlen':len(splited_fulltext),'sortedword':sortedword})


def about(request):
	sometext = 'About Us'
	return render(request, 'about.html',{'sometext':sometext})