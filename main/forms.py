from django import forms
from main.models import ContactMessage, Comment

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5})
        }

class CommitForm(forms.ModelForm):
    parent = forms.ModelChoiceField(queryset=Comment.objects.all(), widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Commit
        fields = ['text', 'parent']
