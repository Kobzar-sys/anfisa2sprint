from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField('Название', max_length=256)
    slug = models.SlugField('Слаг', max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(
        'Порядок отображения',
        default=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField('Название', max_length=256)
    slug = models.SlugField('Слаг', max_length=64, unique=True)

    class Meta:
        verbose_name = 'Топинг'
        verbose_name_plural = 'Топинги'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Уникальное название обёртки, не более 256 символов'
    )

    class Meta:
        verbose_name = 'Обертка'
        verbose_name_plural = 'Обертки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    title = models.CharField('Название', max_length=256)
    description = models.TextField('Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
    )
    toppings = models.ManyToManyField(Topping)
    is_on_main = models.BooleanField('На главную', default=False)

    class Meta:
        verbose_name = 'Морроженное'
        verbose_name_plural = 'Морроженные'

    def __str__(self):
        return self.title
