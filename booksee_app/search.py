from booksee_app.models import Genre, Award, Language
from booksee_app import forms
from booksee_app.forms import award_list, genre_list, language_list
import sqlite3
import re

award_result_select = []
award_result_not_to_select = []
award_results = []

genres_result_select = []
genres_result_not_to_select = []
genres_results = []

languages_result_select = []
languages_result_not_to_select = []
languages_results = []

class SearchAwards():
    def selectingAwards(awards_show, awards_not_to_show, genres_to_show, genres_not_to_show, languages_to_show, pages_from, pages_to, rating_from, rating_to, ratings_from, ratings_to, reviews_from, reviews_to, year_from, year_to):
            conn = sqlite3.connect('books.db')
            # Создаем курсор - это специальный объект который делает запросы и получает их результаты

            cursor = conn.cursor()
            sql = "SELECT id, title, author, raitingValue, published, raitings, reviews FROM books WHERE ("
            where = []
            args = []
            results = []
            cursor.execute("SELECT id, title, author, raitingValue, published, raitings, reviews FROM books")
            award_result_select = cursor.fetchall()

##############################    Awards   ##################################

            if len(awards_show) > 0:
                for award in awards_show:
                    where.append('awards LIKE ?')
                    # Слова передаём отдельно, чтобы защититься от SQL-инъекции
                    args.append('%' + award + '%')

                # Собираем SQL-запрос до конца
                sql += ' OR '.join(where)  # или AND
                # И запускаем. sqlite автоматически заменит вопросики на нужные слова
                sql = sql + ") AND ("

            if len(awards_not_to_show) > 0:
                where = []
                for award in awards_not_to_show:
                    where.append('awards NOT LIKE ?')
                    # Слова передаём отдельно, чтобы защититься от SQL-инъекции
                    args.append('%' + award + '%')
                sql += ' OR '.join(where)
                sql = sql + ") AND ("

##############################    Genres   ##################################

            if len(genres_to_show) > 0:
                where = []
                for genre in genres_to_show:
                    where.append('genres LIKE ?')
                    # Слова передаём отдельно, чтобы защититься от SQL-инъекции
                    args.append('%' + genre + '%')
                sql += ' OR '.join(where)
                sql = sql + ") AND ("

            if len(genres_not_to_show) > 0:
                where = []
                for genre in genres_not_to_show:
                    where.append('genres NOT LIKE ?')
                    # Слова передаём отдельно, чтобы защититься от SQL-инъекции
                    args.append('%' + genre + '%')
                sql += ' OR '.join(where)
                sql = sql + ") AND ("

##############################    Languages   ##################################


            if len(languages_to_show) > 0:
                where = []
                for language in languages_to_show:
                    where.append('language LIKE ?')
                    # Слова передаём отдельно, чтобы защититься от SQL-инъекции
                    args.append('%' + language + '%')
                sql += ' OR '.join(where)
                sql = sql + ") AND ("

##############################    Pages   ##################################
            if len(pages_from) > 0 and len(pages_to) > 0:
                sql = sql + "pages BETWEEN " + pages_from + " AND " + pages_to
                sql = sql + ") AND ("

##############################    Rating   ##################################

            if len(rating_from) > 0 and len(rating_to) > 0:
                sql = sql + "raitingValue BETWEEN " + rating_from + " AND " + rating_to
                sql = sql + ") AND ("

##############################    Ratings   ##################################

            if len(ratings_from) > 0 and len(ratings_to) > 0:
                sql = sql + "raitings BETWEEN " + ratings_from + " AND " + ratings_to
                sql = sql + ") AND ("

##############################    Reviews   ##################################

            if len(reviews_from) > 0 and len(reviews_to) > 0:
                sql = sql + "reviews BETWEEN " + reviews_from + " AND " + reviews_to
                sql = sql + ") AND ("

            sql = sql + ")"

            if sql[len(sql)-8:len(sql)-1] == ") AND (":
                sql = sql[:len(sql)-8] + ")"

            print("SQL: " +str(sql))

            if sql != "SELECT id, title, author, raitingValue, published, raitings, reviews FROM books WHERE ()":
                sql = sql + " ORDER BY raitingValue DESC, raitings DESC LIMIT 200"
                cursor.execute(sql, args)
                award_result_select = cursor.fetchall()
                conn.close()
                #print("Results: " + str(award_result_select))
                print(" ")

##############################    Edition   ##################################

            i = 0
            while (i < len(award_result_select)):
                year = re.search('(\d+$)|(\s\d+\s)', str(award_result_select[i][3]), flags=0)
                try:
                    year = year.group(0).replace(" ", "")
                    if year >= year_from and year <= year_to:
                        results.append(award_result_select[i])
                    i = i + 1
                except AttributeError:
                    i = i + 1

            print(str(len(award_result_select)) + " " + str(len(results)))

            #print("Year results: " + str(results))

            if year_to == "" or year_to < year_from:
                return award_result_select
            else:
                return results

            #SELECT title FROM books WHERE (awards LIKE '%%' OR awards LIKE '%%') AND (awards NOT LIKE '%I%' OR awards NOT LIKE '%I%') AND (genres LIKE '%Adventure%' OR genres LIKE '%Crime%') AND (genres NOT LIKE '%Historical%' OR genres NOT LIKE '%Fiction%') AND (language LIKE '%English%' OR language LIKE '%Russian%') AND (pages BETWEEN 200 AND 400) AND (raitingValue BETWEEN 3.5 AND 4.91) AND (raitings BETWEEN 500 AND 50000) AND (reviews BETWEEN 500 AND 50000);
