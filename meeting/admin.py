from django.contrib import admin  
from meeting.models import User

class UserAdmin(admin.ModelAdmin):
  list_display = ('name', 'gender', 'user_id', 'chance','phone_num', 'candidate_num', 'candidate_now', 'arranger_now', 'fb_email')
  search_fields = ('user', )

admin.site.register(User, UserAdmin)

"""
from books.models import Publisher, Author, Book  
admin.site.register(Publisher)  
admin.site.register(Author, AuthorAdmin)  
admin.site.register(Book, BookAdmin) 
"""