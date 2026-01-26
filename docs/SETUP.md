# Wedding RSVP & Location Mapper - Setup Guide

This document covers all setup and configuration for the project.

## Quick Start

### 1. Install Dependencies

```bash
# Activate virtual environment
source .venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

### 2. Configure Google Cloud Access

The project includes two features that require Google Cloud authentication:
- **RSVP Form**: Submits to Google Forms (no auth needed)
- **Location Mapper**: Loads accommodation data from Google Sheets

#### For Location Mapper Only

```bash
# Authenticate with Google Cloud
gcloud auth application-default login \
  --scopes https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/spreadsheets

# Set quota project
gcloud auth application-default set-quota-project kaffeemoeder
```

**Note:** Google Sheets API must be enabled in the kaffeemoeder GCP project.

### 3. Run the Web Server

```bash
source .venv/bin/activate
python3 -m http.server 8000
```

Then open: `http://localhost:8000/web/overview.html`

### 4. Generate Location Map

```bash
source .venv/bin/activate
python scripts/load_and_plot_locations.py
```

Output: `data/guest_locations_map.html`

---

## Project Structure

```
weddng/
├── web/                          # Website files
│   ├── index.html               # RSVP form
│   ├── overview.html            # Landing page
│   ├── thankyou.html            # Confirmation
│   └── styles.css               # Styling
├── scripts/                      # Python scripts
│   └── load_and_plot_locations.py
├── data/                         # Generated files & outputs
│   └── guest_locations_map.html
├── docs/                         # Documentation
│   ├── SETUP.md                 # This file
│   ├── DESIGN_SYSTEM.md
│   └── CUSTOMIZATION.md
├── .venv/                        # Python virtual environment
├── .github/                      # GitHub configuration
│   └── copilot-instructions.md
├── requirements.txt              # Python dependencies
├── .env                         # Local configuration (git ignored)
└── README.md                     # Project overview
```

---

## Google Cloud Setup Details

### Prerequisites

- Google Cloud project: `kaffeemoeder`
- gcloud CLI installed
- Authenticated user account

### Enable Google Sheets API

1. Go to: https://console.cloud.google.com/
2. Select project: **kaffeemoeder**
3. Navigate to: **APIs & Services** → **Library**
4. Search for: **Google Sheets API**
5. Click **Enable**

### Application Default Credentials

Credentials are stored at: `~/.config/gcloud/application_default_credentials.json`

A backup is also kept in `.env` (for reference only).

### Using Service Account (Alternative)

For automated scripts, you can use a service account instead:

1. Create a service account in GCP console
2. Download JSON key
3. Save as: `./.service-account-key.json`
4. Add to `.gitignore` (never commit!)
5. Update `.env`:
   ```
   GOOGLE_CREDENTIALS_PATH=./.service-account-key.json
   ```

---

## Environment Variables

Create a `.env` file in the project root (copy from `.env.example`):

```env
# Google Sheets Authentication
# (Usually managed by gcloud auth, this is optional)
# GOOGLE_CREDENTIALS_PATH=./google-credentials.json
```

**Important:** Add `.env` to `.gitignore` to prevent credential leaks.

---

## Troubleshooting

### Location Mapper Fails to Load Sheet

**Error:** `Google Sheets API has not been used in project`

**Solution:**
1. Verify Google Sheets API is enabled in kaffeemoeder project
2. Wait 1-2 minutes for the change to propagate
3. Refresh credentials:
   ```bash
   gcloud auth application-default login \
     --scopes https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/spreadsheets
   ```

### RSVP Form Won't Submit

1. Ensure Google Form is accessible
2. Verify form submission URL is correct in `web/index.html`
3. Check browser console (F12) for JavaScript errors

### Port 8000 Already in Use

```bash
# Use different port
python3 -m http.server 8001
```

Then open: `http://localhost:8001/web/overview.html`

---

## Python Development

### Activate Virtual Environment

```bash
source .venv/bin/activate
```

### Add New Dependencies

```bash
pip install <package-name>
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add <package-name> dependency"
```

### Run Scripts

All Python scripts must be run from within the virtual environment:

```bash
source .venv/bin/activate
python scripts/load_and_plot_locations.py
```

---

## Next Steps

- See [CUSTOMIZATION.md](CUSTOMIZATION.md) for design changes
- See [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md) for design documentation
- See [../README.md](../README.md) for project overview
