from django.db import models
from order.models import Order


class Dish(models.Model):
    order = models.ForeignKey(Order)
    name = models.TextField(max_length=200)
    price = models.FloatField(default=0.0)
    qty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'{} {} {}'.format(self.name, self.price, self.qty)


class Ingredient(models.Model):
    '''
    Some spicy thing
    '''
    item_no = models.IntegerField()
    item_description = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)

    def __unicode__(self):
        return u'code: {}, desciption: {}, price: {}'.format(self.item_no, self.item_description, self.price)


class Meat(models.Model):
    '''
    Pork, Cow
    '''
    item_no = models.IntegerField()
    item_description = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)

    def __unicode__(self):
        return u'code: {}, desciption: {}, price: {}'.format(self.item_no, self.item_description, self.price)


class BaseDish(models.Model):
    '''
    Rice or Noodle
    '''
    item_no = models.IntegerField()
    item_description = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)

    def __unicode__(self):
        return u'code: {}, desciption: {}, price: {}'.format(self.item_no, self.item_description, self.price)


class CookingMethod(models.Model):
    '''
    Boil or Fried
    '''
    item_no = models.IntegerField()
    item_description = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)

    def __unicode__(self):
        return u'code: {}, desciption: {}, price: {}'.format(self.item_no, self.item_description, self.price)


class Additional(models.Model):
    '''
    Egg or other
    '''
    item_no = models.IntegerField()
    item_description = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)

    def __unicode__(self):
        return u'code: {}, desciption: {}, price: {}'.format(self.item_no, self.item_description, self.price)