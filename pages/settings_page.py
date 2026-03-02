class SettingsPage:
    TITLE = "settings_title"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.tap(100, 200)

    def is_title_visible(self):
        return self.driver.is_visible(self.TITLE)
