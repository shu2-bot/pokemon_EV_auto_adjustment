from django.db import models
from django import forms

class Pokemon_status(models.Model):
    pokemon_name = models.CharField("Name", max_length=12)
    bs_h = models.BigIntegerField("BaseStat-HP", default=0)
    bs_a = models.BigIntegerField("BaseStat-Attack", default=0)
    bs_b = models.BigIntegerField("BaseStat-Defense", default=0)
    bs_c = models.BigIntegerField("BaseStat-SpecialAttack", default=0)
    bs_d = models.BigIntegerField("BaseStat-SpecialDefense", default=0)
    bs_s = models.BigIntegerField("BaseStat-Speed", default=0)

    def __str__(self):
        return self.pokemon_name
    
class Status_Ev(models.Model):
    pokemon_name = models.CharField("Name", max_length=12)
    ev_h = models.BigIntegerField("EffortValue-HP", default=0)
    ev_a = models.BigIntegerField("EffortValue-Attack", default=0)
    ev_b = models.BigIntegerField("EffortValue-Defense", default=0)
    ev_c = models.BigIntegerField("EffortValue-SpecialAttack", default=0)
    ev_d = models.BigIntegerField("EffortValue-SpecialDefense", default=0)
    ev_s = models.BigIntegerField("EffortValue-Speed", default=0)
    speed = models.BooleanField("Compare-Speed", default=False)
    attack = models.BooleanField("Compare-Attack", default=False)
    defense = models.BooleanField("Compare-Defense", default=False)

    def __str__(self):
        return self.pokemon_name


class My_Pokemon_Input_Form(forms.ModelForm):
    class Meta:
        model = Pokemon_status
        fields = ("pokemon_name",)

class Opposite_Pokemon_Input_Form(forms.ModelForm):
    class Meta:
        model = Status_Ev
        fields = ("pokemon_name", "ev_h", "ev_a", "ev_b", "ev_c", "ev_d", "ev_s", "speed", "attack", "defense")
    