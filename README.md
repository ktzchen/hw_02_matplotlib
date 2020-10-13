# hw_02_matplotlib

For this assignment, I was interested in plotting different measurements of economic development. As an economics and international relations student, I am interested in evaluating different metrics of economic development and studying what aspects of development they can accurately capture.

## Days to Open a Business

I wanted to assess the accuracy of "days required to start business" as a measure of economic development. I tried to choose 6 countries in various stages of development from around the globe. The [data](http://data.un.org/Data.aspx?d=WDI&f=Indicator_Code%3aIC.REG.DURS) is collected from 2018. 

![image of graph](https://raw.githubusercontent.com/ktzchen/hw_02_matplotlib/main/open_business_days.png)

The following countries are in order of least to most days it takes to open a business: DRC, Germany, China, Bangladesh, Philippines, then Venezuela. The bar graph very obviously shows that Venezeula (230 days) is an outlier in this dataset, which I think is an accurate reflection of its current economic state. What is interesting to note is DRC's placement, which boasts a proud 7 days, lower than both China (8.5 days) and Germany (8 days), both of which are significantly more economically developed than the DRC. I think this is because the main inhibitors of economic development stem from the Second Congo War, and as a result is mainly poses infrastructural problems like access to electricity rather than administrative red tape. 

## PPP per Capita: Singapore vs. US

I am interested in economic development in postcolonial countries, and I think Singapore is specifically an interesting successful case study. I chose to compare Singapore's GDP with the US's GDP, as the US is a more traditionally established economic power. I chose a time-series [dataset](http://data.un.org/Data.aspx?d=WDI&f=Indicator_Code%3aNY.GDP.PCAP.PP.CD) of both Singapore and the US's GDP per capita, calculated with purchasing parity power, in current international dollars. 

![image of graph](https://raw.githubusercontent.com/ktzchen/hw_02_matplotlib/main/ppp_sing_us.png)

Singapore was decolonized in 1963, and is one of the "Asian Tigers": a country in East Asia that experienced rapid economic growth from the late 60s to the early 90s. From here we can see that Singapore surpassed the United States in GDP per capita in the early 1990s. This graph also show's Singapore's exponential GDP growth rate compared to the United States. Despite having a smaller population, Singapore proves itself as an economic powerhouse.
