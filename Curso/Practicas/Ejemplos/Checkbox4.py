import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright
 
#pytest --slowmo 1000  --headed Input2.py

def test_checkbox4(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=100)
    #context=browser.new_context()    
    #context=browser.new_context(record_video_dir="Videos/Checkbox/")
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 800 }
      #record_video_dir="Videos/Checkbox/"
    )
    page=context.new_page()
    #page.set_viewport_size({"width": 1500, "height": 700})
    page.goto("https://datatables.net/extensions/select/examples/initialisation/checkbox")
    expect(page).to_have_title("DataTables example - Checkbox selection")
    page.set_default_timeout(4000)
    page.mouse.wheel(0, 400)
    time.sleep(1)
    
    
    
  
    for i in range (1,11):  
          page.locator(f"(//td[contains(@class,'  select-checkbox')])[{i}]").click()
          if i == 3:
                page.locator("//a[contains(@data-dt-idx,'2')]").click()
          elif i==6:
                page.locator("//a[contains(@data-dt-idx,'3')]").click()
          time.sleep(0.5)  
                
    
        
                
          
    
    
    
    #expect(page).to_have_url(re.compile(".*datos-personales/"))
    
    
    time.sleep(3)
    ##Cerrar Context y Navegador     
    context.close()
    browser.close()
    
    
    
    
    
    
    
    
    
   