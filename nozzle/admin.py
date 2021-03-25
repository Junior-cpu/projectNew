from django.contrib import admin
from .models import Nozzle
from .models import Magazine
from .models import Maquina
from .models import Machine
from .models import Location
from .models import Linha

admin.site.register(Nozzle)
admin.site.register(Magazine)
admin.site.register(Maquina)
admin.site.register(Machine)
admin.site.register(Location)
admin.site.register(Linha)
# Register your models here.
