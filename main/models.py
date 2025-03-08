from django.db import models

# Create your models here.
class Main(models.Model):
    site_name = models.CharField(verbose_name="Имя сайта", max_length=50)
    logo = models.ImageField(verbose_name="Логотип сайта", upload_to='logo/')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'



class AboutUs(models.Model):
    photo = models.ImageField(upload_to='about_phoio/')
    description = models.TextField("Описание")
    year_in_business = models.IntegerField("Сколько лет мы в бизнесе")
    happy_people = models.IntegerField("Счастливые люди")
    sales = models.IntegerField("Продажи")
    award_winning = models.IntegerField("Награды")

    def __str__(self):
        return self.description


    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class Team(models.Model):
    photo = models.ImageField(verbose_name="Фотография", upload_to='team_photo/')
    name = models.CharField("Имя", max_length=50)
    job_title = models.CharField( "Должность", max_length=100)
    instagram = models.URLField('Инстаграм')
    facebook = models.URLField("Фейсбук")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Сотрудник"


class Blog(models.Model):
    title = models.CharField("Заголовок", max_length=300)
    photo = models.ImageField('Фото', upload_to='blog_photo/')
    description = models.TextField("Оисание")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject



class ContactUS(models.Model):
    location = models.CharField("Локация", max_length=11)
    phone = models.IntegerField("Телефон")
    email_info = models.EmailField("Инфо почта")
    email = models.EmailField("Почта")


    def __str__(self):
        return self.location

    class Meta:
        verbose_name = "Поддержка"
        verbose_name_plural = "Поддержка"