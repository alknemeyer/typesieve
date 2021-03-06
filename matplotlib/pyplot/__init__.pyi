# It seems the discussion on when and how to add type hints to matplotlib is
# still ongoing:
# https://github.com/matplotlib/matplotlib/issues/13798
# Hopefully they'll do so soon, allowing us to delete this wretched file

from typing import Any, Iterable, List, Optional, Tuple, Union
# Python 3.6 compatibility
try:
    from typing import Literal  # type: ignore
except ImportError:
    from typing_extensions import Literal
from os import PathLike
from . import style


def plot(*args, **kwargs) -> List[Line2D]: ...
def scatter(*args, **kwargs) -> Any: ...
def subplot(*args, **kwargs) -> Axes: ...
def subplots(*args, **kwargs) -> Tuple[Figure, Iterable[Axes]]: ...


def title(x: str) -> Text: ...
def legend(*args, **kwargs) -> Legend: ...


def grid(b: Optional[bool] = None, which: str = 'major',
         axis: str = 'both', **kwargs) -> None: ...


def tight_layout(*,
                 pad: float = 1.08,
                 h_pad: Optional[float] = None,
                 w_pad: Optional[float] = None,
                 rect: Optional[Tuple[float, float, float, float]] = None
                 ):
    ...


def xlabel(x: str) -> Text: ...
def ylabel(x: str) -> Text: ...


def xlim(*args, **kwargs) -> tuple: ...
def ylim(*args, **kwargs) -> tuple: ...
def axis(*args, **kwargs) -> tuple: ...


def show(*args, **kwargs) -> None: ...
def close(*args, **kwargs) -> None: ...


def figure(*args, **kwargs) -> Figure: ...
def gcf() -> Figure: ...
def gca(**kwargs) -> Axes: ...
def cla() -> None: ...


class Figure:
    def legend(self, *args, **kwargs) -> Legend: ...

    def savefig(self,
                fname: Union[str, PathLike, bytes],
                dpi: Optional[Union[float, Literal['figure']]] = None,
                quality: Optional[float] = None,
                optimize: bool = False,
                progressive: bool = False,
                facecolor: Optional[str] = None,
                edgecolor: Optional[str] = None,
                orientation: Literal['landscape', 'portrait'] = 'portrait',
                papertype: Optional[str] = None,
                format: Optional[str] = None,
                transparent: bool = False,
                bbox_inches: Optional[str] = None,
                pad_inches: Optional[float] = None,
                frameon=None, metadata=None): ...

    def show(self, x: bool = True) -> None: ...

    def suptitle(self, t: str, x: float = 0.5, y: float = 0.98,
                 ha: Literal['center', 'left', 'right'] = 'center',
                 va: Literal['top', 'center', 'bottom', 'baseline'] = 'top',
                 fontsize: Optional[float] = None,
                 fontweight: Optional[float] = None,
                 **kwargs_for_text_properties) -> Text: ...

    def subplots_adjust(self,
                        left=None,
                        bottom=None,
                        right=None,
                        top=None,
                        wspace=None,
                        hspace=None,): ...

    def tight_layout(self, renderer=None, pad=1.08,
                     h_pad=None, w_pad=None, rect=None): ...

    def set_size_inches(
            self,
            width_or_width_height: Union[float, Tuple[float, float]],
            height: Optional[float],
            forward: bool = True) -> ...:
        ...

    ...


class Line2D:
    ...


class Text:
    ...


class Legend:
    ...


class Axes:
    def plot(*args: Any, **kwargs: Any) -> Any: ...
    def scatter(*args: Any, **kwargs: Any) -> Any: ...
    def legend(*args: Any, **kwargs: Any) -> Any: ...

    def plot_surface(*args: Any, **kwrags: Any) -> Any: ...

    def view_init(self, *args, **kwargs) -> Any: ...

    def set_xlim(self, *args) -> Any: ...
    def set_ylim(self, *args) -> Any: ...
    def set_zlim(self, *args) -> Any: ...

    def get_xlim(self) -> Any: ...
    def get_ylim(self) -> Any: ...
    def get_zlim(self) -> Any: ...

    def set_xticks(self, *args) -> Any: ...
    def set_yticks(self, *args) -> Any: ...
    def set_zticks(self, *args) -> Any: ...

    def set_xlabel(self, *args) -> Any: ...
    def set_ylabel(self, *args) -> Any: ...
    def set_zlabel(self, *args) -> Any: ...

    def grid(self, x: bool = True) -> Any: ...
    def twinx(self, *args) -> Any: ...
    def _get_lines(self, *args) -> Any: ...
