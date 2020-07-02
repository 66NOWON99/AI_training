
R version 4.0.0 (2020-04-24) -- "Arbor Day"
Copyright (C) 2020 The R Foundation for Statistical Computing
Platform: x86_64-w64-mingw32/x64 (64-bit)

R은 자유 소프트웨어이며, 어떠한 형태의 보증없이 배포됩니다.
또한, 일정한 조건하에서 이것을 재배포 할 수 있습니다.
배포와 관련된 상세한 내용은 'license()' 또는 'licence()'을 통하여 확인할 수 있습니다.

R은 많은 기여자들이 참여하는 공동프로젝트입니다.
'contributors()'라고 입력하시면 이에 대한 더 많은 정보를 확인하실 수 있습니다.
그리고, R 또는 R 패키지들을 출판물에 인용하는 방법에 대해서는 'citation()'을 통해 확인하시길 부탁드립니다.

'demo()'를 입력하신다면 몇가지 데모를 보실 수 있으며, 'help()'를 입력하시면 온라인 도움말을 이용하실 수 있습니다.
또한, 'help.start()'의 입력을 통하여 HTML 브라우저에 의한 도움말을 사용하실수 있습니다
R의 종료를 원하시면 'q()'을 입력해주세요.

> install.packages("ggplot2")
WARNING: Rtools is required to build R packages but is not currently installed. Please download and install the appropriate version of Rtools before proceeding:
  
  https://cran.rstudio.com/bin/windows/Rtools/
  Installing package into ‘C:/Users/user/Documents/R/win-library/4.0’
(as ‘lib’ is unspecified)
also installing the dependencies ‘ps’, ‘processx’, ‘callr’, ‘prettyunits’, ‘backports’, ‘desc’, ‘pkgbuild’, ‘rprojroot’, ‘rstudioapi’, ‘evaluate’, ‘pkgload’, ‘praise’, ‘colorspace’, ‘assertthat’, ‘utf8’, ‘Rcpp’, ‘testthat’, ‘farver’, ‘labeling’, ‘lifecycle’, ‘munsell’, ‘R6’, ‘RColorBrewer’, ‘viridisLite’, ‘cli’, ‘crayon’, ‘ellipsis’, ‘fansi’, ‘magrittr’, ‘pillar’, ‘pkgconfig’, ‘vctrs’, ‘digest’, ‘glue’, ‘gtable’, ‘isoband’, ‘rlang’, ‘scales’, ‘tibble’, ‘withr’


There is a binary version available but the source version is later:
  binary source needs_compilation
backports  1.1.6  1.1.7              TRUE

