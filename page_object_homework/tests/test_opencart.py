from page_object_homework.page_objects.MainPage import MainPage
from page_object_homework.page_objects.CatalogPage import CatalogPage
from page_object_homework.page_objects.RegisterPage import RegisterPage
from page_object_homework.page_objects.ProductPage import ProductPage


def test_main_page(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    assert main_page.count_heading_links() == 7
    logo = main_page.shop_logo()
    assert logo.get_attribute("title") == "Your Store"
    search_placeholder = main_page.search_placeholder()
    assert search_placeholder == "Search"


def test_catalog_page(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.open_page()
    assert driver.title == "Desktops"
    assert catalog_page.count_product_cards == 12
    catalog_page.sort_products_by("Price (High > Low)")
    assert catalog_page.get_current_sort_filter == "Price (High > Low)"


def test_product_page(driver):
    product_page = ProductPage(driver)
    product_page.open_page()
    assert driver.title == "MacBook"


def test_switch_currency(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.change_currency("USD")
    assert main_page.CURRENCY["USD"] == main_page.current_sign_currency


def test_user_registration(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    register_page.create_new_user()
    assert "Your Account Has Been Created!" in register_page.success_register_message
