print("\033[34m{}".format("Вас вітає калькулятор, зроблений з допомогою ООП від Геннадія Патенка"))
math_actions = ("*", "-", "+", "**", "/")

class Calculator():
    def __int__(self, x, z):
        self.x = x
        self.z = z


    def sum(self, x, z):
        print("Сумма дорівнює", int(x) + int(z))


    def difference(self, x, z):
        print("Різниця дорівнює", int(x) - int(z))

    def multiplying(self, x, z):
        print("Результат множення дорівнює", int(x) * int(z))


    def div(self, x, z):
        print("Після ділення отримуємо", int(x) / int(z))


    def grade(self, x, z):
        print("Результат після зведення в степінь", int(x) ** int(z))


k = Calculator()
x = 0
y = 0
z = 0

print("Будь-ласка, введіть дані для обчислень")
def x_input():
    global x
    a = input("Введіть перше число: ")
    if a.isdigit() is False:
        print("""В числовому значенні мають бути тільки числа від 0 до 9
        Будь-ласка, повторіть спробу!""")
        x_input()
    else:
        x = a



def y_input():
    global y
    b = input("Введіть бажану математичну дію +, -, /, *, **: ")
    if b not in math_actions:
        print("""Можна вводити тільки наступні дії: +, -, /, *, **.
        Будь-ласка, повторіть спробу""")
        y_input()
    else:
        y = b

def z_input():
    global z
    c = input("Введіть друге число: ")
    if c.isdigit() is False:
        print("""В числовому значенні мають бути тільки числа від 0 до 9
        Будь-ласка, повторіть спробу!""")
        z_input()
    else:
        z = c

while True:
    x_input()
    y_input()
    z_input()


    if y == "+":
        k.sum(x, z)
        exit_button = input("""Хочеш продовжити, тисни ПРОБІЛ ТА ENTER!
        Хочеш припинити, тисни будь-яку клавішу та ENTER!: """)
        if exit_button == " ":
            continue
        else:
            print("Допобачення!")
            break
    elif y == "-":
        k.difference(x, z)
        exit_button = input("""Хочеш продовжити, тисни ПРОБІЛ ТА ENTER!
                Хочеш припинити, тисни будь-яку клавішу та ENTER!: """)
        if exit_button == " ":
            continue
        else:
            print("Допобачення!")
            break
    elif y == "*":
        k.multiplying(x, z)
        exit_button = input("""Хочеш продовжити, тисни ПРОБІЛ ТА ENTER!
                Хочеш припинити, тисни будь-яку клавішу та ENTER!: """)
        if exit_button == " ":
            continue
        else:
            print("Допобачення!")
            break
    elif y == "/":
        k.div(x, z)
        exit_button = input("""Хочеш продовжити, тисни ПРОБІЛ ТА ENTER!
                Хочеш припинити, тисни будь-яку клавішу та ENTER!: """)
        if exit_button == " ":
            continue
        else:
            print("Допобачення!")
            break
    else:
        k.grade(x, z)
        exit_button = input("""Хочеш продовжити, тисни ПРОБІЛ ТА ENTER!
                Хочеш припинити, тисни будь-яку клавішу та ENTER!: """)
        if exit_button == " ":
            continue
        else:
            print("Допобачення!")
            break
