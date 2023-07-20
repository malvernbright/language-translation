from translate import Translator
import os
file = open('project.txt', 'r')
new_content = file.read()
translating_file = Translator(to_lang='german')
result = translating_file.translate(new_content)
print(result)
