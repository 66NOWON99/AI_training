
#library(ggplot2)
library(dplyr)
heart<-read.csv("C:\\Users\\ilifo\\Desktop\\0526_R_day2\\Heart.csv",header = T,row.names="X",stringsAsFactors = T)


my.rm.na <- function(df){
  rmv <- c()
  for( i in 1:length(df)){ #length// col개수
    if (any(is.na(df[,i]))){  #col의 모든 행을 확인해서 any; 행이 하나라도 T면(is.na=T면) 값이 T가 된다.
      df[,i]<-ifelse(is.na(df[,i]),mean(as.integer(df[,i]),na.rm=T ),df[,i])
      #factor값을 int로 바꿈 as.integer
    }
  }
  return (df) 
} 

#is.na(heart[,13]) #vector를 is.na에 넣으면 vector와 길이가 똑같은 논리형 vector가 return됨
#heart[,13] #vector
heart.new<-my.rm.na(heart)
heart.new
table(is.na(heart.new))


v1<-c(T,F,T,T,F)
v2<-1:5
v1;v2

v2[v1] <- 100
v2
 v2[!v1]<-10
v2 
tapply(v2,v1,sum)



############################
#데이터 시각화
x<-c(2,5,8,5,7,10,11,3,4,7)
y<-c(1:10)
z<-c(3.5,2.2,1.5,4.6,6.9,3.5,2.2,1.5,4.6,6.9)

plot(x,y,main="PLOT",sub="Test",xlab="x",ylab="y",type="n") 
#type="l": 점들이 나타내는 순서대로 이어지는 것
#type="s":계단형 (x축부터) S(y축부터)

#index가 x의 값이됨/ 위의 x vector는 boundary가됨
points(z,pch=1,cex=1) #type="n" , 동그라미
points(z,pch=5,cex=1) #마름모
points(z,pch=11,cex=1) #유다별
#pch=점의 타입, cex=점의 크기

boxplot(x,z)
pie(x) #data는 도수(개수)->전체에 대한 비율로 표시
barplot(x) #x=도수
hist(x)#x=data자체. 해당 데이터가 몇 개 나왔는지 표시해줌
#bias를 확인하려면 barplot보다 hist로 확인해야함.(histogram->정규분포처럼 종모양 곡선)

#산점도
a<-data.frame(x,y)
pairs(a)

library(MASS)
a<-data.frame(x,y,z)
parcoord(a)

ggplot(data=mpg, aes(x=displ, y=hwy)) + geom_point() + xlim(3,6)+ylim(10,30)

library(dplyr)
mpg 
mpg<-as.data.frame(mpg) #ggplot2
str(mpg)#tibble->data.frame format
df_mpg <- mpg %>%
  group_by(drv)%>%
  summarise(mean_hwy = mean(hwy))
df_mpg

ggplot(data=df_mpg, aes(x=drv, y=mean_hwy))+geom_col()
ggplot(data=df_mpg, aes(x=reorder(drv,+mean_hwy), y=mean_hwy))+geom_col()

################################################################################################################
install.packages("ggplot2")
install.packages("foreign")
install.packages("readxl")

library(foreign)
library(dplyr)
library(ggplot2)
library(readxl)

raw_welfare <- read.spss(file="C:\\Users\\ILIFO-017\\Desktop\\backup-20200527\\0527_R_day3\\Koweps_hpc10_2015_beta1.sav",to.data.frame=T)

welfare <- raw_welfare
welfare <-rename(welfare,sex=h10_g3, birth=h10_g4, marriage=h10_g10, religion = h10_g11, income=p1002_8aq1, 
                 code_job=h10_eco9, code_region=h10_reg7)


head(welfare)
str(welfare)
tail(welfare)
View(welfare)

#View(welfare%>%filter(welfare$sex!=3 & welfare$income==0))
#table(is.na(welfare$sex))

#welfare_s <-welfare%>%group_by(sex & income)%>%filter(welfare$sex!=3 & welfare$income!=0) 
welfare_s <-welfare%>%filter(welfare$sex!=3 & welfare$income!=0) 
ncol(welfare_s)

#View(welfare_s$sex)
#length(welfare$sex)
#length(welfare_s$sex)
#length(welfare$income)
#length(welfare_s$income)
#View(welfare_s)
#table(is.na(welfare_s))
#View(welfare_s$marriage)

table(welfare_s$income)
income_mean<-tapply(welfare_s$income,welfare_s$sex,mean)
income_mean
length(income_mean)
length(x)
x<-c(1,2)
ggplot(data=welfare_s,aes(x=x,y=income_mean)) + geom_col()
geom_bar(data=welfare_s,aes(x=welfare_s$sex,y=welfare_s$income))

