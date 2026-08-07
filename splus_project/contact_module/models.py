from django.db import models

class ContactsUs(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    full_name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    message = models.TextField(max_length=350, verbose_name='متن پیام')
    created_at = models.DateTimeField(auto_now_add=True)
    response = models.TextField(max_length=350, verbose_name='پاسخ ادمین')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده/نشده')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.title
