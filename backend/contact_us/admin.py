from django.contrib import admin
from .models import  ContactUs,ContactUsList

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'is_read')
    search_fields = ('first_name', 'last_name', 'email_address', 'phone_number')
    list_filter = ('is_read',)
    ordering = ('-is_read',)
    actions = ['mark_as_read']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, f"{queryset.count()} contact(s) marked as read.")
        
        
        
admin.site.register(ContactUsList)