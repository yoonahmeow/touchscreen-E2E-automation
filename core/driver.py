class TouchDriver:
    def tap(self, x: int, y: int):
        print(f"[TAP] ({x}, {y})")

    def is_visible(self, element_id: str) -> bool:
        print(f"[CHECK] {element_id}")
        return True

    def screenshot(self, name: str):
        print(f"[SCREENSHOT] {name}")
