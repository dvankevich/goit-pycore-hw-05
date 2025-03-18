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
