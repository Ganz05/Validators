from django import forms


def validate_for_t(data):
    if data.lower().startswith('t'):
        raise forms.ValidationError('Invalid Data') #--> for single VALIDATION
    
def validate_length(data):
    if len(data)<5:
        raise forms.ValidationError('Invalid Data')  #--> for single VALIDATION


class AnimalForm(forms.Form):
    name=forms.CharField(validators=[validate_for_t,validate_length])
    zoo=forms.CharField(max_length=100)
    aid=forms.IntegerField()
    re_enter=forms.IntegerField()

    #<-- For multiple VALIDATION -->

    def clean(self):
        id=self.cleaned_data['aid']
        re=self.cleaned_data['re_enter']
        if id!=re:
            raise forms.ValidationError('Invalid Data')
