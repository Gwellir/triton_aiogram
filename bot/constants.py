import yaml

with open("bot/post_data.yml") as f:
    DATA = yaml.safe_load(f)

BUTTON_PRESETS: dict[str, dict[str, str]] = DATA.get("button_presets")

DRAFTS = DATA.get("drafts")

MAX_TEXT_LENGTH = DRAFTS.get("get_text").get("max_length")


class QUERIES:
    CONTINUE = "continue"
    RESTART = "restart"
    FINALIZE = "final_confirm"


class ERRORS:
    NOT_TEXT = "not_text"
    TEXT_TOO_LONG = "text_too_long"
    NOT_MEDIA = "not_media"
    NOT_LINK = "not_link"
