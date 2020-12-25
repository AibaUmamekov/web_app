from django.contrib import admin

from .models import Question



# class QuestionAdmin(admin.ModelAdmin):
# 	fields = [
# 		# (None, 				{'fields':['question_text']}),
# 		# ('Date information'	{'fields':['pub_date']}),
#
# 	#'pub_date', 'question_text'
# 	]

admin.site.register(Question) #QuestionAdmin

