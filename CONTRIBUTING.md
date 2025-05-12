# Contributing to `colormap-tool`

Contributions are welcome, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

You can contribute in many ways:

# Types of Contributions

## Report Bugs

Report bugs at https://github.com/MeridianInnovation/colormap-tool/issues

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

## Fix Bugs

Look through the GitHub issues for bugs.
Anything tagged with "bug" and "help wanted" is open to whoever wants to implement a fix for it.

## Implement Features

Look through the GitHub issues for features.
Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

## Write Documentation

colormap-tool could always use more documentation, whether as part of the official docs, in docstrings, or even on the web in blog posts, articles, and such.

## Submit Feedback

The best way to send feedback is to file an issue at https://github.com/MeridianInnovation/colormap-tool/issues.

If you are proposing a new feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.

# Get Started!

Ready to contribute? Here's how to set up `colormap-tool` for local development.
Please note this documentation assumes you already have `uv` and `Git` installed and ready to go.

1. Fork the `colormap-tool` repo on GitHub.

2. Clone your fork locally:

In a standard setup, you generally have an `origin` and an `upstream` remote. Latter is the upstream repo you forked from.

```bash
cd <directory_in_which_repo_should_be_created>
git clone git@github.com:YOUR_NAME/colormap-tool.git

# Add the upstream remote
git remote add upstream git@github.com:MeridianInnovation/colormap-tool.git
```

Verify that the remote is added correctly:

```bash
git remote -v

origin  git@github.com:YOUR_NAME/colormap-tool.git (fetch)
origin  git@github.com:YOUR_NAME/colormap-tool.git (push)
upstream  git@github.com:MeridianInnovation/colormap-tool.git (fetch)
upstream  git@github.com:MeridianInnovation/colormap-tool.git (push)

```

3. Now we need to install the environment. Navigate into the directory

```bash
cd colormap-tool
```

Then, install and activate the environment with:

```bash
uv venv --seed
uv sync
```

We recommend using [uv](https://docs.astral.sh/uv/) to manage the development environment because it provides a consistent and reproducible environment for all developers and is easy to setup.

4. Install pre-commit to run linters/formatters at commit time:

```bash
uv run pre-commit install --install-hooks
```

We also provide a `Makefile` to help you with these tasks.
You can use the `make` (or `./make` on windows) command to print the available commands.

For Step 3 and 4, you can use below commands as well:

```bash
# On macOS and Linux
make install
# On Windows
./make install
```

5. Once the environment is set up, you can start working on your feature or bugfix.

We follow the **GitFlow** branching model.

All the features and bugfixes should be branched from `develop` instead of `main`.

First, remember to sync with the upstream repo every time you start working on a new feature or bugfix.

```bash
# Switch to the develop branch
git checkout develop
# Fetch the latest changes from the upstream repo
git fetch upstream
# Merge the latest changes from the upstream repo
git pull --rebase upstream develop
# (Optional) Push the updated develop branch to your fork
git push origin develop
```

Or use `Makefile` to sync with upstream repo:

```bash
make sync
```

6. Create a new branch for your feature or bugfix.

You can use the `git flow` extension to simplify this process.

The `git flow` extension is already included in `Git for Windows` version 2.5.3 and later.

```bash
# Using git-flow
git flow feature start feature/your-feature-name

# Using standard git
git checkout develop
git checkout -b feature/your-feature-name
```

Now you can make your changes locally.

Don't forget to add test cases for your added functionality to the `tests` directory.

7. When you're done making changes, check that your changes pass the formatting tests.

```bash
# Use Makefile
# On macOS and Linux
make check
make test

# On Windows
./make check
./make test

# Or Standard Command

# check
uv lock --locked
uv run pre-commit run -a
uv run mypy
uv run deptry src

# test
uv run python -m pytest --doctest-modules

```

8. (Optional) Before raising a pull request you should also run tox.
   This will run the tests across different versions of Python:

```bash
tox
```

This requires you to have multiple versions of python installed.
This step is also triggered in the CI/CD pipeline, so you could also choose to skip this step locally.

9. Commit your changes.

```bash
# Add all changes
git add .

# Commit with a conventional commit message
# Please see #Commit Message Guidelines for details
git commit -m "feat: add your feature"
```

10. After you have finished your feature, you should publish it to your fork.

```bash
# Using git-flow
git flow feature publish feature/your-feature-name

# Using standard git
git push origin feature/your-feature-name
```

11. Now you can submit a pull request on GitHub.

You need to send a pull request that merges your **feature branch** into the `develop` branch of the original repository.

If you don't know how to do this, you can follow the instructions on the [GitHub documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

Once the PR review is passed, the PR will be merged into the `develop` branch.

If for some reason, you are asked to make changes to your PR, you need to:

1. Make the changes in your local branch.
2. Commit the changes with a new commit message.
   - You can use the `git commit --fixup <commit_hash>` command to create a fixup commit.
   - Or you can use the `git commit --amend` and then `git push --force`(be careful!) to update the existing commit.
3. Push the changes to your fork.
4. Add a comment in the PR to notify the reviewer that you have made changes.
5. Wait for the reviewer to review the changes.

---

# Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.

2. If the pull request adds functionality, the docs should be updated.
   Put your new functionality into a function with a docstring, and add the feature to the list in `README.md`.

# Branch Strategy

We follow a simplified **Git Flow + GitHub Flow** model:

| Branch      | Purpose                            |
| ----------- | ---------------------------------- |
| `main`      | Production-ready code only         |
| `develop`   | Integration branch for development |
| `feature/*` | New features (`feature/login-api`) |
| `bugfix/*`  | Non-urgent bug fixes               |
| `hotfix/*`  | Urgent fixes for production        |
| `release/*` | Pre-release preparations           |

## Branch workflow:

- `develop` is the default working branch.
- All features and fixes are branched from `develop`.
- When a feature or bugfix is complete, it is merged into `develop`.
- When `develop` has accumulated enough features for a release, a release branch is created.
- When the release is ready, the release branch is merged into `main`.

# Commit Message Guidelines

All commit messages should follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

- `feat:` - New feature
- `fix:` - Bug fix
- `refactor:` - Code refactoring
- `chore:` - Build tasks or maintenance
- `docs:` - Documentation only changes
- `test:` - Adding or updating tests

## Example:

```plaintext
feat: add user authentication
fix: correct typo in login controller
```

# Workflow Summary

1. Fork the repository.
2. Clone your fork locally.
3. Create a branch for local development.
4. Write clean, tested code and follow the commit message guidelines.
5. Run pre-commit hooks locally.
6. Push to your fork/branch.
7. Open a pull request.
