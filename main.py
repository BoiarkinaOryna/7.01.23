'''
    Модуль об'єднує всі функції написані раніше у інших модулях
'''
import turtle
import modules.create_table as m_table
import modules.create_screen as m_screen
import modules.cell_click_detection as m_click

m_table.draw_table()

m_screen.screen.onclick(m_click.click_cell, btn= 1, add=True)

turtle.done()