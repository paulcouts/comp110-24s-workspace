class Cookie:
    shape: str
    frosted: bool

    def __init__(self, cookie_shape, cookie_frosted) -> None:
        self.shape = cookie_shape
        self.frosted = cookie_frosted
    
def popular(input: list[Cookie]):
    new_dict: dict[str, int] = {}
    for i in range(len(input)):
        if input[i] not in new_dict:
            new_dict.append