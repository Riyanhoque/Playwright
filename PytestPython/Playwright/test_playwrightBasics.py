def test_playwright_basics(playwright):
    # Launch the browser
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()
    
    # Create a new page
    page = context.new_page()
    
    # Navigate to the desired URL
    page.goto("https://www.google.com")
    
    # Perform actions on the page (e.g., click, fill forms, etc.)
    # Example: Click on a link with text "More information"
    page.click("text=More information")
    
    # Close the browser
    browser.close()