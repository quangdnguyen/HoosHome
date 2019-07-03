from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, ListView
from .forms import SignUpForm, SearchForm, ListingForm
from .models import Listing
from django.shortcuts import get_object_or_404
from django.utils import timezone


class ListingList(ListView):
    template_name = 'home/index.html'
    context_object_name = 'all_listings'

    def get_queryset(self):
        """Returns recently published listings."""
        return Listing.objects.all()


class ListingListFilter(ListView):
    template_name = 'home/listing_filter.html'
    context_object_name = 'all_listings'

    def get_queryset(self):
        """Returns recently published listings."""
        return Listing.objects.all()


def search(request):
    if request.method == 'POST':
        key = request.POST['keyword']
        beds = request.POST.get('beds',False)
        baths = request.POST.get('baths',False)
        if key == "" and beds == "Number of Bedrooms" and baths == "Number of Bathrooms":
            return render(request, "home/search_results.html" )
        status = Listing.objects.filter(address__icontains=(key))
        if beds == "1 bed":
            status = status.filter(beds=1)
        elif beds == "2 beds":
            status = status.filter(beds=2)
        elif beds == "3 beds":
            status = status.filter(beds=3)
        elif beds == "3+ beds":
            status = status.filter(beds__gte=3)
        if baths == "1 bath":
            status = status.filter(baths=1)
        elif baths == "2 baths":
            status = status.filter(baths=2)
        elif baths == "3 baths":
            status = status.filter(baths=3)
        elif baths == "3+ baths":
            status = status.filter(baths__gte=3)

        return render(request, "home/search_results.html", {"buy": status})
    else:
        return render(request, "home/search_results.html")

def individual(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    if request.method == "POST":
        input = request.POST['input']
        rating = int(request.POST['rating'])
        if input == "" or input == None:
            return render(request, "home/listing_individual.html", {"listing": listing})

        listing.total_ratings += rating
        listing.number_of_ratings += 1
        listing.ratings = round(int(listing.total_ratings) / int(listing.number_of_ratings),2)
        print(rating)
        print(listing.number_of_ratings)

        temp_list = listing.get_review()
        temp_list.append(input)
        listing.set_review(temp_list)

        temp_list2 = listing.get_reviewer()
        temp_list2.append(request.user.username)
        #print(temp_list2)
        listing.set_reviewer(temp_list2)

        listing.save()

    return render(request, "home/listing_individual.html", {"listing": listing})

def home(request):
    if request.method == 'POST':
        key = request.POST['keyword']
        beds = request.POST.get('beds',False)
        baths = request.POST.get('baths',False)
        if key == "" and beds == "Number of Bedrooms" and baths == "Number of Bathrooms":
            return render(request, "home.html" )
        status = Listing.objects.filter(address__icontains=(key))
        if beds == "1 Bed":
            status = status.filter(beds=1)
        elif beds == "2 Beds":
            status = status.filter(beds=2)
        elif beds == "3 Beds":
            status = status.filter(beds=3)
        elif beds == "3+ Beds":
            status = status.filter(beds__gte=3)

        if baths == "1 Bath":
            status = status.filter(baths=1)
        elif baths == "2 Baths":
            status = status.filter(baths=2)
        elif baths == "3 Baths":
            status = status.filter(baths=3)
        elif baths == "3+ Baths":
            status = status.filter(baths__gte=3)

        return render(request,"home/listing_filter.html", {"all_listings": status})
    else:
        return render(request, "home.html")



def gitlink(request):
    link = redirect('https://github.com/UVA-CS3240-S19/project-102-nautilus')
    return link

def ListingCreateView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        temp = []
        if form["gym"].data == True:
            temp.append(0)
        if form["parking"].data == True:
            temp.append(1)
        if form["wifi"].data == True:
            temp.append(2)
        if form["heating"].data == True:
            temp.append(3)
        if form["furnished"].data == True:
            temp.append(4)
        if form["lounge"].data == True:
            temp.append(5)
        if form["laundry"].data == True:
            temp.append(6)
        if form["pets"].data == True:
            temp.append(7)
        if form["AC"].data == True:
            temp.append(8)
        if form["business_center"].data == True:
            temp.append(9)

        print(form["beds"].data)

        if form.is_valid():
            object = form.save()
            object.pub_date = timezone.now()
            object.beds = form["beds"].data
            object.baths = form["baths"].data
            object.set_features(temp)
            object.save()
            return redirect('/buy')
    else:
        form = ListingForm()
    return render(request, 'home/listing_form.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
