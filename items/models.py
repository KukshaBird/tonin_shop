from django.db import models
#from django.db.models import Count

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=55,verbose_name='Наименование',unique=False,null=True)
    article = models.CharField(max_length=30,verbose_name='Артикул',unique=True,null=True, editable=False)
    image = models.ImageField(upload_to='items/static/products_imgs',blank=True,null=True)
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    type = models.ForeignKey('ProductType',on_delete=models.CASCADE,verbose_name='Размер',null=True)
    fabric = models.CharField(max_length=55,verbose_name='Материал',blank=True,null=True)
    available = models.BooleanField(verbose_name='Наличие',default=True)
    description = models.TextField(verbose_name='Описание',blank=True)
    duvet_cover = models.ForeignKey('DuvetCover',on_delete=models.SET_NULL,verbose_name='Пододеяльник',null=True,blank=True)
    sheet = models.ForeignKey('Sheet',on_delete=models.SET_NULL,verbose_name='Простынь',null=True,blank=True)
    pillowcase = models.ForeignKey('Pillowcase',on_delete=models.SET_NULL,verbose_name='Подушка',null=True,blank=True)
    create_date = models.DateTimeField(auto_now=True,null=True)


    def __str__(self):
        return '{}, {}'.format(self.name, self.type)

    def save(self,*args,**kwargs):
        super(Product, self).save(*args, **kwargs)
        if not self.sheet_id:
            if self.type_id == 1: self.sheet_id = 1
            else: self.sheet_id = 2
        if not self.duvet_cover_id:
            if self.type_id == 1: self.duvet_cover_id = 1
            elif self.type_id == 2: self.duvet_cover_id = 3
            elif self.type_id == 3: self.duvet_cover_id = 2
            elif self.type_id == 4: self.duvet_cover_id = 4
        if not self.pillowcase_id: self.pillowcase_id = 1
        article = 'BLS' + str(self.type.id) + str(self.id)
        self.article = article
        super(Product, self).save(*args, **kwargs)

    def get_img_pass(self):
        try:
            img_pass = self.image.url.split('/')
        except:
            img_pass = ''
        result = ''
        for x in img_pass[-2:]:
            result += x + '/'
        return result[:-1]


class ProductType(models.Model):
    TYPE_SIZE_CHOICES = [
        ('OH', 'Полуторный'),
        ('DB', 'Двуспальный'),
        ('EU', 'Евро'),
        ('FM', 'Семейный')
    ]

    type = models.CharField(
                choices=TYPE_SIZE_CHOICES,
                max_length=2,
                default='OH',
            )

    def __str__(self):
        return self.get_type_display()

class Complectation(models.Model):
        amount = models.PositiveSmallIntegerField()
        size = models.CharField(max_length=30)

        def __str__(self):
            return self.size + ' ' + str(self.amount)

        class Meta:
            abstract = True

class DuvetCover(Complectation):
    class Meta:
        db_table = 'duvet_cover'

class Sheet(Complectation):
    class Meta:
        db_table = 'sheet'

class Pillowcase(Complectation):
    class Meta:
        db_table = 'pillowcase'

#TOWELS
class Towel(models.Model):
    name = models.CharField(max_length=55,verbose_name='Наименование',unique=False,null=True)
    size = models.CharField(max_length=55,verbose_name='Размер',null=True,blank=True)
    article = models.CharField(max_length=30,verbose_name='Артикул',unique=True,null=True, editable=False)
    image = models.ImageField(upload_to='items/static/products_imgs',blank=True,null=True)
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    fabric = models.CharField(max_length=55,verbose_name='Материал',blank=True,null=True)
    available = models.BooleanField(verbose_name='Наличие',default=True)
    description = models.TextField(verbose_name='Описание',blank=True)
    create_date = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return '{}, {}'.format(self.name, self.size)

    def save(self,*args,**kwargs):
        super(Towel, self).save(*args, **kwargs)
        article = 'TOW' + str(self.id)
        self.article = article
        super(Towel, self).save(*args, **kwargs)

    def get_img_pass(self):
        try:
            img_pass = self.image.url.split('/')
        except:
            img_pass = ''
        result = ''
        for x in img_pass[-2:]:
            result += x + '/'
        return result[:-1]

