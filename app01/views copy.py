from django.shortcuts import render
from .models import Post, Mood
from .forms import ContactForm, PostForm

# Create your views here.

# pid=None, del_pass=None 針對兩變數實施"預設值設定"避免報錯 => 若無傳入則為 None
def index(request, pid=None, del_pass=None): 

  # 這裡跟 listing 一樣功能 
  # 篩選 Post裡 啟用(enabled=True)，然後以建立時間(-pub_time)進行降冪排列(-order_by)，[:30]表示顯示 前30筆資料 (0-29)
  # 指定 moods 為物件 => <QuerySet [<Mood: 開心>, <Mood: 難過>]>
  # TODO 此欄位為 LIST => 列出所有已啟用(enabled = True)的資料 
  posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30] 
  moods = Mood.objects.all()
  
  ''' 這一串可以往下移到 Create 的地方
  try: # 從 form ( method='GET')表單中拿取提交後資料(名稱連接 form裡的 input的 name),
    user_id = request.GET.get('user_id')
    user_pass = request.GET.get('user_pass')
    user_post = request.GET.get('user_post')
    user_mood = request.GET.get('mood')
  except:
    user_id = None
    message = '如果要張貼訊息則每一個欄位都要填...'
  '''
  # TODO 此欄位為 DELETE - 刪除貼文 ( JavaScript做 刪除鈕按鍵導向，導到 index這裡做刪除驗證 )
  #! 此地方的值來自於 base.html JavaScript的 var usr = '/' + id + '/' + user_pass 傳值到 urls.
  #! 因為是共用同一個 views.index 所以一旦 del_pass, pid 有值，就會傳入 urls 執行 刪除段，沒有值就會傳入預設值 None
  #! 然後直接不執行 if del_pass and pid ( None 屬於 False )，直接跳到 posting功能
  if del_pass and pid :
    try:
      # 確認密碼及ID後則先找到對應的 pid物件
      post = Post.objects.get(id=pid)
      # 如果沒有找到對應 pid物件則指定 post為空
    except:
      post = None
    # 如果 post 確認有值(非 None)則為 True
    if post:
      # 張貼/刪除碼 在這裡驗證(validation)
      # 確認填寫的刪除碼跟資料庫的一樣就過
      if post.del_pass == del_pass:
        post.delete()
        message = '資料刪除成功'
      else:
        message = '密碼錯誤'

  # TODO 此欄位為 CREATE - 建立貼文後，資料裡 enable = False => 要管理員手動開啟後 改成 True => 所以提示才會說需要管理員審核
  # 這裡跟 posting 一樣功能 
  # 如果 暱稱 user_id有值(不等於none)，則建立一個新的資料
  try: # 從 form ( method='GET')表單中拿取提交後資料(名稱連接 form裡的 input的 name),
    user_id = request.GET.get('user_id')
    user_pass = request.GET.get('user_pass')
    user_post = request.GET.get('user_post')
    user_mood = request.GET.get('mood')
  except:
    user_id = None
    message = '如果要張貼訊息則每一個欄位都要填...'

  if user_id != None:
    mood = Mood.objects.get(status=user_mood)
    post = Post.objects.create(
      mood=mood,
      nickname=user_id, 
      del_pass=user_pass, 
      message=user_post
      )
    post.save()
    message='成功儲存!請記得你的密碼[{}]!，訊息需要經過審查之後才會顯示。'.format(user_pass)
  return render(request, 'index.html', locals())



# ==================================================== 以下都沒用到

# 所以這個沒用到
def listing(request):
  posts = Post.objects.all().order_by('-pub_time')[:150]
  moods = Mood.objects.all()
  return render(request, 'listing.html', locals())

# 所以這個沒用到 (內容跟 index裡面的一樣)
def posting(request):
  moods = Mood.objects.all()
  try:
    user_id = request.POST.get('user_id')
    user_pass = request.POST.get('user_pass')
    user_post = request.POST.get('user_post')
    user_mood = request.POST.get('user_mood')
  except:
    user_id = None
    message = '如果要張貼訊息，則每一個欄位都要填寫'
  if user_id is not None:
    mood = Mood.objects.get(status=user_id)
    #! mood = models.Mood.objects.get(status=user_id) -> teacher's
    post = Post.objects.create(
      mood=mood,
      nickname=user_id,
      del_pass=user_pass,
      message=user_post
      )
    post.save()
    message='成功儲存!請記得你的密碼[{}]!'.format(user_pass)

  return render(request, 'posting.html', locals())


# 這個根本沒建立 ContactForm
def contact(request):
  if request.method == 'POST':
    form = ContactForm(data = request.POST)
    if form.is_valid():
      user_id = form.cleaned_data.get('user_id')
      user_name = form.cleaned_data.get('user_name')
      user_city = form.cleaned_data.get('user_city')
      user_email = form.cleaned_data.get('user_email')
      user_message = form.cleaned_data.get('user_message')
    else:
      form = ContactForm()
    return render(request, 'contact.html', locals())

# 這個沒用到(只是把 request.method改成POST => 這裡要用 POST，那 html裡的 form裡的 method也要改)
def post2db(request):
  if request.method == 'POST':
    post_form = PostForm(data = request.POST)
    if post_form.is_valid():
      message = '你的訊息已儲存，要等管理者啟用後才看的到。'
      post_form.save()
    else:
      message = '如要張貼訊息則每一個欄位都要填...'
  else:
    post_form = PostForm()
    message = '如要張貼訊息則每一個欄位都要填...'

  return render(request, 'post2db.html', locals())
