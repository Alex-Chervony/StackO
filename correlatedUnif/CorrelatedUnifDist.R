## Initialization and parameters 
set.seed(123)
r <- 0.6                            # Target (Spearman) correlation
n <- 500                            # Number of samples

## Functions
gen.unif.cop <- function(r, n){
  rho <- 2 * sin(r * pi/6)        # Pearson correlation
  P <- toeplitz(c(1,rho, rho))    # Correlation matrix
  d <- nrow(P)                    # Dimension
  ## Generate sample
  #U <- punif(matrix(rnorm(n*d), ncol = d) %*% chol(P))
  #U <- ?punif(matrix(runif(n*d), ncol = d) %*% chol(P))
  U <- punif(matrix(runif(n*d), ncol = d) %*% chol(P))
  #U <- runif(matrix(?rnorm(n*d), ncol = d) %*% chol(P))
  #U <- ?pnorm(matrix(rnorm(n*d), ncol = d) %*% chol(P))
  return(U)
}

## Data generation and visualization
#U <- gen.gauss.cop(r = r, n = n)
U <- gen.unif.cop(r = r, n = n)
pairs(U, diag.panel = function(x){
  h <- hist(x, plot = FALSE)
  rect(head(h$breaks, -1), 0, tail(h$breaks, -1), h$counts/max(h$counts))})
#dim(U)
cor(U[,1],U[,2])
cor(U[,1],U[,3])
cor(U[,2],U[,3])
