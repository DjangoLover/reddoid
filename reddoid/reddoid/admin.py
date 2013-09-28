from django.contrib import admin
from sources.models import Source, SourcesList


class SourceAdmin(admin.ModelAdmin):
    pass


class SourcesListAdmin(admin.ModelAdmin):
    pass


admin.site.register(Source, SourceAdmin)
admin.site.register(SourcesList, SourcesListAdmin)
