
from django.urls import include
from django.contrib import admin
from django.urls import path
admin.site.site_header = "Alcheringa Admin"
admin.site.site_title = "Alcheringa Admin Portal"
admin.site.index_title = "Welcome to Alcheringa Portal"
urlpatterns = [
    path('', admin.site.urls),
    path('auth/' ,include('authentication.urls'))
]
