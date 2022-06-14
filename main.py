from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
from time import monotonic

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()


def OleOle(url):
    driver.get(str(url))
    kategories = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div[2]")
    kategories_link = kategories.find_elements(By.CLASS_NAME, "category-list-box-link.selenium-LP-category-list-box-link")
    print(len(kategories_link))
    for p in range(len(kategories_link)):
        try:
            if p == 0:
                pass
            else:
                ti = monotonic()
                try:
                    driver.get(str(url))
                    kategories = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div[2]")
                    kategories_link = kategories.find_elements(By.CLASS_NAME, "category-list-box-link.selenium-LP-category-list-box-link")
                    kat_link = kategories_link[p].get_attribute('href')
                    driver.get(kat_link)
                    if monotonic() - ti > 50:
                        ti = monotonic()
                        print('tick')
                        continue
                    try:
                        x = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div[2]/div")
                        y = x.find_elements(By.CLASS_NAME, "category-list-box-link.selenium-LP-category-list-box-link")
                    except:
                        driver.get(kat_link)
                        try:
                            pages = driver.find_element(By.CLASS_NAME, "paging-numbers")
                            pages_count = pages.find_elements(By.CLASS_NAME, "paging-number")[-1].get_attribute("href")
                            pages_count = pages_count.split("strona")[1]
                            pages_count = pages_count.split(".")[0]
                            pages_count = pages_count.split("-")[1]
                        except:
                            pages_count = 1
                        print("Pages - " + str(pages_count))
                        for page in range(int(pages_count)):
                            pages_count = driver.find_elements(By.CLASS_NAME, "paging-number")
                            page += 1
                            print("Page - " + str(page))
                            if page == 1:
                                next_page = driver.find_elements(By.CLASS_NAME, "paging-number")[1].get_attribute("href")
                                print(next_page)
                                next = str(next_page).split("strona")[0]
                                print(next)
                            else:
                                driver.get(str(next) + "strona-" + str(page) + ".bhtml")
                            names = driver.find_elements(By.CLASS_NAME, "product-main")
                            prices = driver.find_elements(By.CLASS_NAME, "price-normal.selenium-price-normal")
                            print("price - " + str(len(prices)))
                            print(str(len(names)))
                            for z in range(int(len(prices))):
                                print(z)
                                try:
                                    price = prices[z].text
                                except:
                                    continue
                                try:
                                    name = names[z].find_element(By.CLASS_NAME, "js-save-keyword")
                                except:
                                    names.pop(z)
                                    name = names[z].find_element(By.CLASS_NAME, "js-save-keyword")
                                if name.text == "":
                                    continue
                                href = name.get_attribute("href")
                                price = str(price).replace("zł", " ")
                                data = {'name': name.text, 'price': price.strip(), 'url': href}
                                with open('result_oleole.csv', 'a', newline='', encoding='utf-8') as f:
                                    order = ['name', 'price', 'url']
                                    writer = csv.DictWriter(f, delimiter=';', fieldnames=order)
                                    writer.writerow(data)
                            time.sleep(1)
                        continue
                    for i in range(len(y)):
                        if i == 0:
                            pass
                        else:
                            driver.get(kat_link)
                        x = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div[2]/div")
                        y = x.find_elements(By.CLASS_NAME, "category-list-box-link.selenium-LP-category-list-box-link")
                        link = y[i].get_attribute('href')
                        driver.get(link)
                        try:
                            pages = driver.find_element(By.CLASS_NAME, "paging-numbers")
                            pages_count = pages.find_elements(By.CLASS_NAME, "paging-number")[-1].get_attribute("href")
                            pages_count = pages_count.split("strona")[1]
                            pages_count = pages_count.split(".")[0]
                            pages_count = pages_count.split("-")[1]
                        except:
                            pages_count = 1
                        print("Pages - " + str(pages_count))
                        for page in range(int(pages_count)):
                            page += 1
                            print("Page - " + str(page))
                            if page == 1:
                                if int(pages_count) != 1:
                                    next_page = driver.find_elements(By.CLASS_NAME, "paging-number")[1].get_attribute("href")
                                    print(next_page)
                                    next = str(next_page).split("strona")[0]
                                    print(next)
                            else:
                                driver.get(str(next) + "strona-" + str(page) + ".bhtml")
                            names = driver.find_elements(By.CLASS_NAME, "product-main")
                            prices = driver.find_elements(By.CLASS_NAME, "price-normal.selenium-price-normal")
                            print("price - " + str(len(prices)))
                            print(str(len(names)))
                            for z in range(int(len(prices))):
                                print(z)
                                try:
                                    price = prices[z].text
                                except:
                                    continue
                                try:
                                    name = names[z].find_element(By.CLASS_NAME, "js-save-keyword")
                                except:
                                    names.pop(z)
                                    name = names[z].find_element(By.CLASS_NAME, "js-save-keyword")
                                if name.text == "":
                                    continue
                                href = name.get_attribute("href")
                                price = str(price).replace("zł", " ")
                                data = {'name': name.text, 'price': price.strip(), 'url': href}
                                with open('result_oleole.csv', 'a', newline='', encoding='utf-8') as f:
                                    order = ['name', 'price', 'url']
                                    writer = csv.DictWriter(f, delimiter=';', fieldnames=order)
                                    writer.writerow(data)
                            time.sleep(1)
                except Exception:
                    print(Exception.__name__)
                    pass
        except Exception:
            print(Exception.__name__)
            pass


if __name__ == '__main__':
    OleOle("https://www.oleole.pl/agd.bhtml")
    OleOle("https://www.oleole.pl/agd-do-zabudowy.bhtml")
    OleOle("https://www.oleole.pl/agd-male.bhtml")
print('!!!!!!!!!!!!!!!!!!!!!Вci товари успішно зпарсені!!!!!!!!!!!!')