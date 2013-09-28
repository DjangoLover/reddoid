from django.contrib import admin
from sources.models import Source, SourcesList, Post


class SourceAdmin(admin.ModelAdmin):
    pass


class SourcesListAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Source, SourceAdmin)
admin.site.register(SourcesList, SourcesListAdmin)
admin.site.register(Post, PostAdmin)
