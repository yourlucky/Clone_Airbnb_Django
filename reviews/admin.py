from django.contrib import admin
from .models import Review

class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "potato"

    def lookups(self,request,model_admin): 
        return [
            ("good","Good"),
            ("greate","Great"),
            ("awesom","Awesome"),
        ]
    def queryset(self,request,reviews):
        word = self.value()
        return reviews.filter(payload__contains=word)



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