plot(welfare_s$income)
barplot(income_mean)

barplot(income_mean~x)
####
#1.성별에 따른 월급 차이

barplot(mean(welfare$income,na.rm = T))


welfare_1 <-welfare%>%filter(welfare$sex!=3 & welfare$income>=0) 
income_mean<-tapply(welfare_1$income,welfare_1$sex,mean)
barplot(income_mean)
#####


#2.나이와 월급의 관계
tapply(welfare)
table(is.na(welfare$birth))
table(is.na(welfare$income))

welfare_2 <-welfare%>%filter(welfare$income>=0) 
table(is.na(welfare_2$income))

#plot(tapply(welfare_2$income,welfare_2$birth,median))

#plot(tapply(welfare_2$income,welfare_2$birth,mean))
#plot(tapply(welfare_2$income,welfare_2$birth,max))
#plot(tapply(welfare_2$income,welfare_2$birth,min))

#plot(tapply(welfare_2$birth,welfare_2$income,max))

plot(x=welfare$birth,y=welfare$income,xlab="Birth(year)",ylab="Income",main = "Birth vs Income")
qplot(x=welfare_2$birth,y=welfare_2$income,xlab="Birth(year)",ylab="Income",main = "Birth vs Income")

qplot(x=welfare$birth,y=welfare$income,xlab="Birth(year)",ylab="Income",main = "Birth vs Income")

#+xlim(min(welfare$birth),max(welfare$birth))

#k<-data.frame(x=welfare_2$birth,y=welfare_2$income)
#parcoord(k)
#welfare_2 %>%   ggplot(aes(welfare_2$birth, welfare_2$income))+ geom_jitter()

######################################################################

plot(welfare_2$income~welfare_2$birth,data=welfare_2)
ggplot(data=welfare_2,aes(x=welfare_2$birth,y=welfare_2$income)) + geom_point()


#3.연령대에 따른 월급 차이
min(welfare$birth)
max(welfare$birth)

welfare_3 <-welfare%>%filter(welfare$income!=0) 
welfare_3$ages <- ifelse(welfare_3$birth>2010,0,
                         ifelse(welfare_3$birth>2000,10,
                                ifelse(welfare_3$birth>1990,20,
                                       ifelse(welfare_3$birth>1980,30,
                                              ifelse(welfare_3$birth>1970,40,
                                                     ifelse(welfare_3$birth>1960,50,
                                                            ifelse(welfare_3$birth>1950,60,
                                                                   ifelse(welfare_3$birth>1940,70,
                                                                          ifelse(welfare_3$birth>1930,80,
                                                                                 ifelse(welfare_3$birth>1920,90,100))))))))))
welfare_3$ages

#전처리 전
boxplot(welfare$income~welfare$birth,xlab="Ages",ylab="Income",main="Ages vs Income")  

#전처리 후
boxplot(welfare_3$income~welfare_3$ages,xlab="Ages",ylab="Income",main="Ages vs Income")  

#####################################################################
#4. 연령대 및 성별 월급 차이

#전처리 전
ggplot(welfare, aes(x=birth, y=income, fill=as.factor(sex))) + geom_bar(stat='identity', position = 'dodge') 


library(MASS)
welfare_4 <-welfare%>%filter(welfare$sex!=3 & welfare$income>=0)
welfare_4$ages <- ifelse(welfare_4$birth>2010,0,
                         ifelse(welfare_4$birth>2000,10,
                                ifelse(welfare_4$birth>1990,20,
                                       ifelse(welfare_4$birth>1980,30,
                                              ifelse(welfare_4$birth>1970,40,
                                                     ifelse(welfare_4$birth>1960,50,
                                                            ifelse(welfare_4$birth>1950,60,
                                                                   ifelse(welfare_4$birth>1940,70,
                                                                          ifelse(welfare_4$birth>1930,80,
                                                                                 ifelse(welfare_4$birth>1920,90,100))))))))))


set<-data.frame(ages=welfare_4$ages,sex=welfare_4$sex,income=welfare_4$income)
set
library(ggplot2)

#전처리 후
ggplot(set, aes(x=ages, y=income, fill=as.factor(sex))) + geom_bar(stat='identity', position = 'dodge') 


###
#참고코드: ggplot(sleep, aes(ID, extra, fill=group))+geom_bar(stat='identity') 


#######################################
#5.직업별 월급 차이
#전처리 전
boxplot(welfare$income~welfare$code_job,xlab="Job",ylab="Income",main="Job vs Income")  

table(is.na(welfare$code_job))

welfare_5<-welfare%>%filter(is.na(welfare$code_job)==FALSE)
table(is.na(welfare_5$code_job))

