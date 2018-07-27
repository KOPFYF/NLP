import time 
import re
from nltk import tokenize

class ListNode(object):
    def __init__(self, x):
        self.val = x # embedding
        self.next = None

from allennlp.predictors import Predictor
srl_predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/srl-model-2018.05.25.tar.gz")
coref_predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/coref-model-2018.02.05.tar.gz")

def get_srl(sent):
    start_time = time.time()
    results_srl = srl_predictor.predict(sentence=sent)
    # print(results_srl)
    elapsed_time = time.time() - start_time
    print("time for allennlp srl:", elapsed_time)
    for verb_dict in results_srl["verbs"]:
        # print(verb_dict['description'],type(verb_dict['description']))
        if 'ARG' in verb_dict['description']:
            return verb_dict

def build_event_linked_list(sent):
    srl = get_srl(sent) 
    # para = 'Did [ARG0: Uriah] [ARGM-MNR: honestly] [V: think] [ARG1: he could beat The Legend of Zelda in under three hours] ?'
    if re.search(r"(\[ARG0: )(.*?)(\])",srl['description']):
        arg0 = re.search(r"(\[ARG0: )(.*?)(\])",srl['description'])[2]
        print(arg0)
    else:
        arg0 = ''
    if re.search(r"(\[ARG1: )(.*?)(\])",srl['description']):
        arg1 = re.search(r"(\[ARG1: )(.*?)(\])",srl['description'])[2]
        print(arg1)
    else:
        arg1 = ''
    if re.search(r"(\[ARGM-MNR: )(.*?)(\])",srl['description']):
        mod = re.search(r"(\[ARGM-MNR: )(.*?)(\])",srl['description'])[2]
        print(mod)
    else:
        mod = ''
    verb = srl['verb']
    print(verb)
    node_arg0,node_arg1,node_mod,node_v = ListNode(arg0),ListNode(arg1),ListNode(mod),ListNode(verb)
    head = node_arg0
    node_arg0.next = node_v
    node_v.next = node_arg1
    node_arg1.next = node_mod
    return head

# build_event_linked_list()


def get_coref():

    start_time = time.time()
    with open('bbcnews.txt','r') as f:
        doc = f.read()
    print('doc:','\n',doc)
    sents = tokenize.sent_tokenize(doc)
    print('sentence:','\n',sents)
    # doc = 'Did Uriah honestly think he could beat The Legend of Zelda in under three hours?'
    results_coref = coref_predictor.predict(document=doc)
    print(results_coref)
    for index, cluster in enumerate(results_coref["clusters"]):
        print(index, cluster,'\n')
    for sent in sents:
        sent_head = build_event_linked_list(sent)
    elapsed_time = time.time() - start_time
    print("time for allennlp coref:", elapsed_time)

get_coref()
