from django.contrib import admin
from .models import Mood, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
  list_display = ('nickname','message','enabled', 'pub_time','mood', 'del_pass')
  # ordering = ['-pub_time']  #! 可以
  # ordering = ('-pub_time')  #! 不可以
  ordering = ('-pub_time',) #! 可以


admin.site.register(Mood)
admin.site.register(Post,PostAdmin)