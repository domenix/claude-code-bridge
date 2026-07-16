"""Test configuration.

The test module imports Home Assistant's own helpers from ``tests.common`` and
``tests.test_util.aiohttp``, which exist in a home-assistant/core checkout. When
running against this repository instead, point those names at the copies shipped
in ``pytest_homeassistant_custom_component`` so the same file runs either way.
"""

import sys
import types


def _alias_core_test_helpers() -> None:
    try:
        import tests.common  # noqa: F401
    except ImportError:
        pass
    else:
        return  # running inside a core checkout

    import pytest_homeassistant_custom_component.common as common
    import pytest_homeassistant_custom_component.test_util.aiohttp as aiohttp_mock

    package = sys.modules.setdefault("tests", types.ModuleType("tests"))
    package.__path__ = getattr(package, "__path__", [])
    sys.modules["tests.common"] = common

    test_util = types.ModuleType("tests.test_util")
    test_util.__path__ = []
    sys.modules["tests.test_util"] = test_util
    sys.modules["tests.test_util.aiohttp"] = aiohttp_mock


def pytest_configure(config: object) -> None:
    """Prepare the module namespace before the test module is imported."""
    _alias_core_test_helpers()


def pytest_sessionstart(session: object) -> None:
    """Import the integration so its package exposes it by attribute."""
    import custom_components.claude  # noqa: F401
