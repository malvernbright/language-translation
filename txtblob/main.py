from textblob import TextBlob

adding_blob = TextBlob('Easy way to translate a text in Python')
output = adding_blob.translate(to='sw')
print(output)