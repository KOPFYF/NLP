# https://blog.csdn.net/AckClinkz/article/details/78538462
import pandas as pd
import numpy as np
import io
import re

test_df_satire = pd.read_csv('fox.csv')
print(test_df_satire.shape)
doc_texts = test_df_satire["doc_texts"]
# print(doc_texts)
# print(type(doc_texts.loc[1]))

# def para2doc(raw_doc, raw_para_list):



paras = test_df_satire.groupby(test_df_satire['doc_texts'])['paras'].apply(list).to_dict()
# print(paras)
# keys = paras.keys()
# values = paras.values()
# print(keys)
# for key in keys:
# 	key = re.split(,key)
# print(keys)

d = {}
for key, value in paras.items():
	value_list = []
	for i in value:
		i = i + '\n'
		value_list.append(i)
	d[key] = value_list
print(d.values())

# print(paras.shape)
# print(type(paras))
# print(paras)
# print(paras.shape)
# print(list(paras))
# for index,para in paras:
# 	print(type(index))
# 	print('************')
# 	print(type(para))

