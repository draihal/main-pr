from django.db import models
from django.core.validators import validate_image_file_extension


class Course(models.Model):
    name = models.CharField('Название курса', max_length=150, )
    slug = models.SlugField('Slug для url', max_length=150, unique=True,)
    category = models.ForeignKey(
        'pages.CourseCategory', on_delete=models.CASCADE, verbose_name='Категория курса')

    def upload_image_dir(self, filename):
        return f'site/courses/{filename.lower()}'

    image = models.ImageField(
        'Изображение для курса',
        upload_to=upload_image_dir,
        blank=True,
        validators=[validate_image_file_extension])  # TODO hash

    description = models.TextField('Что даст этот курс', )
    necessary_knowledge = models.TextField('Необходимые знания', )
    study_process = models.TextField('Процесс обучения', )
    graduation_project = models.TextField('Выпускной проект', )
    after_training = models.TextField('После обучения', )
    certificate_sample = models.ImageField(
        'Образец сертификата',
        upload_to=upload_image_dir,
        blank=True,
        validators=[validate_image_file_extension])  # TODO hash
    # program_details =  # TODO

    class Meta:
        ordering = ('name',)
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'{self.name}'