Binaries will be installed
URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/ps_1.3.3.zip'을 시도합니다
Content type 'application/zip' length 697841 bytes (681 KB)
downloaded 681 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/processx_3.4.2.zip'을 시도합니다
Content type 'application/zip' length 1121190 bytes (1.1 MB)
downloaded 1.1 MB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/callr_3.4.3.zip'을 시도합니다
Content type 'application/zip' length 389310 bytes (380 KB)
downloaded 380 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/prettyunits_1.1.1.zip'을 시도합니다
Content type 'application/zip' length 37670 bytes (36 KB)
downloaded 36 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/backports_1.1.6.zip'을 시도합니다
Content type 'application/zip' length 77609 bytes (75 KB)
downloaded 75 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/desc_1.2.0.zip'을 시도합니다
Content type 'application/zip' length 287253 bytes (280 KB)
downloaded 280 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/pkgbuild_1.0.8.zip'을 시도합니다
Content type 'application/zip' length 138340 bytes (135 KB)
downloaded 135 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/rprojroot_1.3-2.zip'을 시도합니다
Content type 'application/zip' length 84631 bytes (82 KB)
downloaded 82 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/rstudioapi_0.11.zip'을 시도합니다
Content type 'application/zip' length 280423 bytes (273 KB)
downloaded 273 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/evaluate_0.14.zip'을 시도합니다
Content type 'application/zip' length 76458 bytes (74 KB)
downloaded 74 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/pkgload_1.0.2.zip'을 시도합니다
Content type 'application/zip' length 156810 bytes (153 KB)
downloaded 153 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/praise_1.0.0.zip'을 시도합니다
Content type 'application/zip' length 19654 bytes (19 KB)
downloaded 19 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/colorspace_1.4-1.zip'을 시도합니다
Content type 'application/zip' length 2596269 bytes (2.5 MB)
downloaded 2.5 MB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/assertthat_0.2.1.zip'을 시도합니다
Content type 'application/zip' length 54679 bytes (53 KB)
downloaded 53 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/utf8_1.1.4.zip'을 시도합니다
Content type 'application/zip' length 208303 bytes (203 KB)
downloaded 203 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/Rcpp_1.0.4.6.zip'을 시도합니다
Content type 'application/zip' length 3167560 bytes (3.0 MB)
downloaded 3.0 MB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/testthat_2.3.2.zip'을 시도합니다
Content type 'application/zip' length 1973555 bytes (1.9 MB)
downloaded 1.9 MB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/farver_2.0.3.zip'을 시도합니다
Content type 'application/zip' length 1694083 bytes (1.6 MB)
downloaded 1.6 MB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/labeling_0.3.zip'을 시도합니다
Content type 'application/zip' length 62226 bytes (60 KB)
downloaded 60 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/lifecycle_0.2.0.zip'을 시도합니다
Content type 'application/zip' length 101572 bytes (99 KB)
downloaded 99 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/munsell_0.5.0.zip'을 시도합니다
Content type 'application/zip' length 244889 bytes (239 KB)
downloaded 239 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/R6_2.4.1.zip'을 시도합니다
Content type 'application/zip' length 59066 bytes (57 KB)
downloaded 57 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/RColorBrewer_1.1-2.zip'을 시도합니다
Content type 'application/zip' length 55583 bytes (54 KB)
downloaded 54 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/viridisLite_0.3.0.zip'을 시도합니다
Content type 'application/zip' length 60499 bytes (59 KB)
downloaded 59 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/cli_2.0.2.zip'을 시도합니다
Content type 'application/zip' length 398028 bytes (388 KB)
downloaded 388 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/crayon_1.3.4.zip'을 시도합니다
Content type 'application/zip' length 749284 bytes (731 KB)
downloaded 731 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/ellipsis_0.3.1.zip'을 시도합니다
Content type 'application/zip' length 45957 bytes (44 KB)
downloaded 44 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/fansi_0.4.1.zip'을 시도합니다
Content type 'application/zip' length 222605 bytes (217 KB)
downloaded 217 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/magrittr_1.5.zip'을 시도합니다
Content type 'application/zip' length 157397 bytes (153 KB)
downloaded 153 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/pillar_1.4.4.zip'을 시도합니다
Content type 'application/zip' length 185335 bytes (180 KB)
downloaded 180 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/pkgconfig_2.0.3.zip'을 시도합니다
Content type 'application/zip' length 22311 bytes (21 KB)
downloaded 21 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/vctrs_0.3.0.zip'을 시도합니다
Content type 'application/zip' length 1089359 bytes (1.0 MB)
downloaded 1.0 MB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/digest_0.6.25.zip'을 시도합니다
Content type 'application/zip' length 244485 bytes (238 KB)
downloaded 238 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/glue_1.4.1.zip'을 시도합니다
Content type 'application/zip' length 153923 bytes (150 KB)
downloaded 150 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/gtable_0.3.0.zip'을 시도합니다
Content type 'application/zip' length 431382 bytes (421 KB)
downloaded 421 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/isoband_0.2.1.zip'을 시도합니다
Content type 'application/zip' length 3472896 bytes (3.3 MB)
downloaded 3.3 MB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/rlang_0.4.6.zip'을 시도합니다
Content type 'application/zip' length 1113106 bytes (1.1 MB)
downloaded 1.1 MB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/scales_1.1.1.zip'을 시도합니다
Content type 'application/zip' length 561796 bytes (548 KB)
downloaded 548 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/tibble_3.0.1.zip'을 시도합니다
Content type 'application/zip' length 410085 bytes (400 KB)
downloaded 400 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/withr_2.2.0.zip'을 시도합니다
Content type 'application/zip' length 207055 bytes (202 KB)
downloaded 202 KB

