dim(iris)

names(iris)

str(iris)

attributes(iris)

iris[1:5,]

head(iris)

tail(iris)

iris[1:10, "Sepal.Length"]

iris$Sepal.Length[1:10]

summary(iris)

quantile(iris$Sepal.Length)

quantile(iris$Sepal.Length, c(.1, .3, .65))

var(iris$Sepal.Length)

hist(iris$Sepal.Length)

plot(density(iris$Sepal.Length))


table(iris$Species)

pie(table(iris$Species))


barplot(table(iris$Species))

cov(iris$Sepal.Length, iris$Petal.Length)

cov(iris[,1:4])

cor(iris$Sepal.Length, iris$Petal.Length)

cor(iris[,1:4])

aggregate(Sepal.Length ~ Species, summary, data=iris)


boxplot(Sepal.Length~Species, data=iris)

with(iris, plot(Sepal.Length, Sepal.Width, col=Species, pch=as.numeric(Species)))


plot(jitter(iris$Sepal.Length), jitter(iris$Sepal.Width))


pairs(iris)

library(scatterplot3d)


scatterplot3d(iris$Petal.Width, iris$Sepal.Length, iris$Sepal.Width)


library(rgl)
plot3d(iris$Petal.Width, iris$Sepal.Length, iris$Sepal.Width)

distMatrix <- as.matrix(dist(iris[,1:4]))
heatmap(distMatrix)

library(lattice)

levelplot(Petal.Width~Sepal.Length*Sepal.Width, iris, cuts=9, col.regions=grey.colors(10)[10:1])

filled.contour(volcano, color=terrain.colors, asp=1, plot.axes=contour(volcano, add=T))

persp(volcano, theta=25, phi=30, expand=0.5, col="lightblue")

library(MASS)

parcoord(iris[1:4], col=iris$Species)

parallelplot(~iris[1:4] | Species, data=iris)

library(ggplot2)

qplot(Sepal.Length, Sepal.Width, data=iris, facets=Species ~.)

pdf("myPlot.pdf")
table(iris$Species)

pie(table(iris$Species))
graphics.off()
