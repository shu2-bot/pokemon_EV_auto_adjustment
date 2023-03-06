from django.db import models
from django import forms

class Pokemon_status(models.Model):
    pokemon_name = models.CharField("Name", max_length=12)
    bs_h = models.BigIntegerField("BaseStat-HP")
    bs_a = models.BigIntegerField("BaseStat-Attack")
    bs_b = models.BigIntegerField("BaseStat-Defense")
    bs_c = models.BigIntegerField("BaseStat-SpecialAttack")
    bs_d = models.BigIntegerField("BaseStat-SpecialDefense")
    bs_s = models.BigIntegerField("BaseStat-Speed")

    ev_h = models.BigIntegerField("EffortValue-HP")
    ev_a = models.BigIntegerField("EffortValue-Attack")
    ev_b = models.BigIntegerField("EffortValue-Defense")
    ev_c = models.BigIntegerField("EffortValue-SpecialAttack")
    ev_d = models.BigIntegerField("EffortValue-SpecialDefense")
    ev_s = models.BigIntegerField("EffortValue-Speed")

    def __str__(self):
        return self.pokemon_name

class Input_Form(forms.ModelForm):
    class Meta:
        model = Pokemon_status
        fields = ("pokemon_name", "ev_h", "ev_a", "ev_b", "ev_c", "ev_d", "ev_s")