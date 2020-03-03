from django import forms


class addPost(forms.Form):
    body = forms.CharField(widget=forms.TextInput, max_length=280, required=True)
    # author = forms.ModelChoiceField(queryset=Author.objects.all())
