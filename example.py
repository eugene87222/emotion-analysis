import emotion

var = emotion.Emotion_analysis(u'我很開心，因為年終發很多')

print (var.sentiments_percent())  # 情緒為 positive 的機率

print (var.snownlp_parse_words()) # 用 snownlp 斷詞

print (var.jieba_parse_words())   # 用 jieba 斷詞