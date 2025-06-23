class HomePage:
    def __init__(self, page):
        self.page = page
        self.login_link = page.locator("#login2")
        self.username_input = page.locator("#loginusername")
        self.password_input = page.locator("#loginpassword")
        self.login_button = page.locator("button[onclick='logIn()']")

    def goto(self):
        self.page.goto("https://www.demoblaze.com/")

    def login(self, username, password):
        self.login_link.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

   
        


