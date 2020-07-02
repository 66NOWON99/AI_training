a <- 1
a
a <- 1.5
a
a <- "a"
a

c(1,2,3,4,5) + c(1,2,3)

c("1","2") + c("3","4")

var1 <- c(1,2,3,4,5)

mean(var1)
sd(var1)
var(var1)
sum(var1)
length(var1)
sum(var1)/length(var1)
sum((var1 - mean(var1)) * (var1 - mean(var1))) / (length(var1) - 1)

install.packages("ggplot2")
library(ggplot2)

x <- c("a", "a", "b", "c")
qplot(x)

x <- c(1,2,3,3)
qplot(x)

qplot(data = mpg, x = hwy)

mpg

x <- c(1,2,3,4)
x
x[3]
x[c(1,2)]
x[1:2]
x <- c(T,F,T)
x

height <- c(160, 140, 155)
people <- c("Ned", "Jill", "Pat")

height
people
names(height) <- people
height

height[1]
height["Ned"]
height[c("Ned","Pat")]
height[height>145]
height[c(T,T,F)]
height[x]

var1 <- c(1,2,43)
height[var1>1.5]

str <- c("Hello!","world","is","good!")
str
str[4]

max(str)
mean(str)
min(str)
sort(str)
range(str)
str
1:5
5:1

c(1,2,3,c(4,5))
v2 <- c(4,5)
v1 <- c(1,2,3)
c(v1,v2)
c(1,2,3,v2)

seq(1,5,2)
seq(0,1,length.out=100)

rep(c(1,2,3), times=2)
rep(c(1,2,3),2)
rep(c(1,2,3), each=2)

#c(), :, seq(), rep()

v1 <- seq(1,10)
v1
v1[c(2,4,6,8,10)]
v1[seq(2,10,2)]
v1[-c(1,3,5,7,9)]
v1[-seq(1,10,2)]

mat1 <- matrix(1:9, nrow=3)
mat1

length(mat1)
dim(mat1)
dim(v1)

mat2 <- matrix(v1, nrow=3)
mat2

mat2 <- matrix(v1, nrow=3, byrow=T)
mat2

mat1 <- matrix(1:9, nrow=3)
mat1
mat1 <- matrix(c(1,4,7,2,5,8,3,6,9), nrow=3, byrow=T)
mat1

r1 <- c(1,4,7)
r2 <- c(2,5,8)
r3 <- c(3,6,9)
rbind(r1,r2,r3)

c1 <- 1:3
c2 <- 4:6
c3 <- 7:9
cbind(c1,c2,c3)

m1 <- 1:9
m1
dim(m1)
dim(m1) <- c(3,3)
m1

mat1
mat1[1,1]
mat1[1,]
mat1[,1]
mat1[mat1[,3]>7, 1]

mat1[c(2,3),c(1,2)]
mat1[2:3,1:2]
mat1[c(F,T,T),c(T,T,F)]
mat1[mat1[,3]>7,mat1[1,]<7]

mat1
mat1[,1]
mat1[,1,drop=F]

t(mat1)
mat1 * mat1
mat1 %*% mat1

v1 <- 1:5
v2 <- c("a","b")
v1;v2

v3 <- c(v1, v2)
v3

lst <- list("a", c(2,3,4), c(T,F,T), matrix(1:9, nrow=3))
lst

lst1 <- list(a="a", b=c(2,3,4), c=c(T,F,T), d=matrix(1:9, nrow=3))
lst

length(lst)
names(lst);names(lst1)

lst[[2]][1]
lst1[[2]][1]
lst1$b[c(2,3)]

x <- list(list(1,2), c(3,4))
y <- c(list(1,2), c(3,4))

x;y

x[[2]] <- c(x[[2]],"a")
x

x[[1]]

length(x);length(y)

unlist(x);unlist(y)

people
names(height) <- NULL

df <- data.frame(people, height)
df

df[1,]
df[,2]
df$height
df[,2][1]
df$height[1]

df[1,2]
df[-1,]
df[-c(1,2),]

df_midterm <- data.frame(english = c(90, 80, 60, 70),
                         math = c(50, 60, 100, 20),
                         class = c(1, 1, 2, 2))

df_midterm

df_midterm[df_midterm$class==2 & df_midterm$math > 50,]
df_midterm[,df_midterm$class==2 & df_midterm$math > 50]
df_midterm[df_midterm$class==2 & df_midterm$math > 50]

