## About
- OS : Windows 10
- Language : python 3.6.4
- Library : 
  - [jieba](https://github.com/fxsjy/jieba)
  - opencc
  - [SnowNLP](https://github.com/isnowfy/snownlp)
## Preparation
- 安裝 python 3.x (32bit)
  1. 到 https://www.python.org/downloads/ 下載
  2. 記得將 add python 3.x to path 打勾
  3. 安裝進行到 Optional Features 階段時請將 pip 打勾
- 安裝 jieba, opencc, SnowNLP
  1. 以管理員身分打開命令提示字元
  2. 輸入以下指令
  ```
  pip3 install jieba
  pip3 install opencc-python
  pip3 install snownlp
  ```
  > 註：我用 pip install opencc 的時候出了點問題，後來到 https://pypi.python.org/pypi/opencc-python/ 下載 source code，解壓縮之後再放到 C:\Program Files (x86)\Python36-32\Lib\site-packages 下面
