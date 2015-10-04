from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	category = models.ForeignKey('self', related_name='category_group', blank=True, null=True)
	image = models.ImageField(upload_to="items")

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'categories'

class Item(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	quantity = models.IntegerField()
	image = models.ImageField(upload_to="items")
	category = models.ForeignKey(Category)
