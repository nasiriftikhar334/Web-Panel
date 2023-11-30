from django.contrib import admin
from django.contrib.auth.models import User
from .models import Registration, Dependent

class DependentInline(admin.TabularInline):
    model = Dependent
    extra = 1

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'occupation', 'passport_number', 'visa_status')
    list_filter = ('occupation', 'visa_status')
    search_fields = ('user__username', 'name', 'passport_number', 'visa_status')
    inlines = [DependentInline]

    # Custom admin actions
    actions = ['approve_registration', 'reject_registration', 'suspend_membership']

    def approve_registration(self, request, queryset):
        # Logic to approve registration
        pass

    def reject_registration(self, request, queryset):
        # Logic to reject registration
        pass

    def suspend_membership(self, request, queryset):
        # Logic to suspend membership
        pass

class DependentAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'occupation', 'visa_status')
    list_filter = ('occupation', 'visa_status')
    search_fields = ('user__username', 'nationality', 'visa_status')

# class AttachmentAdmin(admin.ModelAdmin):
#     list_display = ('attachment1', 'attachment2', 'attachment3', 'attachment4')

# Register the models and admins
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Dependent, DependentAdmin)
# admin.site.register(Attachment, AttachmentAdmin)

# Other admin customizations
admin.site.unregister(User)  # Unregister the User model to prevent accidental edits

# Additional admin customization for user management (username and password)
from django.contrib.auth.admin import UserAdmin
admin.site.register(User, UserAdmin)
