```python
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome('C:/Users/ahw48/Documents/GitHub/LIKELION_CODE/Class/chromedriver_90')
url = 'https://www.amazon.com/'
driver.get(url)
sel_search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
sel_btn = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
sel_search.clear()
sel_search.send_keys("keyboard")
sel_btn.click()
```


```python
sel_keyboard = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[5]/div/span/div/div/div[2]/div[2]/div/div[1]/h2/a')
sel_keyboard.click()
```


```python
sel_ratings = driver.find_element_by_xpath('//*[@id="acrCustomerReviewLink"]')
sel_ratings.click()
```


```python
see_all = driver.find_element_by_xpath('//*[@id="cr-pagination-footer-0"]/a')
see_all.click()
```


```python
page = driver.page_source
soup = BeautifulSoup(page,'html.parser')
soup.title
```




    <title>Amazon.com: Customer reviews: Redragon S101 Wired Gaming Keyboard and Mouse Combo RGB Backlit Gaming Keyboard with Multimedia Keys Wrist Rest and Red Backlit Gaming Mouse 3200 DPI for Windows PC Gamers (Black)</title>




```python
import pandas as pd
import time
all_reviews = []


for page in range(1, 11, 1):
    time.sleep(2)
    
    page = driver.page_source
    soup = BeautifulSoup(page,'html.parser')
    all_r = soup.findAll("div", class_="a-section celwidget")
    for one in all_r:
        user = one.find('span', class_='a-profile-name').text
        rating = one.find('span',class_='a-icon-alt').text.split()[0]
        date = one.find('span',class_='a-size-base a-color-secondary review-date').text.split('on')[-1]
        region= one.find('span', class_='a-size-base a-color-secondary review-date').text.split('on')[0]
        review = one.find('span', class_='a-size-base review-text review-text-content').text.strip()
        helpful = one.find('span', class_='a-size-base a-color-tertiary cr-vote-text')
        
        if helpful is not None:
            helpful = helpful.text.split()[0]
            if helpful == "One":
                helpful = "1"
        else:
            helpful = "0"
        
        all_reviews.append({
            "user": user,
            "rating": rating,
            "date": date,
            "region": region,
            "review": review,
            "helpful": helpful
        })
    
    sel_next = driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
    sel_next.click()
    
review_dat = pd.DataFrame(all_reviews)
review_dat.to_csv("amazon_reviews.csv", index=False)
review_dat
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user</th>
      <th>rating</th>
      <th>date</th>
      <th>region</th>
      <th>review</th>
      <th>helpful</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Michael D. Cole</td>
      <td>5.0</td>
      <td>April 10, 2018</td>
      <td>Reviewed in the United States</td>
      <td>My job gave me a computer with a crap ass keyb...</td>
      <td>1,152</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Kels</td>
      <td>5.0</td>
      <td>April 23, 2018</td>
      <td>Reviewed in the United States</td>
      <td>I was looking for a keyboard/mouse set to play...</td>
      <td>476</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jon Almada</td>
      <td>5.0</td>
      <td>August 4, 2018</td>
      <td>Reviewed in the United States</td>
      <td>I bought this combination, expecting it to wor...</td>
      <td>357</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Shawn</td>
      <td>5.0</td>
      <td>July 11, 2018</td>
      <td>Reviewed in the United States</td>
      <td>I bought this for my kid so I wasn't too conce...</td>
      <td>162</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Brian S.</td>
      <td>5.0</td>
      <td>August 25, 2018</td>
      <td>Reviewed in the United States</td>
      <td>My son wasn't enjoying my old 2005 logitech wi...</td>
      <td>152</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>James Paul Williams</td>
      <td>1.0</td>
      <td>April 26, 2020</td>
      <td>Reviewed in the United States</td>
      <td>In the game I play, function keys are used to ...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Willie V. Hughes</td>
      <td>5.0</td>
      <td>December 13, 2020</td>
      <td>Reviewed in the United States</td>
      <td>I bought two of these sets during the pandemic...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>97</th>
      <td>jp</td>
      <td>4.0</td>
      <td>October 22, 2020</td>
      <td>Reviewed in the United States</td>
      <td>I got my first pc a couple of months ago to st...</td>
      <td>0</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Amazon Customer</td>
      <td>1.0</td>
      <td>August 26, 2020</td>
      <td>Reviewed in the United States</td>
      <td>I bought this keyboard because I like the colo...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>99</th>
      <td>Kindle Customer</td>
      <td>3.0</td>
      <td>September 2, 2020</td>
      <td>Reviewed in the United States</td>
      <td>This keyboard/mouse was fine with me for every...</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 6 columns</p>
</div>




```python

```
