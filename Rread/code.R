setwd='C:/Users/alecherv/Documents/GitHub/Internal/stackEx/Rread'
filename <- 'C:/Users/alecherv/Documents/GitHub/Internal/stackEx/Rread/datacsv.csv'
#data <- as.data.frame(read.csv(file=filename))
data <- read.csv(file=filename)
#data[1,]
i <- 1
length(data)
listedData <- array(data=c(),dim=length(data))
for (i in 1:length(data)){
  print(i)
  datum <- data[i,]
  print(c(datum))
  #listedData[i] <- c(datum)
}
#data[1,]
listedData