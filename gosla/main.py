import goslate

inserted_text = "I am Malvern"
new_gs = goslate.Goslate()
# new_gs.get_languages()
t = new_gs.translate(inserted_text, 'es')
print(t)