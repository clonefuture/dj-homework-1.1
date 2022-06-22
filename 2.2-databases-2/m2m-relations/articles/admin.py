from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class TopicInlineFormset(BaseInlineFormSet):
    def clean(self):
        list_scope = [form.cleaned_data.get('is_main') for form in self.forms]
        if list_scope.count(True) == 1:
            return super().clean()
        else:
            raise ValidationError('Укажите основной раздел, основным может быть только один раздел')


class TopicInline(admin.TabularInline):
    model = Scope
    formset = TopicInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TopicInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

