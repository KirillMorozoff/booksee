from django import forms

class MultiWidget(forms.SelectMultiple):
    class Media:
        css = {
            'all': ('/css/bootstrap-multiselect.css', )
        }
        js = ('/js/bootstrap-multiselect.js', '/plugins/jquery-1.11.3.min.js', '/plugins/bootstrap/js/bootstrap.min.js')
