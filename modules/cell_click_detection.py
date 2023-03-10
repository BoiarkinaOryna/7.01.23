'''
    Модуль дає змогу ставити знак у комірці, під час натискання
'''

import modules.player_way as m_way
#
def click_cell(x, y):
    # перший рядок таблиці із трьох комірок
    if y > 0 and y < 100:
        # задаємо координати х першої комірки
        if x < 0 and x > -100:
            m_way.who_turn(-100, 100)
        # задаємо координати х другої комірки
        elif x < 100 and x > 0:
            m_way.who_turn(0, 100)
        # задаємо координати х третьої комірки
        elif x < 200 and x > 100:
            m_way.who_turn(100, 100)
    # другий рядок таблиці із трьох комірок
    if y > -100 and y < 0:
        # задаємо координати х четвертої комірки
        if x < 0 and x > -100:
            m_way.who_turn(-100, 0)
        # задаємо координати х п'ятої комірки
        elif x < 100 and x > 0:
            m_way.who_turn(0, 0)
        # задаємо координати х шостої комірки
        elif x < 200 and x > 100:
            m_way.who_turn(100, 0)
    # третій рядок таблиці із трьох комірок
    if y > -200 and y < -100:
        # задаємо координати х першої комірки
        if x < 0 and x > -100:
            m_way.who_turn(-100, -100)
        # задаємо координати х другої комірки
        elif x < 100 and x > 0:
            m_way.who_turn(0, -100)
        # задаємо координати х третьої комірки
        elif x < 200 and x > 100:
            m_way.who_turn(100, -100)
