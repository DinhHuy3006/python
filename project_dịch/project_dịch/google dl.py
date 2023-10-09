from googletrans import Translator


t = Translator()

# Translate text from Korean to English`                                                                                                                `
translation_ko_to_en = t.translate('안녕하세요.')
print(translation_ko_to_en.text)

# Translate text from Korean to Japanese
translation_ko_to_ja = t.translate('안녕하세요.', dest='ja')
print(translation_ko_to_ja.text)

# Translate text from Latin to English
translation_la_to_en = t.translate('veritas lux mea', src='la')
print(translation_la_to_en.text)
# <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>
a = t.translate('hello', src='en')
print(translation_la_to_en.text)