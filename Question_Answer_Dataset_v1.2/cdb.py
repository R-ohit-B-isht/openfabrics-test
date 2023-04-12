import pip
import sys
import os
import math
import subprocess
# subprocess.check_call([sys.executable, '-m', 'pip', 'install',
# 'pandas'])
# subprocess.check_call([sys.executable, '-m', 'pip', 'install',
# 'numpy'])
# subprocess.check_call([sys.executable, '-m', 'pip', 'install',
# 'spacy'])
# subprocess.check_call([sys.executable, '-m', 'pip', 'install',
# 'sklearn'])

import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
import csv
from nltk.tag import pos_tag # for proper noun,
from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd
import numpy as np
from nltk.stem import PorterStemmer
import re
import spacy
from spacy import displacy

# NER = spacy.load("en_core_web_sm")
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()

