from django import forms
from .models import Editor, Debug
from ckeditor.widgets import CKEditorWidget

class EditorForm(forms.Form):
    body = forms.CharField(widget=CKEditorWidget(), label="Text Editor")
