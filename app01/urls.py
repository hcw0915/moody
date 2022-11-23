from django.urls import path
from .views import index, listing, posting, contact, post2db

urlpatterns = [
  path('', index),
  
  # 這是給刪除功能
  path('<int:pid>/<str:del_pass>', index),

  # 實際只是把 index 裡的功能分離出來 => 發布貼文、列表、
  # path('list/', listing),
  # path('post/', posting),
  # path('post2db/', post2db),

  # 恩?? 好像沒這個東西
  # path('contact/', contact),

]
