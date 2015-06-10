from django.contrib import admin

# Register your models here.
from .models import Join

#this adds customization to the model
class JoinAdmin(admin.ModelAdmin):
	list_display= ['__unicode__', 'email', 'timestamp', 'updated']
	class Meta:
		model = Join

admin.site.register(Join, JoinAdmin)