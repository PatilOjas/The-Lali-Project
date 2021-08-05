mid_x=seq(5,65,10)
freq=c(5,8,7,12,28,20,10)
table=data.frame(mid_x,freq)
N=sum(freq)
mean=sum(mid_x*freq)/N
cf=cumsum(freq)
medianClassCF=min(which(cf>(N/2)))
f=freq[medianClassCF]
h=10
c=cf[medianClassCF-1]
l=mid_x[medianClassCF]-h/2
median=l+((h/f)*((N/2)-c))
modalClassFreq=match(max(freq),freq)
f0=freq[modalClassFreq]
f1=freq[modalClassFreq-1]
f2=freq[modalClassFreq+1]
lMode=mid_x[modalClassFreq]-h/2
mode=lMode+(h*(f0-f1)/(2*f0-f1-f2))
cat("Mean is:",mean)
cat("Median is:",median)
cat("Mode is:",mode)