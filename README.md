# flashCardsBot

A vocabulary learning system that parses lesson content from a website, extracts new words and their definitions, and organizes them into lesson-specific flashcards. The flashcards are delivered through a Telegram bot for convenient review and practice.

## Tech stack

- Python 3.12
- [aiogram 3](https://docs.aiogram.dev/) for the Telegram bot
- [httpx](https://www.python-httpx.org/) as the async HTTP client
- [pydantic](https://docs.pydantic.dev/) / [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) for data models and configuration
- [uv](https://docs.astral.sh/uv/) for dependency management

## Getting started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- `make`

### Installation

```bash
git clone <repo-url>
cd flashCardsBot
make install
```

`make install` installs all dependencies (including dev tools) into `.venv` and sets up the git hooks.

### Configuration

Settings are read from environment variables or a `.env` file in the project root. Copy the sample and fill in your values:

```bash
cp .env.sample .env
```

| Variable            | Description                  |
|---------------------|------------------------------|
| `TUTORIUM_EMAIL`    | Tutorium account email       |
| `TUTORIUM_PASSWORD` | Tutorium account password    |

`.env` is git-ignored. Never commit credentials.

### Running

```bash
make run
```

## Development

### Make commands

| Command        | Description                                         |
|----------------|-----------------------------------------------------|
| `make install` | Install dependencies and git hooks                  |
| `make run`     | Run the bot locally (`python -m bot.main`)          |
| `make lint`    | Check the code with ruff                            |
| `make fix`     | Auto-fix lint issues (e.g. import order)            |
| `make format`  | Format the code with ruff                           |
| `make check`   | Run all pre-commit hooks against the whole codebase |

### Git hooks

Hooks are managed by [pre-commit](https://pre-commit.com/) and installed by `make install`. They run automatically on every commit:

- **ruff**: lints (with auto-fix) and formats staged Python files
- **gitlint**: validates the commit message
- **branch name check**: rejects commits from branches that don't follow the naming convention

To run all hooks against the whole codebase manually:

```bash
make check
```

If a hook modifies files (e.g. ruff reformats them), the commit is aborted. Review the changes, `git add` them and commit again.

### Branch naming

Branches must start with one of these prefixes:

```
feature/  bugfix/  hotfix/  release/  support/  chore/  docs/
```

Example: `feature/telegram-dispatcher`, `chore/update-deps`.

### Commit messages

Commit titles follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<optional scope>): <description>
```

Allowed types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`, `merge`, `release`, `wip`.

Examples:

```
feat(auth): add Tutorium login token request
chore: set up uv, ruff, pre-commit and gitlint
```

A commit body is optional.
