from playwright.sync_api import Page, expect

def test_basic_duckduckgo_search(page: Page):
    """Test DuckDuckGo search functionality"""
    # Navigate to DuckDuckGo
    page.goto("https://www.duckduckgo.com")
    
    # Type into search box
    page.fill("input[name=q]", "Playwright")
    
    # Press Enter
    page.press("input[name=q]", "Enter")
    
    # Assert title contains search term
    expect(page).to_have_title("Playwright at DuckDuckGo")

def test_github_navigation(page: Page):
    """Test GitHub navigation"""
    # Go to GitHub
    page.goto("https://github.com")
    
    # Click sign in button
    page.click("text=Sign in")
    
    # Verify we're on the login page
    expect(page).to_have_url("https://github.com/login")
    
    # Verify login form exists
    expect(page.locator("input[name=login]")).to_be_visible()
    expect(page.locator("input[name=password]")).to_be_visible()

def test_responsive_design(page: Page):
    """Test responsive design by checking different viewport sizes"""
    page.goto("https://www.example.com")
    
    # Test mobile viewport
    page.set_viewport_size({"width": 375, "height": 667})
    expect(page).to_have_title("Example Domain")
    
    # Test tablet viewport
    page.set_viewport_size({"width": 768, "height": 1024})
    expect(page).to_have_title("Example Domain")
    
    # Test desktop viewport
    page.set_viewport_size({"width": 1920, "height": 1080})
    expect(page).to_have_title("Example Domain")
