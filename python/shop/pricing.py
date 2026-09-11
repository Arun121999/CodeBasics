from config.config import GST_RATE


def calculate_gst(amount, gst_rate=GST_RATE):
    return amount * gst_rate / 100