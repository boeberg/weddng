# Copilot Instructions

## Project Overview
- Wedding RSVP website with multi-language support
- Location mapper for accommodations
- Organized into web, scripts, and documentation folders

## Code Style
- Use TypeScript with strict mode (for web components, if added)
- Follow ESLint rules in this project
- Clean, readable code with meaningful variable names
- Add comments for complex logic

## Architecture
- **Web:** `web/` - HTML, CSS, JavaScript for the website
- **Scripts:** `scripts/` - Python utilities (load_and_plot_locations.py)
- **Data:** `data/` - Generated outputs (maps, exports)
- **Docs:** `docs/` - Project documentation

## Web Development (`web/`)
- `index.html` - RSVP form with multi-language support
- `overview.html` - Landing page with language selector
- `thankyou.html` - Confirmation page
- `styles.css` - All styling (use CSS variables for theming)

### Guidelines
- Keep HTML semantic and accessible
- Use CSS variables for colors and spacing
- Add translations in the translations object
- Comment non-obvious JavaScript logic

## Python Development (`scripts/`)
- All Python code must run within `.venv` virtual environment
- Activate before running: `source .venv/bin/activate`
- When adding new Python dependencies:
  1. Install packages within `.venv`: `pip install <package-name>`
  2. Update `requirements.txt` immediately: `pip freeze > requirements.txt`
  3. Commit both the code changes and updated `requirements.txt`
- Never suggest running Python without activating `.venv` first

## Testing
- Write unit tests for all Python functions
- Use pytest for testing (add to requirements.txt if needed)
- Test locally before committing

## Documentation
- Update relevant docs when making changes:
  - **docs/SETUP.md** - Installation and configuration
  - **docs/DESIGN_SYSTEM.md** - Design tokens
  - **docs/CUSTOMIZATION.md** - How to customize
  - **README.md** - Project overview
- Keep documentation in sync with code

## Branching & Git
- Use descriptive commit messages
- Reference issue numbers when relevant
- Keep commits focused on single features/fixes

## Local Development
```bash
# Setup
source .venv/bin/activate
pip install -r requirements.txt

# Web server
python3 -m http.server 8000
# Open: http://localhost:8000/web/overview.html

# Location mapper
python scripts/load_and_plot_locations.py
```

## Configuration
- Google Sheets API authentication via `gcloud auth application-default login`
- Credentials stored in `~/.config/gcloud/application_default_credentials.json`
- Environment variables in `.env` (git ignored)
- Form submission URL in `web/index.html`

## Best Practices
✅ DO:
- Use CSS variables for styling consistency
- Keep translations in sync across pages
- Test with Python server (not file:// URLs)
- Comment code sections
- Update requirements.txt when adding dependencies

❌ DON'T:
- Hardcode values (use CSS variables or config)
- Commit credentials or .env files
- Use inline styles (use styles.css)
- Change HTML field IDs without updating JavaScript
- Run Python without activating .venv
