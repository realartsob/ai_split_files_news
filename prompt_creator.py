from ai_split_files.config import DEFAULT_COMPLEXITY
from config import MAX_WORD_COUNT, DEFAULT_COMPLEXITY

class PromptCreator:
    def __init__(self):
        self.output_type = None
        self.platform = None
        self.category = None
        self.prompt = None
        self.word_count = None
        self.complexity = None
        self.structure = None

    # ... rest of the class methods ...

    def set_word_count(self):
        self.word_count = MAX_WORD_COUNT

    def set_complexity(self):
        self.complexity = DEFAULT_COMPLEXITY

class PromptCreator:
    # ...
    def print_state(self):
        print(f"output_type: {self.output_type}")
        print(f"platform: {self.platform}")
        print(f"category: {self.category}")
        print(f"prompt: {self.prompt}")
        print(f"word_count: {self.word_count}")
        print(f"complexity: {self.complexity}")
        print(f"structure: {self.structure}")
    # ...
