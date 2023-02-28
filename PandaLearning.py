# Databricks notebook source
# MAGIC %sh
# MAGIC python -m pip install --upgrade pip
# MAGIC python -m pip install pandas

# COMMAND ----------

# MAGIC %md
# MAGIC # Basics

# COMMAND ----------

import pandas as pd
dataset = {
    'cars' : ["BMW","Ferari","Alto"],
    'passings' : [1,2,0]
}

data = pd.DataFrame(dataset)
print(data)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Checking panda version

# COMMAND ----------

print(pd.__version__)

# COMMAND ----------

# MAGIC %md
# MAGIC ### WHAT IS A SERIES
# MAGIC 
# MAGIC A Pandas Series is like a column in a table.

# COMMAND ----------

data = [1,2,3,4,5]
d = pd.Series(data)
print(d)

# COMMAND ----------

# MAGIC %md
# MAGIC ### WHAT IS A LABEL
# MAGIC If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

# COMMAND ----------

print(d[0])

# COMMAND ----------

# MAGIC %md
# MAGIC how to create labels

# COMMAND ----------

d=pd.Series(data,index=["x","y","z","a","b"])
print(d)
print("Accessing data with labels")
print(d["x"])
print(d["a"])

# COMMAND ----------

# MAGIC %md
# MAGIC Dealing with KEY/VALUE OBJECTS AND SERIES

# COMMAND ----------

calories = {"day1": 420, "day2": 380, "day3": 390}
d = pd.Series(calories)
print(d)

# COMMAND ----------

# MAGIC %md
# MAGIC To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

# COMMAND ----------

d = pd.Series(calories,index=["day1","day2"])
print(d)

# COMMAND ----------

# MAGIC %md
# MAGIC #DATAFRAMES
# MAGIC 
# MAGIC A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

# COMMAND ----------

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## LOCATE ROW
# MAGIC 
# MAGIC 
# MAGIC As you can see from the result above, the DataFrame is like a table with rows and columns.
# MAGIC 
# MAGIC Pandas use the "loc" attribute to return one or more specified row(s)

# COMMAND ----------

print(df.loc[0])
print(df.loc[[0,1]])
print(df.loc[[0,1,2]])

# COMMAND ----------

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data,index=["day1","day2","day3"])

print(df)

# COMMAND ----------

# MAGIC %md
# MAGIC locate named Indexes

# COMMAND ----------

print(df.loc["day1"])

# COMMAND ----------

# MAGIC %md
# MAGIC ##Locating file in dataframe

# COMMAND ----------

# MAGIC %md
# MAGIC LOAD FILE IN TO DATAFRAMES
# MAGIC 
# MAGIC A simple way to store big data sets is to use CSV files (comma separated files)
# MAGIC 
# MAGIC 
# MAGIC CSV files contains plain text and is a well know format that can be read by everyone including Pandas

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/tables/data.csv")
print(df) #to see range of data

print(df.to_string()) #to see all data at once

# COMMAND ----------

# MAGIC %md
# MAGIC MAX_ROWS
# MAGIC 
# MAGIC The number of rows returned is defined in Pandas option settings.
# MAGIC 
# MAGIC You can check your system's maximum rows with the pd.options.display.max_rows statement.

# COMMAND ----------

print(pd.options.display.min_rows)


print(pd.options.display.max_rows)

# COMMAND ----------

pd.options.display.max_rows = 99999

df = pd.read_csv("/dbfs/FileStore/tables/data.csv")
print(df) #to see range of data


# COMMAND ----------

# MAGIC %md
# MAGIC ##READ JSON

# COMMAND ----------

jsondf = pd.read_json("/dbfs/FileStore/tables/data.json")
print(jsondf)

# COMMAND ----------

# MAGIC %md
# MAGIC JSON= Python Dictionary

# COMMAND ----------

{
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}


jdf = pd.DataFrame(data)
print(jdf)

# COMMAND ----------

# MAGIC %md
# MAGIC One of the most used method for getting a quick overview of the DataFrame, is the head() method.
# MAGIC 
# MAGIC The head() method returns the headers and a specified number of rows, starting from the top.

# COMMAND ----------

print(jsondf.head())
print("...")
print(jsondf.tail())

# COMMAND ----------

print(jsondf.info())

# COMMAND ----------

# MAGIC %md
# MAGIC #DATA CLEANING

# COMMAND ----------

# MAGIC %md
# MAGIC TYPES OF BADA DATA
# MAGIC - Empty cells
# MAGIC - Data in wrong format
# MAGIC - Wrong data
# MAGIC - Duplicates

