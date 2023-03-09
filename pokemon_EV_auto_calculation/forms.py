from django import forms

class Calculation_input_form(forms.Form):
    pokemon_name = forms.CharField(label="Name", max_length=12)
    ev_h = forms.IntegerField(label="EffortValue-HP", initial=0)
    ev_a = forms.IntegerField(label="EffortValue-Attack", initial=0)
    ev_b = forms.IntegerField(label="EffortValue-Defense", initial=0)
    ev_c = forms.IntegerField(label="EffortValue-SpecialAttack", initial=0)
    ev_d = forms.IntegerField(label="EffortValue-SpecialDefense", initial=0)
    ev_s = forms.IntegerField(label="EffortValue-Speed", initial=0)


class Calculation_Select_Form(forms.Form):
    CHOICE = (
		('y', '検証する'),
		('n', '検証しない'),
	    )
    speed = forms.fields.ChoiceField(label="Compare-Speed", required=True, widget=forms.widgets.Select, choices=CHOICE)
    attack = forms.fields.ChoiceField(label="Compare-Attack", required=True, widget=forms.widgets.Select, choices=CHOICE)
    defense = forms.fields.ChoiceField(label="Compare-Defense", required=True, widget=forms.widgets.Select, choices=CHOICE)
