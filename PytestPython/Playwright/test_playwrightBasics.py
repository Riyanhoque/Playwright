from playwright.sync_api import Page

# def test_playwright_basics(playwright):
#     # Launch the browser
#     browser = playwright.chromium.launch(headless=False)

#     context = browser.new_context()
    
#     # Create a new page
#     page = context.new_page()
    
#     # Navigate to the desired URL
#     page.goto("https://www.youtube.com")
    
#     # Perform actions on the page (e.g., click, fill forms, etc.)
#     # Example: Click on a link with text "More information"
#     page.click("text=More information")
    
#     # Close the browser
#     browser.close()


# def test_playwright_basics_with_page(page: Page):
#     # Navigate to the desired URL
#         page.goto("https://www.google.com")
#     # Perform actions on the page (e.g., click, fill forms, etc.)
#     # Example: Click on a link with text "More information" 


def test_playwright_basics_with_page(page: Page):
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        page.get_by_label("Username:").fill("rahulshettyacademy")
        page.get_by_label("Password:").fill("learning")
        page.get_by_role("combobox").select_option("teach")
        page.locator("#terms").check()
        page.get_by_role("button", name="Sign In").click()