from django.contrib import admin
from .models import Post, Category, SiteDetail, Ability
from django.contrib.sites.models import Site
from django_summernote.admin import SummernoteModelAdmin
from django.utils.safestring import mark_safe


class SiteDetailInline(admin.StackedInline):
    model = SiteDetail


class SiteAdmin(admin.ModelAdmin):
    inlines = [SiteDetailInline]


admin.site.unregister(Site)
admin.site.register(Site, SiteAdmin)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('id', 'thumbnail_preview',
                    'title', 'tag_list', 'is_public')
    list_display_links = ('id', 'title')

    def thumbnail_preview(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.thumbnail.url))
    thumbnail_preview.short_description = 'サムネ'

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


class AbilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview',
                    'name', 'description')
    list_display_links = ('id', 'image_preview', 'name')
    save_as = True

    def image_preview(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.image.url))
    image_preview.short_description = 'サムネ'


admin.site.register(Post, PostAdmin)
admin.site.register(Ability, AbilityAdmin)
admin.site.register(Category)
