import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_list_all_prices_bags(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    assert driver.current_url == "https://magento.softwaretestingboard.com/gear/bags.html"
    price_locator = (By.XPATH, '//div[contains(@class, "price-final_price")]//span[contains(@id, "product-price")]/span')
    all_prices_1 = driver.find_elements(*price_locator)
    all_prices_text_1 = [item.text[1:] for item in all_prices_1]
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '(//div[@class="pages"]//span[contains(text(), "2")])[2]'))
    )
    next_button.click()

    all_prices_2 = driver.find_elements(*price_locator)
    all_prices_text_2 = [item.text[1:] for item in all_prices_2]
    all_prices_text = all_prices_text_1 + all_prices_text_2
    print()
    print(all_prices_text)
