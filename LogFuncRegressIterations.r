# This will run iterations using a variation of the apply process.
rm(list = ls()) # Clean environment.
cat("\014") # Clean console.
#### Packages ####
# install.packages("XLConnect") # Load data.
library(XLConnect)

#### Prepare frq data ####
MaxFreq=26  

DailyFRQ = readWorksheet(loadWorkbook("Name.xlsx"), sheet="tabname")
DataMat <- as.matrix(cbind(FRQ=DailyFRQ$maxImp,CostPerAggConversion=DailyFRQ$cpc))
# Set dependent var.
y <- as.matrix(DataMat[,2])[2:(MaxFreq+1)]
# Remove dependent var from data.
X <- as.matrix(DataMat[,1])[2:(MaxFreq+1)]

checkTrans <- function(var){
  lm <- lm(y ~ var)
  lmfunc <- function(var){
    lm$coefficients[1]+lm$coefficients[2]*var
  }
  return(mean(lm$residuals^2))
}

# Identify best transformation power 
optfunc <- function(lpower) {return(list(lpower,unlist(checkTrans((log(X))^lpower))))  }

#### Initiallize ####
rmsevect <- sapply(seq(0.1,3,0.1),optfunc)
ind <- which.min(rmsevect[2,])
current_optimal <- unlist(rmsevect[1,ind])
granularity <- 0.1;
iterations <- 0;
current_optimal <- 0;

#### Iterate ####
while (iterations<8){
  ind <<- which.min(rmsevect[2,])
  current_optimal <<- unlist(rmsevect[1,ind])
  rmsevect <<- sapply(seq(current_optimal-5*granularity,current_optimal+5*granularity,granularity),optfunc);
  
  iterations <<- iterations+1;
  granularity <<- granularity/10;
  #print(current_optimal)
}

#### Visualize found formula ####
Xtrans <-(log(X))^current_optimal
lmfound <- lm( y ~ Xtrans)
lmfunc <- function(X){
  coefficients(lmfound)[1] +coefficients(lmfound)[2]*(log(X))^current_optimal
}

plot(X,y,xlab="Frequency",ylab = "Cost",col='blue',cex=1.5,type='l',lwd=3.5,yaxt="n",main="Aggregate Frequency CpC")
axis(2, at=axTicks(2), labels=sprintf("$%s", axTicks(2)))
plot.function(lmfunc,min(X),max(X),add=T,col='green',cex=1.5,type='l',lwd=3.5)

# Predict and calcualte empirically
ci.manual <- data.frame(lower=lmfound$fitted.values - 2*sd(lmfound$residuals),fitted=lmfound$fitted.values,upper=lmfound$fitted.values + 2*sd(lmfound$residuals))
lines(x=X,y=ci.manual$lower,col="grey",lwd=2)
lines(x=X,y=ci.manual$upper,col="grey",lwd=2)
legend(x="bottomright",y=0.92,c("Observed CpC","Expected CpC","95% Confidence Interval"),fill=c("blue","green","grey"), ncol = 1,cex=1.5)

lmfound$coefficients
current_optimal
# RMSE
mean(lmfound$residuals^2)

TargetFRQ <- function(CpC){
  return(exp(((5-lmfound$coefficients[1])/lmfound$coefficients[2])^(1/current_optimal)) )
}
TargetFRQ(7)
