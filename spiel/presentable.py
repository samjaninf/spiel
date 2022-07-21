import inspect
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any

from rich.console import ConsoleRenderable

from spiel.triggers import Triggers


@dataclass
class Presentable:  # Why not an ABC? https://github.com/python/mypy/issues/5374
    title: str = ""

    def render(self, triggers: Triggers) -> ConsoleRenderable:
        raise NotImplementedError

    def get_render_kwargs(
        self, function: Callable[..., ConsoleRenderable], triggers: Triggers
    ) -> Mapping[str, Any]:
        signature = inspect.signature(function)

        kwargs: dict[str, Any] = {}
        if "triggers" in signature.parameters:
            kwargs["triggers"] = triggers

        return kwargs
