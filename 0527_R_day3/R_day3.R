heart <- read.csv("c:\\Users\\ilifo\\Desktop\\R\\Data\\heart.csv", 
                  header=T, row.names="X", stringsAsFactors=T)
str(heart)
head(heart)
table(is.na(heart))

my.rm.na1 <- function(df) {
   for (i in 1:length(df)) {
      if (any(is.na(df[,i]))) {
         df[,i] <- ifelse(is.na(df[,i]), mean(as.integer(df[,i]), na.rm=T),
                                         df[,i])   
      }
   }
   return (df)
}

heart.new <- my.rm.na1(heart)
table(is.na(heart.new))
str(heart.new)
summary(heart.new)
heart.new$Thal <- as.factor(heart.new$Thal)
levels(heart.new$Thal)

v1 <- c(T,F,T,T,F)
v2 <- 1:5
v1;v2

v2[v1] <- c(100,200,300,400,500)
v2
!v1
v2[!v1] <- 10
v2

tapply(v2, v1, sum)

x <- c(1,5,8,5,7,10,11,3,4,7)
y <- c(1:10)
z <- c(3.5,2.2,1.5,4.6,6.9,3.5,2.2,1.5,4.6,6.9)

plot(x,y,main="PLOT",sub="Test",xlab="x",ylab="y",type="n")

points(z, pch=1, cex=1)
points(z, pch=5, cex=1)
points(z, pch=11, cex=1)

boxplot(x,z)
pie(x)
barplot(x)
hist(x)

a <- data.frame(x,y)
pairs(a)

library(MASS)
a <- data.frame(x,y,z)
parcoord(a)

install.packages("dplyr")
library(dplyr)
library(ggplot2)

str(mpg)
mpg <- as.data.frame(mpg)

df_mpg <- mpg %>%
  group_by(drv) %>%
  summarise(mean_hwy = mean(hwy))

str(df_mpg)

ggplot(data = df_mpg, aes(x = reorder(drv, -mean_hwy), y = mean_hwy)) + geom_col()

install.packages("foreign")  # foreign 패키지 설치
library(foreign)             # SPSS 파일 로드
library(dplyr)               # 전처리
library(ggplot2)             # 시각화
library(readxl)              # read xls 파일

raw_welfare <- read.spss(file = "C:\\Users\\ilifo\\Desktop\\R\\Data\\Koweps_hpc10_2015_beta1.sav",
                         to.data.frame = T)
str(raw_welfare)
welfare <- raw_welfare

welfare <- rename(welfare,
                  sex = h10_g3,            # 성별
                  birth = h10_g4,          # 태어난 연도
                  marriage = h10_g10,      # 혼인 상태
                  religion = h10_g11,      # 종교
                  income = p1002_8aq1,     # 월급
                  code_job = h10_eco9,     # 직종 코드
                  code_region = h10_reg7)  # 지역 코드

welfare <- welfare[,c("sex","birth","marriage","religion","income","code_job","code_region")]
str(welfare)
welfare <- na.omit(welfare)
str(welfare)

summary(welfare)

welfare <- welfare[welfare$income!=0,]
str(welfare)
welfare$sex <- as.factor(welfare$sex)
welfare$marriage <- as.factor(welfare$marriage)
welfare$religion <- as.factor(welfare$religion)
welfare$code_job <- as.factor(welfare$code_job)
welfare$code_region <- as.factor(welfare$code_region)
str(welfare)
summary(welfare)   

my.quantile <- function(vec) {
   ret <- c()
   for (i in 1:length(vec)) {
      if (vec[i] < quantile(vec)[2]) {
         ret <- c(ret, paste("<",quantile(vec)[2]))
      } else if (vec[i] < quantile(vec)[3]) {
         ret <- c(ret, paste(quantile(vec)[2], "< >", quantile(vec)[3]))
      } else if (vec[i] < quantile(vec)[4]) { 
         ret <- c(ret, paste(quantile(vec)[3], "< >", quantile(vec)[4]))
      } else {
         ret <- c(ret, paste(">", quantile(vec)[4]))
      }
   }

   return (ret)
}   

my.quantile(c(1,2,3,4,5))

welfare$ages = as.factor(my.quantile(welfare$birth))
str(welfare)

df <- as.data.frame(tapply(welfare$income, list(welfare$ages,welfare$sex), mean))
str(df)
df
df$ages <- rownames(df)

df