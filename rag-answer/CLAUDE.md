# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based AI agent project that follows onion architecture principles. 

## Architecture

The project follows onion architecture with these layers:
- **Domain Layer**: Core business logic including
- **Application Layer**: business operations
- **Infrastructure Layer**: External dependencies, data persistence, and technical implementations
- **Presentation Layer**: user interface using MVC pattern

## Development Environment

The project uses:
- **Language**: Python 3.10
- **Virtual Environment**: `venv/`
- **Version Control**: Git with GitHub integration
- **Testing Framework**: pytest (recommended)

## Common Commands

### Environment Setup
```bash
# Activate virtual environment
source venv/bin/activate
```

### Testing

#### Running Tests
```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run specific test file
pytest tests/unit/domain/entities/test_board.py

# Run tests with coverage
pytest --cov=src

# Run tests for specific layer
pytest tests/unit/domain/
```

#### Test Structure
```
tests/
├── __init__.py
├── unit/                 # Unit tests
│   ├── __init__.py
│   ├── domain/          # Domain layer tests
│   │   ├── __init__.py
│   │   ├── entities/    # Entity tests
│   │   │   ├── __init__.py
│   │   ├── value_objects/ # Value object tests
│   │   │   ├── __init__.py
│   │   └── services/    # Domain service tests
│   │       ├── __init__.py
│   ├── application/     # Application layer tests
│   │   ├── __init__.py
│   │   └── services/
│   │       ├── __init__.py
│   └── presentation/    # Presentation layer tests
│       ├── __init__.py
└── integration/         # Integration tests
    └── __init__.py
```

#### Test Development Guidelines

**Test Naming Convention:**
- Test files: `test_<class_name>.py` (e.g., `test_board.py`)
- Test methods: `test_<method_name>_<condition>` (e.g., `test_put_valid_position`)

**Test Organization:**
- Unit tests: Test individual classes/methods in isolation
- Integration tests: Test component interactions
- Follow the same directory structure as `src/`

**Test-Driven Development:**
1. Write failing tests first
2. Implement minimal code to make tests pass
3. Refactor while keeping tests green
4. Maintain high test coverage (aim for >90%)

### Development Workflow

#### Feature Development Flow
```bash
# 1. Create and switch to feature branch
git checkout -b feature/feature-name

# 2. Implement the feature with tests
# ... write tests first (TDD) ...
# ... implement code to make tests pass ...

# 3. Run tests to ensure quality
pytest -v

# 4. Commit changes
git add .
git commit -m "Add feature description

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# 5. Push to remote and create pull request
git push -u origin feature/feature-name
gh pr create --title "Feature title" --body "Description of changes"

# 6. After PR is merged, cleanup
git checkout main
git pull origin main
git branch -d feature/feature-name
```

#### Common Git Commands
```bash
# View project issues
gh issue list
gh issue view 1  # View main Othello implementation issue

# Check current status
git status
git branch

# Run basic GitHub Actions workflow
git push  # Triggers hello.yaml workflow
```

#### Issue Registration with Templates
```bash
# Create issue using domain layer template
gh issue create --title "[ドメイン層] エンティティ実装" \
  --body "$(cat .github/ISSUE_TEMPLATE/domain_implementation.md)" \
  --label "domain,enhancement"

# Create issue using application layer template
gh issue create --title "[アプリケーション層] Service実装" \
  --body "$(cat .github/ISSUE_TEMPLATE/application_implementation.md)" \
  --label "application,enhancement"

# Create issue using infrastructure layer template
gh issue create --title "[インフラストラクチャ層] データベース実装" \
  --body "$(cat .github/ISSUE_TEMPLATE/infrastructure_implementation.md)" \
  --label "infrastructure,enhancement"

# Create issue using presentation layer template
gh issue create --title "[プレゼンテーション層] UI実装" \
  --body "$(cat .github/ISSUE_TEMPLATE/presentation_implementation.md)" \
  --label "presentation,enhancement"

# Create bug report
gh issue create --title "[バグ] 問題の概要" \
  --body "$(cat .github/ISSUE_TEMPLATE/bug_report.md)" \
  --label "bug"

# Create general feature request
gh issue create --title "[機能実装] 機能名" \
  --body "$(cat .github/ISSUE_TEMPLATE/feature_request.md)" \
  --label "enhancement"
```

## Project Structure

```
src/
├── main.py          # Main game entry point (currently empty)
├── date.py          # Date utility program
├── utils/           # Project-wide utility functions
│   ├── __init__.py
│   ├── constants.py     # Non-domain constants (system, config, etc.)
│   ├── exceptions.py    # Custom exception classes
│   └── helpers.py       # Common helper functions
├── domain
|   ├── services         # domain service
|   ├── value_objects    # value objects (game constants, enums, etc.)
|   ├── entities         # entities 
|   └── repositories     # repository interface
├── application
|   └── services         # application services
├── infrastructure
|   ├── repositories     # repository implementations
|   └── services         # service implementation
└── presentation
    ├── models           # call usecase with application service
    ├── views            # preferences components
    └── controllers      # call model
```

## Development Notes

- The main implementation is tracked in GitHub Issue #1 with detailed requirements
- Follow onion architecture patterns when implementing new features
- The project uses Japanese language for documentation and some code comments
- Virtual environment is already set up - activate before development
- Testing framework: pytest (install with `pip install pytest pytest-cov`)
- No build tools or dependency management files are present yet

## Key Implementation Tasks

Based on Issue #1, the main development work involves:
1. Implementing domain entities
2. Creating domain services
3. Building application services
4. Developing infrastructure layer
5. Developing presentation layer

Focus on the domain layer first, then application layer, then infrastructure layer, then presentation layer following onion architecture principles.