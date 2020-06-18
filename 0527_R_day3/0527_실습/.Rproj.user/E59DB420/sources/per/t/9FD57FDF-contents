fl2000 <- read.table("c:\\Users\\ilifo\\Desktop\\R\\Data\\fl2000.txt", header=T)
str(fl2000)
fl2000

fl2000 <- fl2000[,-c(2:5)]
str(fl2000)

fl2000_f <- cbind(fl2000, sum=apply(fl2000[2:13],1,sum))
fl2000_f$sum <- apply(fl2000[2:13],1,sum)
str(fl2000_f)

fl2000_f <- fl2000_f[,-c(4:13)]
str(fl2000_f)

Total <- c(list(county="Total"), apply(fl2000_f[,2:4],2,sum))
Total

fl2000_f <- rbind(fl2000_f, Total)
str(fl2000_f)

mat1 <- matrix(1:9, ncol=3)
mat1
apply(mat1,1,sum)
apply(mat1,2,sum)

lst <- list(a=1, b=1:3, c=10:100)
lst
length(lst)
unlist(lapply(lst, length))
sapply(lst, length)

mapply(sum, 1:5, 1:5, 1:5)
mapply(rep, 1:4, 4:1)

lst1 <- list(a=list(a1="boo", b1=2, c1="eeek"), 
             b=3, 
             c="Yikes", 
             d=list(a2=1, b2=list(a3="hey", b3=5)))

lapply(lst1, length)
rapply(lst1, length)

x <- 1:20
y <- rep(letters[1:5], 4)
x;y
tapply(x,y,sum)

d <- data.frame(list(gender=c("M","M","F","M","F","F"),
                     age=c(47,59,21,32,33,24),
                     income=c(55000,88000,32450,76500,123000,45650)))
d
d$over25 <- ifelse(d$age>25, 1, 0)
d

tapply(d$income,list(d$gender,d$over25),mean)

ls()
rm(fl2000_f)
ls()

rm(list=ls())

head(fl2000)
str(fl2000)
summary(fl2000)

fl2000$technology <- as.factor(fl2000$technology)
str(fl2000)
summary(fl2000)

mat1 <- matrix(1:9, ncol=3)
dimnames(mat1) <- list(paste("row", c(1:3)), paste("col", c(1:3)))
mat1
df <- data.frame(mat1)
df1 <- as.data.frame(mat1)

df;df1

no <- c(1:5)
name <- c("Lee","Park","So","Kim","Yoon")
age <- c(45,47,35,26,29)
gender <- factor(c("M","F","M","F","M"))

d <- data.frame(no, name, age, gender)
str(d)
head(d)
d <- d[-2,]
d <- d[d$no != 2,]

d <- rbind(d, list(6,"Hwang",21,"F"))
d
d <- rbind(d, list(7,"Cho",39,"M"))
d

d$ages <- ifelse(d$age>=40,40,
                 ifelse(d$age>=30,30,20))

d$ages1 <- ifelse(d$age>=30,
                           ifelse(d$age>=40,40,30),
                           ifelse(d$age<=10,10,20))
d
tapply(d$age,d$ages,mean)

d$ages2 <- as.integer(d$age / 10)
d

tapply(d$age, d$ages2, mean)


x <- c(1:10)

if (sum(x) > 10) {
    if (length(x) > 5) {
       print(mean(x))
    } else {
       print(length(x))
    }
} else {
    print(var(x))
}

for (i in 1:5) {
    print(i)
}

a <- 1
while(a<=5) {
    print(rep(a,a))
    a <- a+1
}

a <- 1
repeat {
    if (a>5) break
    print(rep(a,a))
    a <- a+1
}

v2 <- c()
for (i in 1:100) {
    if (i%%2==0) {
        v2 <- c(v2, i)
    }
}
v2

v2 <- c()
for (i in seq(2,100,2)) {
    v2 <- c(v2, i)
}
v2

my.mean <- function(x) {
    return (sum(x) / length(x))
}

my.mean(1:5)

v1 <- c(0,0,0,1,0,0,1,1,1)

first1 <- function(x) {
   if (!is.vector(x)) {
      print("Input object should be vector~!!!")
      return (NULL)
   }

   for (i in 1:length(x)) {
      if (x[i] == 1) return (i)
   }

   return (NULL)
}

mat <- matrix(1:9,ncol=3)
first1(v1)
first1(mat)
first1(c(0,0,0,1))
first1(c(0,0,0,0))

ages <- function(x) {
   ret <- c()
   for (i in 1:length(x)) {
      if (x[i] >= 40) {
         ret <- c(ret, 40)
      } else if (x[i] >= 30) {
         ret <- c(ret, 30)
      } else {
         ret <- c(ret, 20)
      }
   }
   return (ret)
}

d

d$ages3 <- ages(d$age)
d

heart <- read.csv("c:\\Users\\ilifo\\Desktop\\R\\Data\\heart.csv", 
                  header=T, row.names="X", stringsAsFactors=T)
str(heart)
head(heart)
table(is.na(heart))

my.rm.na <- function(df) {
   rmv <- c()
   for (i in 1:nrow(df)) {
      if (any(is.na(df[i,]))) {
         rmv <- c(rmv, i)
      }
   }
   print(df[rmv,])
   return (df[-rmv,])
}

heart.new <- my.rm.na(heart)    
table(is.na(heart.new))

heart.new1 <- na.omit(heart)
table(is.na(heart.new1))



