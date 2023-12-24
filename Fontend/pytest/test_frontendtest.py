from playwright.sync_api import Page, expect
import pytest

def test_search(page:Page):
    page.goto('https://flights-app.pages.dev')

    countryList = ["Istanbul", "New York", "London", "Paris", "Tokyo", "Sydney", "Los Angeles", "Chicago", "Beijing", "Dubai", "Singapore", "Hong Kong", "Frankfurt", "Madrid", "Rome"]
    
    button_from = page.get_by_role("button", name="From")
    button_to = page.get_by_role("button", name="To")

    listbox_from = page.get_by_role("listbox", name="From")
    listbox_to = page.get_by_role("listbox", name="To")

    for country_name in countryList:

        button_from.click()
        listbox_from.get_by_role("option", name=country_name).click()
        
        button_to.click()
        expect(listbox_to.get_by_role("option", name=country_name)).not_to_be_enabled()



            
        

            


            



