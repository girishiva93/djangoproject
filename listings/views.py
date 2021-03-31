from django.shortcuts import get_object_or_404,render
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .choices import price_choices,bedroom_choices,state_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) # filter kina gareko bane yedi hami lay unpublished gareko balama data haru website ma ne nadakhawos banera #order by kina gareko vane hamle rakheko kura haru tei time ko anuasr aawos banera # calling the data from database
    paginator = Paginator(listings, 6) # yesma tei kati ota list haru dakhaune vanne kura vako xa
    page = request.GET.get('page') # aarko page ma jana page ko link change garna lai use gareko ho 
    paged_listings = paginator.get_page(page) # yes ma tei kun link ho banera verify gareko xam 
    context = {
        'listings' : paged_listings
    } # calling the data from database 
    return render(request, 'listings/listings.html', context)

def listing(request,listing_id): 
    listing = get_object_or_404(Listing,pk=listing_id) # yesma yedi id vanda aaru values haru halo vani page not found vana vaneko xa

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html',context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    #keyword - yesma tei description search garna ko lagi use gareko ho
    if 'keyword' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords) # icontains lay k baneko xa vane, description ma vako data haru sabai aauw baneko xa

    # city (search code city ko lagi)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city) # iexact tei case sensitive hudaina

    # state (search code city ko lagi)
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state) # iexact tei case sensitive hudaina

    # bedroom (search code city ko lagi)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) # lte vaneko tei yedi user lay 4 press garyo vani 1 to 4 samba sabai data dakhau vaneko ho
    
    # price (search code city ko lagi)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price) # lte vaneko tei yedi user lay 4 press garyo vani 1 to 4 samba sabai data dakhau vaneko ho

    context = {
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
        'listings': queryset_list,
        'values' : request.GET, # yo tei yedi user lay data haru halera search garxa vani tei data search.htmk ma ne aauw banera ho
    }
    return render(request, 'listings/search.html',context)

