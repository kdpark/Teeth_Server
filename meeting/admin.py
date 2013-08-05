from django.contrib import admin  
from meeting.models import User

#class UserAdmin(admin.ModelAdmin):
	#fields = ('name', 'password', 'email')

admin.site.register(User)

"""
from books.models import Publisher, Author, Book  
admin.site.register(Publisher)  
admin.site.register(Author, AuthorAdmin)  
admin.site.register(Book, BookAdmin) 
"""