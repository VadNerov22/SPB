#Игра "Крестики-нолики" для 2-х игроков или 1-ого игрока и компьютера
import random

def print_instructon():
    """Выводит на экран инструкцию для игрока."""
    print(
        """
Добро пожаловать в игру "Крестики-нолики". В данной игре Вы сможете сами определить размер игрового поля 
(количество ячеек в строке), стандартный размер игрового поля 3*3 ячейки. Чтобы сделать ход, Вам необходимо 
определить ячейку куда Вы хотите пойти, т.е. поставить букву "Х" (англ. расскладка клавиатуры), или цифру -"0"). 
Для этого необходимо вести номер строки и столбца от 1 до 9 (для стандартного размера игрового поля), 
как показано ниже:   
            0   1   2
        0 |___|___|___|
        1 |___|___|_X_|  так "X" стоит в ячейке: строка - 1; столбец - 2.
        2 |___|___|___|
         """
        )


# Блок 1 - ввод данных
def input_int(input_data: str, min_i: int=1, max_i: int=None) -> int:
    """
    Проверяет введенные данные и приводит их к целому числу. Также возможно
    установить границы допустимого значения.
    :param input_data: введенные данные;
    :param min_i: минимально допустимое числовое значение (по умолчанию 1);
    :param max_i: максимально допустимое числовое значение;
    :return: возвращает целое число
    """
    while True:
        try:
            value = int(input(input_data))
        except ValueError:
            print("Вы ошиблись. Необходимо ввести целое число. Попробуйте ещё раз.")
            continue
        if min_i != 1 and max_i is not None:
            if not min_i <= value <= max_i:
                print(f"Необходимо ввести целое число в пределах от {min_i} до {max_i}.")
                continue
        return value


def input_str(text: str, list_control: list) -> str:
    """
    Проверяет введенные данные на наличие символов в списке и выводит строчные данные.
    :param text: определяет введенные данные согласно условиям;
    :param list_control: содержит список заданных символов;
    :return: возвращает строчный символ из заданного списка.
    """
    while True:
        value = input(text).capitalize()
        if value not in list_control:
            print(f"Вы ввели некорректные данные. Выберите значения из списка: {list_control}")
            continue
        return value


# Блок 2 - игровое поле и операции с ним
def base_field(cells: int, empty_cell: str=" ") -> list[list]:
    """
    Создает пустое игровое поле.
    :param cells: количество ячеек игрового поля в строке (количество строк = количеству ячеек в строке);
    :param empty_cell: символы, заполняющие пустые ячейки;
    :return: возвращает игровое поле в виде списка списков.
    """
    return [[empty_cell] * cells for row in range(cells)]


def draw_field(field: list[list]) -> None:
    """
    Выводит поле согласно заданным параметрам.
    :param field: размер поля;
    :return: None
    """
    for row in field:
        for column in row:
            print(f"| __{column}__", end=" ")
        print("|")


def free_players_step(field: list[list], cells: int) -> [int, int]:
    """
    Определяем индексы (строка, столбец) не занятых ячеек.
    :param field: размер поля;
    :param cells: количество ячеек в строке;
    :return: возвращает индексы доступных ячеек
    """
    while True:
        index_row = input_int("Введите номер строки:\n", 0, cells - 1)
        index_column = input_int("Введите номер столбца:\n", 0, cells - 1)
        if field[index_row][index_column] != ' ':
            print("ВНИМАНИЕ!!! Выберите другую ячейку, эта уже занята!")
            continue
        return index_row, index_column


def player_step(field: list[list], player: str, index_row: int, index_column: int) -> list[list]:
    """
    Возвращает игровое поле с отметкой хода, выполненного игроком.
    :param field: игровое поле;
    :param player: игрок, выполнивший ход;
    :param index_row: номер строки ячейки;
    :param index_column: номер столбца ячейки;
    :return: Возвращает обновленное игровое поле.
    """
    field = field.copy()
    field[index_row][index_column] = player
    return field


# Блок 3 - смена игрока, проверка (победа/ничья/поражение)
def next_player_s(player_s: str) -> str:
    """
    Меняет символ игрока, совершившего ход, на символ другого игрока.
    :param player: игрок, совершивший ход;
    :return: возвращает символ другого игрока.
    """
    new_player_symbol = "X" if player_s == "0" else "0"
    return new_player_symbol


def winer(field: list[list]) -> bool:
    """
    Проводит проверку на выигрыш одним из игроков.
    :param field: игровое поле;
    :return: возвращает если есть выиграшная комбинация True, если нет - False
    """
    n = len(field)
    for row in field:
        if row[0] != " " and all([row[0] == cell for cell in row[0:]]):
            return True
    for col in zip(*field):
        if col[0] != " " and all([col[0] == cell for cell in col[0:]]):
            return True
    for i in range(n):  # главная диагональ
        if field[i][i] != " " and all([field[i][i] == field[0][0] for i in range(n)]):
            return True
    for i in range(n): # побочная диагональ
        if field[i][n - 1 - i] != " " and all([field[i][n - 1 - i] == field[0][n - 1] for i in range(n)]):
            return True

    return False


