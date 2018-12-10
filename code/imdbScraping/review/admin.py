from django.contrib import admin

# Register your models here.
from review.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('url', 'movie', 'comment', 'date')


admin.site.register(Review, ReviewAdmin)
