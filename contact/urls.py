#type: ignore
from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', view=views.index, name='index'),
    path('search/', view=views.search, name='search'),

    # contacts (CRUD)
    path('contact/<int:contact_id>/detail', view=views.contact_view, name='contact'),
    path('contact/create/', view=views.create, name='create'),
    path('contact/<int:contact_id>/update/', view=views.update, name='update'),
]
