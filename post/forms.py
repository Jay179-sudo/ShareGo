from django.forms import ModelForm
from .models import Post

class ArticleForm(ModelForm):
    class Meta:
        model = Post
        exclude = ["author"]
