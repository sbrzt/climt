from modules.text import TextModule
from modules.words import WordsModule
from modules.pos import POSModule
from modules.readability import ReadabilityModule
from modules.sentiment import SentimentModule


MODULE_MAP = {
    "text": TextModule,
    "words": WordsModule,
    "pos": POSModule,
    "read": ReadabilityModule,
    "sent": SentimentModule
}

REPORT_DIR = "output"

SUPPORTED_EXTENSIONS = {".txt", ".docx", ".pdf"}