import allure
from selenoid_homework.page_objects.AdminPage import AdminPage


@allure.feature('Admin')
class TestAdmin:

    @allure.title("Authorization to admin")
    def test_login_to_admin_page(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        assert driver.title == "Administration"
        admin_page.login()
        assert driver.title == "Dashboard"

    @allure.title("Add product in admin")
    def test_add_new_product_in_admin(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        admin_page.login()
        product_name = "Test Product"
        admin_page.open_products_list()
        assert product_name not in admin_page.get_products_list(), f"Product {product_name} already exists"
        admin_page.add_new_product(product_name)
        assert product_name in admin_page.get_products_list(), f"Product {product_name} wasn't found"

    @allure.title("Delete product in admin")
    def test_delete_product_in_admin(self, driver):
        admin_page = AdminPage(driver)
        admin_page.open_page()
        admin_page.login()
        product_name = "Test Product"
        admin_page.open_products_list()
        assert product_name in admin_page.get_products_list(), f"Product {product_name} wasn't found"
        admin_page.delete_product()
        assert product_name not in admin_page.get_products_list(), f"Product {product_name} still exists"
