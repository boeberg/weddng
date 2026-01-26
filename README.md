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

Everything is designed to be easy to customize. Here are the main customization points:

### 1️⃣ Change Colors & Styling

**File:** `web/styles.css` (top section - CSS variables)

```css
:root {
  /* Colors - change these! */
  --color-primary: #b89b5e;              /* Main accent (gold) */
  --color-text: #1f1f1f;                 /* Text color (dark) */
  --color-background: #faf9f6;           /* Background (cream) */
  
  /* Fonts */
  --font-primary: "Roboto", sans-serif;
  
  /* Spacing */
  --spacing-small: 6px;
  --spacing-medium: 12px;
  --spacing-large: 20px;
}
```

Just change the CSS variables and the entire website updates! 🎨

### 2️⃣ Edit Website Content

**Files to edit:**
- `web/overview.html` - Landing page, language buttons
- `web/index.html` - RSVP form
- `web/info.html` - Practical information (Accommodations, Dress Code, Getting There, Gifts)
- `web/thankyou.html` - Thank you message

All page content is in simple HTML. Easy to find and update!

**Example:** To change the title, find and edit:
```html
<h1>Babette & Felix</h1>  <!-- Change to your names -->
```

### 3️⃣ Add Multiple Languages

**Files:** `web/overview.html`, `web/index.html`, `web/info.html`

Find the `translations` object and add your language:

```javascript
const translations = {
  en: { /* English translations */ },
  de: { /* German translations */ },
  fr: {  // NEW LANGUAGE
    title: "Babette & Felix",
    subtitle: "Nous sommes...",
    // ... add all translation keys
  }
};
```

Then add the language button on overview.html:
```html
<button onclick="setLanguage('fr')" data-lang="fr">FR</button>
```

### 4️⃣ Customize RSVP Form

**File:** `web/index.html`

Change form fields by editing the HTML:

```html
<label for="guestName">Guest Name</label>
<input id="guestName" name="entry.108083471" type="text" required />

<!-- Add/remove fields as needed -->
```

To change where the form submits, update:
```html
<form id="rsvpForm" action="https://docs.google.com/forms/d/YOUR_FORM_ID/formResponse" method="POST">
```

### 5️⃣ Customize Information Pages

**File:** `web/info.html`

Each section (Accommodations, Dress Code, Getting There, Gifts) has an ID you can edit:

```html
<h2 id="accommodations-title">Accommodations</h2>
<p id="accommodations-text">
  We've collected nearby accommodations...
</p>
```

Then update the translations object at the bottom with your custom text.

### 6️⃣ Update Accommodation Map

**File:** `scripts/load_and_plot_locations.py`

The script loads accommodations from a Google Sheet and creates an interactive map:

```bash
source .venv/bin/activate
python scripts/load_and_plot_locations.py
```

The map automatically:
- ✅ Marks "Alte Schule" in **red** (your venue)
- ✅ Marks "Sportplatz" in **green**
- ✅ Marks other locations in **blue**
- ✅ Shows distance to your venue when you hover
- ✅ Shows website links for each accommodation

**To use it:** Share your Google Sheet with `kaffeemoeder` project credentials.

### 7️⃣ Test Locally

```bash
cd /Users/felixschilling/Documents/weddng/web
python3 -m http.server 8000
```

Then visit:
- `http://localhost:8000/overview.html` - Landing page
- `http://localhost:8000/index.html` - RSVP form
- `http://localhost:8000/info.html` - Practical information
- `http://localhost:8000/thankyou.html` - Thank you page

### 📋 Customization Checklist

- [ ] Change `--color-primary` in `web/styles.css` to your color
- [ ] Edit titles and names (find "Babette & Felix" in HTML files)
- [ ] Update RSVP form fields in `web/index.html`
- [ ] Customize content in `web/info.html`
- [ ] Add/update languages in translation objects
- [ ] Update Google Forms submission URL in `web/index.html`
- [ ] Run location mapper: `python scripts/load_and_plot_locations.py`
- [ ] Test locally and review all pages

For more detailed guidance, see [docs/CUSTOMIZATION.md](docs/CUSTOMIZATION.md)

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
