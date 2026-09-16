from django.urls import path
from .views import (
    home,
    laptop_list,
    laptop_detail,
    brands,
    services,
    sell_laptop,
    about,
    contact,
)


urlpatterns = [
    path('', home, name='home'),

    path('laptops/', laptop_list, name='laptop_list'),

    path(
        'laptop/<int:pk>/',
        laptop_detail,
        name='laptop_detail'
    ),

    path(
        'brands/',
        brands,
        name='brands'
    ),

    path(
        'services/',
        services,
        name='services'
    ),
    path(
    'sell-laptop/',
    sell_laptop,
    name='sell_laptop'
),

path(
    'about/',
    about,
    name='about'
),
path(
    'contact/',
    contact,
    name='contact'
),
]