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

nounList = list()
nounList.extend( ['korea' for t in range(180)] )
nounList.extend( ['rabbit' for t in range(20)] )
nounList.extend( ['carot' for t in range(15)] )
nounList.extend( ['law' for t in range(30)] )
nounList.extend( ['arrest' for t in range(80)] )
nounList.extend( ['cloud' for t in range(90)] )
nounList.extend( ['machine' for t in range(8)] )
nounList.extend( ['deeplearning' for t in range(75)] )
nounList.extend( ['peach' for t in range(15)] )
nounList.extend( ['banana' for t in range(66)] )
nounList.extend( ['orange' for t in range(99)] )
nounList.extend( ['작약' for t in range(299)] )
nounList.extend( ['장미' for t in range(99)] )
nounList.extend( ['수국' for t in range(99)] )
nounList.extend( ['국화' for t in range(99)] )
nounList.extend( ['불두화' for t in range(99)] )
nounList.extend( ['벚꽃' for t in range(99)] )
nounList.extend( ['진달래' for t in range(99)] )


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
