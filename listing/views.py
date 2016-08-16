
from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
from django.http import Http404
from .forms import SearchForm, SubmitForm
import datetime
def list_detail(request, listing_id):
	try:
		thislisting = Listing.objects.get(pk=listing_id)
	except Listing.DoesNotExist:
		raise Http404("Listing doesn't exist.")
	return render(request, 'listing/detail.html', {'listing': thislisting})

def get_search(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			return HttpResponse("Thanks!")
	else:
		form = SearchForm()
	return render(request, 'listing/search.html', {'form': form})

def get_submit(request):
	if request.method == 'POST':
		if request.is_valid():
			form = SubmitForm(request.POST)
		else:
			form = SubmitForm()
	else:
		form = SubmitForm()
	return render(request, 'listing/submit.html', {'form': form})

def fetch_results(request):
	if request.method == 'POST':
		searchresult=request.POST
		listings=Listing.objects.filter(subject=searchresult['subject_code']).filter(course_number=searchresult['class_number'])
		if len(listings)==0:
			return render(request, 'listing/nolistings.html')

		return render(request, 'listing/results.html', {'listings': listings})

def process_submission(request):
	if request.method == 'POST':
		submission=request.POST
		temp = Listing(title=submission['title'],pub_date=datetime.datetime.now(),email=submission['email'],price=submission['price'],body=submission['body'],subject=submission['subject'],course_number=submission['course_number'])
		temp.save()
		return render(request, 'listing/success.html')

def index(request):
	return HttpResponse("This is a list of listings.")

def home(request):
	return render(request, 'listing/home.html')
# Create your views here.
