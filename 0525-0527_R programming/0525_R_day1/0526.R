exam<-read.csv("C:\\Users\\user\\Desktop\\0525_R_day1\\Data\\csv_exam.csv")
exam
head(exam)
head(exam,10)
tail(exam)
tail(exam,10)
View(exam)
str(exam)
dim(exam)
summary(exam)
mpg<-as.data.frame(ggplot2::mpg)
mpg
head(mpg)
tail(mpg)
View(mpg)
dim(mpg)
str(mpg)
summary(mpg)



#ex
df<-data.frame(list(no=c(1,2,3,4,5),
                    name=c("Lee","Park","So","Kim","Yoon"),
                   age=c(45,47,35,26,29),
                   gender=c("M","F","M","F","M")))

#no가 2번인 data를 삭제하시오
df<-df[-2,]
df
#(Hwang,21,F),(Cho,39,M) 데이터를 추가하시오
df<-rbind(df,list(6,"Hwang",21,"F"))
df<-rbind(df,list(7,"Cho",39,"M"))
df
str(df)
#mean(df$age)
#연령대별 나이의 평균을 구하시오


#성별별 나이의 평균을 구하시오
tapply(df$age,df$gender,mean)
     
     
#해설
no<-c(1:5)
name<-c("Lee","Park","So","Kim","Yoon")
age<-c(45,47,35,26,29)
gender<-factor(c("M","F","M","F","M"))

d<-data.frame(no,name,age,gender)
str(d)
head(d)

#no가 2번인 data를 삭제하시오
d<-d[-2,]
d
#no가 index와 일치하지않을때
d<-d[d$no !=2,]
d

#(Hwang,21,F),(Cho,39,M) 데이터를 추가하시오
d<-rbind(d,list(6,"Hwang",21,"F"))
d<-rbind(d,list(7,"Cho",39,"M"))
d

#연령대별 나이의 평균을 구하시오
d$ages<-ifelse(d$age>=40,40,
               ifelse(d$age>=30,30,20))
d
tapply(d$age,d$ages,mean)

#성별별 나이의 평균을 구하시오
tapply(d$age,d$gender,mean)

#///////end////

x<- c(1:10)

#조건문
if(sum(x)>10){
  if(length(x)>5){
    print(mean(x))
  }else{
    print(length(x))
  }
}else{
  print(var(x))
}

#반복문
for(i in 1:5){
  print(i)
}

a<-1
while(a<=5){
  print(rep(a,a))
  a<- a+1
}

a<-1
repeat{
  if(a>5) break
  print(rep(a,a))
  a<-a+1
}

for(i in 1:50){
  print(2*i)
}

v2<-c()
for (i in 1:100){
  if(i%%2==0){
    v2<-c(v2,i)
    }
}
v2

v2<-c()
for(i in seq(2,100,2)){
  v2<-c(v2,i)
}
v2

my.mean <- function(x){
  return (sum(x) / length(x))
}
my.mean(1:5)
v1<-c(0,0,0,1,0,0,1,1,1)
first<-function(x){
  
  for(i in 1:length(x)){
    if(x[i]==1)return (i)  
    #else {i<-i+1} 
  }
}

first(v1)
#첫번째 1 이나오는 인덱스 값을 리턴하는 function

##해설
first1<-function(x){
  if(!is.vector(x)){
    print("Input object should be vector")
    return (NULL)
  }
  
  for ( i in 1:length(x)){
    if (x[i]==1) return (i)
  }
  return (NULL)
}

mat<- matrix(1:9, ncol=3)
first1(v1)
first1(mat)
first1(c(0,0,0,1))
first1(c(0,0,0,0,0))

ages<-function(x){
  ret<-c()
  for( i in 1:length(x)){
    if(x[i]>=40){
      ret<-c(ret,40)
    }
    else if(x[i]>=30){
      ret<-c(ret,30)
    } else{
      ret<-c(ret,20)
    }
  }
  return (ret)
}
d$ages3<-ages(d$age)
d

library(dplyr)
#install.packages("dplyr")

exam<-read.csv("C:\\Users\\user\\Desktop\\0525_R_day1\\Data\\csv_exam.csv")
exam%>%filter(class == 1)
exam%>%filter(class == 2)
exam%>%filter(class != 1)

exam%>%filter(math >= 50)
exam%>%filter(math < 50)

exam%>%filter(class==1 & math < 50)
exam%>%filter(english>70 | math < 50)
exam%>%filter(class==1 | class==3 | class==5)
exam%>%filter(class %in% c(1,3,5))

class1<-exam%>%filter(class==1)
class1
class2<-exam%>%filter(class==2)
class2
mean(class1$english)
mean(class2$science)

exam%>%select(math)
exam%>%select(english)
exam%>%select(english,science)
exam%>%select(-math)
exam%>%select(-math,-class)
exam%>%filter(class==1)%>%select(science)

exam%>%select(math,science)%>%tail

exam%>%arrange(math)
exam%>%arrange(desc(math))
exam%>%arrange(class,math)
exam%>%arrange(english,math)

exam%>%mutate(total=math+english+science) 
exam
exam%>%mutate(total=math+english+science, 
              mean=(math+english+science)/3) 
