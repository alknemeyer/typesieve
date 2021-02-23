# typesieve

_"Catch some bugs a bit earlier/code a bit faster"_


## About

A collection of type annotations (see [PEP484](https://www.python.org/dev/peps/pep-0484/), and the ["stub files"](https://www.python.org/dev/peps/pep-0484/#stub-files) section in particular) for some popular Python packages, created as needed for the projects I work on. I do this instead of contributing to the official [Python typeshed](https://github.com/python/typeshed/tree/master/third_party) or the packages themselves, because:

1. it's a lot easier
2. I can commit directly to master

So I _definitely_ don't want you to think that this is reliable or production ready, but you may find it useful for your side projects or as a template to start your own type annotations


## Usage

You may have noticed that the packages here are hard to "properly" type annotate for one reason or another, largely because they change a lot at runtime or accept all sorts of types as input. I'm not a developer for any of these projects, and it seems at least some of them have ongoing efforts to type hint them, but I don't want to wait months to remove all the red squiggles from my code!

So, I've typed _just_ the subset of these libraries that I need, and annotated arguments/return values as `Any`, `**kwargs`, etc in places where it doesn't matter too much, so that I can at least remove the false positives. (I'd rather have a not-overwhelming type-checker that lets some false negatives slip through, than have a thousand alleged errors which mostly turn out to be nothing)

Similarly, I've taken a more "creative" approach to typing some of this stuff, since it's seemingly not possible to treat these libraries as totally static without investing a ton of time into this. For example, we make the return type of `sympy.Symbol` multiplying with another value return a `sympy.Expression` (instead of `sympy.Mul`), which is a type that simply doesn't exist in the SymPy codebase. I think that's a far more useful way of working with SymPy, since one generally cares more about whether something is a `float` vs `sympy.Matrix` vs some sort of SymPy expression, as opposed to a multiplication node specifically (at least, for a user API. I'm sure sympy devs care a lot about that). I'll refer to these as _"proxy types"_

The unfortunate side effect is that your type checker will lead you to believe that writing `sympy.Expression` is perfectly valid, even though results in a `RuntimeError` since, again, `sympy` doesn't actually have an `Expression` class that I'm aware of. Instead, you have to partially annotate your functions using strings, as in the following example:

```python
import sympy as sp

def plus1(x: sp.Symbol) -> 'sp.Expression':
    return x + 1
```

Python's type checkers are perfectly aware of annotations like that

Projects that use these types might have code that looks like the following:

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sympy import Expression

def plus2(x: sp.Symbol) -> 'Expression':
    return x + 2
```

`TYPE_CHECKING` is a variable which the type checker will take as `True` (meaning `mypy` will "import" `Expression`) but which is `False` at runtime (meaning that Python won't _actually_ try to import `Expression` from SymPy, which would result in an error)

THE POINT of this, is that similar skullduggery runs rife through this repo! And although it takes all of 2 minutes to familiarize yourself with it, it's still not necessarily obvious. Notes on the packages are as follows:


### matplotlib

`matplotlib` is huge, and since it's so visual there's not that much need to have proper typing. I've mostly just added a bunch of `Any`s, along with the functions/classes I need, to avoid false positives


### ODrive

In order to reduce development time/duplicated code, the Python code in the `odrive` package is sort of "generated" from the C++ code dynamically. That is largely fine since the main way to interact with an ODrive is via `ipython` (`odrivetool`) which picks up on the dynamically added attributes and methods without problems, but it's annoying if you have to minimize time spent in the lab with your robot (due to covid-19, amongst other reasons) making that whole system fall apart :/ so, the hints are here to give you IDE auto-complete goodness/checking without plugging in the ODrive

Anyway, `odrive.ODrive`, `odrive.Axis`, etc are all "proxy types". This is mostly complete, though it was done using firmware using `0.4.12`. I'll update it to `0.5.1` at some point using the [migration guide](https://docs.odriverobotics.com/migration). Another idea would be to use [`typing.Annotated`](https://realpython.com/python39-new-features/#annotated-type-hints) to add units to everything


### PyOmo

`pyomo.environ` is partially implemented. There is a limit to how well this library can be typed, since it
1. contains frankly astonishing amounts of sub-classing and indirection (which is hard to follow) (no disrespect intentioned - I'm very thankful for Pyomo!), and
2. has dynamism core to the way it operates: a users model is literally dynamically added to a `ConcreteModel` during runtime, so when you write `model.x = pyo.Var()`, don't expect the type checker to catch errors like `model.ex` later on


### SymPy

There are three main types which I think about here: `sympy.Symbol`, `sympy.Matrix` and `sympy.Expression` (which is a proxy type for the result of any arithmetic operation on `Symbol`s and `Expression`). For example:

```python
import sympy as sp
x, y = sp.symbols('x y')

def add(a: sp.Symbol, b: 'sp.Expression') -> 'sp.Expression':
    return a + b

add(x, y**2)            # no problems :)
add(x, sp.Matrix([y]))  # type error
```


## Installation

Two approaches that I can think of:

1. Add it as a [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) in your project:
   ```
   git submodule add https://github.com/alknemeyer/typesieve
   ```
2. Clone it to some global place on your computer, so that all projects share the same files

The next step depends on your programming setup:

- VS code with the [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extension:
    - Settings UI: navigate to Settings > Extensions > Pylance. Make sure the type checker is switched on ("Python › Analysis: Type Checking Mode"), then set "Python › Analysis: Stub Path" to the directory where you keep your stubs. If you went with option 1 above, you'd type `./typesieve/`
    - JSON UI: make sure the type checker is switched on (`"python.analysis.typeCheckingMode": "basic",`) then set `"python.analysis.stubPath": "./typesieve/",` (or wherever you put your stubs)

There is probably a way to `pip install` this, though that seems like more of a hassle than I'm willing to deal with right now :)


## Contributing

Please feel free to contribute type hints! You can add them to your local clone of the repo and benefit straight away, and then submit a pull request which I will almost certainly accept
