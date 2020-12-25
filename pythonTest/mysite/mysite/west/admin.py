from django.contrib import admin

# from west.models import Character
from west.models import Character,Contact,Tag

# Register your models here.
# admin.site.register(Character)
# admin.site.register([Character,Contact,Tag])

'''
# self define
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)
admin.site.register([Character, Tag])
'''

'''
# spilit as two parts
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Character, Tag])
'''

#inline 
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
	# list_display = ('name','age', 'email') # list
	list_display = ('name', 'email') # list
	inlines = [TagInline]  # Inline
	search_fields = ('name',)
	fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), #css 
            'fields': ('age',),
        }]

    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Character])