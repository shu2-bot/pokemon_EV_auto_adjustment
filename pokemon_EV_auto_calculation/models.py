from django.db import models
from django import forms

class Pokemon_status(models.Model):
    pokemon_name = models.CharField("Name", max_length=12)
    bs_h = models.IntegerField("BaseStatHitPoint", default=0)
    bs_a = models.IntegerField("BaseStatAttack", default=0)
    bs_b = models.IntegerField("BaseStatDefense", default=0)
    bs_c = models.IntegerField("BaseStatSpecialAttack", default=0)
    bs_d = models.IntegerField("BaseStatSpecialDefense", default=0)
    bs_s = models.IntegerField("BaseStatSpeed", default=0)
    type1 = models.CharField("Type1", max_length=8)
    type2 = models.CharField("Type2", max_length=8)

    def __str__(self):
        return self.pokemon_name
    
class Move_Status(models.Model):
    move_name = models.CharField("Name", max_length=20)
    type = models.CharField("Type", max_length=8)
    category = models.CharField("Category", max_length=8)
    power = models.IntegerField("Power", default=0)
    def __str__(self):
        return self.move_name
    class Meta:
        db_table = "move_status"
    
# Not used
"""
class Status_Ev(models.Model):
    pokemon_name = models.CharField("Name", max_length=12)
    ev_h = models.IntegerField("EffortValue-HP", default=0)
    ev_a = models.IntegerField("EffortValue-Attack", default=0)
    ev_b = models.IntegerField("EffortValue-Defense", default=0)
    ev_c = models.IntegerField("EffortValue-SpecialAttack", default=0)
    ev_d = models.IntegerField("EffortValue-SpecialDefense", default=0)
    ev_s = models.IntegerField("EffortValue-Speed", default=0)
    speed = models.BooleanField("Compare-Speed", default=False)
    attack = models.BooleanField("Compare-Attack", default=False)
    defense = models.BooleanField("Compare-Defense", default=False)

    def __str__(self):
        return self.pokemon_name
"""


class My_Pokemon_Input_Form(forms.ModelForm):
    class Meta:
        model = Pokemon_status
        fields = ("pokemon_name",)

class My_Move_Input_Form(forms.ModelForm):
    class Meta:
        model = Move_Status
        fields = ("move_name",)

class Opposite_Move_Input_Form(forms.ModelForm):
    class Meta:
        model = Move_Status
        fields = ("move_name",)

# Not used
"""
class Opposite_Pokemon_Input_Form(forms.ModelForm):
    class Meta:
        model = Status_Ev
        fields = ("pokemon_name", "ev_h", "ev_a", "ev_b", "ev_c", "ev_d", "ev_s", "speed", "attack", "defense")
"""
    
