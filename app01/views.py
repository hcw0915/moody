from django.shortcuts import render, redirect
from .models import Post, Mood
# from .forms import ContactForm, PostForm

def index(request, pid=None, del_pass=None):
  #TODO 這裡是 PostsList
  posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
  moods = Mood.objects.all()

  try:
    user_id = request.GET.get('user_id')
    user_pass = request.GET.get('user_pass')
    user_post = request.GET.get('user_post')
    user_mood = request.GET.get('mood')
  except:
    user_id = None

  #==============================================建立貼文
  if user_id and user_post:
    mood = Mood.objects.get(status=user_mood)
    post = Post.objects.create(
      mood = mood,
      nickname = user_id, 
      del_pass = user_pass, 
      message = user_post
      )
    post.save()
    message='成功儲存!請記得你的密碼[{}]!，訊息需要經過審查之後才會顯示。'.format(user_pass)

  #===============================================刪除貼文
  else:
    #* 真刪除
    # if pid and del_pass:
    #   post = Post.objects.get(id=pid)
    #   if post.del_pass == del_pass:
    #     post.delete()        
    #     message = '資料刪除成功'
    #   else:
    #     message = '密碼錯誤'

    #* 偽刪除
    if pid and del_pass:
      post = Post.objects.get(id=pid)
      if post.del_pass == del_pass:
        # post.delete()        
        post.enabled = False
        post.save()
        message = '資料刪除成功'
      else:
        message = '密碼錯誤'


  return render(request, 'index.html', locals())




# from django.views import View


# class Index(View):

#   def get(self, request, *args, **kwargs):
#     posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
#     moods = Mood.objects.all()

#     return render(request, 'index.html', locals())

#   def post(self, request, *args, **kwargs):
#     user_id = request.POST.get('user_id')
#     user_pass = request.POST.get('user_pass')
#     user_post = request.POST.get('user_post')
#     user_mood = request.POST.get('mood')

#     mood = Mood.objects.get(status=user_mood)
#     post = Post.objects.create(
#       mood = mood,
#       nickname = user_id, 
#       del_pass = user_pass, 
#       message = user_post)
#     post.save()
#     message='成功儲存!請記得你的密碼[{}]!，訊息需要經過審查之後才會顯示。'.format(user_pass)

#     return redirect('/')



#   def delete(self, request, pid=None, del_pass=None , *args, **kwargs):
#     print(pid)
#     print(del_pass)
#     if pid and del_pass:
#       post = Post.objects.get(id=pid)
#       if post.del_pass == del_pass:
#         post.delete()        
#         message = '資料刪除成功'
#       else:
#         message = '密碼錯誤'

#     return render(request, 'index.html', locals())
