import matplotlib.pyplot as plt


class PlotDrawer:
    def __init__(self, df):
        self.df = df

    def draw_plots(self, column):
        plt.figure(figsize=(10, 6))  # Увеличение размера графика
        sorted_df = self.df.sort_values(by=column, ascending=False)
        ax = sorted_df[column].plot(kind='bar')
        plt.title(f'Plot of {column}')
        plt.ylabel(column)
        ax.set_xticks([])  # Убираем все метки на оси X
        plot_path = f'plots/{column}_plot.png'
        plt.savefig(plot_path)
        plt.close()  # Закрытие графика для предотвращения перекрытия
        return plot_path

    def draw_scatter_plot(self, column_x, column_y):
        plt.figure(figsize=(10, 6))  # Увеличение размера графика
        plt.scatter(self.df[column_x], self.df[column_y])
        plt.title(f'Scatter Plot of {column_x} vs {column_y}')
        plt.xlabel(column_x)
        plt.ylabel(column_y)
        plot_path = f'plots/{column_x}_vs_{column_y}_scatter_plot.png'
        plt.savefig(plot_path)
        plt.close()  # Закрытие графика для предотвращения перекрытия
        return plot_path
