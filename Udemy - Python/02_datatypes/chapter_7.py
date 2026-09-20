masala_spices = "cardmom, cinnamon, cloves, black pepper"
(spice1, spice2, spice3, spice4) = masala_spices.split(", ")
print(f"Main masala Spices: {spice1}, {spice2}, {spice3}, {spice4}")

ginger_ratio, cardmom_ratio = 8,2
print(f"Ginger to Cardmom ratio: {ginger_ratio}:{cardmom_ratio}")
cardmom_ratio, ginger_ratio = ginger_ratio, cardmom_ratio
print(f"Ginger to Cardmom ratio: {ginger_ratio}:{cardmom_ratio}")