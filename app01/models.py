from django.db import models

# Create your models here.
class Mood(models.Model):
  status = models.CharField(max_length=10, null=False)
  # 這是儲存圖片的路徑
  pic_path = models.CharField(max_length=50, null=True)

  def __str__(self):
    return self.status

class Post(models.Model):
  mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
  nickname = models.CharField(max_length=10, default='不願意透漏身分的人')
  message = models.TextField(null=False)
  del_pass = models.CharField(max_length=10)
  pub_time = models.DateTimeField(auto_now=True)
  enabled = models.BooleanField(default=False)
  '''心情(mood)與狀態(status)連動 foreignkey
  心情、小名、訊息、刪除用密碼、建立時間、啟用(布林)
  '''

  def __str__(self):
    return self.message