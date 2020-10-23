from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views



urlpatterns = [
    url(r'^$',stores_views.index,name="index"),
    url(r'^rest/$',stores_views.StoreList.as_view(),name="rest_index")
]
