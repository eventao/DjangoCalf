from django.contrib import admin
from TestModel.models import Test, Contact

admin.site.register([Test, Contact])

