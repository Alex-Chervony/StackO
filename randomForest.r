# Unsupervised random forest
# https://www.tutorialspoint.com/r/r_random_forest.htm
# https://cran.r-project.org/web/packages/randomForest/randomForest.pdf

#install.packages("randomForest")
library("randomForest")
data(iris)
#iris.rf <- randomForest(iris[,-5], iris[,5], prox=TRUE)
iris.rf <- randomForest(iris[,-5],  prox=TRUE)
iris.p <- classCenter(iris[,-5], iris[,5], iris.rf$prox)
plot(iris[,3], iris[,4], pch=21, xlab=names(iris)[3], ylab=names(iris)[4],
     bg=c("red", "blue", "green")[as.numeric(factor(iris$Species))],
     main="Iris Data with Prototypes")
points(iris.p[,3], iris.p[,4], pch=21, cex=2, bg=c("red", "blue", "green"))
#?classCenter
#?randomForest
