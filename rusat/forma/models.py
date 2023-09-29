from django.db import models

class Forma(models.Model):

    GROUPS = (
        ('ИВТ','ИВТ'),
        ('ИТСС','ИТСС'),
        ('КБ','КБ'),
        ('ПМ','ПМ'),
        ('ИБ','ИБ'),
        ('Другое','Другое'),
        (None,'Направление подготовки не выбрано'),
    )


    surname = models.CharField('Фамилия', max_length=50, blank=True)
    name = models.CharField('Имя', max_length=50, blank=True)
    patronymic = models.CharField('Отчество', max_length=50, blank=True)
    finish_year = models.CharField('Код окончания МИЭМ', max_length=4, blank=True)
    op = models.CharField('ОП', max_length=6, choices=GROUPS, blank=True)
    yearrusa = models.CharField('Год', max_length=50, blank=True)
    photo = models.FileField('Фото в Рузе', upload_to='photorusa/', blank=False, null=True)
    job_name = models.CharField('Ваше место работы', max_length=100, blank=True)
    job_status = models.CharField('Занимаемая должность в организации, компании', max_length=50, blank=True)
    phone = models.CharField('Телефон', max_length=20, blank=True)
    mail = models.EmailField('Электронная почта', max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма'
