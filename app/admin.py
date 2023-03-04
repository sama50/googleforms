from django.contrib import admin
from app.models import UserForms , SubmissionForm ,QueationForImage , Queation_Text_ans
# Register your models here.


@admin.register(UserForms)
class UserFormsAdmin(admin.ModelAdmin):
    list_display = ('id','user','form_name','form_id')
    

@admin.register(SubmissionForm)
class SubmissionFormAdmin(admin.ModelAdmin):
    list_display = ('id','formid','quetion')

@admin.register(QueationForImage)
class QueationForImageAdmin(admin.ModelAdmin):
    list_display = ('id','formid','quetion')


@admin.register(Queation_Text_ans)
class Queation_Text_ansAdmin(admin.ModelAdmin):
    list_display =('id','email','form_id','que','ans')

    

    


