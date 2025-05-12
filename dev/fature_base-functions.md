# Branch: feature/base-functions

## Description

This branch adds base functions to the project.

## Changes

- Added base functions to the project.
- Added documentation to the project.
- Added tests to the project.

## Features

- See documentation for more details.

## Tests

- See Tests for more details.

## Documentation

#### 1. Initial Requirements Analysis

- Identified need for clear documentation structure
- Defined navigation hierarchy
- Planned content organization
- Selected documentation tools

#### 2. Tool Selection

- Chose mkdocs with material theme for modern, responsive design
- Selected mkdocs-include-markdown-plugin for content reuse
- Integrated mkdocstrings[python] for API documentation
- Using uv for dependency management

#### 3. Documentation Structure Implementation

- Created navigation structure:
  ```
  - Home
    - Overview - index
    - Usage
    - Changelog
    - License
  - API Reference
  ```
- Set up content organization:
  - Overview: Project introduction and features
  - Usage: Detailed usage examples and API documentation
  - Changelog: Version history
  - License: Project license information

#### 4. Content Management

- Implemented content inclusion using mkdocs-include-markdown-plugin
- Organized README.md content into appropriate sections
- Set up proper content boundaries for each section
- Ensured consistent formatting across all pages

#### 5. Issues and Solutions

1. How to include the README.md file in the index.md file?

   - Solution: Use the include-markdown plugin to include the README.md file in the index.md file.
   - Reference: [mkdocs-include-markdown-plugin documentation](https://github.com/mondeja/mkdocs-include-markdown-plugin)

2. How to include the LICENSE file in the license.md file?

   - LICENSE file should be included as a quote instead of text.
   - Solution: use below code:

   ```
   {%
       include-markdown "../../LICENSE"
       preserve-includer-indent=true
   %}
   ```

### References

- [Material for MkDocs Documentation](https://squidfunk.github.io/mkdocs-material/)
- [mkdocs-include-markdown-plugin](https://github.com/mondeja/mkdocs-include-markdown-plugin)
- [mkdocstrings Documentation](https://mkdocstrings.github.io/)
