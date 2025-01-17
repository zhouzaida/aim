import inspect

from typing import Callable, Dict


class Function:
    registry: Dict[str, 'Function'] = {}

    def __init__(self, func: Callable, name: str):
        self._validate_function(func)
        self._func = func
        self._name = f'{name}.{func.__name__}'

    @staticmethod
    def _validate_function(func: Callable):
        signature = inspect.signature(func)
        for parameter in signature.parameters.values():
            if parameter.kind in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.VAR_POSITIONAL):
                raise ValueError(f'Aim function {func.__name__} must accept keyword arguments.')

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_generator(self) -> bool:
        return inspect.isgeneratorfunction(self._func)

    def execute(self, **kwargs):
        return self._func(**kwargs)
