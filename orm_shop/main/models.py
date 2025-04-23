from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    brand = models.CharField('Марка', max_length=40)
    model = models.CharField('Модель', max_length=50)
    year = models.IntegerField('Год выпуска', default=2024)
    gearbox = models.CharField('Коробка передач', max_length=10, choices=GEARBOX_CHOICES)
    fuel_type = models.CharField('Тип топлива', max_length=10, choices=FUEL_TYPE_CHOICES)
    body_type = models.CharField('Тип кузова', max_length=10, choices=BODY_TYPE_CHOICES)
    drive_unit = models.CharField('Привод', max_length=10, choices=DRIVE_UNIT_CHOICES)
    volume = models.DecimalField('Объем двигателя', max_digits=4, decimal_places=1)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField('Изображение', upload_to='cars/images/')

    def __str__(self):
        return f'{self.brand} {self.model} {self.year}'


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sales')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='sales')
    sale_date = models.DateField('Дата продажи', auto_now_add=True)
    price = models.DecimalField('Цена продажи', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Продажа {self.car} клиенту {self.client} на сумму {self.price}'
