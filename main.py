#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 20:31:01 2026

@author: arturo
"""
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
from pathlib import Path
from time import sleep
import xlsxwriter
import openpyxl
import os, sys, re

def logging_page(driver:webdriver, user:str, password:str):
    try:
        page_load = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-link")))        
        if bool(page_load.text):
            page_load.click()

            # Insert credential to web page            
            user_cred = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inputID_identifier")))
            user_cred.send_keys(user)
            
            pass_cred = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inputID_password")))
            pass_cred.send_keys(password)
            sleep(2)

            btn_logging = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='inputID_method']")))
            btn_logging.click()

            main_user_cv = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cv-views")))
                        
            if bool(main_user_cv.text):
                return True
        
        return False

    except Exception as e:
        print(f"Error: {e}")
        return False
        
def open_web_page(driver:webdriver, url_web_page:str):
    driver.get(url_web_page)

def excel_search_role_pos(excel_file_path:str):
    try:
        # Validate if excel file exists
        if not os.path.isfile(excel_file_path):
            wb = xlsxwriter.Workbook(excel_file_path)
            ws = wb.add_worksheet("vacantes")
            ws.write(0, 0, 'Nombre de la vacante a buscar')
            wb.close()
            return False
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False

def excel_has_roles_to_search(excel_file_path:str):
    # Search if exist excel input for to search roles in OCC 
    ls_roles_to_search = []
    
    wb = openpyxl.load_workbook(filename=excel_file_path)
    sh = wb["vacantes"]    
    
    for row in sh.iter_rows(values_only=True):
        if not row[0] == "Nombre de la vacante a buscar" and not row[0] is None:
            ls_roles_to_search.append(str(row[0]).strip())
    
    if bool(ls_roles_to_search):
        return ls_roles_to_search
    return []

def search_role_pos_in_occ(roles_to_search:list[str]):
    pass

def main():
    # Read dot env file
    load_dotenv()

    # Load variables
    url_occ_mundial  = os.getenv("URL_OCC")
    user_cred        = os.getenv("MAIL_USER")
    pass_cred        = os.getenv("PASS_USER")
    excel_file       = os.getenv("EXCEL_FILE")
    
    base_path = str(Path(__file__).parent)
    excel_file_path = os.path.join(base_path, excel_file)
    
    if not bool(excel_search_role_pos(excel_file_path)):
        raise Exception(f"Ejecutar nuevamente: Archivo excel '{excel_file}' se creo.")

    ls_roles_to_search = excel_has_roles_to_search(excel_file_path=excel_file_path)
    if not bool(ls_roles_to_search):
        raise Exception(f"Especificar las vacantes que desea buscar por nombre o palabra clave en archivo '{excel_file_path}'")

    # Create the instance of driver (Who control the web page)
    service = Service(ChromeDriverManager().install())
    driver  = webdriver.Chrome(service=service)
        
    # Wait for o load the web page
    driver.implicitly_wait(30)
    driver.maximize_window()
    
    # Enter to the web page
    open_web_page(driver=driver, url_web_page=url_occ_mundial)
    logging_result = logging_page(driver=driver, user=user_cred, password=pass_cred)
    
    if logging_result:
        print("Logging success")        
        search_btn = driver.find_element(By.CSS_SELECTOR, '[data-testid="nav-search"]')
        search_btn.click()

        # Search Roles position in OCC search input
        for role in ls_roles_to_search:
            search_role_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "prof-cat-search-input-desktop")))
            search_role_input.send_keys(Keys.CONTROL, "a")
            search_role_input.send_keys(Keys.BACKSPACE)

            search_role_input.send_keys(role.lower())
            search_role_input.send_keys(Keys.ENTER) 
            sleep(4)
            
            all_jobs_search = driver.find_elements(By.CSS_SELECTOR, "div[data-offers-grid-offer-item-container]")
    
            if bool(all_jobs_search):
                print("********** EMPLEOS ENCONTRADOS **********")
                for job_pos in all_jobs_search:
                    try:
                        job_name = job_pos.find_element(By.TAG_NAME, "h2").text.strip()
                        print(f" - {job_name}")
                        #driver.execute_script("arguments[0].click();", job_pos)
                                                
                    except StaleElementReferenceException:
                        continue
                print("===============================================")
    driver.close()

if __name__ == "__main__":
    main()