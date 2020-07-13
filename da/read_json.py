#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: lpx
@Date: 2020-07-13 20:16:37
@LastEditTime: 2020-07-13 20:44:37
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /JD_project_2/da/read_json.py
'''

import json
import jieba
from data_utils import write_samples


samples = set()

with open('data/服饰_50k.json', 'r', encoding='utf8') as file:
    jsf = json.load(file)

for jsobj in jsf.values():
    title = jsobj['title'] + ' '
    kb = dict(jsobj['kb']).items()
    kb_merged = ''
    for key, val in kb:
        kb_merged += key+' '+val+' '

    ocr = ' '.join(list(jieba.cut(jsobj['ocr']))).replace('，', '')
    texts = []
    texts.append(title + kb_merged + ocr)
    texts.append(title + ocr + kb_merged)
    reference = ' '.join(list(jieba.cut(jsobj['reference'])))
    for text in texts:
        sample = text.replace('｜', '，')+' ｜ '+reference.replace('｜', '，')
        samples.add(sample)

write_samples(samples, 'output/samples.txt')
