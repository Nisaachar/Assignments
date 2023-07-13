str(Titanic)

df <- as.data.frame(Titanic)

head(df)

titanic.raw <- NULL

for(i in 1:4) {
  titanic.raw<- cbind(titanic.raw, rep(as.character(df[,i]), df$Freq))
  }

titanic.raw<- as.data.frame(titanic.raw) 

names(titanic.raw) <- names(df)[1:4] 

dim(titanic.raw)


str(titanic.raw)


head(titanic.raw)                      


summary(titanic.raw)


library(arules)

rules.all <- apriori(titanic.raw)


rules.all


inspect(rules.all)


titanic.raw[, 1:4] <- lapply(titanic.raw[, 1:4], as.factor)

titanic.discretized <- discretizeDF(titanic.raw)

rules <- apriori(titanic.discretized, control = list(verbose = FALSE),
                 parameter = list(minlen = 2, supp = 0.005, conf = 0.8),
                 appearance = list(rhs = c("Survived=No", "Survived=Yes"),
                                   default = "lhs"))


quality(rules) <- round(quality(rules), digits=3)

rules.sorted<- sort(rules, by="lift")

inspect(rules.sorted)


subset.matrix<- is.subset(rules.sorted, rules.sorted)

subset.matrix[lower.tri(subset.matrix, diag=T)] <- NA
redundant<- colSums(subset.matrix, na.rm=T) >= 1


which(redundant)

rules.pruned <- rules.sorted[!redundant]

inspect(rules.pruned)


rules <- apriori(titanic.raw, parameter= list(minlen=3, supp=0.002, conf=0.2), appearance= list(rhs=c("Survived=Yes"),
                    lhs=c("Class=1st", "Class=2nd", "Class=3rd", "Age=Child ", "Age=Adult "), default="none"), control = list(verbose=FALSE))



library(arulesViz)
plot(rules.all)  
plot (rules.all, method="grouped")
plot (rules.all, method="graph")


plot(rules.all, method="graph", control=list(type="items"))

plot (rules.all, method="paracoord", control=list ( reorder=TRUE))




