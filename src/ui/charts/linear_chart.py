from numpy import ndarray
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class LinearChart(FigureCanvasQTAgg):
    def __init__(
        self,
        data: tuple[ndarray, ndarray],
        title: str,
        labels: tuple[str, str],
        width: int = 5,
        height: int = 4,
        dpi: int = 100,
    ):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.plot(data[0], data[1])
        self.axes.set_title(title)
        self.axes.set_xlabel(labels[0])
        self.axes.set_ylabel(labels[1])
        self.axes.grid(True)

        super().__init__(fig)
