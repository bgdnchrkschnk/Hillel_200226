from playwright.sync_api import sync_playwright, Locator, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) # headless - запуск без візуалу
    # context = browser.new_context()
    # context.set_default_timeout(10000)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com")
    expect(page).to_have_title("The Internet")
    expect(page).to_have_url("https://the-internet.herokuapp.com/")

    # inputs_link: Locator = page.locator("//a[@href='/inputs']")
    # inputs_link = page.get_by_role(role="link", name="Inputs")
    # inputs_link = page.locator("//*[text()='Inputs']")
    # inputs_link: Locator = page.get_by_text(text="Inputs", exact=True)       # //*[text()='Inputs']


    links = page.locator("a")

    first_link_v2 = links.first
    second_link_v2 = links.nth(2)
    third_link_v2 = links.nth(3)
    lastname_link_v2 = links.last
# --------------------------------------------------
    all_links: list[Locator] = links.all()
    first_link = all_links[0]
    second_link = all_links[1]
    third_link = all_links[2]


    for link in all_links:
        print(link.text_content(), link.get_attribute("href"))
    #
    #
    # page.mouse.wheel(0, 1000)
    # # page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    #
    # checkboxes_link: Locator = page.locator("//a[@href='/checkboxes']")
    # checkboxes_link.click()
    #
    # checkbox_1: Locator = page.locator("//input[@type='checkbox']").first
    # checkbox_2: Locator = page.locator("//input[@type='checkbox']").nth(1)
    # checkbox_1.check()
    # checkbox_2.uncheck()

    dropdown_link: Locator = page.locator("//a[@href='/dropdown']")
    dropdown_link.click()

    dropdown: Locator = page.locator("#dropdown")

    # dropdown.select_option(label="Option 2")
    dropdown.select_option(index=1)

    page.wait_for_timeout(3000)

    # login_button: Locator = page.locator("//a[@href='/login']")
    # login_button.click()
    #
    # username_field: Locator = page.locator("#username")
    # password_field: Locator = page.locator("#password")
    # submit_button = page.locator("button[type='submit']")
    #
    # # fill
    # # username_field.fill("tomsmith")
    # # password_field.fill("SuperSecretPassword!")
    #
    # # type
    # username_field.type("tomsmith", delay=100)
    # password_field.type("SuperSecretPbhjejhjhbassword!", delay=100)
    # # submit_button.click()
    #
    # page.keyboard.press("Enter")
    #
    # success_message: Locator = page.locator("#flash")
    #
    # expect(success_message).to_be_visible()
    # # assert "You logged into a secure area!" in success_message.text_content()
    # expect(success_message).to_contain_text("You logged into a secure area!")

    page.wait_for_timeout(5000) # time.sleep analog


"""
.locator() 
Locator -> якщо елемент знайдено один

.locator().all()
list[Locator] -> якщо забрати всі елементи - більше одного
.
"""