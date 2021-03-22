# Module-10
Visual Graphs

#Matplot lib line plot
plt.plot(stock.reset_index().iloc[:,0],stock["Adj Close"])
plt.show()
print("e")
print("e")


#Set x and y
x=PlottingData["Adj Close"]
y=PlottingData.reset_index()["Date"]
#matplot bar plot
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = y
students = x
ax.bar(langs,students)
plt.show()

#Make matplotlib scatter
fig, ax = plt.subplots()


#Make a scatter graph of all the stock prices
colors = {"TWX":'red',"DIS":'green', "JJ":'blue', "TSLA":'yellow',"GOOGL":"purple","IBM":"black","ELF":"gray","AAPL":"brown"}
grouped = PlottingData.reset_index().groupby('Name')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='Date', y='Adj Close', label=key, color=colors[key])
plt.show()
