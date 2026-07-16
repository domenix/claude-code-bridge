# Changelog

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
