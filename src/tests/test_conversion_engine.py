import unittest
from src.analyzer import Analyzer
from src.modules.text_module import TextModule
from src.conversion_engine import ConversionEngine


analyzer = Analyzer("Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness.")
analyzer.plug_modules("text")
converter = ConversionEngine(analyzer.generate_analysis())

class TestConversionEngine(unittest.TestCase):

    def test_convert_data(self):
        print(converter.convert_data())

    

if __name__ == "__main__":
    unittest.main()