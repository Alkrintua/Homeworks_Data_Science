# create a car class
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."


blue_car = Car("blue", 20000)
red_car = Car("red", 30000)
# print(blue_car)
# print(red_car)

class Bezpilotnyk:
    def __init__(self, model, count_engine, count_camers):
        self.model = model
        self.count_engine = count_engine
        self.count_camers = count_camers

    def in_air(self, seconds, engines):
        return f"""Перевірте всі технічні елементи, безпілотник {self.model} планує взліт. {engines} із 
        {self.count_engine} доступних працюють на повну. Взліт можливий через {seconds} секунд."""

    def on_earth(self, coordinates, seconds):
        return f"""Підготуйте зачищену поверхню для посадки, безпілотник {self.model} готується сісти. Для посадки 
        заплановані {coordinates}. Посадка відбудуться очікувано через {seconds} секунд."""


mavik = Bezpilotnyk("Mavik7", "3", 5)
# print(mavik.in_air(30, 3))
# print(mavik.on_earth("30:60:77", 45))

class User_Service(object):
    def __init__(self, email, age, user_type, data_access, username):
        self.__email = email
        self.__age = age
        self.__user_type = user_type
        self.__data_access = data_access
        self.username = username

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    # def set_age(self, age):
    #     if self.__check_value(age):
    #         self.__age = age
    #     else:
    #         raise ValueError("Вік має бути числовим")

    @property
    def get_email(self):
        return f"Електронна пошта {self.username} така:{self.__email}"


    def give_email(self, value):
        self.__email = value

    @property
    def get_age(self):
        return f"Вік {self.username} {self.__age} років."


    def give_age(self, age):
        if self.__check_value(age):
            self.__age = age
        else:
            raise ValueError("Вік має бути числовим")

    def accces_is(self):
        if self.__user_type == "superuser" or self.__user_type == "moderator":
            return "access granted"
        else:
            return "access denied"

petro = User_Service("petro@gmail.com", 35, "superuser", "full", "petya_p")

print(petro.get_age)
petro.give_email("alrintua@gmail.com")
petro.give_age(55)
print(petro.get_age)
print(petro.get_email)
print(petro.accces_is())






