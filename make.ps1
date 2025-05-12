param([string]$task = "help")

function Show-Help {
    $scriptContent = Get-Content $PSCommandPath -Raw
    $matches = [regex]::Matches($scriptContent, "function\s+([A-Za-z-]+)\s+\{[\s\S]*?#\s+(.+?)\r?\n")

    foreach ($match in $matches) {
        $taskName = $match.Groups[1].Value.Replace("Task-", "").ToLower()
        $description = $match.Groups[2].Value
        Write-Host "$($taskName.PadRight(20, ' '))" -ForegroundColor Cyan -NoNewline
        Write-Host " $description"
    }
}

function Task-Install {
    # Install the virtual environment and install the pre-commit hooks
    Write-Host "Creating virtual environment using uv" -ForegroundColor Blue
    uv venv --seed
    uv sync
    Write-Host "Installing pre-commit hooks" -ForegroundColor Blue
    uv run pre-commit install --install-hooks
}

function Task-Check {
    # Run code quality tools
    Write-Host " Checking lock file consistency with 'pyproject.toml'" -ForegroundColor Blue
    uv lock --locked
    Write-Host " Linting code: Running pre-commit" -ForegroundColor Blue
    uv run pre-commit run -a
    Write-Host " Static type checking: Running mypy" -ForegroundColor Blue
    uv run mypy

    Write-Host " Checking for obsolete dependencies: Running deptry" -ForegroundColor Blue
    uv run deptry src

}

function Task-Test {
    # Test the code with pytest
    Write-Host " Testing code: Running pytest" -ForegroundColor Blue

    uv run python -m pytest --doctest-modules

}

function Task-Sync {
    # Sync with the upstream repository
    Write-Host " Syncing with upstream repository" -ForegroundColor Blue
    Write-Host " Checking out develop branch" -ForegroundColor Blue
    git checkout develop
    Write-Host " Fetching upstream changes" -ForegroundColor Blue
    git fetch upstream
    Write-Host " Rebasing develop branch" -ForegroundColor Blue
    git pull --rebase upstream develop
    Write-Host " Pushing changes to origin" -ForegroundColor Blue
    git push origin develop
}

function Task-Build {
    # Build wheel file
    Task-CleanBuild
    Write-Host " Creating wheel file" -ForegroundColor Blue
    uvx --from build pyproject-build --installer uv
}

function Task-CleanBuild {
    # Clean build artifacts
    Write-Host " Removing build artifacts" -ForegroundColor Blue
    if (Test-Path -Path "dist") {
        Remove-Item -Path "dist" -Recurse -Force
    }
}


function Task-Publish {
    # Publish a release to PyPI
    Write-Host " Publishing." -ForegroundColor Blue
    uvx twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
}

function Task-BuildAndPublish {
    # Build and publish
    Task-Build
    Task-Publish
}



function Task-DocsTest {
    # Test if documentation can be built without warnings or errors
    Write-Host " Testing documentation build" -ForegroundColor Blue
    uv run mkdocs build -s
}

function Task-Docs {
    # Build and serve the documentation
    Write-Host " Building and serving documentation" -ForegroundColor Blue
    uv run mkdocs serve
}


switch ($task.ToLower()) {
    "install" { Task-Install }
    "check" { Task-Check }
    "test" { Task-Test }
    "build" { Task-Build }
    "clean-build" { Task-CleanBuild }

    "publish" { Task-Publish }
    "build-and-publish" { Task-BuildAndPublish }


    "docs-test" { Task-DocsTest }
    "docs" { Task-Docs }

    "help" { Show-Help }
    default {
        Write-Host "Unknown task: $task" -ForegroundColor Red
        Write-Host "Use 'help' to see available tasks" -ForegroundColor Yellow
        Show-Help
    }
}
