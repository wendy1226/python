from ckiptagger import WS, POS, NER
import pandas as pd
import time
#path
ws = WS("C:/Users/acer/AppData/Local/Programs/Python/Python39/Lib/site-packages/ckiptagger/data") #斷詞
pos = POS("C:/Users/acer/AppData/Local/Programs/Python/Python39/Lib/site-packages/ckiptagger/data") #詞性標註
ner = NER("C:/Users/acer/AppData/Local/Programs/Python/Python39/Lib/site-packages/ckiptagger/data") #命名實體識別

#要斷的句子
sentence_list = [
"這到底在公三洨w很明顯非台灣原住民最近明明滿涼的",
"啥時",
"北七粉紅祝他早日享受黨的愛",
"看那個標題”中共用詞”",
"先撇除加壓馬達的問題你家的馬桶為什麼會在短時間塞滿屎啊",
"這種情況正在大陸東北，江蘇等地發生，他們照搬文字就可以了，真方便",
"三小時內大便堆滿馬桶",
"這家人好會拉屎，是台灣之光。",
"堆滿了大便，怎麼會用水沖？是要換腦啊！",
"早上5:00就可以大便喔真的是腸胃很好",
"劇本抄襲",
"可能是屎大克星人 馬桶要加大 水流要加壓馬達來沖",
"早上六點42就沒水可以沖大便?他家沒水塔?",
"「啥 」露餡了",
"這篇作文零分，國文死當 ",
"他中國停電是因為習近平死了",
"一停電，全家人大便大到馬桶堆起來?",
"我在南部，冷氣3點就設定停了，睡到天亮都很舒服😌真不知文中的人他是睡在正在煮飯瓦斯爐旁邊嗎？",
"智障文章",
"台灣也不必認他們是自己人。",
"一般公寓大樓，特別是山坡地社區，平均都五層樓以上。高樓層住戶日常都會需要馬達抽水來維持正常供水。碰上停電就導致整棟樓特別是高樓層連馬桶都沒水可用，是很常見的情況。也不是每一個社區或住宅大樓都有自己的備用發電機。（重要單位多的建築通常地下室會有）冰箱的部分，若是那種老舊且長期不手動除霜的，那碰上停電在室溫32度下，四小時左右開始滴水也是很常見的事情。如果排水孔本就有阻塞或是箱體老舊密封出問題，那漏水也不是啥新鮮事。（當然都這樣了最好換台新的，舊機可以考慮捐給里辦的資收活動）有些人自稱為在地的民兵組織，卻缺乏在地的生活常識，恐怕到時候連搞恐怖攻擊都未必能勝任。這些人應該先去社區管委甚至是里辦公室培養一下經驗。老話，靠這些人，死得更早而已。",
"你們不覺得自從朱立倫選上之後國民黨整個活躍起來了嗎？ 看來江啟臣真的是不被青睞的黨主席，中國的資源完全不想幫他製造聲量"

]

word_sentence_list = ws(
    sentence_list,
    sentence_segmentation = True, # To consider delimiters 分隔符號
    segment_delimiter_set = ({",", "。", ":", "?", "!", ";"}), # This is the defualt set of delimit$
    # recommend_dictionary = dictionary1, # words in this dictionary are encouraged
    # coerce_dictionary = dictionary2, # words in this dictionary are forced
)

pos_sentence_list = pos(word_sentence_list)
# print('WS: ', word_sentence_list)
# print('POS: ', pos_sentence_list)
df = {'comment':[],'pos':[]}
#三個步驟組合
def combine_wandp(word_sentence_list, pos_sentence_list):
    assert len(word_sentence_list) == len(pos_sentence_list)
    for w, p in zip(word_sentence_list, pos_sentence_list):
        print ('{}({})'.format(w, p), end='\u3000')

time.sleep(3)
for c in word_sentence_list:
    df['comment'].append(c)
for p in pos_sentence_list:
    df['pos'].append(p)
df = pd.DataFrame.from_dict(df) # 直的
time.sleep(3)
df.to_csv("segword101-122.csv",index = False,encoding='utf-8-sig')