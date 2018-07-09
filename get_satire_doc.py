import pandas as pd
import numpy as np
import io 
#https://stackoverflow.com/questions/19591458/python-reading-from-a-file-and-saving-to-utf-8/19591815

# test_df_satire = pd.read_csv('tribune.csv')
# doc_df = test_df_satire[["paras"]]

# doc_ex = test_df_satire.loc[2, 'paras']
# print(type(doc_ex))
# satire_file = 'satire_tribune.txt'

# def list2file(doc_df, file):
#     with io.open(file,'w',encoding='utf8') as f:
#         for i, doc in doc_df.iterrows():
#             print('inloop:',i)
#             print(type(doc))
#             doc = test_df_satire.loc[i, 'paras']
#             f.write(doc)
#             f.write('\n******\n')

# list2file(doc_df,satire_file)

test_df_satire = pd.read_csv('spoof.csv')
doc_df = test_df_satire[["doc"]]

doc_ex = test_df_satire.loc[3, 'doc']
print(type(doc_ex))
print(doc_ex)
satire_file = 'satire_spoof.txt'

def list2file(doc_df, file):
    with io.open(file, 'w',encoding='utf8') as f:
    # with open(file, 'w') as f:
        for i, doc in doc_df.iterrows():
            print('inloop:',i)
            # print(type(doc))
            doc = test_df_satire.loc[i, 'doc']
            f.write(doc)
            f.write('\n******\n')

list2file(doc_df,satire_file)


