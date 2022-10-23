from django.contrib import admin
from .models import Filmwork, PersonRole


class PersonRoleInline(admin.TabularInline):
    model = PersonRole
    extra = 0

@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ('title', 'type', 'creation_date', 'rating')
    # порядок следования полей в форме создания/редактирования
    fields = (
'title', 'type', 'description', 'creation_date',
'certificate', 'file_path', 'rating', 'genres'
    ) 

    inlines = [
        PersonRoleInline
    ] 
