from django.urls import path
from .views import index
# from .views import Index


urlpatterns = [
  path('', index),
  # 這是給刪除功能
  path('<int:pid>/<str:del_pass>', index),

  # path('', Index.as_view(), name="Index"),
  # path('<int:pid>/<str:del_pass>', Index.as_view()),



  # 實際只是把 index 裡的功能分離出來 => 發布貼文、列表、
  # path('list/', listing),
  # path('post/', posting),
  # path('post2db/', post2db),

  # 恩?? 好像沒這個東西
  # path('contact/', contact),

]
