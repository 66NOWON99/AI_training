heart<-read.csv("C:\\Users\\ilifo\\Desktop\\0526_R_day2\\Heart.csv",header = T,row.names="X",stringsAsFactors = T)
heart

library(dplyr)

my.rm.na <- function(df){
  rmv <- c()
  for( i in 1:nrow(df)){
    if (any(is.na(df[i,]))){  #col의 모든 행을 확인해서 any; 행이 하나라도 T면(is.na=T면) 값이 T가 된다.
      print(df[i,])
      rmv <- c(rmv, i)#na 가 있는 행들을 따로 모았음
      
      
    }
  }
  return (df[-rmv,])#모은 행들을 마지막에 제외함; 작동 중에 index가 엉키는 것을 막기위해서
} 
heart.new<-my.rm.na(heart)
heart[-3,1]
heart[3,1]
#1
my.rm.na <- function(df){
  for( i in 1:nrow(df)){
    if (any(is.na(df[i,]))){ 
      for(j in 1:ncol(df)){
        if(is.na(df[i,j])==TRUE){
          col<-df[-i,j]
          df[i,j]=mean(col,na.rm=T)}
      
      }
    }
  }
  return (df)
}

ht.new<-my.rm.na(heart)
table(is.na(ht.new))
table(is.na(heart))
#2
tapply(heart$Chol,list(heart$AHD,heart$Sex),mean)


##3
heart%>%filter(heart$ChestPain=="typical"&heart$Chol>mean(heart$Chol))%>%select(ChestPain,Chol,AHD)

#4
x<-heart%>%filter(heart$Age>mean(heart$Age))
x$AHD.N.Y<-ifelse(x$AHD=="Yes",1,0)
x
x<-x[,-c(2:13)]
x
