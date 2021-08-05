ages=c(18,19,19,19,19,20,20,20,20,20,21,21,21,21,22,23,24,27,30,36)
mean(ages)
median(ages)

y=ages[ages<25]
median(y)

a=c(0,1,2,3)
f=c(8,11,5,1)

mean=sum(a*f)/sum(f)

replicate=rep(a,f)

mean2=sum(replicate)/length(replicate)
median(replicate)