# Блок 4 - игра человек-человек
def game_human(field: list[list], player_1_name: str, player_1_symbol: str, cells: int) -> str:
    """
    Запуск игры "человек-человек".
    :param field: игровое поле;
    :param player_1_name: имя первого игрока;
    :param player_1_symbol: символ первого игрока ("X", "0");
    :param cells: количество ячеек в строке игрового поля;
    :return: возвращает результат игры.
    """
    current_player_symbol = player_1_symbol
    current_player_name = player_1_name
    player_2_name = input("Введите имя второго игрока:\n").capitalize()
    count_player_steps = 0 # счетчик сделанных игроками ходов
    draw_field(field)
    while count_player_steps < cells ** 2:  # выполнятся, пока есть хоть одна свободная ячейка на поле
        print(f"Ваш ход, {current_player_name}!")
        index_row, index_column = free_players_step(field, cells) # проверяем ход игрока
        field = player_step(field, current_player_symbol, index_row, index_column) # обновляем поле
        count_player_steps += 1
        draw_field(field)
        if winer(field):
            print(f"Поздравляю! Вы победили {current_player_name}!")
            return current_player_name
        current_player_symbol = next_player_s(current_player_symbol)
        current_player_name = player_2_name if current_player_name == player_1_name else player_1_name
    print("Ничья. Попробуйте еще раз!")


# Блок 5 - игра человек-компьютер
def free_players_step_pc(field: list[list], cells: int) -> [int, int]:
    """
    Определяем индексы (строка, столбец) не занятых ячеек.
    :param field: размер поля;
    :param cells: количество ячеек в строке;
    :return: возвращает индексы доступных ячеек
    """
    while True:
        index_row = random.randint(0, cells - 1)
        index_column = random.randint(0, cells - 1)
        if field[index_row][index_column] != ' ':
            continue
        return index_row, index_column


#def best_step_pc(field: list[list], cells: int, count_player_steps: int) -> [int, int]:
    """
    Определяет лучший ход для завершения игры Компьютера и не дает выиграть другому игроку.
    :param field: размер поля;
    :param cells: количество ячеек в строке;
    :param count_player_steps: количество совершенных ходов игроками;
    :return: возвращает лучшие индексы доступных ячеек для выигрыша или сведения игры в ничью.
    """
    #while True:
        #index_row = ????_#ограничения поля(0, cells - 1) + условия winer
        #index_column = ????_#ограничения поля(0, cells - 1) + условия winer
        #if field[index_row][index_column] != ' ':
            #continue
        #elif count_player_steps < cells * 2 - 2: #пока остается последний ход у игроков
            #pass
        #return index_row, index_column
# В РАЗРАБОТКЕ!!!


def game_pc(field: list[list], player_1_name: str, player_1_symbol: str, cells: int) -> str:
    """
    Запуск игры "человек-человек".
    :param field: игровое поле;
    :param player_1_name: имя первого игрока;
    :param player_1_symbol: символ первого игрока ("X", "0");
    :param cells: количество ячеек в строке игрового поля;
    :return: возвращает результат игры.
    """
    current_player_symbol = player_1_symbol
    current_player_name = player_1_name
    player_pc = "Компьютер"
    count_player_steps = 0 # счетчик сделанных игроками ходов
    draw_field(field)
    while count_player_steps < cells ** 2:  # выполнятся, пока есть хоть одна свободная ячейка на поле
        if current_player_name == player_1_name:
            print(f"Ваш ход, {current_player_name}!")
            index_row, index_column = free_players_step(field, cells) # проверяем ход игрока
            field = player_step(field, player_1_symbol, index_row, index_column) # обновляем поле
            count_player_steps += 1
            draw_field(field)
        elif current_player_name == player_pc:
            print(f"Ходит, {player_pc}!")
            index_row, index_column = free_players_step_pc(field, cells)  # проверяем ход игрока
            field = player_step(field, current_player_symbol, index_row, index_column)  # обновляем поле
            count_player_steps += 1
            draw_field(field)
        if winer(field):
            print(f"Поздравляю! Вы победили {current_player_name}!")
            return current_player_name
        current_player_symbol = next_player_s(current_player_symbol)
        current_player_name = player_pc if current_player_name == player_1_name else player_1_name
    print("Ничья. Попробуйте еще раз!")
# Блок 6 - запуск приложения
def app():
    """
    Запуск приложения игры "Крестики-нолики".
    :return: определяем необходимые значения для запуска игры.
    """
    print_instructon()
    cells = input_int("НАЧИНАЕМ ИГРАТЬ!!!\nВведите количество ячеек в одной строке:\n", 3, 10)
    field = base_field(cells)
    player_1_name = input("Вы ходите первым! Введите Ваше имя:\n").capitalize()
    player_1_symbol = input_str("Что выбираем? 'X' или '0':\n", ["X", "0"])
    flag_game = input_str("Против кого будем играть? "
                          "Выберите: 1 - против человека, 2 - против компьютера:\n", ["1", "2"]
                          )
    if flag_game == "1":
        game_human(field, player_1_name, player_1_symbol, cells)
    else:
        game_pc(field, player_1_name, player_1_symbol, cells)


if __name__ == "__main__":
    app()
