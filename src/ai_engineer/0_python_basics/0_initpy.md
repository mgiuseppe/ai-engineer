# \_\_init\_\_.py
* Marks a folder as a Python package so you can import from it.
* Modern Python (3.3+) can import from folders without it (\"namespace packages\"), but it's still the standard, safer choice.

## What it's for
* Can stay empty — just marks the folder as a package.
* Can re-export names, so callers don't need to know your internal file/folder layout:
```
    myapp/
        main.py
        services/
            __init__.py
            payment/
                __init__.py
                stripe.py
```
```python
    # services/payment/stripe.py
    class StripeProcessor:
        ...

    # services/payment/__init__.py
    from .stripe import StripeProcessor

    # services/__init__.py
    from .payment import StripeProcessor
```
```python
    # main.py
    from services import StripeProcessor   # instead of services.payment.stripe.StripeProcessor
```

## Applies everywhere
* Not just external libraries — any folder in your own project (models/, services/, utils/, etc.) works the same way.
* Works identically for functions and classes — \_\_init\_\_.py cares about package structure, not what's inside the files.

## Nested folders
* Each folder in the chain needs its own \_\_init\_\_.py.
* Re-exports can be chained upward through multiple levels to flatten deep paths down to a single short import.
* Trade-off: chaining re-exports through many levels means importing the top package eagerly loads everything underneath — convenient for callers, but can slow startup or risk circular imports in large trees."