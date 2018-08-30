# From inside your project's urls.py file
from django.conf.urls import url, include
from django.contrib import admin
  # THIS SECTION IS NEW!
  # ********************
from apps.awesomeApp.models import User as U, Fruit, Donut, Group
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
    url(r'^admin/',admin.site.urls),
    url(r'^awesomeApp/', include('apps.awesomeApp.urls')),
]