from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless") # not open the browser
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(live_url)

price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price_dollar.text)
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
print(price_cents.text)

print(f"The price is {price_dollar.text}.{price_cents.text}")

driver.get("https://www.python.org")

search_bar = driver.find_element(By.NAME, "q")
button = driver.find_element(By.ID, "submit")
print(search_bar)
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))
pprint(button.size)

anchor_elements = driver.find_elements(By.TAG_NAME, "a")
specific_anchors = driver.find_elements(By.CSS_SELECTOR, "a[href*='python.org']")
for anchor in specific_anchors:
    print(anchor.text)

#xpath
bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


driver.quit()
#driver.close() # close one tab