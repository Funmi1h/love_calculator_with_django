from django import forms
from . import models
class LoveForm(forms.ModelForm):
    class Meta:
        model = models.LoveResult
        fields = ['name1', 'name2', ]
        widgets = {
            'name1': forms.TextInput(
                attrs= {
                    'placeholder': 'Toi 💖',
                    'class': 'form-control',
                }
            ),

            'name2': forms.TextInput(
                attrs= {
                    'placeholder': 'Lui/Elle 💘',
                    'class': 'form-control',
                }
            ),
            
        }

    def clean(self):
        cleaned_data =  super().clean()

        name1 = cleaned_data.get('name1')
        name2 = cleaned_data.get('name2')
        if name1:
            name1 = name1.lower().replace(" ", "")
        if name2:
            name2 = name2.lower().replace(" ", "")
        combined_name = name1 + name2
        # on fait la somme des codes ascii de chaque caractere
        combined_name = sum(ord(n) for n in combined_name) # ord() converti un cacombined_ractere en son code ascii
        score = combined_name % 101
        cleaned_data['percentage'] = score
        percentage = cleaned_data['percentage']
            
        return cleaned_data
        