from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import requests
driver = webdriver.Chrome(ChromeDriverManager().install())
for c in range (100,102):
    for i in range (1,40):
        driver.get("https://www.clinido.com/?gclid=CjwKCAiA1aiMBhAUEiwACw25MfExmoEvwCUbccrvjtBGb9Hpus0dbG4hFQ38ln6Zni_FU8rSfgIAcBoCTzcQAvD_BwE/"+str(c)+"/"+str(i))
        elem = driver.find_elements_by_tag_name("img")
        print(elem)
        for img in elem:
            f = open(img.get_attribute('alt')+'.jpg','wb')
            f.write(requests.get(img.get_attribute('src')).content)
            f.close()
            print(img.get_attribute("src"))
driver.close()