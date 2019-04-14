'''
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. 
If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?

'''
from random import randint
validCharInUrl = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
LENGTH = 6
CHAR_SIZE = 62
class UrlShortener(object):

    def __init__(self):
        self.shortUrls = dict()
        self.urlToShort = dict()

    def convert(self):
        shortCode = ''
        i = 0
        while(i < 6):
            randIdx = randint(0,61)
            randomChar = validCharInUrl[randIdx]
            shortCode += randomChar
            i += 1
        return shortCode

    def shorten(self, url):
        if (url in self.urlToShort):
            return self.urlToShort[url]
        # else create encoding and set
        shortCode = self.convert()
        i = 0
        while(shortCode in self.shortUrls):
            shortCode = self.convert()
        self.shortUrls[shortCode] = url
        self.urlToShort[url] = shortCode
        return shortCode

    def restore(self, short):
        if (short not in self.shortUrls):
            print("No url for short code")
            return None
        return self.shortUrls[short]

urlShorter = UrlShortener()

url1 = 'http://www.amazon.com'

url2 = 'http://www.facebook.com'

short1 = urlShorter.shorten(url1)
res1 = urlShorter.restore(short1)

print('1: {} {} {}'.format(url1, short1, res1))

short2 = urlShorter.shorten(url2)
res2 = urlShorter.restore(short2)

print('2: {} {} {}'.format(url2, short2, res2))

print('access again')

short1 = urlShorter.shorten(url1)
res1 = urlShorter.restore(short1)

print('1: {} {} {}'.format(url1, short1, res1))
