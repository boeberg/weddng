# Wedding RSVP & Location Mapper

A beautiful, maintainable wedding website with:
- 🌍 Multi-language RSVP form
- 🗺️ Interactive accommodation map
- 📱 Mobile-responsive design
- 🎨 Easy customization

## Project Structure

```
weddng/
├── web/                      # Website files
│   ├── index.html           # RSVP form
│   ├── overview.html        # Landing page & language selector
│   ├── thankyou.html        # Confirmation page
│   └── styles.css           # Styling (main customization point)
├── scripts/                  # Python utilities
│   └── load_and_plot_locations.py  # Generate accommodation map
├── data/                     # Generated outputs
│   └── guest_locations_map.html    # Interactive map
├── docs/                     # Documentation
│   ├── SETUP.md             # Setup & deployment guide
│   ├── DESIGN_SYSTEM.md     # Design tokens & system
│   └── CUSTOMIZATION.md     # How to customize
├── .github/
│   └── copilot-instructions.md
├── requirements.txt          # Python dependencies
├── config.yaml              # Configuration
└── README.md                # This file
```

## Quick Start

### 1. Setup Environment

```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Serve Locally

```bash
source .venv/bin/activate
python3 -m http.server 8000
```

Open: `http://localhost:8000/web/overview.html`

> **Note:** localStorage only works with HTTP/HTTPS, not `file://` URLs

### 3. Generate Location Map (Optional)

```bash
source .venv/bin/activate
python scripts/load_and_plot_locations.py
```

Output: `data/guest_locations_map.html`

---

## Documentation

- **[Setup Guide](docs/SETUP.md)** - Installation, configuration, and troubleshooting
- **[Design System](docs/DESIGN_SYSTEM.md)** - Colors, typography, spacing
- **[Customization Guide](docs/CUSTOMIZATION.md)** - How to customize the website

## Customization

For detailed customization instructions, see [docs/CUSTOMIZATION.md](docs/CUSTOMIZATION.md)

### Quick Tips

- **Styling:** Edit `web/styles.css` (CSS variables at the top)
- **Languages:** Add translations in `web/index.html` and `web/overview.html`
- **Form Fields:** Modify form structure in `web/index.html`
- **Design System:** Check [docs/DESIGN_SYSTEM.md](docs/DESIGN_SYSTEM.md)

---

## Features

### RSVP Form (`web/index.html`)

- Multi-language support (English, German)
- Form fields:
  - Guest name (required)
  - Attending status (Yes/No)
  - Plus one name (optional)
  - Number of children (optional)
  - Meal preference (optional)
- Dynamic field visibility
- Submits to Google Forms
- Redirect to thank you page on success

### Location Mapper (`scripts/load_and_plot_locations.py`)

- Loads accommodation data from Google Sheets
- Generates interactive map using folium
- Supports multiple coordinate formats
- Requires Google Sheets API access

### Design

- Mobile-responsive
- Customizable with CSS variables
- Clean, elegant aesthetic
- Accessible HTML structure

---

## Development

### Python Environment

All Python code must run within the `.venv` virtual environment:

```bash
source .venv/bin/activate
python scripts/load_and_plot_locations.py
```

### Adding Dependencies

```bash
source .venv/bin/activate
pip install <package-name>
pip freeze > requirements.txt
```

### Code Quality

- TypeScript with strict mode (for web components, if added)
- ESLint rules enforced (if added)
- Unit tests for all functions (if test framework added)

See [.github/copilot-instructions.md](.github/copilot-instructions.md) for coding standards.

---

## Support

For setup issues, see [docs/SETUP.md](docs/SETUP.md)

For design questions, see [docs/DESIGN_SYSTEM.md](docs/DESIGN_SYSTEM.md)

For customization help, see [docs/CUSTOMIZATION.md](docs/CUSTOMIZATION.md)
