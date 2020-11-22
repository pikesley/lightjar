import platform

from lib.conf import conf

if "arm" in platform.platform():  # nocov
    import board
    from neopixel import NeoPixel


def get_pixels():
    """Return real or fake pixels depending on our platform."""
    if "arm" in platform.platform():
        return NeoPixel(board.D18, conf["lights-count"], auto_write=True)  # nocov
    else:
        return FakePixel(conf["lights-count"])


class FakePixel(list):
    """Fake NeoPixels for testing."""

    def __init__(self, length):  # pylint: disable=W0231
        """Construct."""
        self.length = length
        for _ in range(self.length):
            self.append((0, 0, 0))

    def __setitem__(self, index, value):
        """Override [i] = foo."""
        super().__setitem__(index, value)

    def fill(self, colour):
        """Pretend to fill the pixels."""
        for index, _ in enumerate(self):
            self[index] = colour
