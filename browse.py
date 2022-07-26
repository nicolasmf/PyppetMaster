import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    ## length of password from the user
    length = random.randint(11, 16)

    ## shuffling the characters
    random.shuffle(characters)

    ## picking random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    ## shuffling the resultant password
    random.shuffle(password)

    ## converting the list to string
    ## printing the list
    return "".join(password)


def wait_for_element(driver, xpath):

    elem = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    return elem


def create_proton_account(puppet):

    driver = webdriver.Firefox()
    driver.get("https://account.proton.me/signup?plan=free")

    password = wait_for_element(driver, "//input[@id='password']")
    confirm_password = driver.find_element(By.XPATH, "//*[@id='repeat-password']")

    password_string = generate_random_password()

    password.send_keys(password_string)
    confirm_password.send_keys(password_string)

    driver.switch_to.frame(
        driver.find_element(By.CSS_SELECTOR, ".challenge-width-increase.h-custom")
    )
    username = driver.find_element(By.XPATH, "//*[@id='email']")
    username.send_keys(puppet.username)

    driver.switch_to.default_content()

    submit = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/button"
    )

    submit.click()

    print(puppet.email, password_string)

    # Captcha
    wait_for_element(driver, "//*[@id='key_0']")
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".w100.h-custom"))
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
    captcha = wait_for_element(driver, "//*[@id='checkbox']")
    captcha.click()

    # Wait for captcha to be solved
    WebDriverWait(driver, 120).until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "h1"),
            "Congratulations on choosing privacy!",
        )
    )

    next_button = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[3]/div/div/main/div[2]/form/button"
    )

    next_button.click()


def create_instagram_account(puppet):
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com/accounts/emailsignup/")

    allow_cookies = wait_for_element(driver, "/html/body/div[4]/div/div/button[1]")
    allow_cookies.click()

    email = wait_for_element(
        driver,
        "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[3]/div/label/input",
    )
    full_name = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input",
    )
    username = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/label/input",
    )
    password = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input",
    )

    email.send_keys(puppet.email)
    full_name.send_keys(puppet.first_name + " " + puppet.last_name)
    username.send_keys(puppet.username)
    password_string = generate_random_password()
    password.send_keys(password_string)

    time.sleep(0.5)

    submit = wait_for_element(
        driver,
        "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button",
    )
    submit.click()

    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/div[1]/div"),
            "Add Your Birthday",
        )
    )

    select = Select(
        driver.find_element(
            By.XPATH,
            "/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select",
        )
    )

    select.select_by_value("1995")  # Random year

    next_button = wait_for_element(
        driver, "/html/body/div[1]/section/main/div/div/div[1]/div/div[6]/button"
    )
    next_button.click()

    print(puppet.email, password_string)
