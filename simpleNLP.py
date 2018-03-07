# coding: utf-8

import warnings
warnings.filterwarnings('ignore') # 忽略警告訊息 (warning)

import jieba    # 結巴分詞
import opencc   # 繁簡體轉換
from snownlp import SnowNLP  # 情緒分析

class Emotion_analysis:
	def __init__(self, text):
		cc = opencc.OpenCC('mix2s')
		self.text_s = cc.convert(text)
		self.text_t = text

	def sentiments_percent(self):
		s = SnowNLP(self.text_s)
		return s.sentiments

	def snownlp_parse_words(self):
		s = SnowNLP(self.text_s)
		return s.words

	def jieba_parse_words(self):
		jieba.set_dictionary('dict.txt.big')
		return jieba.lcut(self.text_t, cut_all=False)