# COMMAND ----------

# MAGIC %md
# MAGIC ####Empty Cells
# MAGIC ####Empty cells can potentially give you a wrong result when you analyze data.

# COMMAND ----------

# MAGIC %md
# MAGIC Remove Rows

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/tables/data2.csv")
print(df) #by looking into data you can see that few of the dates and calorieas are null
#to remove the null column we will usedropna()
df2 = df.dropna()
print(df2)
#if you want to make the same editing in original dataframe use inplace = True
df.dropna(inplace = True)
print(df)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Replace Empty Values

# COMMAND ----------

# MAGIC %md
# MAGIC another way of dealing with empty value is fill it with new value

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/tables/data2.csv")
df.fillna(130, inplace = True)
print(df)

# COMMAND ----------

# MAGIC %md
# MAGIC replace only for specific column

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/tables/data2.csv")
df["Calories"].fillna(130, inplace = True)
print(df)

# COMMAND ----------

# MAGIC %md
# MAGIC Replacing using mean median mode

# COMMAND ----------

# MAGIC %md
# MAGIC ###### MEAN

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/tables/data2.csv")

x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
print(df)


# COMMAND ----------

# MAGIC %md
# MAGIC ###### MEDIAN

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/tables/data2.csv")

x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
print(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### MODE

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/tables/data2.csv")

x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
print(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Cleaning Data of Wrong Format

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Correcting the format

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/tables/data2.csv")
df["Date"] = pd.to_datetime(df["Date"])
print(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Removing ROWS

# COMMAND ----------

df.dropna(subset=['Date'], inplace = True)

print(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Fixing Wrong Data
# MAGIC 
# MAGIC 
# MAGIC "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Replacing Values

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/tables/data2.csv")
df.loc[7, 'Duration'] = 45
print(df)

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/tables/data2.csv")
df["Date"] = pd.to_datetime(df["Date"])
df.dropna(subset=['Date'], inplace = True)
for x in df.index:
    if df.loc[x,"Duration"] > 120:
        df.loc[x,"Duration"] = 45


print(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### removing the row

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/tables/data2.csv")
df["Date"] = pd.to_datetime(df["Date"])
df.dropna(subset=['Date'], inplace = True)
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
for x in df.index:
    if df.loc[x,"Duration"] > 120:
        df.drop(x,inplace = True)


print(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Removing Duplicates

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Checking if the duplicate Exists

# COMMAND ----------

print(df.duplicated())

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Removing The Duplicate

# COMMAND ----------

df.drop_duplicates(inplace = True)
print(df)

# COMMAND ----------

print(df.duplicated())

# COMMAND ----------

# MAGIC %md
# MAGIC #Data Co-Relation

# COMMAND ----------

# MAGIC %md
# MAGIC ###Finding Relationship

# COMMAND ----------

print(df.corr())

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Explaining the result

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC - The number varies from -1 to 1
# MAGIC - 1 means that there is a 1 to 1 relationship (a perfect correlation)
# MAGIC     - for this data set, each time a value went up in the first column, the other one went up as well.
# MAGIC - 0.9 is also a good relationship
# MAGIC     - if you increase one value, the other will probably increase as well.
# MAGIC - -0.9 would be just as good relationship as 0.9
# MAGIC     - if you increase one value, the other will probably go down.
# MAGIC - 0.2 means NOT a good relationship
# MAGIC     - if one value goes up does not mean that the other will.

# COMMAND ----------

# MAGIC %md
# MAGIC Explaination
# MAGIC 
# MAGIC 
# MAGIC * "Duration" and "Duration" got the number 1.000000, which makes sense, each column always has a perfect relationship with itself.
# MAGIC 
# MAGIC * "Duration" and "Calories"got a 0.922721 correlation, which is a very good correlation, and we can predict that the longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, you probably had a long work out.
# MAGIC 
# MAGIC * "Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, meaning that we can not predict the max pulse by just looking at the duration of the work out, and vice versa.

# COMMAND ----------

# MAGIC %md
# MAGIC #PLOTTING
# MAGIC 
# MAGIC panda uses the plot() to plot the diagram
# MAGIC 
# MAGIC We can use PyPlot a sub module of Matplotlib

# COMMAND ----------

# MAGIC %sh
# MAGIC python -m pip install matplotlib

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Normal Plotting (Linear Graph)

# COMMAND ----------

import matplotlib.pyplot as plot

df.plot()

plot.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Scatter Plot

# COMMAND ----------

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plot.show()

# COMMAND ----------

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Histogram Plotting

# COMMAND ----------

df["Duration"].plot(kind = 'hist')
