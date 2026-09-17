def make_chai():
    if not kettle_has_water():
        fill_kettle()
    plug_in_kettle()
    boil_water()
    if not cup_is_clean():
        wash_up()
    add_to_cup("tea leaves")
    add_to_cup("Sugar")
    pour("Boiled water")
    stie("cup")
    serve("chai")

make_chai()