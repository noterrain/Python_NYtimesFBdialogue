
class MarkovGenerator(object):

  def __init__(self, n, max):
    self.n = n # order (length) of ngrams
    self.max = max # maximum number of elements to generate
    self.ngrams = dict() # ngrams as keys; next elements as values
    beginning = tuple(["China", "is"]) # beginning ngram of every line
    beginning2 = tuple(["But", "it"])
    self.beginnings = list()
    self.beginnings.append(beginning)
    self.beginnings.append(beginning2)
    


  def tokenize(self, text):
    return text.split(" ")

  def feed(self, text):

    tokens = self.tokenize(text)

    # discard this line if it's too short
    if len(tokens) < self.n:
      return

    # store the first ngram of this line
    #beginning = tuple(tokens[:self.n])
    #self.beginnings.append(beginning)

    for i in range(len(tokens) - self.n):

      gram = tuple(tokens[i:i+self.n])
      next = tokens[i+self.n] # get the element after the gram

      # if we've already seen this ngram, append; otherwise, set the
      # value for this key as a new list
      if gram in self.ngrams:
        self.ngrams[gram].append(next)
      else:
        self.ngrams[gram] = [next]

  # called from generate() to join together generated elements
  def concatenate(self, source):

      haha = list()
      kk = list()
      
      haha = " ".join(source)
      ouou = haha.split(".")
      kk = ouou[0]

      return kk
    # return " ".join(source)

  # generate a text from the information in self.ngrams
  def generate(self,i):

    from random import choice

    # get a random line beginning; convert to a list. 
      #current = choice(self.beginnings)
    current = self.beginnings[i]
    output = list(current)

    for i in range(self.max):
      if current in self.ngrams:
        possible_next = self.ngrams[current]
        next = choice(possible_next)
        output.append(next)
        # get the last N entries of the output; we'll use this to look up
        # an ngram in the next iteration of the loop
        current = tuple(output[-self.n:])
      else:
        break

    output_str = self.concatenate(output)
    return output_str
    

  def search_facebook_posts(self):
      import json
      import urllib
      import time
      FB = list()
      query = {'q': "feel", 'limit': 200}
      resp = urllib.urlopen('http://graph.facebook.com/search?' + urllib.urlencode(query))
      data = json.loads(resp.read())
      posts = list()
      for item in data['data']:
          if 'message' in item:
              posts.append(item)
      
      
      for post in posts:
          FB.append(post['message'].encode('ascii', 'replace'))
       
      return FB

  def together(self):
      import re
      sentences = list()
      manysentences = list()
      togetherlist = self.search_facebook_posts()
      for line in togetherlist:
          line = line.replace(".", "\n")
          line = line.replace(",", "\n")
          line = line.replace("?", "\n")
          line = line.replace(";", "\n")
          line = line.replace("!", "\n")
          line = line.replace("...", "\n")
          line = line.replace(":", "\n")
          sentenca = line.split("\n")
          for i in range(len(sentenca)):
            sentences.append(sentenca[i])

      for sentence in sentences:
          if "feel" in sentence:
              for matching in re.findall(r'\b[Ff]eel(.*)$',sentence):
                manysentences.append(matching)
 
      sentencesnew = random.choice(manysentences)
      haha = "I feel" + sentencesnew
      return haha


  def namelist(self):
      import random 
      namelisty = list()
      for line in open("namelist"):
          namelisty.append(line+"said")

      thisname = random.choice(namelisty)

      return thisname 


if __name__ == '__main__':

  import sys
  import random
  import codecs

  f = codecs.open('output.txt', 'w', encoding ='utf-8')
  generator = MarkovGenerator(n=2, max=16)
  for line in open("china"):
    line = line.strip()
    generator.feed(line) 

  for i in range(2):
    f.write(generator.generate(i)+".")
    print generator.generate(i)+"."

  f.write("written by NYtimes, any thoughts?" + "\n")
    

  #generator.search_facebook_posts()
  print generator.together()+"."
  f.write(generator.together()+".")
  f.write(generator.namelist())

  f.close()



