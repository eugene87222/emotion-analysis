# coding: utf-8

import simpleNLP

var = simpleNLP.simpleNLP(u'''如果知道最後還是會分手那麼之前還會選擇在一起嗎''')

print (var.sentiments_snowNLP())  # 情緒為 positive 的機率 (SnowNLP)

print (var.sentiments_baidu())  # 情緒為 positive 的機率 (BaiduNLP)

print (var.parse_words_snownlp()) # 用 snownlp 斷詞

print (var.parse_words_baidu())   # 用 baidu 斷詞

print (var.parse_words_jieba())   # 用 jieba 斷詞