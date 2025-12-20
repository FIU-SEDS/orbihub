# OrbiHub App Developer Guide

## Quick Start

Create an OrbiHub-compatible app in 3 steps:

### 1. Create Entry Point

**`__main__.py` at repository root:**
```python
"""Entry point for OrbiHub"""

def main():
    print("Hello from OrbiHub!")
    # Your app logic here

if __name__ == "__main__":
    main()
```

### 2. List Dependencies

**`requirements.txt`:**
```
# Add your dependencies
PySide6>=6.6.0
numpy>=1.24.0
```

### 3. Push to GitHub
```bash
git init
git add __main__.py requirements.txt
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/your-app
git push -u origin main
```

## App Structure

### Minimal App
```
your-app/
├── __main__.py
└── requirements.txt
```

### App with Package
```
your-app/
├── __main__.py          # Entry point
├── requirements.txt
└── your_app/            # Package
    ├── __init__.py
    ├── ui.py
    └── logic.py
```

**`__main__.py` imports from package:**
```python
from your_app.ui import start_gui

if __name__ == "__main__":
    start_gui()
```

## Testing Locally

### Simulate OrbiHub Installation
```bash
# Clone your repo
git clone https://github.com/yourusername/your-app test-install
cd test-install

# Create venv
python -m venv venv

# Activate venv
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Test launch
python __main__.py
```

## Registry Configuration

When submitting your app to OrbiHub, provide:

**Required Information:**
```python
{
    "id": "your-repo-name",  # MUST match GitHub repo name
    "name": "Display Name",   # User-friendly name
    "description": "Brief description",
    "version": "1.0.0",
    "repo": "https://github.com/username/your-repo-name",
    "author": "Your Name",
    "image": "icon_filename.png"  # Optional
}
```

### App ID Rules

**CRITICAL:** The `id` field must match your repository name (without owner).

✅ **Correct:**
- Repo: `github.com/erielC/pyside6-calculator`
- App ID: `"id": "pyside6-calculator"` ← Matches repo name

❌ **Wrong:**
- Repo: `github.com/erielC/pyside6-calculator`
- App ID: `"id": "calculator"` ← Doesn't match!

**Why:**
OrbiHub clones your repo as:
```bash
git clone https://github.com/erielC/pyside6-calculator ~/.orbihub/apps/pyside6-calculator/
```

If your app_id doesn't match, OrbiHub can't find your `__main__.py`.

### Repository Naming Tips

- Use lowercase with hyphens: `flight-analyzer` ✅
- Avoid underscores in repo name: `flight_analyzer` ❌ (breaks on some systems)
- Keep it short and descriptive: `telemetry-viewer` ✅
- Avoid version numbers: `app-v2` ❌

**Note:** Your package folder *inside* the repo can use any name (including underscores).

**Example:**
```
pyside6-calculator/        ← Repo name (matches app_id)
├── __main__.py
└── calculator/            ← Package name (can be different)
    └── ...
```

## Best Practices

### ✅ Do
- Keep `__main__.py` simple (just imports and runs)
- Use semantic versioning (1.0.0, 1.1.0, 2.0.0)
- Add README with usage instructions
- Test on clean virtual environment
- Pin major versions in requirements.txt (`PySide6>=6.0.0,<7.0.0`)

### ❌ Don't
- Don't use relative imports in root `__main__.py`
- Don't assume specific Python version (support 3.9+)
- Don't hardcode file paths (use pathlib)
- Don't require system packages (stay in Python ecosystem)

## Examples

### CLI Tool
```python
# __main__.py
import argparse
from your_app import process

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    args = parser.parse_args()
    process(args.input)

if __name__ == "__main__":
    main()
```

### GUI App (PyQt6/PySide6)
```python
# __main__.py
import sys
from PySide6.QtWidgets import QApplication
from your_app.ui import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
```

### Data Processing Tool
```python
# __main__.py
from your_app.processor import analyze_flight_data

def main():
    data_file = input("Enter flight data file: ")
    results = analyze_flight_data(data_file)
    print(f"Results: {results}")

if __name__ == "__main__":
    main()
```

## Troubleshooting

**Q: My app won't launch**
- Check `__main__.py` is at repository root
- Verify all dependencies in `requirements.txt`
- Test with fresh venv locally

**Q: Import errors**
- Ensure `__init__.py` files in all package directories
- Use absolute imports from your package name

**Q: App crashes on launch**
- Check OrbiHub logs: `~/.orbihub/logs/orbihub.log`
- Test locally with same Python version (3.9+)

## Publishing to OrbiHub

Currently apps are added manually to OrbiHub registry.

**Contact:** eriel@fiu.edu to add your app

**Future (Phase 2):** Web portal for app submission

---

*Last Updated: December 20, 2025*