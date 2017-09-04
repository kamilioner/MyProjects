import urllib.request

fullURL = "http://finance.yahoo.com/d/quotes.csv?s=aapl&f=nagh"
response = urllib.request.Request(fullURL)
# print(response)
result = urllib.request.urlopen(response)
resulttext = result.read()
print(resulttext)
