from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import localtime, strftime
# import datetime

# Create your views here.
def root(request):
	return redirect('/time_display')

def time_display(request):
	# now = datetime.datetime.now()
	context = {
		"title": "Date and Time",
		"day": strftime("%A", localtime()),
		"date": strftime("%B %d, %Y", localtime()),
		"time": strftime("%I:%M %p", localtime()),
		"zone": strftime("%Z", localtime())
		# "day": now.strftime("%A"),
		# "date": now.strftime("%B %d, %Y"),
		# "time": now.strftime("%I:%M %p")
	}
	return render(request, "index.html", context)