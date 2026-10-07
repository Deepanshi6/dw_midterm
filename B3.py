from tables import sales

print("i :",sales.isnull().sum().sum())

print("ii :",sales.dropna().shape)

#part iii

sales['units']=sales['units'].fillna(sales['units'].median())
#checking if any null after filling missing values
print("checking if any null after filling missing values :",sales['units'].isnull().sum())


