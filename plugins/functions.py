from re import findall

def get_urls_from_text(text: str) -> bool:
    regex = r"""(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]
                [.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(
                \([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\
                ()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))""".strip()
    return [x[0] for x in findall(regex, str(text))]
