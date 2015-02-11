#### myapp/admin.py

polls/admin.py
from django.contrib import admin
from polls.models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


### added later to QuestionAdmin
list_display = ('question_text', 'pub_date', 'was_published_recently')

### added later to Question in models.py
def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
	
### added later to QuestionAdmin
list_filter = ['pub_date']

### added later to QuestionAdmin
search_fields = ['question_text']
