from django.contrib.postgres.fields import ArrayField
from django.forms import ModelForm, CharField, TextInput, ModelChoiceField, Select

from authorsapp.models import Author
from quotesapp.models import Quote


class QuoteForm(ModelForm):
    quote = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    # author = ModelChoiceField(queryset=Author.objects.all()
    #                           .exclude(fullname=' ')
    #                           .values('fullname')
    #                           .distinct()
    #                           .order_by('fullname'),
    #                           to_field_name='fullname',
    #                           required=True,
    #                           widget=Select(attrs={'class': 'form-control'})
    #                           )
    author = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    tags = ArrayField(CharField(min_length=3, max_length=25, required=True, widget=TextInput()))

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
