# File to preprocess reviews into their sentiment stuff.

import textacy
import re
import sys
from textblob import TextBlob

#==========Functions===================

def remove(sent):
  sent = re.sub(r'\n', "", sent)
  sent = re.sub(r'.*Helpful', "", sent)
  sent = re.sub(r'.*Report abuse', "", sent)
  sent = re.sub(r'By.*', "", sent)
  sent = re.sub(r'By.*', "", sent)
  sent = re.sub(r'.*20.*', "", sent)
  sent = re.sub(r'.*Purchase', "", sent)
  sent = re.sub(r'[\d\.]+.*stars', "", sent)
  sent = re.sub(r'.*found this helpful', "", sent)
  sent = re.sub(r'.*image', "", sent)
  sent = re.sub(r'Color:', "", sent, flags = re.I)
  return sent

def removeNouns(sent, nouns):
  for noun in nouns:
    sent = re.sub(noun, "[product]", sent, flags = re.I);
  return sent

def removeDuplicates(sents):
  uniq = set()
  for sent in sents:
    uniq.add(sent.text)
  return uniq


def getProductList(filename):
  f = open(filename, 'r')
  plist = list(map(lambda x : re.sub(r'\n', "", x), f.readlines()))
  f.close()
  return plist


#================Code============================

reviewsFile = sys.argv[1]
productsFile = sys.argv[2]
productList = getProductList(productsFile);

# This line gets all of data into one giant string.
str = next(textacy.io.text.read_text(reviewsFile));

# Gives us sentences automatically.
doc = textacy.Doc(str);

sents = removeDuplicates(doc.sents)

for sent in sents:
  sent = removeNouns(remove(sent), productList);
  if len(sent) > 0:
    b = TextBlob(sent)
    print(b.sentiment.polarity, b.sentiment.subjectivity, sent, sep="|");



