class BasicView(object):
    def __init__(self, driver):
        self.driver = driver

    def find_elemenr(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

