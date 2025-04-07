import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    phone_number_button = (By.CSS_SELECTOR, ".np-button")
    phone_number_field = (By.ID, "phone")
    next_button = (By.CSS_SELECTOR, ".button.full")
    sms_code_field = (By.ID, "code")
    sms_confirmation_button = (By.XPATH, "//div[@class='buttons']/button[text()='Confirmar']")
    payment_method_button = (By.CSS_SELECTOR, ".pp-button")
    add_card_button = (By.CSS_SELECTOR, ".pp-plus-container")
    card_number_field = (By.ID, "number")
    code_field = (By.NAME, "code")
    add_card_confirmation_button = (By.XPATH, "//div[@class='pp-buttons']/button[text()='Agregar']")
    card = (By.XPATH, "//div[@class='pp-title' and text()='Tarjeta']")
    payment_method_close_button = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    driver_message_field = (By.ID, "comment")
    driver_message_label = (By.XPATH, "//label[@for='comment']")
    blanket_and_handkerchief_switch = (By.CLASS_NAME, 'switch')
    blanket_and_handkerchief_input = (By.CLASS_NAME, 'switch-input')
    add_ice_cream_button = (By.CLASS_NAME, 'counter-plus')


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        # self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.request_taxi_button)
        )

    def set_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.comfort_icon)
        )

    def set_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_phone_number_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.phone_number_button)
        )

    def click_on_phone_number_button(self):
        self.get_phone_number_button().click()

    def get_phone_number_field(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.phone_number_field)
        )

    def set_phone_number(self, phone_number):
        self.get_phone_number_field().send_keys(phone_number)

    def get_next_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.next_button)
        )

    def click_on_next_button(self):
        self.get_next_button().click()

    def get_sms_code_field(self):
        return WebDriverWait(self.driver, 5). until(
            expected_conditions.presence_of_element_located(self.sms_code_field)
        )
    def set_sms_code(self):
        code = retrieve_phone_code(self.driver)
        self.get_sms_code_field().send_keys(code)

    def get_confirmation_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.sms_confirmation_button)
        )
    def click_on_sms_confirmation_button(self):
        self.get_confirmation_button().click()

    def get_payment_method_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.payment_method_button)
        )
    def click_on_payment_method_button(self):
        self.get_payment_method_button().click()

    def get_add_card_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_card_button)
        )
    def click_on_add_card_button(self):
        self.get_add_card_button().click()

    def get_card_number_field(self):
        return  WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.card_number_field)
        )

    def set_card_number(self):
        self.get_card_number_field().send_keys(data.card_number)

    def get_code_field(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.code_field)
        )

    def set_code_number(self):
        self.get_code_field().send_keys(data.card_code)

    def get_add_card_confirmation_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_card_confirmation_button)
        )

    def click_on_add_card_confirmation_button(self):
        self.get_add_card_confirmation_button().click()

    def get_card_option(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.card)
        )

    def get_payment_method_close_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.payment_method_close_button)
        )

    def click_on_payment_method_close_button(self):
        self.get_payment_method_close_button().click()

    def get_driver_message_field(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.driver_message_field)
        )

    def set_driver_message(self, message):
        self.get_driver_message_field().send_keys(message)

    def get_driver_message_label(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.driver_message_label)
        )

    def click_on_driver_message_label(self):
        self.get_driver_message_label().click()

    def get_blanket_and_handkerchief_switch(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.blanket_and_handkerchief_switch)
        )

    def set_blanket_and_handkerchief_switch(self):
        self.get_blanket_and_handkerchief_switch().click()

    def get_blanket_and_handkerchief_input(self):
        return self.driver.find_element(*self.blanket_and_handkerchief_input)

    def get_add_ice_cream_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_ice_cream_button)
        )

    def set_ice_cream(self, ice_cream_number):
        for i in range (ice_cream_number):
            self.get_add_ice_cream_button().click()

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_request_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_request_taxi_button()
        routes_page.set_comfort_icon()

    def test_enter_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_phone_number_button()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_on_next_button()
        routes_page.set_sms_code()
        routes_page.click_on_sms_confirmation_button()
        assert data.phone_number == routes_page.get_phone_number_field().get_property("value")
        assert routes_page.get_phone_number_button().text == data.phone_number

    def test_enter_payment_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_payment_method_button()
        routes_page.click_on_add_card_button()
        routes_page.set_card_number()
        routes_page.get_card_number_field().send_keys(Keys.TAB)
        routes_page.set_code_number()
        routes_page.get_code_field().send_keys(Keys.TAB)
        routes_page.click_on_add_card_confirmation_button()
        assert routes_page.get_card_option().text == 'Tarjeta'
        routes_page.click_on_payment_method_close_button()

    def test_send_message_to_the_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_driver_message_label()
        routes_page.set_driver_message(data.message_for_driver)
        assert routes_page.get_driver_message_field().get_property('value') == data.message_for_driver

    def test_add_blanket_and_handkerchief(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_blanket_and_handkerchief_switch()
        assert routes_page.get_blanket_and_handkerchief_input().get_property('checked')

    def test_order_two_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_ice_cream(2)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
