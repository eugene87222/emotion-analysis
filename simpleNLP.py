# coding: utf-8

import warnings
warnings.filterwarnings('ignore') # 忽略警告訊息 (warning)

import jieba    # 結巴分詞
import opencc   # 繁簡體轉換
from aip import AipNlp       # 百度NLP
from snownlp import SnowNLP  # 情緒分析

APP_ID = '10892513'
API_KEY = '0gnO2IciyrzPKWvN16FKoxeD'
SECRET_KEY = 'qeoiLP8dNEA7jolzcjD9AP9zqAiDR6H2'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

class simpleNLP:
	def __init__(self, text):
		cc = opencc.OpenCC('mix2s')
		self.text_s = cc.convert(text)
		self.text_t = text

	def sentiments_snowNLP(self):
		res = SnowNLP(self.text_s)
		return res.sentiments

	def sentiments_baidu(self):
		res = client.sentimentClassify(self.text_s)
		return res['items'][0]['positive_prob']

	def parse_words_snownlp(self):
		res = SnowNLP(self.text_s)
		return res.words

	def parse_words_baidu(self):
		res = client.lexer(self.text_s)
		res = [each['item'] for each in res['items']]
		return res

	def parse_words_jieba(self):
		jieba.set_dictionary('dict.txt.big')
		return jieba.lcut(self.text_t, cut_all=False)
