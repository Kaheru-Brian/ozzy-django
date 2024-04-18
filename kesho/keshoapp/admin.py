from django.contrib import admin
from .models import * #from the current folde import the file called models to access the clases. we are  accessing our models upon which  we are going to build interfaces  from the admin panel/dashboard
#from .models import Categorystaty, Babe


# Register your models here.
admin.site.register(Categorystay)
admin.site.register(Babe)
admin.site.register(Pay)
