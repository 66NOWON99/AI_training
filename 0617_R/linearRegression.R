getwd()

insurance = read.csv("insurance.csv", stringsAsFactors=T)
str(insurance)

summary(insurance)
hist(log(insurance$charges))

ins_model <- lm(charges~., data=insurance)
summary(ins_model)

ins_model2 <- lm(log(charges)~., data=insurance)
summary(ins_model2)

insurance$age2 <- insurance$age^2
str(insurance)
insurance$bmi30 <- ifelse(insurance$bmi >= 30, 1, 0)

ins_model3 <- lm(charges~age+age2+children+bmi+sex+bmi30*smoker+region,
                 data=insurance)
summary(ins_model3)