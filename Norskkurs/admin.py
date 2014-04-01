from django.contrib import admin
from Norskkurs.models import Elev
from Norskkurs.models import Fravar
from Norskkurs.models import Kurs
from Norskkurs.models import Larer
from Norskkurs.models import KursInstance
from Norskkurs.models import ElevAdmin
from Norskkurs.models import Norsk_vedtak


admin.site.register(Fravar)
admin.site.register(Kurs)
admin.site.register(Larer)
admin.site.register(KursInstance)
admin.site.register(Elev, ElevAdmin)

