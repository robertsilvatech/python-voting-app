from django import forms


OPTIONS_VOTING = (
    ('docker', 'Docker'),
    ('kubernetes', 'Kubernetes'),
    ('python', 'Python'),
    ('ansible', 'Ansible'),
    ('aws', 'AWS')
)

class VotingForm(forms.Form):
    option = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={
        'class': 'form-control list-group-item-check pe-none',
        'type': 'radio',
        }), 
        choices=OPTIONS_VOTING, 
        required=False, 
        label='Escolha um')
    #hostname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Hostname'}), required=True) 
    #visiblename = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Visible Name'}), required=False) 