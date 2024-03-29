from django import forms
from django.forms import TextInput

from cities.models import City

__all__ = (
    'RouteForm', 'RouteModelForm',
)

from routes.models import Route

from trains.models import Train


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='Из города', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control js-example-basic-single'
    }))
    to_city = forms.ModelChoiceField(label='В город', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control js-example-basic-single'
    }))
    cities = forms.ModelMultipleChoiceField(label="Через города", queryset=City.objects.all(), required=False,
                                            widget=forms.SelectMultiple(attrs={
                                                'class': 'form-control js-example-basic-multiple'}))
    travelling_time = forms.IntegerField(label='Время в пути', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Время в пути'
    }))


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(label='Название маршрута', widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название маршрута'
    }))
    from_city = forms.ModelChoiceField(label='Из города', queryset=City.objects.all(), widget=forms.HiddenInput())
    to_city = forms.ModelChoiceField(label='В город', queryset=City.objects.all(), widget=forms.HiddenInput())
    trains = forms.ModelMultipleChoiceField(label="Через города", queryset=Train.objects.all(), required=False,
                                            widget=forms.SelectMultiple(attrs={
                                                'class': 'form-control d-none'}))
    travel_times = forms.IntegerField(label='Время в пути', widget=forms.HiddenInput())

    class Meta:
        model = Route
        fields = '__all__'
