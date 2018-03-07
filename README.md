## About
- OS : Windows 10
- Language : python 3.6.4
- Library : 
  - [jieba](https://github.com/fxsjy/jieba)
  - opencc
  - [SnowNLP](https://github.com/isnowfy/snownlp)
  - [Baidu NLP Python SDK](https://cloud.baidu.com/product/nlp)
## Preparation
- 安裝 python 3.x (32bit)
  1. 到 https://www.python.org/downloads/ 下載
  2. 記得將 add python 3.x to path 打勾
  3. 安裝進行到 Optional Features 階段時請將 pip 打勾
- 安裝 jieba, opencc, SnowNLP, Baidu NLP
  1. 以管理員身分打開命令提示字元
  2. 輸入以下指令
  ```
  pip3 install jieba
  pip3 install opencc-python
  pip3 install snownlp
  pip3 install baidu-aip
  ```
  > 註：我用 pip install opencc 的時候出了點問題，後來到 https://pypi.python.org/pypi/opencc-python/ 下載 source code，解壓縮之後再放到 C:\Program Files (x86)\Python36-32\Lib\site-packages 下面
## example.py
``` python
  import simpleNLP

  var = simpleNLP.simpleNLP(u'''如果知道最後還是會分手那麼之前還會選擇在一起嗎''')

  print (var.sentiments_snowNLP())  # 情緒為 positive 的機率 (SnowNLP)
  # output: 0.9928669544056079

  print (var.sentiments_baidu())    # 情緒為 positive 的機率 (BaiduNLP)
  # output: 0.644316

  print (var.parse_words_snownlp()) # 用 snownlp 斷詞
  # output: ['如果', '知道', '最后', '还是', '会', '分手', '那么', '之前', '还会', '选择', '在', '一起', '吗']
  
  print (var.parse_words_baidu())   # 用 baidu 斷詞
  # output: ['如果', '知道', '最后', '还是', '会', '分手', '那么', '之', '前', '还会', '选择', '在一起', '吗']

  print (var.parse_words_jieba())   # 用 jieba 斷詞
  # output: ['如果', '知道', '最後', '還是', '會', '分手', '那麼', '之前', '還會', '選擇', '在', '一起', '嗎']
```
> 註：dict.txt.big 取自 [fxsjy/jieba 结巴中文分词](https://github.com/fxsjy/jieba) (繁體字典)

---
simpleNLP.py 裡面的程式碼都是別人開發好的，我只抓出我要的拿來用  
想了解更多有關 jieba, snowNLP, Baidu 自然語言處理 請到他們的官網
