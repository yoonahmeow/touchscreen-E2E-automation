import yaml
from core.driver import TouchDriver
from pages.settings_page import SettingsPage

def run_scenario(path: str):
    driver = TouchDriver()
    page = SettingsPage(driver)

    with open(path) as f:
        steps = yaml.safe_load(f)

    for step in steps:
        if "open_settings" in step:
            page.open()

        if "settings_title_visible" in step:
            assert page.is_title_visible()

        if "screenshot" in step:
            driver.screenshot(step["screenshot"])

if __name__ == "__main__":
    run_scenario("scenarios/sample_flow.yaml")
