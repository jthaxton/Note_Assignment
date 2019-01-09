from django import forms 
from notes.models import Note

class NoteForm(forms.ModelForm):
    note = forms.CharField(max_length=150, min_length=4)
    class Meta:
        model = Note
        fields = ('note',)