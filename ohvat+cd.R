library(haven)
library(plm)
library(ggplot2)
library(dplyr)
library(lmtest)
library(sandwich)
library(psych)
library(lattice)
library(lme4)
library(jtools)
library(huxtable)
library(car)
library(olsrr)
library(tidyverse)
library(modelr)
library(broom)
#install.packages('broom')
library(corrplot)
#install.packages('ggcorrplot')
library(ggcorrplot)
#install.packages('dplyr')
library(dplyr)

budget$budget <- as.numeric(budget$budget)


forcor <- budget %>% select_if(is.numeric)
corel <- cor(forcor)
corrplot(corel, method='pie', type = 'lower')

options("scipen"=100, "digits"=4)

data <- filter(budget, budget != 0)
data <- filter(data, ohvat != 0)
data <- filter(data, cd != 0)

#ohvat

b1 <- lm(ohvat~budget, data = data)
summary(b1)

moh <- lm(ohvat~budget + as.factor(month) + as.factor(year) + platform, data = data)
summary(moh)

sample_size <- nrow(data)
cook <- cooks.distance(moh)
influential <- as.numeric(names(cook)[(cook > (4/sample_size))])
bud1 <- data[-influential, ]

moh1 <- lm(ohvat~budget + as.factor(month) + year + platform, data = bud1)
summary(moh1)

data$p <- predict(moh, data = data)
RMSE(moh$residuals)
RMSE(moh1$residuals)

#cd
b2 <- lm(cd~budget, data = data)
summary(b2)

mcd <- lm(cd~budget + as.factor(month) + year + platform, data = data)
summary(mcd)

sample_size <- nrow(data)
cook <- cooks.distance(mcd)
influential <- as.numeric(names(cook)[(cook > (4/sample_size))])
bud2 <- data[-influential, ]

mcd1 <- lm(cd~budget + as.factor(month) + year + platform, data = bud2)
summary(mcd1)

export_summs(b1, b2, model.names = c('Охват', 'ЦД'))
ggpairs(forcor)


oh = ggplot(data = bud1, aes(x = budget, y = ohvat)) + 
  geom_point() +
  labs(x = "Бюджет",
       y = "Охват",
       title = "Зависимость охвата от бюджета") +
  geom_smooth(method=lm)

cdp = ggplot(data = bud2, aes(x = budget, y = cd)) + 
  geom_point() +
  labs(x = "Бюджет",
       y = "ЦД",
       title = "Зависимость ЦД от бюджета") +
  geom_smooth(method=lm)

require(scales)
oh + scale_x_continuous(labels = comma) + scale_y_continuous(labels = comma)
cdp + scale_x_continuous(labels = comma) + scale_y_continuous(labels = comma)

opred<-predict(moh1, data.frame(budget = c(300000), month = 1, year = 2021, platform = 'fbinst'))
print(opred)

cdpred <- predict(mcd1, data.frame(budget = c(300000),month = 1, year = 2021, platform = 'vk'))
print(cdpred)
