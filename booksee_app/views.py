from django.shortcuts import render
from django.http import HttpResponse
from booksee_app.models import Genre, Award, Language
from booksee_app import forms
from booksee_app.forms import award_list, genre_list, language_list
from booksee_app.search import SearchAwards
import sqlite3


def index(request):
    form = forms.MainForm()
    listf = {'form':form}
    if request.method == 'POST':
        form = forms.MainForm(request.POST)
        if form.is_valid():
            #Выводим список премий для показа
            selected_awards_ids = form.cleaned_data.get('awards')
            selected_awards = []
            for i in selected_awards_ids:
                selected_awards.append(award_list.get(id=i)[1])
            #selected_awards = str(selected_awards).replace('[', '').replace(']', '').replace("'", "")
            print("Selected Awards(to show): " + str(selected_awards))
            #Выводим список премий для исключения
            selected_awards_ids = form.cleaned_data.get('awards_dont_show')
            selected_awards_no = []
            for i in selected_awards_ids:
                selected_awards_no.append(award_list.get(id=i)[1])
            print("Selected Awards(not to show): " + str(selected_awards_no))


            #Выводим список жанров для показа
            selected_genres_ids = form.cleaned_data.get('genres')
            selected_genres = []
            for i in selected_genres_ids:
                selected_genres.append(genre_list.get(id=i)[1])
            print("Selected Genres(to show): " + str(selected_genres))
            #Выводим список жанров для исключения
            selected_genres_ids = form.cleaned_data.get('genres_dont_show')
            selected_genres_no = []
            for i in selected_genres_ids:
                selected_genres_no.append(genre_list.get(id=i)[1])
            print("Selected Genres(not to show): " + str(selected_genres_no))


            #Выводим список Языков для показа
            selected_languages_ids = form.cleaned_data.get('languages')
            selected_languages = []
            for i in selected_languages_ids:
                selected_languages.append(language_list.get(id=i)[1])
            print("Selected Languages(to show): " + str(selected_languages))
            #Выводим список Языков для исключения
            selected_languages_ids = form.cleaned_data.get('languages_dont_show')
            selected_languages_no = []
            for i in selected_languages_ids:
                selected_languages_no.append(language_list.get(id=i)[1])
            print("Selected Languages(not to show): " + str(selected_languages_no))


            #Выводим период перводго издания
            first_edition_from_date = form.cleaned_data['first_edition_from']
            first_edition_to_date = form.cleaned_data['first_edition_to']
            print("First Edition Range: " + first_edition_from_date + "-" + first_edition_to_date)

            #Выводим диапазон веков
            century_from_date = form.cleaned_data['century_from']
            century_to_date = form.cleaned_data['century_to']
            print("Century Range: " + century_from_date + "-" + century_to_date)

            #Выводим диапазон страниц
            pages_from_count = form.cleaned_data['number_of_pages_from'].split(" - ")[0]
            pages_to_count = form.cleaned_data['number_of_pages_from'].split(" - ")[1]
            print("Pages Range: " + pages_from_count + "-" + pages_to_count)

            #Выводим диапазон рейтинга
            raiting_from_value = form.cleaned_data['rating_from'].split(" - ")[0]
            raiting_to_value = form.cleaned_data['rating_from'].split(" - ")[1]
            
            print("Raiting Range: " + str(raiting_from_value) + "-" + raiting_to_value)

            #Выводим диапазон голосований
            raitings_from_count = form.cleaned_data['number_of_ratings_from'].split(" - ")[0]
            raitings_to_count = form.cleaned_data['number_of_ratings_from'].split(" - ")[1]
            print("Raitings Range: " + raitings_from_count + "-" + raitings_to_count)

            #Выводим диапазон рецензий
            reviews_from_count = form.cleaned_data['number_of_reviews_from'].split(" - ")[0]
            reviews_to_count = form.cleaned_data['number_of_reviews_from'].split(" - ")[1]
            print("Reviews Range: " + reviews_from_count + "-" + reviews_to_count)


            #SearchAwards.selectingAwards(selected_awards, selected_awards_no, selected_genres, selected_genres_no, selected_languages, pages_from_count, pages_to_count, raiting_from_value, raiting_to_value, raitings_from_count, raitings_to_count, reviews_from_count, reviews_to_count, first_edition_from_date, first_edition_to_date)
            books = SearchAwards.selectingAwards(selected_awards, selected_awards_no, selected_genres, selected_genres_no, selected_languages, pages_from_count, pages_to_count, raiting_from_value, raiting_to_value, raitings_from_count, raitings_to_count, reviews_from_count, reviews_to_count, first_edition_from_date, first_edition_to_date)

            listf = {'form':form, 'books':books}
            print(str(books))

    return render(request, 'booksee_template/index.html', context=listf)


def contacts(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            #do something code
            print("Validation SUCCESS!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])
    return render(request, 'booksee_template/contacts.html', {'form':form})