#전처리 후
#직업의 분야를 나누는 기준을 알 수 없기에 모든 직업을 포함하는 그래프로 표시했다.
boxplot(welfare_5$income~welfare_5$code_job,xlab="Job",ylab="Income",main="Job vs Income")  


###########################################
#6.성별 직업 빈도
#전처리 전
set1<-data.frame(sex=welfare$sex,code_job=welfare$code_job)

ggplot(set1, aes(x=code_job,fill=as.factor(sex))) + geom_bar(position = 'dodge') 
plot(welfare$code_job,welfare$sex)#,xlab="Job",ylab="Income",main="Job vs Income")  

#전처리 후
table(is.na(welfare_6$code_job))

welfare_6<-welfare%>%filter(is.na(welfare$code_job)==FALSE & welfare$sex!=3)
set2<-data.frame(sex=welfare_6$sex,code_job=welfare_6$code_job)
ggplot(set2, aes(x=code_job,fill=as.factor(sex))) + geom_bar(position = 'dodge') 






#전처리 전
#...

####그래프 2개 그려놓고 색 다르게 합치기? TT
##전처리 후
welfare_6f<-welfare%>%filter(is.na(welfare$code_job)==FALSE & welfare$sex==2)
f<-data.frame(welfare_6f$sex,welfare_6f$code_job)
f
hist(x=f[,2],xlab="Code_Job",main="Frequency of Code_Job ;Sex=2")

welfare_6m<-welfare%>%filter(is.na(welfare$code_job)==FALSE & welfare$sex==1)
m<-data.frame(welfare_6m$sex,welfare_6m$code_job)
m

hist(x=m[,2],xlab="Code_Job",main="Frequency of Code_Job ;Sex=1")
?hist


#ggplot(data=welfare_6,aes(x=c[,2]))+geom_bar()
#ggplot(data=welfare_6,aes(x=welfare_6$code_job)) + geom_bar()
#min(welfare_6$code_job)

#welfare_6<-welfare%>%filter(is.na(welfare$code_job)==FALSE & welfare$sex==1)
#ggplot(data=welfare_6,aes(x=welfare_6$code_job)) + geom_bar()


#ggplot(data=welfare_6,aes(x=welfare_6$code_job),xlim=range(min(welfare_6$code_job),max(welfare_6$code_job))) + #geom_bar()
#min(welfare_6$code_job)

#plot(x=range(min(welfare_6$code_job),y=welfare_6$code_job)
#plot(x1, y1, type='p', xlim=range(x1,x2), ylim=range(y1,y2))



#7.종교 유무에 따른 혼인상태
#welfare$marriage
#welfare$religion
#table(is.na(welfare$religion))

##전처리 전
c<-data.frame(welfare$marriage,welfare$religion)
hist(c[,1],xlab='혼인 상태',main='혼인상태 vs Frequency')

##전처리 후
#종교 = 1
a<-welfare%>%filter(religion==1)
hist(x=a$marriage,xlab="marriage", main="Frequency of Marriage when Religion=1")

b<-welfare%>%filter(religion==2)
hist(x=b$marriage,xlab="marriage", main="Frequency of Marriage when Religion=2")


#####################
#qplot(data=c,x=c(1,2),y=c$religion,geom=boxplot())

set3<-data.frame(marriage=welfare$marriage,religion=welfare$religion)
ggplot(set3, aes(x=marriage,fill=as.factor(religion))) + geom_bar(position = 'dodge') 

###########################
##8. 지역별 연령대 비율

#전처리 전
tmp1<-data.frame(birth=welfare$birth,region=welfare$code_region,birth=welfare$birth)
ggplot(data=tmp1,aes(x=region,y=birth,fill=as.factor(birth)))+ geom_bar(stat='identity',position='fill')


#전처리 과정
table(is.na(welfare$code_region))

tmp<-data.frame(region=welfare$code_region,birth=welfare$birth)
tmp

tmp$ages <- ifelse(tmp$birth>2010,0,
                         ifelse(tmp$birth>2000,10,
                                ifelse(tmp$birth>1990,20,
                                       ifelse(tmp$birth>1980,30,
                                              ifelse(tmp$birth>1970,40,
                                                     ifelse(tmp$birth>1960,50,
                                                            ifelse(tmp$birth>1950,60,
                                                                   ifelse(tmp$birth>1940,70,
                                                                          ifelse(tmp$birth>1930,80,
                                                                                 ifelse(tmp$birth>1920,90,100))))))))))
tmp$ages
tmp


ggplot(data=tmp,aes(x=region,y=ages,fill=as.factor(ages)))+ geom_bar(stat='identity',position='fill')

