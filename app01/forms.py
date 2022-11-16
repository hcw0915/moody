from django import forms
from .models import Post


class ContactForm(forms.Form):
  CITY = [
      ['TP', 'Taipei'],
      ['TY', 'Taoyuang'],
      ['TC', 'Taichung'],
      ['TN', 'Tainan'],
      ['KS', 'Kaohsiung'],
      ['NA', 'Others'],
    ]
  user_name = forms.CharField(label='你的姓名', max_length=50, initial="陳時中")
  user_city = forms.ChoiceField(label='居住城市')
  user_school = forms.BooleanField(label='是否在學', required=False)
  user_email = forms.EmailField(label="電子郵件")
  user_message = forms.CharField(label='你的意見', widget=forms.Textarea)


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['mood', 'nickname', 'message', 'del_pass']
    # ! 跟下面差在哪????
    labels = {
      'mood':'現在心情',
      'nickname':'你的暱稱',
      'message':'心情留言',
      'del_pass':'設定密碼'
    }
  # def __init__(self, *args, **kwargs):
  #   # super(PostForm, self).__init__(*args, **kwargs) # python2
  #   super().__init__(*args, **kwargs) # python3 以上
  #   self.fields['mood'].label = '現在心情'
  #   self.fields['nickname'].label = '你的暱稱'
  #   self.fields['message'].label = '心情留言'
  #   self.fields['del_pass'].label = '設定密碼'