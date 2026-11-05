import logging
from pathlib import Path

def get_logger(name="qa_automation"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        Path("logs").mkdir(exist_ok=True)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        for handler in (logging.StreamHandler(), logging.FileHandler("logs/automation.log", encoding="utf-8")):
            handler.setFormatter(formatter); logger.addHandler(handler)
    return logger
