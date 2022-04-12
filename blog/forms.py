from django     import forms
from .models    import Komentar 

class KomentarForm(forms.ModelForm):
    class Meta:
        model   = Komentar
        fields=[
            'komentar_nama',
            'komentar_email',
            'komentar_isi'
        ]
        labels={
            'blogs':''
        }
        widgets={
            'komentar_nama':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'komentar_email':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'komentar_isi':forms.Textarea(
                attrs={
                    'class':'form-control'
                }
            ),
        }