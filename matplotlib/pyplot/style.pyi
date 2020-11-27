from pathlib import Path
from typing import List, Literal, Union

available: List[str]


# style options copy-pasted from plt.style.available
# this isn't strictly correct (since `use` accepts strings
# as paths) but possibly more useful/convenient
def use(style: Union[
    Path,
    Literal['Solarize_Light2',
            '_classic_test_patch',
            'bmh',
            'classic',
            'dark_background',
            'fast',
            'fivethirtyeight',
            'ggplot',
            'grayscale',
            'seaborn',
            'seaborn-bright',
            'seaborn-colorblind',
            'seaborn-dark',
            'seaborn-dark-palette',
            'seaborn-darkgrid',
            'seaborn-deep',
            'seaborn-muted',
            'seaborn-notebook',
            'seaborn-paper',
            'seaborn-pastel',
            'seaborn-poster',
            'seaborn-talk',
            'seaborn-ticks',
            'seaborn-white',
            'seaborn-whitegrid',
            'tableau-colorblind10'],
]) -> None: ...
