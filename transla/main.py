from translate import Translator
translator=Translator(from_lang='english', to_lang='swahili')
translation=translator.translate('Hello, world')
print(translation)
