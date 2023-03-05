from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    FirstName = models.CharField('نام', blank=False, max_length=100)
    LastName = models.CharField('نام خانوادگی', blank=False, max_length=100)
    PhoneNumber = models.IntegerField('تلفن همراه', blank=True, null=False, default='09')
    PelakNumber = models.IntegerField('شماره پلاک', blank=True, null=False, default='100')
    JoinedDate = models.DateField('تاریخ بازرسی', null=False, blank=False)
    RoqanMotor = models.BooleanField('روغن موتور', default=False)
    RoqanGirbox = models.BooleanField('روغن گیربوکس', default=False)
    FilterRoqan = models.BooleanField('فیلتر روغن', default=False)
    FilterHava = models.BooleanField('فیلتر هوا', default=False)
    FilterOtaq = models.BooleanField('فیلتر اتاق', default=False)
    LETTER = (
        ('a', 'الف'),
        ('b', 'ب'),
        ('p', 'پ'))
    letter = models.CharField('سری', max_length=1, choices=LETTER, blank=False, default='a')
    
    class Meta:
        ordering = ["JoinedDate"]
        verbose_name_plural = "مشتری ها"
        permissions = (( 'can_mark_returned', 'set book as returned' ),)
    
    def __str__(self):
        return self.FirstName
    
    def get_absolute_url(self):
        return "/"


# class Post(models.Model):
#     author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     title = models.CharField('موضوع', blank=False, max_length=100, help_text="این یک متن راهنما برای موضوع است")
#     text = models.TextField('متن پست', max_length=500, help_text="در کادر بالا باید متن و یا ممحتویات پستتون رو بنویسید")
#     pub_date = models.DateField('تاریخ انتشار', null=False, blank=False, help_text="تاریخ انتشار این پست را وارد کنید")
#     image = models.ImageField('تصویر پست', default='/home/mostafa/Pictures/1.png', help_text="عکس پست را آپلود کنید")
#     bol = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ["pub_date"]
#         verbose_name_plural = "پست ها"
#         permissions = (( 'can_mark_returned', 'set book as returned' ),)

#     def get_absolute_url(self):
#         return "/"


# class Product(models.Model):
#     author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     name = models.CharField('نام کالا', max_length=30, blank=False, help_text='نام کالای مورد نظر را وارد کنید')
#     info = models.CharField('درباره کالا', max_length=100, blank=False, help_text='درباره ی کالای مورد نظر توضیحاتی وارد کنید')
#     link = models.CharField('لینک خرید محصول', max_length=100, blank=False, help_text='لینک درگاه خرید محصول را وارد کنید')
#     price = models.IntegerField('قیمت', blank=True, null=False, default='100', help_text='قیمت محصول مورد نظر را وارد کنید')

#     STATUS = (
#         ('a', 'موجود'),
#         ('u', 'ناموجود'),
#         ('d', 'تخفیف'))
#     status = models.CharField('وضعیت محصول', max_length=1, choices=STATUS, blank=False, default='y', help_text='وضعیت محصول')

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ["price"]
#         verbose_name_plural = "محصولات"
#         permissions = (( 'can_mark_returned', 'set book as returned' ),)

#     #def get_absolute_url(self):
#         #return "/%i" %self.id

#     def get_absolute_url(self):
#         return "/"
