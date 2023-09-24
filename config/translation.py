from modeltranslation.translator import translator, TranslationOptions
from polls.models import todoModel

class TodoTranslationOptions(TranslationOptions):
    fields = ('todo_name', 'description')
    required_languages = ('uz',)
translator.register(todoModel, TodoTranslationOptions)