URL 'https://cran.rstudio.com/bin/windows/contrib/4.0/ggplot2_3.3.0.zip'을 시도합니다
Content type 'application/zip' length 4015425 bytes (3.8 MB)
downloaded 3.8 MB

package ‘ps’ successfully unpacked and MD5 sums checked
package ‘processx’ successfully unpacked and MD5 sums checked
package ‘callr’ successfully unpacked and MD5 sums checked
package ‘prettyunits’ successfully unpacked and MD5 sums checked
package ‘backports’ successfully unpacked and MD5 sums checked
package ‘desc’ successfully unpacked and MD5 sums checked
package ‘pkgbuild’ successfully unpacked and MD5 sums checked
package ‘rprojroot’ successfully unpacked and MD5 sums checked
package ‘rstudioapi’ successfully unpacked and MD5 sums checked
package ‘evaluate’ successfully unpacked and MD5 sums checked
package ‘pkgload’ successfully unpacked and MD5 sums checked
package ‘praise’ successfully unpacked and MD5 sums checked
package ‘colorspace’ successfully unpacked and MD5 sums checked
package ‘assertthat’ successfully unpacked and MD5 sums checked
package ‘utf8’ successfully unpacked and MD5 sums checked
package ‘Rcpp’ successfully unpacked and MD5 sums checked
package ‘testthat’ successfully unpacked and MD5 sums checked
package ‘farver’ successfully unpacked and MD5 sums checked
package ‘labeling’ successfully unpacked and MD5 sums checked
package ‘lifecycle’ successfully unpacked and MD5 sums checked
package ‘munsell’ successfully unpacked and MD5 sums checked
package ‘R6’ successfully unpacked and MD5 sums checked
package ‘RColorBrewer’ successfully unpacked and MD5 sums checked
package ‘viridisLite’ successfully unpacked and MD5 sums checked
package ‘cli’ successfully unpacked and MD5 sums checked
package ‘crayon’ successfully unpacked and MD5 sums checked
package ‘ellipsis’ successfully unpacked and MD5 sums checked
package ‘fansi’ successfully unpacked and MD5 sums checked
package ‘magrittr’ successfully unpacked and MD5 sums checked
package ‘pillar’ successfully unpacked and MD5 sums checked
package ‘pkgconfig’ successfully unpacked and MD5 sums checked
package ‘vctrs’ successfully unpacked and MD5 sums checked
package ‘digest’ successfully unpacked and MD5 sums checked
package ‘glue’ successfully unpacked and MD5 sums checked
package ‘gtable’ successfully unpacked and MD5 sums checked
package ‘isoband’ successfully unpacked and MD5 sums checked
package ‘rlang’ successfully unpacked and MD5 sums checked
package ‘scales’ successfully unpacked and MD5 sums checked
package ‘tibble’ successfully unpacked and MD5 sums checked
package ‘withr’ successfully unpacked and MD5 sums checked
package ‘ggplot2’ successfully unpacked and MD5 sums checked

