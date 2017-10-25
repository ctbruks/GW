

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


```python
city_df = pd.read_csv("raw_data/city_data.csv")
ride_df = pd.read_csv("raw_data/ride_data.csv")
```


```python
city_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nguyenbury</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Douglas</td>
      <td>12</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>West Dawnfurt</td>
      <td>34</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rodriguezburgh</td>
      <td>52</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
ride_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South Roy</td>
      <td>2016-01-02 18:42:34</td>
      <td>17.49</td>
      <td>4036272335942</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wiseborough</td>
      <td>2016-01-21 17:35:29</td>
      <td>44.18</td>
      <td>3645042422587</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spencertown</td>
      <td>2016-07-31 14:53:22</td>
      <td>6.87</td>
      <td>2242596575892</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nguyenbury</td>
      <td>2016-07-09 04:42:44</td>
      <td>6.28</td>
      <td>1543057793673</td>
    </tr>
  </tbody>
</table>
</div>




```python
city_grouped = ride_df.groupby("city")

avg_fare = city_grouped["fare"].mean()

rides_per_city = city_grouped["ride_id"].count()

drivers_per_city = city_df.groupby("type")

merged_df = pd.merge(ride_df,city_df, on= "city", how = "outer").groupby("type")

bubble = city_df
bubble = bubble.set_index(["city"], drop = True)
bubble["Average Fare per City"] = avg_fare
bubble["Total Rides per City"] = rides_per_city

bubble.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>driver_count</th>
      <th>type</th>
      <th>Average Fare per City</th>
      <th>Total Rides per City</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Kelseyland</th>
      <td>63</td>
      <td>Urban</td>
      <td>21.806429</td>
      <td>28</td>
    </tr>
    <tr>
      <th>Nguyenbury</th>
      <td>8</td>
      <td>Urban</td>
      <td>25.899615</td>
      <td>26</td>
    </tr>
    <tr>
      <th>East Douglas</th>
      <td>12</td>
      <td>Urban</td>
      <td>26.169091</td>
      <td>22</td>
    </tr>
    <tr>
      <th>West Dawnfurt</th>
      <td>34</td>
      <td>Urban</td>
      <td>22.330345</td>
      <td>29</td>
    </tr>
    <tr>
      <th>Rodriguezburgh</th>
      <td>52</td>
      <td>Urban</td>
      <td>21.332609</td>
      <td>23</td>
    </tr>
  </tbody>
</table>
</div>




```python
#find % total fares by type
total_fare = merged_df.sum()
total_fare
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>fare</th>
      <th>ride_id</th>
      <th>driver_count</th>
    </tr>
    <tr>
      <th>type</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rural</th>
      <td>4255.09</td>
      <td>658729360193746</td>
      <td>727</td>
    </tr>
    <tr>
      <th>Suburban</th>
      <td>20335.69</td>
      <td>3139583688401015</td>
      <td>9730</td>
    </tr>
    <tr>
      <th>Urban</th>
      <td>40078.34</td>
      <td>7890194186030600</td>
      <td>64501</td>
    </tr>
  </tbody>
</table>
</div>




```python
# The colors of each section of the pie chart
colors = ["lightskyblue","lightcoral", "gold"]


plt.pie(
    total_fare["fare"], labels=total_fare.index, colors=colors, explode = (0,0.01,0.08), startangle= 120, autopct="%1.2f%%"
        )

plt.axis('equal')
plt.title("% of Total Fares by City Type")

#plt.tight_layout()
plt.savefig("FaresbyCityType.png")
plt.show()
```


![png](output_6_0.png)



```python
rides_by_citytype = merged_df["ride_id"].count()
```


```python
#% of Total Rides by City Type
colors = ["lightskyblue","lightcoral", "gold"]

plt.pie(
    rides_by_citytype, labels=total_fare.index, colors=colors, explode = (0,0.01,0.08), startangle= 120, autopct="%1.2f%%"
        )

plt.axis('equal')
plt.title("% of Total Rides by City Type")

#plt.tight_layout()
plt.savefig("RidesbyCityType.png")
plt.show()
```


![png](output_8_0.png)



```python
drivers_by_citytype = merged_df["driver_count"].sum()
```


```python
#% of Total Rides by City Type
colors = ["lightskyblue","lightcoral", "gold"]
plt.pie(
    drivers_by_citytype, labels=total_fare.index, colors=colors, explode = (0,0.01,0.08), startangle= 120, 
    autopct="%1.2f%%"
        )
plt.axis('equal')
plt.title("% of Total Drivers by City Type")

#plt.tight_layout()
plt.savefig("DriversbyCityType.png")
plt.show()
```


![png](output_10_0.png)



```python
plt.figure(figsize=(9,9))

plt.scatter(bubble["Total Rides per City"][bubble["type"]=="Urban"],
            bubble["Average Fare per City"][bubble["type"]=="Urban"],
            c = "lightcoral",
            alpha = .75,
            s = bubble['driver_count'][bubble["type"]=="Urban"]*15,
            label = "Urban")

plt.scatter(bubble["Total Rides per City"][bubble['type']=="Suburban"],
            bubble["Average Fare per City"][bubble['type']=="Suburban"],
            c = "lightskyblue",
            alpha = .75,
            s = bubble['driver_count'][bubble["type"]=="Suburban"]*15,
            label = "Suburban")

plt.scatter(bubble["Total Rides per City"][bubble['type']=="Rural"],
            bubble["Average Fare per City"][bubble['type']=="Rural"],
            c = "gold",
            alpha = .75,
            s = bubble['driver_count'][bubble["type"]=="Rural"]*15,
            label = "Rural")

plt.title('Pyber Ride Sharing Data (2016)')

#plt.ylabel('Average Fare per City')

#plt.xlabel('Total Rides per City')

plt.grid(True)
plt.legend(loc='upper right')
plt.show()
```


![png](output_11_0.png)



```python

```
