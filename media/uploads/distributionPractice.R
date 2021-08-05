#binomial distribution
t=pbinom(3,7,0.5)
ans=1-t
1-pbinom(1,50,0.12)

p=0.1
q=1-p
n=30
dbinom(0,n,p)
pbinom(2,n,p)

dbinom(2,20,0.1)
1-pbinom(1,20,0.1)
dbinom(1,20,0.1)+dbinom(2,20,0.1)+dbinom(3,20,0.1)

#poission distribution
dpois(4,2.6)
1-ppois(1,2.6)

lambda=2
dpois(0,lambda)
dpois(2,lambda)
ppois(3,lambda)
x<-0:10
plot(x,dpois(x,lambda=2),type="h",main="poisson")

#normal distribution
x1<-seq(-10,10,0.1)
y<-dnorm(x1,2.5,0.5)
y1<-pnorm(x1,2.5,0.5)
plot(x1,y)
plot(x1,y1)

mean=527
sd=105
1-pnorm(309,mean,sd)

pnorm(72,70,5)-pnorm(69,70,5)
pnorm(68,70,5)
1-pnorm(72,70,5)

2000*(1-pnorm(2150,2040,60))
2000*(pnorm(1950,2040,60))
2000*(pnorm(2160,2040,60)-pnorm(1920,2040,60))