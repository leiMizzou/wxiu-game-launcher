# Contributing

Contributions are welcome for session modes, media discovery, local tracking, release workflows, free play-money poker candidates, game aliases, recommendation logic, documentation, tests, and safety improvements.

## Development workflow

1. Fork and clone the repository.
2. Create a focused branch.
3. Edit files under `plugins/codex-lounge/`.
4. Run `python3 scripts/validate.py`.
5. Run `python3 -m unittest discover -s tests -v`.
6. Test Browser-backed behavior in a new Codex task with OpenAI's Browser plugin enabled.
7. Open a pull request describing the behavior change and test prompts.

Do not contribute ROMs, game files, copied website assets, credentials, personal data, scraping workflows, paid-gambling features, or instructions for bypassing access restrictions.
