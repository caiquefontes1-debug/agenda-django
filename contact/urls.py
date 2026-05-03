from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
   
    path('<int:contact_id>/', view=views.contact, name='contact'),
    path('search/', view=views.search, name='search'),
    path('', view=views.index, name='index'),
]