df_midterm[df_midterm$class==2 & df_midterm$math > 50, "english"]
df_midterm[df_midterm$class==2 & df_midterm$math > 50, 1]

df_midterm$english

install.packages("readxl")
library(readxl)

#C:\Users\ilifo\Desktop\R\Data
getwd()

df_exam <- read_excel("C:\\Users\\ilifo\\Desktop\\R\\Data\\excel_exam.xlsx")
df_exam

str(df_exam)
summary(df_exam)

df_exam <- read.csv("C:\\Users\\ilifo\\Desktop\\R\\Data\\csv_exam.csv")
df_exam

df_test <- read.csv("C:\\Users\\ilifo\\Desktop\\R\\Data\\test.txt")
df_test 
str(df_test)

x <- factor(c("m","f","f","m"))
x

df_test <- cbind(df_test, gender=c("m","f","f","m"))
df_test
str(df_test)

df_test$gender <- factor(df_test$gender)
str(df_test)

df_test <- rbind(df_test, list(id=5,name="Cho",height=190,weight=100,gender="m"))
df_test

fl2000 <- read.table("C:\\Users\\user\\Desktop\\R_exercise\\fl2000.txt", header=T)
str(fl2000)
fl2000

fl2000 <- fl2000[,-c(2:5)]
str(fl2000)

county_sum <- fl2000[,2] + fl2000[,3] + fl2000[,4] + fl2000[,5] + 
              fl2000[,6] + fl2000[,7] + fl2000[,8] + fl2000[,9] + 
              fl2000[,10] + fl2000[,11] + fl2000[,12] + fl2000[,13]
 
fl2000_f <- cbind(fl2000, sum=county_sum)
str(fl2000_f)
fl2000_f <- fl2000_f[,-c(4:13)]
str(fl2000_f)
Total <- list("Total", sum(fl2000_f$Bush), sum(fl2000_f$Gore), sum(fl2000_f$sum))
Total

fl2000_f <- rbind(fl2000_f, Total)
str(fl2000_f)
head(fl2000_f)
tail(fl2000_f)




##
mat1 <-matrix(1:9,3)
mat1
apply(mat1,1,sum)
apply(mat1,2,sum)
#str(apply(mat1,2,sum))

apply(fl2000[2:13],1,sum)
fl2000_f <-cbind(fl2000, sum=apply(fl2000[2:13],1,sum))
#같은 결과: 
#fl2000_f$sum<-apply(fl2000[2:13],1,sum)
fl2000_f

fl2000_f <-fl2000_f[,-c(4:13)]
fl2000_f


Total<- c(list(county="Total"),apply(fl2000_f[,2:4],2,sum))
Total
str(Total)

fl2000_f <-rbind(fl2000_f,Total)
fl2000_f

###############################0526##########################################

lst<-list(a=1, b=1:3,c=1:100)
lst
length(lst)
lapply(lst,sum)
lapply(lst,length)

sapply(lst,length) #unlist와 결과값이 같음

mapply(sum, 1:5, 1:5, 1:5)
mapply(rep, 1:4, 4:1)

rep(1:4)

lst1 <- list(a=list(a1="boo", b1=2, c1="eeel"), 
             b=3, 
             c="Yikes", 
             d=list(a2=1, b2=list(a3="hey", b3=5)) )
lst1
lapply(lst1,length)
rapply(lst1,length)
#sum(rapply(lst1,length))

x<-1:20
y<-rep(letters[1:5],4)
x;y
tapply(x,y,sum)

d <- data.frame(list(gender=c("M","M","F","M","F","F"),
                     age=c(47,59,21,32,33,24),
                     income=c(55000,88000,32450,76500,123000,45650)))
d
d$over25 <-ifelse(d$age > 25, 1, 0)
d

tapply(d$income, list(d$gender,d$over25), mean)
tapply(d$income, list(d$gender,d$over25), sum)

ls()
rm(fl2000_f)
ls()
rm(list=ls()) #전 객체 메모리 삭제

#fl2000$technology<-as.factor(fl2000$technology)
#summary(fl2000)

mat1<-matrix(1:9, ncol=3)
dimnames(mat1) <- list(paste("row",c(1:3)),paste("col",c(1:3)))
mat1
df<-data.frame(mat1)
df1<-as.data.frame(mat1)
df;df1
#df<data.frame(mat1)
#위 둘의 df가 다름. as는 v(vector), data.frame 은 x로 나옴

