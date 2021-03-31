from django.contrib import admin
from.models import Listing

# here i have show the id title in the listing page so that users can read the data in details
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_links = ('id','title') #when user click on title or id then user can go inside the page
    list_filter = ('realtor',) # here showing the little icon for realtor
    list_editable = ('is_published',) # from the listing page the user can published or unpublished
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price',)
    list_per_page = 25


admin.site.register(Listing,ListingAdmin)
