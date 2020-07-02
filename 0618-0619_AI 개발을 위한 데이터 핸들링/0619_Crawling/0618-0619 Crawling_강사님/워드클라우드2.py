#워드클라우드.py
#워드클라우드 - 단어를 분석해서 

"""
pip install wordcloud
pip install konlpy   
pip install pytagcloud
pip install pygame 
pip install simplejson 

문서를 읽어서 단어를 분리작업을 한다 
단어의 등장 회수를 세서 
등장 회수별로 많은가 중앙에 크게나오게 점점 작게 

"""


#단어 배열을 생성 
print (['korea' for t in range(8) ])

file = open("data.txt", "r", encoding="utf8")
read_data = file.read() 
file.close() 

#명사를 추출하기
#자연어 해석 도와주는 라이브러리 
import nltk 
from konlpy.tag import  Okt  #Twitter -> Okt 

okt = Okt()
nounList = okt.nouns(read_data)
print( nounList[:5])

from collections import Counter 
#각 단어마다 {korea:180, rabbit:20 ....  }
word_count = Counter(nounList)
print( word_count )

import pytagcloud

#pytagcloud 그래픽 정보를 만든다  -- list of tuple 
#{'korea':180, 'cloud':100...} -> [ ('korea', 180), ('cloud', 100)....]
tag = word_count.most_common(50)
print(tag)

#차트를 그리기 위한 정보 추가 
tagList = pytagcloud.make_tags(tag, maxsize=80)
print(tagList)

pytagcloud.create_tag_image(tagList, 'firstcloud.png', size=(600,500), 
        fontname = "Korean",
      rectangular=False)
