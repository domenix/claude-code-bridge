# Tests

Smoke tests for the integration. The Claude Agent SDK is patched out, so no CLI,
network or credentials are required.

```sh
uv venv .venv
uv pip install --python .venv pytest-homeassistant-custom-component claude-agent-sdk
.venv/bin/python -m pytest tests -q
```

Home Assistant pulls extra requirements for the platforms under test
(`conversation` needs `hassil` and `home-assistant-intents`, `ai_task` needs
`PyTurboJPEG`). Install them at the versions pinned in the installed Home
Assistant's `homeassistant/package_constraints.txt`.

`conftest.py` maps the `tests.*` helper imports onto
`pytest_homeassistant_custom_component`, so the same test file also runs
unchanged inside a home-assistant/core checkout.
