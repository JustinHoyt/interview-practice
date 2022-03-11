class Logger:
    def __init__(self):
        self.messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.messages:
            if timestamp >= self.messages[message] + 10:
                self.messages[message] = timestamp
                return True
            else:
                return False
        else:
            self.messages[message] = timestamp
            return True


def test_happy_path():
    logger = Logger()
    assert logger.shouldPrintMessage(1, "foo") ==  True # return true, next allowed timestamp for "foo" is 1 + 10 = 11
    assert logger.shouldPrintMessage(2, "bar") ==  True # return true, next allowed timestamp for "bar" is 2 + 10 = 12
    assert logger.shouldPrintMessage(3, "foo") ==  False # 3 < 11, return false
    assert logger.shouldPrintMessage(8, "bar") ==  False # 8 < 12, return false
    assert logger.shouldPrintMessage(10, "foo") == False # 10 < 11, return false
    assert logger.shouldPrintMessage(11, "foo") == True # 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
    assert logger.shouldPrintMessage(12, "foo") == False # 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21


if __name__ == "__main__":
    test_happy_path()

