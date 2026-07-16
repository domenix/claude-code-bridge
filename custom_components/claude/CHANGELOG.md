# Changelog

## 1.0.1

- Raise the default run timeout to 290 s (was 90 s) and the per-tool timeout to
  180 s (was 45 s), so multi-step turns and slow tools have room to finish.
  290 s sits just under Assist's own 300 s pipeline timeout, so a run that
  overruns reports what timed out instead of a generic pipeline error.

## 1.0.0

Initial release.

- Conversation agent and AI Task entities backed by your Claude subscription,
  with Assist device control, streaming, attachments, extended thinking, web
  search / fetch and structured output.
- **Log in with Claude** in the config flow, or enter an OAuth token / API key
  manually. The login expiry is watched: a repair issue is raised 14 days ahead
  of it and again once it lapses.
- Home Assistant LLM tools are exposed to the model through an in-process MCP
  server and executed directly via the conversation's LLM API.
- Per-subentry options for model, thinking budget / effort, code execution,
  subagents, web search / fetch, activity streaming and run timeout.
