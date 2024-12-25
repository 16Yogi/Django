from django.contrib import admin
from .models import lessions,lessionReview,Store,lessionCertificate
# Register the Lessions model
class lessionReviewAdmin(admin.TabularInline):
    model = lessionReview
    extra = 2

class lessionVerietyAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added')
    inlines = [lessionReviewAdmin]

class storeAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('lession_list',)

class lessionCertificateAdmin(admin.ModelAdmin):
    list_display = ('lession','certificate_number')

admin.site.register(lessions,lessionVerietyAdmin)
admin.site.register(Store,storeAdmin)
admin.site.register(lessionCertificate,lessionCertificateAdmin)

# admin.site.register(lessions)
