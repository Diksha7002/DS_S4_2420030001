#1.Data Visualization- Scripting Layer
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,30,40]
plt.plot(x,y)
plt.show()

#2.
import matplotlib.pyplot as plt
y1=[] #stores +ve values
y2=[] #stores -ve values
x=range(-100,100,10) #Generates values from -100 to 90 with an interval of 10(-100.-90,-80,..)
for i in x: y1.append(i**2)
for i in x: y2.append(-i**2)

plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(-2000,2000) #yaxis limit
plt.axhline(0) #horizontal line
plt.axvline(0) #vertical line
plt.savefig("quad.png")
plt.show()

#3.Scatter Plot
import matplotlib.pyplot as plt

#Create data for plotting
x_values=[0,1,2,3,4,5]
y_values=[0,1,4,9,16,25]
plt.scatter(x_values,y_values,s=30,color="blue")
plt.show()

#4.Scatter Plot
import matplotlib.pyplot as plt

#x-axis values
x=[1,2,3,4,5,6,7,8,9,10]
#y-axis values
y=[2,4,5,7,6,8,9,11,12,12]

#plotting points as a scatter plot
plt.scatter(x,y,label="stars",s=30,color="blue",marker="*")

#x-axis label
plt.xlabel('X-axis')
#frequency label
plt.ylabel('Y-axis')
#plot title
plt.title('My Star Plot!')
#showing legend
plt.legend()
#function to show the plot
plt.show()

#5.Bar Graph
import matplotlib.pyplot as plt

#Create data for plotting
values=[5,6,3,7,2]
names=["A","B","C","D","E"]
plt.bar(names,values,color="red")
plt.show()

#6.Bar Graph- Horizontally
import matplotlib.pyplot as plt

#Create data for plotting
values=[5,6,3,7,2]
names=["A","B","C","D","E"]
plt.barh(names,values,color="yellowgreen")
plt.show()

#7.Bar Graph- Multiple Bars
import matplotlib.pyplot as plt
#heights of bars
height=[10,24,36,40,5]
#labels for bars
names=['one','two','three','four','five']
#plotting a bar chart
c1=['red','green']
c2=['b','g'] #we can use this for colours
plt.bar(names,height,width=0.8,color=c1)
#naming the x-axis
plt.xlabel('x-axis')
#naming the y-axis
plt.ylabel('y-axis')
#plot title
plt.title('My Bar Chart!')
#function to show the plot
plt.show()

#8.Subplots
import pandas as pd
from sklearn.datasets import load_iris
# Load the iris dataset
iris = load_iris()
# Create a DataFrame with feature names
df = pd.DataFrame(iris.data, columns=iris.feature_names)
import matplotlib.pyplot as plt

plt.subplot(2,3,1)
plt.plot(df['sepal length (cm)'], df['petal length (cm)'])
plt.subplot(2,3,2)
plt.plot(df['sepal width (cm)'], df['petal width (cm)'])
plt.subplot(2,3,3)
plt.scatter(df['sepal length (cm)'],
            df['petal length (cm)'],
            c='green')
plt.title('Subplots')
plt.show()

#9.Histogram
import matplotlib.pyplot as plt
#frequencies
ages=[2,5,70,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,20,40]
#setting thr ranges ans no.of intervals
range=(0,100)
bins=10
#plotting a histogram
plt.hist(ages,bins,range,color='blue',histtype='bar',rwidth=0.8)
#x-axis label
plt.xlabel('Age')
#frequency label
plt.ylabel('No. of people')
#plot title
plt.title('My Histogram')
#function to show the plot
plt.show()

#10.histogram- using alpha for transparency
import matplotlib.pyplot as plt
#generate random data
x=[2,1,6,4,5,3,7,8,9,10]
plt.hist(x, bins=5, alpha=0.5, color='blue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram with Transparency')
plt.show()

#11.seaborn
import seaborn as sns
data=sns.load_dataset("iris")
sns.lineplot(x="sepal_length",y="petal_length",data=data)

#12.Customizing Seaborn Plots- importing pacakges
import seaborn as sns
import matplotlib.pyplot as plt
#Loading dataset
data=sns.load_dataset("iris")
#Changing the theme to dark
sns.set_style("dark")
#draw lineplot
sns.lineplot(x="sepal_length",y="sepal_width",data=data)
plt.show()


#13.removal of spines
#importing packages
import seaborn as sns
import matplotlib.pyplot as plt
#Loding dataset
data=sns.load_dataset("iris")
#draw lineplot
sns.lineplot(x="sepal_length",y="sepal_width",data=data)
#removing spines
sns.despine()
plt.show()