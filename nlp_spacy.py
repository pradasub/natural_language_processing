import spacy
import nltk

nlp=spacy.load('en_core_web_sm')

doc = nlp(u'Tesla is looking for buying us start up for 6 millions')

for token in doc:
    print(token.text, token.pos)

nlp.pipeline
nlp.pipe_names

doc2 = nlp(u"Tesla isn't looking into startups anymore")

for token in doc:
    print(token.text, token.pos_, token.dep_)

doc2[0].pos_
doc2[0].dep_