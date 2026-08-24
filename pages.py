import data
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    order_taxi_button = (By.XPATH, "//button[@class='button round' and text()='Pedir un taxi']")
    comfort_tariff = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    comfort_tariff_active = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    phone_button = (By.XPATH, "//div[@class='np-button']//div[text()='Número de teléfono']")
    phone_field = (By.ID, 'phone')
    code_field = (By.ID, 'code')
    next_button = (By.XPATH, "//button[@class='button full' and text()='Siguiente']")
    confirm_code_button = (By.XPATH, "//button[@class='button full' and text()='Confirmar']")

    payment_method_button = (By.XPATH, "//div[@class='pp-text' and text()='Método de pago']")
    add_card_row = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number_field = (By.CSS_SELECTOR, '.card-number-input input')
    card_code_field = (By.CSS_SELECTOR, '.card-code-input input')
    add_card_button = (By.XPATH, "//button[@type='submit' and text()='Agregar']")
    card_added_checkbox = (By.ID, 'card-1')
    driver_message_field = (By.ID, 'comment')

    requirements_header = (By.XPATH, "//div[@class='reqs-header']")
    blanket_and_tissues_switch = (By.XPATH,
        "//div[@class='r-sw-container'][.//div[@class='r-sw-label' and text()='Manta y pañuelos']]//span[@class='slider round']")
    blanket_and_tissues_checkbox = (By.XPATH,
        "//div[@class='r-sw-container'][.//div[@class='r-sw-label' and text()='Manta y pañuelos']]//input[@class='switch-input']")

    ice_cream_plus_button = (By.XPATH,
        "//div[@class='r-counter-label' and text()='Helado']/ancestor::div[@class='r-counter-container']//div[@class='counter-plus']")
    ice_cream_counter_value = (By.XPATH,
        "//div[@class='r-counter-label' and text()='Helado']/ancestor::div[@class='r-counter-container']//div[@class='counter-value']")

    request_taxi_search_button = (By.CSS_SELECTOR, 'button.smart-button')
    order_header_title = (By.CLASS_NAME, 'order-header-title')
    driver_name = (By.XPATH, "//div[@class='order-btn-group'][.//div[@class='order-btn-rating']]/div[not(@class)]")
    overlay = (By.CLASS_NAME, 'overlay')
    close_payment_section_button = (By.CSS_SELECTOR, 'button.close-button.section-close')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def set_from(self, from_address):
        field = self.wait.until(expected_conditions.visibility_of_element_located(self.from_field))
        field.clear()
        field.send_keys(from_address)

    def set_to(self, to_address):
        field = self.wait.until(expected_conditions.visibility_of_element_located(self.to_field))
        field.clear()
        field.send_keys(to_address)

    def get_from(self):
        return self.wait.until(expected_conditions.presence_of_element_located(self.from_field)).get_property('value')

    def get_to(self):
        return self.wait.until(expected_conditions.presence_of_element_located(self.to_field)).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def click_order_taxi_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.order_taxi_button)).click()

    def select_comfort_tariff(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.comfort_tariff)).click()

    def open_comfort_order(self):
        self.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.click_order_taxi_button()
        self.select_comfort_tariff()

    def is_comfort_tariff_selected(self):
        tariff = self.wait.until(
            expected_conditions.visibility_of_element_located(
                self.comfort_tariff_active
            )
        )
        return tariff.text == "Comfort"

    def click_phone_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.phone_button)).click()

    def set_phone_number(self, phone_number):
        field = self.wait.until(expected_conditions.visibility_of_element_located(self.phone_field))
        field.clear()
        field.send_keys(phone_number)

    def click_next_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.next_button)).click()

    def click_confirm_code_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.confirm_code_button)).click()

    def set_phone_code(self, code):
        field = self.wait.until(expected_conditions.visibility_of_element_located(self.code_field))
        field.clear()
        field.send_keys(code)

    def fill_phone_number(self, phone_number):
        self.click_phone_button()
        self.set_phone_number(phone_number)
        self.click_next_button()

    def is_code_modal_closed(self):
        try:
            self.wait.until(expected_conditions.invisibility_of_element_located(self.code_field))
            return True
        except TimeoutException:
            return False

    def click_payment_method_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.payment_method_button)).click()

    def click_add_card_row(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.add_card_row)).click()

    def set_card_number(self, card_number):
        self.wait.until(expected_conditions.visibility_of_element_located(self.card_number_field)).send_keys(card_number)

    def set_card_code(self, card_code):
        code_input = self.wait.until(expected_conditions.visibility_of_element_located(self.card_code_field))
        code_input.send_keys(card_code)
        code_input.send_keys(Keys.TAB)

    def click_add_card_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.add_card_button)).click()

    def add_credit_card(self, card_number, card_code):
        self.click_payment_method_button()
        self.click_add_card_row()
        self.set_card_number(card_number)
        self.set_card_code(card_code)
        self.click_add_card_button()
        self.click_close_payment_section_button()

    def is_card_added(self):
        try:
            checkbox = self.wait.until(expected_conditions.presence_of_element_located(self.card_added_checkbox))
            return checkbox.is_selected()
        except TimeoutException:
            return False

    def set_driver_message(self, message):
        field = self.wait.until(expected_conditions.visibility_of_element_located(self.driver_message_field))
        field.clear()
        field.send_keys(message)

    def get_driver_message(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.driver_message_field)).get_property('value')

    def wait_for_overlay_to_disappear(self):
        self.wait.until(expected_conditions.invisibility_of_element_located(self.overlay))

    def click_requirements_header(self):
        self.wait_for_overlay_to_disappear()
        header = self.wait.until(expected_conditions.element_to_be_clickable(self.requirements_header))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", header)
        try:
            header.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", header)

    def get_requirement_control(self, locator):
        self.wait_for_overlay_to_disappear()

        try:
            return WebDriverWait(self.driver, 3).until(
                expected_conditions.element_to_be_clickable(locator)
            )
        except TimeoutException:
            self.click_requirements_header()
            self.wait_for_overlay_to_disappear()

            return self.wait.until(
                expected_conditions.element_to_be_clickable(locator)
            )

    def click_blanket_and_tissues_switch(self):
        switch = self.get_requirement_control(
            self.blanket_and_tissues_switch
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", switch
        )
        switch.click()

        try:
            self.wait.until(lambda d: self.is_blanket_and_tissues_selected())
        except TimeoutException:
            switch = self.get_requirement_control(
                self.blanket_and_tissues_switch
            )
            switch.click()

    def is_blanket_and_tissues_selected(self):
        checkbox = self.wait.until(expected_conditions.presence_of_element_located(self.blanket_and_tissues_checkbox))
        return checkbox.is_selected()

    def click_ice_cream_plus_button(self):
        button = self.get_requirement_control(self.ice_cream_plus_button)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", button
        )
        try:
            button.click()
        except ElementClickInterceptedException:
            self.wait_for_overlay_to_disappear()
            self.driver.execute_script("arguments[0].click();", button)

    def order_two_ice_creams(self):
        self.click_ice_cream_plus_button()
        self.click_ice_cream_plus_button()

    def get_ice_cream_count(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.ice_cream_counter_value)).text.strip()

    def click_request_taxi_search_button(self):
        self.wait_for_overlay_to_disappear()
        button = self.wait.until(expected_conditions.element_to_be_clickable(self.request_taxi_search_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        try:
            button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", button)

    def wait_for_driver_assigned(self):
        long_wait = WebDriverWait(self.driver, 45)
        long_wait.until(
            lambda driver: "conductor" in driver.find_element(*self.order_header_title).text.strip().lower()
        )

    def get_order_header_title(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.order_header_title)).text.strip()

    def get_driver_name(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.driver_name)).text.strip()

    def click_close_payment_section_button(self):
        self.wait_for_overlay_to_disappear()
        long_wait = WebDriverWait(self.driver, 15)

        def visible_close_button(driver):
            buttons = driver.find_elements(By.CSS_SELECTOR, 'button.close-button.section-close')
            for b in buttons:
                if b.is_displayed():
                    return b
            return False

        button = long_wait.until(visible_close_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        try:
            button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", button)