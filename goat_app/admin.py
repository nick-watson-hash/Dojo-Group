from django.contrib import admin

from .models import User, GOAT, Matchup, GOATdb
# admin.site.register(User)

# Register your models here.
from goat_app.models import User 
class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

from goat_app.models import GOAT
class GOATAdmin(admin.ModelAdmin):
    pass
admin.site.register(GOAT, UserAdmin)

from goat_app.models import Matchup
class MatchupAdmin(admin.ModelAdmin):
    pass
admin.site.register(Matchup, UserAdmin)

from goat_app.models import GOATdb
class GOATdbAdmin(admin.ModelAdmin):
    pass
admin.site.register(GOATdb, UserAdmin)

# Register your models here.