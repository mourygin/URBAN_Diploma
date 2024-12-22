from django.db import models


class Category(models.Model):
    # Класс категории игрушек
    cat_name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.cat_name


class Action(models.Model):
    # Класс акций (скидки, подарки...).
    title = models.CharField(max_length=128, null=False, blank=False)
    text = models.TextField()
    first_date = models.DateField()
    last_date = models.DateField()
    picture_fn = models.CharField(max_length=256)
    published = models.BooleanField(default=False)
    presents = models.BooleanField(default=False)
    discont = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        null=True,
        default=0)
    actual = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Toy(models.Model):
    # Класс игрушек.
    title = models.CharField(max_length=100, null=False, blank=False)
    articul = models.CharField(max_length=10, null=False, blank=False)
    cost = models.DecimalField(decimal_places=2, max_digits=7, null=True)
    actual_cost = models.DecimalField(
        decimal_places=2, max_digits=7, null=True)
    weight = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    description = models.CharField(max_length=1024, null=True, blank=True)
    in_stock = models.IntegerField()
    picture_min = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default='')
    picture_max = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default='')
    toy_cat = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Buyer(models.Model):
    # Класс покупателея.
    name = models.CharField(max_length=100,)
    balance = models.DecimalField(decimal_places=2, max_digits=11)
    age = models.IntegerField()
    psw = models.CharField(max_length=100, default='')
    phone_nr = models.CharField(max_length=16, default='')
    address = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.name


class Basket(models.Model):
    # Класс корзины покупателя.
    buyer_id = models.ForeignKey(Buyer, on_delete=models.PROTECT)
    toy_id = models.ForeignKey(Toy, on_delete=models.PROTECT)
    toy_name = models.CharField(max_length=64, default='')
    toy_descr = models.CharField(max_length=128, default='')
