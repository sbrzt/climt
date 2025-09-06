from src.modules.text_module import TextModule
from src.modules.word_stats_module import WordStatModule
from src.modules.pos_module import POSModule
from src.modules.readability_module import ReadabilityModule
from src.modules.sentiment_module import SentimentModule


module_map = {
    "text": TextModule,
    "word_stats": WordStatModule,
    "pos_stats": POSModule,
    "readability": ReadabilityModule,
    "sentiment": SentimentModule
}

