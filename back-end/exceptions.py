class GPTSimException(Exception):
    __module__ = 'builtins'
    def __init__(self, error_code):
        self.message = f"\nf'GPT Simulation Base Exception Has Occurred`. {error_code}"
        super().__init__(self.message)

class GPTSimConfigException(Exception):
    __module__ = 'builtins'
    def __init__(self, error_code):
        self.message = f"\nGPT Simulation Configuration Failed. {error_code}"
        super().__init__(self.message)

