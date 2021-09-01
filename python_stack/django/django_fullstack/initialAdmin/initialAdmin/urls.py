# From inside your project's urls.py file
  from django.urls import path, include
  from django.contrib import admin
  # THIS SECTION IS NEW!
  # ********************
  from awesomeApp.models import User as U, Fruit, Donut, Group
  class UAdmin(admin.ModelAdmin):
      pass
  admin.site.register(U, UAdmin)
  class FruitAdmin(admin.ModelAdmin):
      pass
  admin.site.register(Fruit, FruitAdmin)
  class DonutAdmin(admin.ModelAdmin):
      pass
  admin.site.register(Donut, DonutAdmin)
  class GroupAdmin(admin.ModelAdmin):
      pass
  admin.site.register(Group, GroupAdmin)
  # ****************
  urlpatterns = [
  # Your app's urls is lined to the project
      path('admin/',admin.site.urls),
      path('awesomeApp/', include('awesomeApp.urls')),
      ]
