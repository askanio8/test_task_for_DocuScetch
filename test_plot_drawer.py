import unittest
import os
import pandas as pd
from drawing.drawing import PlotDrawer


class TestPlotDrawer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Загрузка данных для тестов
        file_url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
        cls.df = pd.read_json(file_url)
        cls.plot_drawer = PlotDrawer(cls.df)

    def test_draw_plots(self):
        # Тестирование метода draw_plots
        plot_path = self.plot_drawer.draw_plots('mean')
        self.assertTrue(os.path.exists(plot_path))
        os.remove(plot_path)  # Удаление тестового файла после проверки

    def test_draw_scatter_plot(self):
        # Тестирование метода draw_scatter_plot
        plot_path = self.plot_drawer.draw_scatter_plot('mean', 'max')
        self.assertTrue(os.path.exists(plot_path))
        os.remove(plot_path)  # Удаление тестового файла после проверки


if __name__ == '__main__':
    unittest.main()
