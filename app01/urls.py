from django.urls import path
from .views import index, listing, posting, contact, post2db

urlpatterns = [
  path('', index),
  path('<int:pid>/<str:del_pass>', index),
  path('list/', listing),
  path('post/', posting),
  path('contact/', contact),
  path('post2db/', post2db),
]
