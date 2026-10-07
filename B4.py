import pandas as pd
import matplotlib.pyplot as plt

region_units=pd.DataFrame({'region':['North','South','East'],
                           'units':[15,9,10]})

plt.figure(figsize=(10, 6))
plt.bar(region_units['region'],region_units['units'])
plt.title("Units sold by region")
plt.xlabel('region')
plt.ylabel('units sold')
plt.show()