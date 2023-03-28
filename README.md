# PARSING_JS

`content` - находим область с новостями.

`news` - находим новости.

`n.find_element(By.TAG_NAME, "a").get_attribute("href")` - из новости берём ссылку.

Собирается словарь:
```
data_news.update({n.text:n.find_element(By.TAG_NAME, "a").get_attribute("href")})
```

---


```
---------ChromeDriver 112.0.5615.28 (2023-03-16)---------
Supports Chrome version 112
Resolved issue 4357: Chromedriver version 110.0.5481.77 session issue with --headless and --user-data-dir options. [Pri-1]
```
