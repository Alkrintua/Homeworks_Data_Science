# task 1 for lesson_9
class Automobile(object):
    def __init__(self, model, color, engine_capacity):
        self.model = model
        self.color = color
        self.engine_capacity = engine_capacity

    def move_forward(self, distance):
        return (f"{self.color} {self.model} automobile moved forward for {distance} kilometers")

    def move_backward(self, distance):
        return (f"{self.color} {self.model} automobile moved backward for {distance} kilometers")

class Automobile_junior(Automobile):
    def turn_left(self, deegrees):
        return (f"{self.color} {self.model} automobile turned left for {deegrees} deegrees")

    def turn_right(self, deegrees):
        return (f"{self.color} {self.model} automobile turned right for {deegrees} deegrees")

red_renault = Automobile('Renault', "Red", "1.6 MPI")
black_bmw = Automobile_junior('BMW', "Black", "2.2 Turbo")

# print(red_renault.move_forward(15))
# print(black_bmw.turn_left(90))
# print(black_bmw.move_backward(10))

# task_2 for lesson_9
class TextProcessor(object):
    def __init__(self):
        self.__punctuation_symbs = [".", ",", "!", "?", ";", ":", "-", "'", "\"", \
                                    "(", ")", "[", "]", "{", "}", "<", ">"]

    def __is_punktiantian(self, symb):
        return symb in self.__punctuation_symbs

    def get_clean_string(self, string):
        result = ""
        for char in string:
            if not self.__is_punktiantian(char):
                result += char
        return result


class TextLoader(object):
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ""

    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print("Виводиться очищений текст:")
        return self.__clean_string

class DataInterface(object):
    def __init__(self):
        self._text_loader = TextLoader()

    def process_text(self, list_strings):
        for i in list_strings:
            self._text_loader.set_clean_text(i)
            print(self._text_loader.clean_string)



# data_interface = DataInterface()
# texts = ["Hello, world!", "This is a sample text."]
# data_interface.process_text(texts)


# task_3 for lesson_9
class Parallelogram(object):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

class Square(Parallelogram):
    def get_area(self):
        if self.width is not None:
            return self.width ** 2
        elif self.length is not None:
            return self.length ** 2

paral = Parallelogram(10, 15)
sqr = Square(2, 2)

print(paral.get_area())
print(sqr.get_area())