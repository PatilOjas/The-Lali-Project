n=6
p=1/2
#probability of 2 success:
ans1=dbinom(2,n,p)
cat("Probability of 2 success:",ans1)

#probabilites of whole space
ans2=dbinom(0:n,n,p)
cat("Probabilites of whole space:",ans2)

#Displaying probabilities in table:
table=data.frame(0:n,ans2)
table

#Displaying graph:
y=ans2
x=0:n
plot(x,y,type="b",xlab="n values",ylab="binomial distribution",main="Binomial Distribution graph")

ans1
ans2
table