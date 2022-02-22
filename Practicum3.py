import pandas as pd, matplotlib.pyplot as plt#import panda

towns = ['Butte','Bozeman','Billings','Great Falls', 'Helena', 'Kalispell', 'Missoula']#defining data
population = [34551, 52619, 109843, 59243, 34256, 25857, 67466]
growth_10_yrs = [3.06, 40.99, 5.10, -2.44, 18.50, 28.89, 13.81]
on_I90 = [True, True, True, False, False, False, True]

dataset = list(zip(towns, population, growth_10_yrs, on_I90))#making the data into something we can process as a whole

df = pd.DataFrame(data = dataset, columns=['Towns', 'Population', 'Growth', 'On I90'], index=towns)#making the data into something we can put into a graphic

df = df.sort_values(['Population'], ascending=True)#sorting the data in ascending order based on population 
print(df)

plt.bar(towns, growth_10_yrs, color = ['gray'], width = 0.5)#graph will be a bar chart with a gray bar color and a width of 0.5
plt.ylabel("Growth (10 year period)")#y-axis label is now "Growth (10 year period)"
plt.xlabel("Towns in MT")#x-axis label is now "Towns in MT"
plt.title("Growth per town in MT")#graph title is now "Growth per town in MT"
plt.show()#show the graph when we run the program
