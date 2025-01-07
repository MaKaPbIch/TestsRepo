# Test Repository Example

This repository contains example tests using different testing frameworks:

## Frameworks Used
- PyTest
- UnitTest
- Robot Framework
- Playwright

## Directory Structure
```
tests/
├── pytest/
│   └── test_examples.py
├── unittest/
│   └── test_examples.py
├── robot/
│   └── test_examples.robot
└── playwright/
    └── test_examples.spec.js
```

## Running Tests

### PyTest
```bash
pytest tests/pytest
```

### UnitTest
```bash
python -m unittest discover tests/unittest
```

### Robot Framework
```bash
robot tests/robot/test_examples.robot
```

### Playwright
```bash
npx playwright test tests/playwright
```
