import nltk
from nltk.corpus import stopwords
from string import punctuation
import json
import logging
import os
import pickle
from gensim.utils import simple_preprocess

# Tokenize the documents.
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer

# Compute bigrams.
from gensim.models import Phrases

# Remove rare and common tokens.
from gensim.corpora import Dictionary

from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
from collections import defaultdict

# nltk.download('wordnet')
# nltk.download('stopwords')

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
stop_words = list(stopwords.words('english')) + list(punctuation)
stemmer = SnowballStemmer('english')

# Split the documents into tokens.
tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()

class KeywordAnalyzer(object):
    
    def __init__(self):
        self.docs             = None
        self.dictionary       = None
        self.corpus           = None
        self.keyword_map_rel  = None
        self.keyword_map      = None
        self.topic_map        = None
        
    def prepare(self,docs,topics):
        """Take the document and pick keywords
        and pair with possibly related keywords
        """
        
        self.docs, self.dictionary, self.corpus = self.clean_docs(docs)
        
        # Create keyword map
        self.set_keyword_map()
        
        # Create keyword map with their relatives
        self.set_keyword_map_rel()
        
        self.topic_map = {topic: set(self.get_related_keywords(topic,self.keyword_map_rel,_score=False)) 
                                  for topic in topics}
        
    def clean_docs(self,docs):
        """Removes uneccessary words (noise) or in this case words
        that will bring our models to the worse case scenario"""

        # Remove numbers, but not words that contain numbers.
        docs = [[token for token in doc if not token.isnumeric()] for doc in docs]

        # Remove words that are only one character.
        docs = [[token for token in doc if len(token) > 1 and token not in stop_words] for doc in docs]

        # lemmatizer = WordNetLemmatizer()
        # docs = [[lemmatizer.lemmatize(token) for token in doc] for doc in docs]

        # Add bigrams and trigrams to docs (only ones that appear 20 times or more).
        bigram = Phrases(docs, min_count=20)
        for idx in range(len(docs)):
            for token in bigram[docs[idx]]:
                if '_' in token:
                    # Token is a bigram, add to document.
                    docs[idx].append(token)

        # Create a dictionary representation of the documents.
        dictionary = Dictionary(docs)

        # Filter out words that occur less than 20 documents, or more than 50% of the documents.
        dictionary.filter_extremes(no_below=20, no_above=0.5)

        # Bag-of-words representation of the documents.
        corpus = [dictionary.doc2bow(doc) for doc in docs]

        return docs,dictionary,corpus
    
    def set_keyword_map(self):
        """Creates a map of keywords and where they show up in the documents"""
        
        ret = defaultdict(list)
        for idx, doc in enumerate(self.docs):
            for token in doc:
                if token in self.dictionary.token2id:
                    ret[token].append(idx)
                    
        self.keyword_map = ret
        return ret
    
    def set_keyword_map_rel(self,threshold=100):
        """Create a map of keywords as a key and related keywords as the value"""
        
        ret = {}

        for keyword,related in self.keyword_map.items():
            related = related if len(related) > threshold else []
            rels = defaultdict(list)
            rels_with_score = []
            for idx in related:
                for k in self.docs[idx]:
                    if k != keyword:
                        rels[k].append(idx)
            for k,v in rels.items():
                if k not in rels_with_score:
                    score = (len(v) * (100/len(related)))/100
                    if score >= 0.009:
                        rels_with_score.append((k,score))  
            rels_with_score.sort(key=lambda x : x[1], reverse=True)

            ret[keyword] = rels_with_score
        self.keyword_map_rel = ret
        
        return ret
    
    def get_related_keywords(self,keyword,min_len=30,_score=False):
        if type(keyword) == str:
            ret = self.keyword_map_rel.get(keyword,[])
        else:
            ret = []
            for k in keyword:
                ret += self.keyword_map_rel.get(k,[])

        ret = [x[0] for x in ret] if _score == False else ret
        return ret

    
    def get_related_topics(self,keyword,cut=0.5):
        """Returns all topics related to a certain keyword of set of 
        keywords."""
        
        ret = []

        if type(keyword) == str:
            if keyword in self.topic_map.keys():
                ret = [(keyword,1.0)]
            keyword = ""
        else:
            _keyword = []
            for k in keyword:
                if k in self.topic_map.keys():
                    ret.append((k,1.0))
                else:
                    _keyword.append(k) 
            keyword = _keyword

        keyword_rels = set(self.get_related_keywords(keyword,self.keyword_map_rel,_score=False))

        if len(keyword_rels) > 0:
            for topic,topic_rels in self.topic_map.items():
                alike = keyword_rels.intersection(topic_rels)
                score = (len(alike) * (100/len(keyword_rels)))/100
                ret.append((topic,round(score,3)))
            ret.sort(key=lambda x : x[1], reverse=True)
        ret = [t for t in ret if t[1] >= cut]
        
        return ret
    
    def save(self,filename):
        with open(f"{filename}","wb") as fp:
            pickle.dump(self,fp)
            
        return self
    
    def load(self,filename):
        with open(filename,"rb") as fp:
            self = pickle.load(fp)
        return self
    

def create_model(filename,docs,topics):
    model = KeywordAnalyzer()
    model.prepare(docs,topics)
    model.save(filename)
    return model

def load_model(filename):
    model = KeywordAnalyzer()
    model = model.load(filename)
    return model