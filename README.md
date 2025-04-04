# goit-pycore-hw-05

Часова складність алгоритму обчислення чисел Фібоначчі з кешуванням (мемоізації) є \(O(n)\).
https://poe.com/s/Eak681zglDGLsPQo2rkd

### Пояснення:

1. **Основна ідея кешування**:

    - Використовуючи кеш (словник) для збереження вже обчислених значень чисел Фібоначчі, ви уникаєте повторних обчислень для одних і тих самих аргументів.
    - Кожне число Фібоначчі обчислюється лише один раз, після чого його значення зберігається в кеші.

2. **Рекурсивні виклики**:

    - Хоча рекурсивна версія без використання кешування має експоненційну складність \(O(2^n)\), з кешуванням кожне число від 0 до \(n\) обчислюється лише один раз.
    - Таким чином, загальна кількість унікальних обчислень становить \(n\).

3. **Отже**:
    - Ваша функція виконає в середньому \(O(n)\) обчислень, а доступ до кешу для перевірки та зберігання значень виконується за константний час \(O(1)\).
    - В результаті загальна часова складність алгоритму з кешуванням дорівнює \(O(n)\).

У підсумку, кешування значно покращує ефективність обчислення серії чисел Фібоначчі порівняно з некешованим підходом.

### модуль `typing`

У Python рекомендується використовувати модуль `typing`, зокрема `Callable`, для вказання типів функцій, замість використання вбудованого типу `callable`. Ось чому:

### Переваги використання `from typing import Callable`:

1. **Більш точний опис**:

    - Використовуючи `Callable`, ви можете вказати не тільки те, що значення є функцією, але й визначити типи її аргументів і тип повернутого значення. Це робить типізацію більш структурованою і зрозумілою.

2. **Документація**:

    - Використання `Callable` покращує документацію коду. Це особливо корисно для людей, які читають ваш код, оскільки вони можуть швидко побачити, які аргументи очікує функція і що вона повертає.

3. **Стандартизація**:
    - Використання `Callable` відповідає трендам та стандартам в розвитку Python і типізації. Це робить ваш код більш читабельним і підтримуваним, особливо в середовищі колективної роботи.

## інші фреймворки і бібліотеки Python, які значно полегшують розробку утиліт командного рядка.

https://poe.com/s/eSshDD1abARTZ4d4XLbQ

-   https://click.palletsprojects.com/en/stable/
-   https://typer.tiangolo.com/
-   https://google.github.io/python-fire/
-   http://docopt.org/

Ось деякі з найпопулярніших:

1. **Click**:

    - Click є популярною бібліотекою для створення командних утиліт у Python. Вона простіша у використанні, ніж стандартна бібліотека `argparse`, і дозволяє створювати більш зручні інтерфейси командного рядка.
    - Переваги: простий синтаксис, підтримка підкоманд, автоматичне генерування допомоги та документації.

    **Приклад використання**:

    ```python
    import click

    @click.command()
    @click.argument('name')
    @click.option('--greeting', default='Hello', help='Greeting message')
    def greet(name, greeting):
        click.echo(f'{greeting}, {name}!')

    if __name__ == '__main__':
        greet()
    ```

2. **Typer**:

    - Typer — це ще одна бібліотека для створення командних рядків, яка базується на `Click`, але з підтримкою типізації. Це дозволяє автоматично генерувати документацію та полегшує валідацію аргументів.
    - Переваги: інтеграція з Pydantic для валідації, автозавершення команд і аргументів.

    **Приклад використання**:

    ```python
    from typer import Typer

    app = Typer()

    @app.command()
    def greet(name: str, greeting: str = "Hello"):
        """Greet the user with a friendly message."""
        print(f"{greeting}, {name}!")

    if __name__ == "__main__":
        app()
    ```

3. **Argparse**:

    - Хоча `argparse` уже згадувався, це стандартна бібліотека Python для обробки аргументів командного рядка. Вона достатньо потужна, але може бути дещо громіздкою для налаштувань, порівняно з Click або Typer.

4. **Fire**:

    - Google Fire є фреймворком, який автоматично генерує CLI з будь-якого Python-об'єкта, включаючи функції, класи та модулі. Завдяки цьому, ви можете швидко перетворити свої програми в командні утиліти.

    **Приклад використання**:

    ```python
    import fire

    class Greeter(object):
        def greet(self, name='World'):
            return f'Hello, {name}!'

    if __name__ == '__main__':
        fire.Fire(Greeter)
    ```

5. **docopt**:

    - docopt дозволяє вам описати інтерфейс командного рядка у формі рядка документації. Він автоматично парсить аргументи на основі цього опису.

    **Приклад використання**:

    ```python
    """Simple program to greet users.

    Usage:
      greet.py <name> [--greeting=<greet>]

    Options:
      -h --help     Show this help.
      --greeting=<greet> Greeting message [default: Hello].
    """
    from docopt import docopt

    if __name__ == '__main__':
        arguments = docopt(__doc__)
        name = arguments['<name>']
        greeting = arguments['--greeting']
        print(f"{greeting}, {name}!")
    ```

### Висновок

Ці фреймворки і бібліотеки створені для спрощення процесу створення утиліт командного рядка, і ви можете вибрати той, який найкраще відповідає вашим потребам.
