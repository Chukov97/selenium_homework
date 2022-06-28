from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main(driver):
    driver.get(driver.url)
    header_links = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "top-links")))
    elements = header_links.find_elements(By.TAG_NAME, 'li')
    assert len(elements) == 7
    logo = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "logo")))
    assert logo.text == ""
    search = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, "search")))
    assert search.get_attribute("placeholder") == "Search"
    menu = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "menu")))
    assert "Tablets" in menu.text
    footer_rights = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "footer > div > p")))
    assert "Your Store © 2022" in footer_rights.text


def test_catalog(driver):
    driver.get(driver.url + "/desktops")
    name = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > h2")))
    assert "Desktops" == name.text
    sort_filter = driver.find_element(By.CSS_SELECTOR, "#input-sort > option:nth-child(7)")
    assert "Rating (Lowest)" == sort_filter.text
    add_to_cart_btn = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".button-group > button:nth-child(1)")))
    assert add_to_cart_btn.find_element(By.TAG_NAME, "span").text == "ADD TO CART"


def test_product(driver):
    driver.get(driver.url + "/desktops/macbook-air")
    product_title = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content .col-sm-4 h1")))
    assert product_title.text == "MacBook Air"
    product_price = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content .col-sm-4 > .list-unstyled h2")))
    assert product_price.text == "$1,202.00"
    cart_btn = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    assert cart_btn.is_enabled()
    product_description = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#tab-description")))
    assert "MacBook Air" in product_description.text


def test_login_admin(driver):
    driver.get(driver.url + "/admin")
    username = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, "input-username")))
    assert username.get_attribute("placeholder") == "Username"
    password = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, "input-password")))
    assert password.get_attribute("placeholder") == "Password"
    forgotten = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.LINK_TEXT, "Forgotten Password")))
    assert forgotten.text == "Forgotten Password"
    login_btn = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button[type='submit']")))
    assert login_btn.text == "Login"
    assert login_btn.is_enabled()


def test_registration(driver):
    driver.get(driver.url + "/index.php?route=account/register")
    page_title = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > h1")))
    assert page_title.text == "Register Account"
    account_links = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".list-group")))
    assert ("Register" in account_links.text) and ("My Account" in account_links.text)
    continue_btn = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "input[type='submit']")))
    assert continue_btn.is_enabled()
