from src.modules.text import TextModule
from src.modules.words import WordsModule
from src.modules.pos import POSModule
from src.modules.readability import ReadabilityModule
from src.modules.sentiment import SentimentModule


module_map = {
    "text": TextModule,
    "words": WordsModule,
    "pos": POSModule,
    "read": ReadabilityModule,
    "sent": SentimentModule
}

