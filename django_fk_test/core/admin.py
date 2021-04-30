from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Foo, Bar


class FooModelAdmin(SimpleHistoryAdmin):
    list_display = ["name", "email", "phone"]


class BarModelAdmin(SimpleHistoryAdmin):
    list_display = ["foo", "kind", "get_value", "status"]

    actions = ["mark_changes"]

    def get_value(self, obj):
        return getattr(obj, obj.kind)

    def mark_changes(self, request, queryset):
        for obj in queryset:
            setattr(obj.foo, obj.kind, getattr(obj, obj.kind))
            obj.foo.save(update_fields=[obj.kind])

            obj.status = obj.ACCEPTED
            obj.save()

        self.message_user(request, "Ok")


admin.site.register(Foo, FooModelAdmin)
admin.site.register(Bar, BarModelAdmin)
