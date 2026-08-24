import data
from selenium import webdriver
from pages import UrbanRoutesPage
from helpers import retrieve_phone_code


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_tariff(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_order_taxi_button()
        routes_page.select_comfort_tariff()
        assert routes_page.is_comfort_tariff_selected(), "La tarifa Comfort no quedó seleccionada"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.open_comfort_order()
        routes_page.fill_phone_number(data.PHONE_NUMBER)
        code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(code)
        routes_page.click_confirm_code_button()
        assert routes_page.is_code_modal_closed(), "El modal del código no se cerró, el teléfono no quedó confirmado"

    def test_add_credit_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.open_comfort_order()
        routes_page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)
        assert routes_page.is_card_added(), "La tarjeta no quedó agregada como método de pago"

    def test_set_driver_message(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.open_comfort_order()
        routes_page.set_driver_message(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_driver_message() == data.MESSAGE_FOR_DRIVER, "El mensaje para el conductor no coincide"

    def test_order_blanket_and_tissues(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.open_comfort_order()
        routes_page.click_blanket_and_tissues_switch()
        assert routes_page.is_blanket_and_tissues_selected(), "Manta y pañuelos no quedó seleccionado"

    def test_order_two_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.open_comfort_order()
        routes_page.order_two_ice_creams()
        assert routes_page.get_ice_cream_count() == '2', "La cantidad de helados no quedó en 2"

    def test_request_taxi_search(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.open_comfort_order()
        routes_page.fill_phone_number(data.PHONE_NUMBER)
        code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(code)
        routes_page.click_confirm_code_button()
        routes_page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.set_driver_message(data.MESSAGE_FOR_DRIVER)
        routes_page.click_blanket_and_tissues_switch()
        routes_page.click_request_taxi_search_button()
        routes_page.wait_for_driver_assigned()
        assert "conductor" in routes_page.get_order_header_title().lower(), "No se encontró el mensaje de conductor asignado"
        assert routes_page.get_driver_name() != "", "No se obtuvo el nombre del conductor"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
