"""Matplotlib helpers shared by the linear algebra pages."""

import numpy as np
from matplotlib.axes import Axes
from numpy.typing import ArrayLike


def matrix_heatmap(
    ax: Axes, data: ArrayLike, title: str, cmap: str | None = None
) -> None:
    """
    Draw an annotated heatmap for a matrix on the given Axes.

    Uses a diverging colourmap (RdBu_r) when the data contains negative
    values, and a sequential colourmap (Blues) otherwise.  Passing `cmap`
    overrides this and lets matplotlib scale the colours to the data.  Each
    cell is labelled with its value formatted to four significant figures.

    Args:
        ax: The axes to draw on.
        data: The matrix values to visualise.
        title: Title displayed above the heatmap.
        cmap: Colourmap to use instead of the default choice.
    """
    values = np.array(data, dtype=float)
    abs_max = np.abs(values).max() or 1
    if cmap is not None:
        ax.imshow(values, cmap=cmap, aspect="equal")
    elif values.min() < 0:
        ax.imshow(values, cmap="RdBu_r", aspect="equal", vmin=-abs_max, vmax=abs_max)
    else:
        ax.imshow(values, cmap="Blues", aspect="equal", vmin=0, vmax=abs_max * 2)
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            ax.text(
                j,
                i,
                f"{values[i, j]:.4g}",
                ha="center",
                va="center",
                fontsize=12,
                fontweight="bold",
            )
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, fontsize=11)


def plot_transformed_shape(
    ax: Axes,
    M: ArrayLike,
    shape: ArrayLike,
    color: str,
    label: str,
    alpha: float = 0.3,
) -> None:
    """Apply matrix M to a 2D shape (2×n array of column points) and plot it."""
    transformed = np.asarray(M) @ np.asarray(shape)
    closed = np.hstack([transformed, transformed[:, [0]]])
    ax.fill(closed[0], closed[1], color=color, alpha=alpha)
    ax.plot(closed[0], closed[1], color=color, linewidth=2, label=label)
