from casper.tests import CasperTestCase
import os.path


class SaveImageTests(CasperTestCase):

    def test_save(self):
        self.assertTrue(self.casper(
            os.path.join(os.path.dirname(__file__),
                         'casper-tests/save-image.js')))
