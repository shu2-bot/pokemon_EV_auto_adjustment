

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemon_EV_auto_adjustment.settings')


from django import setup
setup()


from pokemon_EV_auto_calculation.models import Move_Status
sample_move = Move_Status(Name='10まんボルト', Type="electric", Category="special")
sample_move.save()
"""

from pokemon_EV_auto_calculation.models import Move_Status

# Create a new record
new_record = Move_Status(Name='10まんボルト', Type="electric", Category="special")
new_record.save()
"""