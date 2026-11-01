import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pytest
from maths_lib.plotting import matrix_heatmap, plot_transformed_shape

matplotlib.use("Agg")


@pytest.mark.parametrize(
    ("data", "cmap", "expected_cmap", "expected_clim"),
    [
        ([[1, 2], [3, 4]], None, "Blues", (0, 8)),
        ([[-1, 2], [3, -4]], None, "RdBu_r", (-4, 4)),
        ([[0, 0], [0, 0]], None, "Blues", (0, 2)),
        ([[1, 2], [3, 4]], "coolwarm", "coolwarm", (1, 4)),
    ],
)
def test_matrix_heatmap_colour_scale(data, cmap, expected_cmap, expected_clim):
    """Verify the colourmap and scale follow the heatmap convention."""
    _, ax = plt.subplots()
    matrix_heatmap(ax, data, "title", cmap=cmap)
    image = ax.get_images()[0]
    assert image.get_cmap().name == expected_cmap
    assert image.get_clim() == expected_clim
    assert ax.get_title() == "title"
    assert len(ax.texts) == 4
    plt.close("all")


def test_plot_transformed_shape_closes_and_transforms_the_shape():
    """Verify the matrix is applied and the outline returns to its first point."""
    _, ax = plt.subplots()
    square = np.array([[0, 1, 1, 0], [0, 0, 1, 1]])
    plot_transformed_shape(ax, 2 * np.eye(2), square, "red", "scaled")
    xs, ys = ax.get_lines()[0].get_data()
    assert list(xs) == [0, 2, 2, 0, 0]
    assert list(ys) == [0, 0, 2, 2, 0]
    plt.close("all")
