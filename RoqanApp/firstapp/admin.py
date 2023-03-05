from django.contrib import admin
from . import models


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'PhoneNumber', 'PelakNumber', 'JoinedDate')
    list_filter = ('FirstName', 'LastName', 'PhoneNumber', 'PelakNumber', 'JoinedDate')
    fields = (('FirstName', 'LastName'), ('PhoneNumber', 'PelakNumber', 'letter'), 'JoinedDate', ('RoqanMotor', 'RoqanGirbox', 'FilterRoqan', 'FilterHava', 'FilterOtaq'))
    # date_hierarchy = 'JoinedDate'
    actions_on_bottom = True
    view_on_site = True
    search_fields = ['text']
    list_display_links = ('FirstName', 'LastName', 'PhoneNumber', 'PelakNumber', 'JoinedDate')
    # ordering = ('-JoinedDate',)
    show_full_result_count = False


# @admin.register(models.Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'pub_date', 'author', 'bol')
#     list_filter = ('title', 'pub_date', 'author')
#     fields = (('title', 'text', 'pub_date', 'image'), 'author', 'bol')
#     # exclude = ('pub_date',)
#     date_hierarchy = 'pub_date'
#     actions_on_bottom = True
#     view_on_site = True
#     search_fields = ['text']
#     list_display_links = ('title', 'author', 'pub_date')
#     ordering = ('-pub_date',)
#     autocomplete_fields = ['author']
#     show_full_result_count = False


# @admin.register(models.Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'status', 'price', 'author')
#     list_filter = ('name', 'status', 'author')
#     fieldsets = (
#     ('متن مورد نظر', {'fields': ('name', 'info', 'link')}),
#     ('متن مورد نظر', {'fields': ('status', 'price', 'author')}),
#     )
#     actions_on_bottom = True
#     actions_on_top = False
#     actions_selection_counter = True
#     empty_value_display = '-ترتیب بندی بر اساس خالی-'
#     list_editable = ['status']
#     list_select_related = ['author']
#     list_per_page = 2
#     # readonly_fields = ('info',)
#     raw_id_fields = ("author",)
#     save_on_top = True
#     view_on_site = True
