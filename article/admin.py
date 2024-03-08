from django.contrib import admin
from .models import Article
# Register your models here.

@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','created_date'] #Makale ile ilgili Başlıkları Belirledik.

    search_fields = ['title'] # Arama Çubuğu ekledik.

    list_filter = ['created_date'] # admin panelinde oluşturulma tarihi süzgeci ekledik.
    class Meta:
        model = Article
