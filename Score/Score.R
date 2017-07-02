#https://stackoverflow.com/questions/44165285/data-science-scoring-methodology

# Stage Data:
userid <- c("a1","a2","a3","a4","a11","a12","a13","a14","u2","wtf42","ub40","foo","bar","baz","blue","bop","bob","boop","beep","mee","r")
events <- c(0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,2,3,6,122,13,1)
df1 <- data.frame(userid,events)

# Normalize events to be in [1,2] (helpfull to get sensitivity right and for logarythmic properties):
normevents <- (events-mean(events))/((max(events)-min(events))*2)+1.5

# score = normevents^exponent
MaxScoreThreshold=0.25
# MaxScore = 100 => 100 = quantile(normevents,MaxScoreThreshold)^expnent
# 0 events -> socre 0

#qts <- quantile(normevents, c(seq(from=0, to=100,by=5)/100))
#qts <- quantile(events, c(seq(from=0, to=100,by=5)/100))
qts <- quantile(events[events>min(events) & events<max(events)], c(seq(from=0, to=100,by=5)/100))
MaxScoreEvents <- quantile(qts,MaxScoreThreshold)



# Calculations 
# Must be: exponent>0
exponent <- log(100)/log(MaxScoreEvents)

#apply(as.matrix(normevents^exponent),1,FUN = function(x) {
df1$Score <- apply(as.matrix(events^exponent),1,FUN = function(x) {
  if (x > 100) {
    result <- 100
  }
  else if (x < 0) {
    result <- 0
  }
  else {
    result <- x
  }
  return(ceiling(result))
})

df1
# Allow the data to define the threasholds
