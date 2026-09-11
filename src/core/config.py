class Config:
    def __init__(self) -> None:
        self._github_link: str = (
            "https://github.com/PurpleSwtr/asu-ai-environment/tree/dev/"
        )

    def get_github_link(self):
        return self._github_link


config = Config()
