from django.db import models

class Pokemon_status(models.Model):
    pokemon_name = models.CharField("Name", max_length=6)
    bs_h = models.BigIntegerField("BaseStat-HP")
    bs_a = models.BigIntegerField("BaseStat-Attack")
    bs_b = models.BigIntegerField("BaseStat-Defense")
    bs_c = models.BigIntegerField("BaseStat-SpecialAttack")
    bs_d = models.BigIntegerField("BaseStat-SpecialDefense")
    bs_e = models.BigIntegerField("BaseStat-Speed")

    def __str__(self):
        return self.pokemon_name
