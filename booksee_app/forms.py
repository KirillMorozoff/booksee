from django import forms
from django.core import validators
from booksee_app.models import Genre, Award, Language
from booksee_app.widgets import MultiWidget

genre_list = Genre.objects.order_by('genre_name').values_list('id', 'genre_name')
award_list = Award.objects.order_by('award_name').values_list('id', 'award_name')
language_list = Language.objects.order_by('language_name').values_list('id', 'language_name')



class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.EmailField(required=False, widget=forms.HiddenInput, validators=[validators.MaxValueValidator(0)])

class MainForm(forms.Form):
    awards = forms.MultipleChoiceField(required=False, widget=MultiWidget, choices=award_list)
    awards_dont_show = forms.MultipleChoiceField(required=False, widget=MultiWidget, choices=award_list)


    genres = forms.MultipleChoiceField(required=False, widget=MultiWidget, choices=genre_list)
    genres_dont_show = forms.MultipleChoiceField(required=False, widget=MultiWidget, choices=genre_list)

    languages = forms.MultipleChoiceField(required=False, widget=MultiWidget, choices=language_list)
    languages_dont_show = forms.MultipleChoiceField(required=False, widget=MultiWidget, choices=language_list)

    first_edition_from = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '0'}))
    first_edition_to = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '2017'}))

    century_from = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '1'}))
    century_to = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '15'}))

    number_of_pages_from = forms.CharField(required=False, widget=forms.TextInput(attrs={'id': 'price2'}))
    number_of_pages_to = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '9999'}))

    rating_from = forms.CharField(required=False, widget=forms.TextInput(attrs={'id': 'price3'}))
    rating_to = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '4.7'}))

    number_of_ratings_from = forms.CharField(required=False, widget=forms.TextInput(attrs={'id': 'price4'}))
    number_of_ratings_to = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '9999'}))

    number_of_reviews_from = forms.CharField(required=False, widget=forms.TextInput(attrs={'id': 'price5'}))
    number_of_reviews_to = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '9999'}))