The downloaded binary packages are in
C:\Users\user\AppData\Local\Temp\Rtmpmcuj5t\downloaded_packages
> library(ggplot2)
> x<-c("a","a","b","c")
> x
[1] "a" "a" "b" "c"
> gplot(x)
Error in gplot(x) : 함수 "gplot"를 찾을 수 없습니다
> install.packages(gplot)
Error in install.packages : 객체 'gplot'를 찾을 수 없습니다
> install.packages(gplots)
Error in install.packages : 객체 'gplots'를 찾을 수 없습니다
> ggplot(x)
에러: `data` must be a data frame, or other object coercible by `fortify()`, not a character vector
Run `rlang::last_error()` to see where the error occurred.
> qplot(x)
> qplot(data=mpg, x=hwy)
`stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
> qplot(data=mpg, x=cty)
`stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
> qplot(data=mpg, x=drv, y = hwy)
> qplot(data=mpg, x=drv, y = hwy, geom = "line")
> qplot(data=mpg, x=drv, y = hwy, geom = "boxplot")
> qplot(data=mpg, x=drv, y = hwy, geom = "boxplot", colour=drv)
> X_ <- C(1,2,3,4)
Error in C(1, 2, 3, 4) : 요인으로서 해석되어 질 수 없는 객체입니다
> X_ <- c(1,2,3,4)
> x_[3]
에러: 객체 'x_'를 찾을 수 없습니다
> x_[2]
에러: 객체 'x_'를 찾을 수 없습니다
> y <- c(1,2,3,4)
> y[3]
[1] 3
> x[3]
[1] "b"
> y[3]
[1] 3
> y[c(1,2)]
[1] 1 2
> y[1,2]
Error in y[1, 2] : incorrect number of dimensions
> y[c(1,3)]
[1] 1 3
> y[1:3]
[1] 1 2 3
> y[1:]
에러: 예기치 않은 ']'입니다 in "y[1:]"
> y[1:4]
[1] 1 2 3 4
> x<-c(T,F,F)
> height <- (160, 140, 155)
에러: 예기치 않은 ','입니다 in "height <- (160,"
> height <- c(160, 140, 155)
> people<-c("Ned", "Jill","Pat")
> heught
에러: 객체 'heught'를 찾을 수 없습니다
> people
[1] "Ned"  "Jill" "Pat" 
> height
[1] 160 140 155
> names(height) <- people
> height
Ned Jill  Pat 
160  140  155 
> people
[1] "Ned"  "Jill" "Pat" 
> height[1]
Ned 
160 
> height["Ned"]
Ned 
160 
> height
Ned Jill  Pat 
160  140  155 
> height[c(1,2)]
Ned Jill 
160  140 
> height[c(1,3)]
Ned Pat 
160 155 
> height[heught>145]
에러: 객체 'heught'를 찾을 수 없습니다
> height[height>145]
Ned Pat 
160 155 
> height[height>155]
Ned 
160 
> height[height<155]
Jill 
140 
> height[T,F,F]
Error in height[T, F, F] : incorrect number of dimensions
> height[T]
Ned Jill  Pat 
160  140  155 
> height[F]
named numeric(0)
> height[c(T)]
Ned Jill  Pat 
160  140  155 
> height[c(T,F,F)]
Ned 
160 
에러: 객체 'HEIGHT'를 찾을 수 없습니다
> height[x]
Ned 
160 
> var1<-c(1,2,3)
> height[var1>1.5]
Jill  Pat 
140  155 
> 
str<-c("Hello", "world", "is","good!")  
str
str[4]  
max(str)  
min(str)
mean(str)
sort(str) # vector 배열을 변경하진 않음 -> str의 두배의 메모리 사용(copy)
          #사용하려면 변수에 저장을 해줘야함함

range(str) #min, max 값을 같이 보여줌.
1:5
5:1
z=c(1,2,3,4,5,c(1,2,3,6))
z[7]
v2<-c(4,5)
v1<-c(1,2,3)
c(v1,v2)
c(v1,v2,v1,9,9,9)

#combine 안의 combine =  중첩이 아니라 1차원이 형성됨
seq(1,5,2)
seq(1,6,2)
seq(0,1,length.out=100)
rep(c(1,2,3,4),times=3)
rep(c(1,2,3,4),3)
rep(c(1,2,3,4),each=2)

# vector create: c(), :, seq(), rep() - 1dim
v1<-seq(1,10)
v1
v1[c(2,4,6,8,10)]
v1[seq(2,10,2)]
v1[-c(1,3,5,7,9)] # 1,3,5,7,9 번 index는 빼라는 뜻임
v1[-seq(1,10,2)]

#2차원 데이터 저장
mat1 <- matrix(1:12, nrow=3) #matrix는 항상 column 우선!! 3x4
mat2 <- matrix(1:12, ncol=3) #4x3
mat1
mat2
 
length(mat1) #해당 데이터의 개수가 return 
dim(mat1)
dim(mat2)
dim(v1)
var1<-seq(1,9)
mat2<- matrix( v1, nrow=3)
mat2

mat2<- matrix(v1, nrow=3, byrow =T)
mat2
mat1<-matrix(1:9, nrow=3)
mat1
mat1<-matrix(c(1,4,7,2,5,8,3,6,9), nrow=3, byrow=T)
mat1

r1 <-c(1,4,7)
r2 <- c(2,5,8)
r3 <- c(3,6,9)
rbind(r1,r2,r3)
 
c1 <-1:3
c2 <- 4:6
c3 <- 7:9

