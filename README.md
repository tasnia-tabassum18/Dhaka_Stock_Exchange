# Dhaka Stock Exhange DSE
Some of the data such as company details and other information was collected by Web Scraping and stored into a CSV file. Later on, database was constructed using postgresql.

<strong>Installations:</strong> <br>
```pip install pandas``` <br>
```pip install python``` <br>
```pip install beautifulsoup4```<br>
```pip install requests```<br>

<strong>For API:</strong> <br>
```pip install djangorestframework```

<strong>For Database: </strong><br>
```Install PostgreSQL```

<strong>For visualization:</strong><br>
```Install PowerBI Desktop```

<h1>Web Scraping</h1>
<h3> Why is web scraping needed? </h3><br>

1. Data gathering and analysis: Web scraping enables you to swiftly acquire enormous amounts of data from websites. Information including product specifics, costs, ratings, news stories, information from social media, weather information, and more can be extracted. For research, market analysis, corporate intelligence, or data-driven decision making, this data can be processed, analyzed, and utilised.<br>

2. Competitor monitoring: Web scraping can be used to keep tabs on the websites of your rivals to learn more about their goods, costs, special offers, and other marketing tactics. To stay competitive in the market, you may want to modify your own pricing, marketing, and product development plans using this knowledge. <br>

3. Market Research and Sentiment Analysis: Web scraping can be used to gather information from social media platforms, forums, review websites, and consumer feedback portals for market research and sentiment analysis. This information can be used to gain understanding of consumer trends, sentiment analysis, public opinion, and brand reputation management.<br>

4. Analysis of financial data: Web scraping can be used to gather financial information like stock prices, business financials, economic indicators, or exchange rates. For investment analysis, algorithmic trading, or financial research, this information may be useful.<br>

<i> Apart from these, there are many more uses of Web Scraping</i>

<h3> How the web scraping was carried out in this repo?</h3><br>
<ol>
  <li>DSE's website was inspected</li>
  <li>The class where the data we want was noted</li>
  <li>BeautifulSoup was used to get response from the website</li>
  <li>Dataframe was created to create the table</li>
  <li>Data was inserted by scraping for each column of the dataframe </li>
  <li>Dataframe was converted into two csv files: companies and holdings </li>
  
</ol>
<h1>From csv files to PostgreSQL Database</h1>

<ol>
  
  <li>A database was created in PostgreSQL</li>
  <li>Psycopg2 library was used to connect to the database</li>
  <li>Table was created in the database according to the parameters of the csv file data using python</li>
  <li>A loop was used to enter all the data from the csv file to the table in the database</li>
  
</ol>

<h1>Data Visualization</h1>

<ol>
  
  <li>Microsoft PowerBI was used to visualize the data</li>
  <li>The extracted data of the csv file was transformed and loaded into PowerBI</li>
  <li>Different cards, charts, filters, slicers and tables were used to show the data and comparison we needed to see</li>
  
</ol>
