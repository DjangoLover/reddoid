from django.contrib import admin

from entities.models import Link, LinkPost, Image, ImagePost

from sources.models import Source, SourcesList, Post


class LinkAdmin(admin.ModelAdmin):
    pass


class LinkPostAdmin(admin.ModelAdmin):
    pass


class ImageAdmin(admin.ModelAdmin):
    pass


class ImagePostAdmin(admin.ModelAdmin):
    pass


class SourceAdmin(admin.ModelAdmin):
    pass


class SourcesListAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Link, LinkAdmin)
admin.site.register(LinkPost, LinkPostAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(ImagePost, ImagePostAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(SourcesList, SourcesListAdmin)
admin.site.register(Post, PostAdmin)
