import jieba
import jieba.analyse
# 1、分词----HMM
# 导入词典：
jieba.load_userdict('mydict.txt')
# filename：'北京清华' 1 n

# 全模式
text = "我来到北京清华大学"
seg_list = jieba.cut(text, cut_all=True)
print(u"[全模式]: ", "/ ".join(seg_list))

# 精确模式
seg_list = jieba.cut(text, cut_all=False)
print(u"[精确模式]: ", "/ ".join(seg_list))

# 默认是精确模式
seg_list = jieba.cut(text)
print(u"[默认模式]: ", "/ ".join(seg_list))

# 搜索引擎模式
seg_list = jieba.cut_for_search(text)
print(u"[搜索引擎模式]: ", "/ ".join(seg_list))

#2、词性标注
import jieba.posseg as pseg
words =pseg.cut("我爱北京天安门")
for w in words:
   print(w.word,w.flag)
# 3、关键词提取
content=open('text2tags').read()
tags = jieba.analyse.extract_tags(content, topK=2)
print(",".join(tags))
