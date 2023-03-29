import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# Google chrome drive eklentisi eklendi
driver = webdriver.Chrome()

# Eklentiye link verildi
driver.get("https://www.avansas.com/")

time.sleep(5)


def search(searchKey):
    #Windows penceresini büyütür
    driver.maximize_window()
    print(driver.current_url)
    time.sleep(5)

    #url var ise gir
    if driver.current_url:
        print("True")
        #inputa kalem diye arat
        driver.find_element(By.XPATH, '//*[@id="multiple-datasets"]/span/input[2]').send_keys(searchKey)
        time.sleep(5)
        #butona tıkla
        driver.find_element(By.XPATH, '//*[@id="multiple-datasets"]/button').click()
        time.sleep(20)

        # Kategori listesini bul
        category_list = driver.find_element(By.XPATH,
                                            '//*[@id="main"]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[2]/ul')

        # Kategori listesinin son öğesini bul
        last_item = category_list.find_elements(By.TAG_NAME, 'li')[-1]

        # Son öğeye kadar kaydır
        actions = ActionChains(driver)
        actions.move_to_element(last_item)
        actions.perform()

        time.sleep(5)
        driver.find_element(By.XPATH,
                            '//*[@id="main"]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[2]/ul/li[18]/form/label/a').click()

        time.sleep(10)

        # sayfa kaynağını alır
        get_source = driver.page_source
        
        # aranacak kelimeyi gir
        search_text = "Bic Evolution"
        
        # kelime varsa true yok ise false döner
        print(search_text in get_source)



# Search fonksiton unu çağır ve arama kelimesi kalem olsun
search("kalem")
