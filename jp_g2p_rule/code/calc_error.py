import json
from pickletools import string1
import epitran
import collections
import Levenshtein

with open('proc_jpn_kana_narrow.json', 'r') as f:
    dic = json.load(f)

epi = epitran.Epitran('jpn-Ktkn')

# Function to remove chr(865), applied to epi.transliterate(str).
def remove_tie(str):
    if chr(865) in str:
        str = str.replace(chr(865), '')
    return str

# Add notations of IPA converted by own our rule
new_dic = {}
for k,v in dic.items():
    new_dic[k] = [v, remove_tie(epi.transliterate(k))]

# WER
word_error_keyL = []
word_error_dic = {}
for k, vL in new_dic.items():
    if vL[0] != vL[1]:
        word_error_keyL.append(k)
        word_error_dic[k] = vL
print(len(word_error_keyL) / len(new_dic))

# word errorに引っかかったkey, valuesを出力
with open('word_error.json', 'w') as f:
    json.dump(word_error_dic, f, ensure_ascii=False, indent=0)

# PER
levL = []
len_vL0 = []
for vL in new_dic.values():
    levL.append(Levenshtein.distance(vL[0], vL[1]))
    len_vL0.append(len(vL[0]))
print(sum(levL) / sum(len_vL0))