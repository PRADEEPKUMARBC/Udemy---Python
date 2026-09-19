is_boilding = True
stri_count = 10
total_actions = stri_count + is_boilding
print(f"Total actions: {total_actions}")

milk_Present = 0
print(f"Is milk present: {bool(milk_Present)}")

water_hot = True
tea_added = False
can_serve_tea = water_hot and tea_added
print(f"Can serve tea: {can_serve_tea}")

import sys
ideal_temp = 95.5
current_temp = 95.49
print(f"Ideal temp {ideal_temp} and current temp {current_temp}")
print(f"Difference in temp: {ideal_temp - current_temp}")
print(sys.float_info)