cbind(c1,c2,c3)
ml <- 1:9
dim(ml) <- c(3,3)
ml
mat1
mat1[1,1]
mat1[2,3]
mat1[1,]
mat1[,3]
mat1[mat1[,3]>7,1]
mat1[c(F,T,T),1]

mat1[c(F,T,T),c(1,2)]
mat1[c(2,3),c(1,2)]
mat1[1:2,3]

mat1[c(F,T,T),c(T,T,F)]
mat1[mat1[,3]>7,mat1[1,]<7]

mat1
mat1[,1]
mat1[3,1]
mat1[,1,drop=F] #drop = F << vector로 바꾸는게 아니라 matrix 의 형태를 유지함(=downsizing 요소가 있더라도 matrix의 속성을 바꾸지않음)

mat1[,2,drop=F]
mat1[1]

t(mat1) #transpose
mat1 * mat1
mat1 %*% mat1

v1 <- 1:5
v2 <- c("a", "b")
v1;v2 #; 한줄에서 실행가능

v3<- c(v1, v2)
v3 #숫자를 문자로 바꿈. v3~ 전부 문자타입


lst<- list("a", c(2,3,4), c(T,F,T), matrix(1:9,nrow=3))
lst1<- list(a="a", b=c(2,3,4), c=c(T,F,T), d=matrix(1:9,nrow=3))
lst  #component는 괄호 두개로 표시 [[]]

length(lst) #component의 개수
names(lst1)
length(lst1$b)

lst[[2]][1]  #2번째 component의 1번째 값
lst1$b[1]
lst1$b[c(2,3)]

x <- list(list(1,2), c(3,4))
y <- c(list(1,2), c(3,4))
x;y
length(x);length(y)
unlist(x); unlist(y)

list(1,2) #2개짜리 component lsit 생성
list(list(1,2),c(3,4))

x[[2]]<-c(x[[2]],"a") #data type 이 str 로 바뀜
x
length(x); length(y)

english<-c(90, 80, 60, 70)
math<-c(50,60,100,20)
df_midterm <- data.frame(english,math)
df_midterm
names(height)<-NULL

df_ex <-data.frame(height, people)
df_ex

df_ex[1,]
df_ex[,2]
df_ex$height
df_ex$people
df_ex[1,][1]
df_ex$height[1]
df_ex[-1,] #1행의 요소만 제외


df_midterm <- data.frame(english=c(90,80,60,70), math=c(50,60,100,20),class=c(1,1,2,2))
df_midterm
df_midterm[df_midterm$math>50 &df_midterm$class==2,] #바른 예시
df_midterm[,df_midterm$math>50 &df_midterm$class==2] #DROP = TRUE
df_midterm[df_midterm$math>50 &df_midterm$class==2] #df_midterm$math>50 &df_midterm$class==2이 행에 적용됨 (4개행;FFTF)  ','가 생략되면 열의 요소로 간주됨 ,,,, DROP=FALSE

df_midterm[df_midterm$math>50 &df_midterm$class==2,"english"]
df_midterm[df_midterm$math>50 &df_midterm$class==2,1] #앞 두개의 조건 만족하는 행에 대해서 1번 column 의 data 출력



install.packages("readxl")
library(readxl)
getwd()
df_exam<-read_excel("excel_exam.xlsx")
df_exam
str(df_exam)
summary(df_exam)

mean(df_exam$english)

df_csv_exam <- read.csv("csv_exam.csv")
df_csv_exam <- read.csv("csv_exam.csv",stringsAsFactors = F)
df_csv_exam

df_test<- read.csv("test.txt")

df_test<- read.csv("test.txt",stringsAsFactors = F)
df_test
str(df_test)

x<-factor(c("ma","f","f","m"))
x
x[2]<-"t"
x
x[2]<-"m"
x
#factor:grouping data 
#level=class information
#>>class에 있는 단어만 저장이 됨
df_test<-cbind(df_test,gender=c("m","f","f","m"))
df_test
str(df_test)

df_test$gender <-factor(df_test$gender)
str(df_test)

df_test <- rbind(df_test,list(id=5,name="Cho",height=190,weight=100,gender="m"))  
#행추가시엔 list
df_test

