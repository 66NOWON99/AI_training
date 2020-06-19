#워드클라우드.py
#워드클라우드 - 단어를 분석해서

"""
pip install wordcloud
pip install konlpy #한국 형태소 분석
pip install pytagcloud
pip install pygame
pip install simplejson

워드클라우드: 
문서를 읽어서 단어를 분리한다.
단어의 등장 횟수를 세서 등장 횟수별로 많은 것이 중앙에 크게나오고
적을수록 점점 작고 중앙에서 멀어진다.
""" 

#단어 배열을 생성
# print(['korea' for t in range(8)]) # for loop ; korea를 8번 반복출력
nounList = list()
nounList.extend(['korea' for t in range(180)])
nounList.extend(['south' for t in range(20)])
nounList.extend(['kimch' for t in range(18)])
nounList.extend(['ramen' for t in range(16)])
nounList.extend(['macitta' for t in range(14)])
nounList.extend(['baegopa' for t in range(12)])
nounList.extend(['bibimbob' for t in range(8)])
nounList.extend(['kuk-ak' for t in range(5)])
nounList.extend(['palace' for t in range(2)])
nounList.extend(['Queen-yeonA' for t in range(38)])
nounList.extend(['Tteokbokki' for t in range(38)])
nounList.extend(['kiwa-jip' for t in range(3)])
nounList.extend(['Hanbok' for t in range(22)])
nounList.extend(['Dalgona' for t in range(10)])
nounList.extend(['wairanoWairano' for t in range(8)])
nounList.extend(['cloud' for t in range(100)])



from collections import Counter 
#각 단어마다 {korea:180. south:20, ...}
word_count = Counter(nounList)
print(word_count)

import pytagcloud

#pytagclout : 그래픽 정보를 만든다  -- list of tuple
#타입전환중~
#most_common()= {'korea':'180', 'cloud' : 100} -> [('korea,180), ('cloud',100)]
tag = word_count.most_common(50)
print(tag)

#차트를 그리기 위한 정보 추가
tagList = pytagcloud.make_tags(tag,maxsize=80)
print(tagList)



pytagcloud.create_tag_image(tagList, 'firstcloud.jpg', size=(600,500), 
        fontname = "Korean",
      rectangular=False)

# HMFMMUEX

#C:\Users\ILIFO-017\anaconda3\Lib\site-packages\pytagcloud\fonts
#C:\Windows\Fonts\HMFMMUEX.ttf 