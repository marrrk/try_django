from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2,max_digits=10)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(null=False, default=False)

    # blank = True means the fields can be left as not necessarry
    # blank = False means the fields are required
    # blank is how the fields are shown
    # null = True means the data can be empty in the database
    # default = True means everything already in the database has been set as true

    #gets a url of the current model
    def get_absolute_url(self):
        # return f'/products/{self.id}'     # allows for dynamic routing. ie adding link to your stuff
        # now we want to make the function itself dynamic. we want the link to be developed based on the path name
        return reverse('products:single-product', kwargs={'my_id': self.id}) # the key in the dictionary needs to match the arguments of the function
