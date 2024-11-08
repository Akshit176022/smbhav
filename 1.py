from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


driver.get("https://www.instagram.com/p/DB_AIIySLUx/?igsh=d3p3eDh3encwYnd1")

try:

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(@class, '_ap3a') and contains(@class, '_aaco') and contains(@class, '_aacu') and contains(@class, '_aacx')]")
        )
    )
    

    print("Text Element found:", element.text)


    image_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[contains(@class, 'x5yr21d') and contains(@class, 'xu96u03')]")
        )
    )
    

    image_url = image_element.get_attribute("src")
    print("Image URL:", image_url)

except Exception as e:
    print("Error:", e)
    print(driver.page_source)

finally:

    driver.quit()
