from django import forms

from .models import Post

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body',  'status','author','publish']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
     	    'author' : forms.Select(attrs={'class': 'form-control'}),
	    'publish' : forms.DateTimeInput(attrs={'class': 'form-control'}),
    	    #'created' : forms.DateTimeInput(attrs={'class': 'form-control'}),
    	    #'updated' : forms.DateTimeInput(attrs={'class': 'form-control'}),

    	     'status' : forms.Select(attrs={'class': 'form-control'}),

}
