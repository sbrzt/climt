from src.modules.text_module import TextModule
from src.modules.word_stats_module import WordStatModule
from src.modules.pos_module import POSModule


module_map = {
    "text": TextModule,
    "word_stats": WordStatModule,
    "pos_stats": POSModule,
}

