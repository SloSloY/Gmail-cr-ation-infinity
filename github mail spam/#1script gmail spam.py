import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Génération aléatoire d'informations pour le compte Gmail
first_name = ''.join(random.choice(string.ascii_letters) for _ in range(10))
last_name = ''.join(random.choice(string.ascii_letters) for _ in range(10))
username = first_name + '.' + last_name + '@gmail.com'
password = ''.join(random.choice(string.ascii_letters + string.digits)
                   for _ in range(15))

# Enregistrement des informations dans un fichier texte
with open('account_info.txt', 'w') as f:
    f.write(f'Email: {username}\nPassword: {password}\n')

# Utilisation de Selenium pour automatiser l'inscription à un compte Gmail
driver = webdriver.Chrome()
driver.get('https://accounts.google.com/signup')

# Remplissage des champs de formulaire avec les informations générées aléatoirement
driver.find_element_by_name('firstName').send_keys(first_name)
driver.find_element_by_name('lastName').send_keys(last_name)
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('Passwd').send_keys(password)
driver.find_element_by_name('ConfirmPasswd').send_keys(password)
driver.find_element_by_xpath(
    '//*[@id="accountDetailsNext"]/content/span').click()

# Attente de la confirmation de l'adresse email
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="view_container"]/form/div[2]/div/div[1]/div[1]/div/div[2]/div[2]'))
    )
except:
    driver.quit()

# Vérification de l'adresse email
driver.find_element_by_xpath('// *[@id="view_container"]/form/div[2]
