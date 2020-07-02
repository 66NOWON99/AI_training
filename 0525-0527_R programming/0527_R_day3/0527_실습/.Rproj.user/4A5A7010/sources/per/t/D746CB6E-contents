ht<-read.csv("C:\\Users\\user\\Desktop\\0526_R_day2\\Heart.csv")
ht
str(ht)

ht%>%filter(!is.na(Ca))
ht%>%filter(is.na(Ca))
ht<-na.omit(ht)
ht

table(is.na(ht))

ht

##########해설
ht<-read.csv("C:\\Users\\user\\Desktop\\0526_R_day2\\Heart.csv",header = T,row.names="X",stringsAsFactors = T)
#row.names="X" >> "X"라는 이름의 COL에 대해서는 ROW의 이름으로 넣겠다
#Categorical data는 factor로 설정한다>stringsAsFactors = T
ht
str(ht)
head(ht)
table(is.na(ht))

#na.omit 작동원리
my.rm.na <- function(df){
  rmv <- c()
  for( i in 1:nrow(df)){
    if (any(is.na(df[i,]))){  #col의 모든 행을 확인해서 any; 행이 하나라도 T면(is.na=T면) 값이 T가 된다.
      rmv <- c(rmv, i)
    }
  }
  return (df[-rmv,])
} 

ht.new<-my.rm.na(ht)
ht.new
table(is.na(ht.new))

ht.new1<-na.omit(ht)
table(is.na(ht.new1))
