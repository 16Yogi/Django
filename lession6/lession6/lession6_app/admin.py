from django.contrib import admin
from . models import lession6,lessionReview,Store,lessionCertificate

# Register your models here.
class lessionReviewInlineAdmin(admin.TabularInline):
    model = lessionReview
    extra = 2 

class lessionVerietyAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added')
    inlines = [lessionReviewInlineAdmin]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('lession_list',) 

class lessionCertificateAdmin(admin.ModelAdmin):
    list_display = ('lession','certificate_number') #this fileds name are store in models also

admin.site.register(lession6,lessionVerietyAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(lessionCertificate,lessionCertificateAdmin)


