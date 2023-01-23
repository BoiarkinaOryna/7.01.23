'''
   Иодуль ставить символи по черзі
'''

import modules.create_cross as m_cross
import modules.create_zero as m_zero
import modules.data_base as m_data
def who_turn(x, y):
    if m_data.step[0] == "cross":
        m_cross.draw_cross(x, y)
        m_data.step[0] = "zero"
    elif m_data.step[0] == "zero":
        m_zero.make_zero(x + 50, y - 100)
        m_data.step[0] = "cross"