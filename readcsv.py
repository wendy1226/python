import pandas as pd
from ckiptagger import WS, POS, NER
import time

ws = WS("C:/Users/acer/AppData/Local/Programs/Python/Python39/Lib/site-packages/ckiptagger/data") #斷詞
pos = POS("C:/Users/acer/AppData/Local/Programs/Python/Python39/Lib/site-packages/ckiptagger/data") #詞性標註
ner = NER("C:/Users/acer/AppData/Local/Programs/Python/Python39/Lib/site-packages/ckiptagger/data") #命名實體識別

df=pd.read_excel("C:/Users/acer/Desktop/python/result/CheckedResult/crawler40.xlsx")
# print(df)

mylist = df['comment'].tolist()
print(mylist)
word_sentence_list = ws(
    mylist,
    sentence_segmentation = True,
    segment_delimiter_set = ({",", "。", ":", "?", "!", ";"}),)
pos_sentence_list = pos(word_sentence_list)
df = {'word':[],'pos':[]}
#三個步驟組合
def combine_wandp(word_sentence_list, pos_sentence_list):
    assert len(word_sentence_list) == len(pos_sentence_list)
    for w, p in zip(word_sentence_list, pos_sentence_list):
        print ('{}({})'.format(w, p), end='\u3000')
time.sleep(3)
for c in word_sentence_list:
    df['word'].append(c)
for p in pos_sentence_list:
    df['pos'].append(p)
df = pd.DataFrame.from_dict(df) # 直的
time.sleep(3)
df.to_excel("segword40.xlsx",index = False,encoding='utf-8-sig')
