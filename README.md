# Wedding RSVP Website - Developer Guide

## Overview

This is a simple, maintainable wedding RSVP website with multi-language support. The design is clean and easy to customize for less experienced developers.

## File Structure

```
weddng/
├── styles.css          # Shared CSS (EDIT THIS to change styling)
├── index.html          # RSVP form page
├── overview.html       # Landing/language selection page
├── thankyou.html       # Thank you/confirmation page
├── config.yaml         # Configuration file
└── README.md           # This file
```

## Quick Start

### Serving Locally

```bash
cd /Users/babettesophiabresser/Develop/weddng
python3 -m http.server 8000
```

Then open `http://localhost:8000/overview.html` in your browser.

> **Important**: localStorage only works with HTTP/HTTPS, not `file://` URLs

---

## How to Customize

### 1. Change Colors & Styling

**Edit `styles.css`** - All design customization happens here!

At the top of the file, you'll find CSS variables that control the entire look:

```css
:root {
  /* Colors */
  --color-primary: #b89b5e;              /* Main accent color */
  --color-text: #1f1f1f;                 /* Text color */
  --color-background: #faf9f6;           /* Background color */
  --color-card-bg: linear-gradient(...); /* Card background */
  
  /* Fonts */
  --font-primary: "Roboto", sans-serif;  /* Main font */
  
  /* Spacing */
  --spacing-small: 6px;
  --spacing-medium: 12px;
  --spacing-large: 20px;
  
  /* Layout */
  --container-max-width: 520px;
  --container-padding: 48px 36px;
}
```

Simply change these values to update the entire site's appearance!

### 2. Add or Change Fonts

Edit the `<link>` tag in the HTML files or in `styles.css`:

```html
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=YOUR-FONT:wght@300;400;700&display=swap" rel="stylesheet">
```

Then update the `--font-primary` variable in `styles.css`.

### 3. Add Images

Add image references to `styles.css`:

```css
.container {
  background-image: url('path/to/your/image.jpg');
  background-size: cover;
  background-position: center;
}
```

Or in HTML:

```html
<img src="your-image.jpg" alt="Description" style="max-width: 100%; margin-bottom: 20px;">
```

### 4. Add a New Language

1. **Edit `index.html`** - Add translations to the `translations` object:

```javascript
const translations = {
  en: { /* ... */ },
  de: { /* ... */ },
  fr: {  // NEW
    guestName: "Nom du convi",
    attending: "Allez-vous assister?",
    // ... add all keys
  }
};
```

2. **Edit `overview.html`** - Add translations:

```javascript
const translations = {
  en: { /* ... */ },
  de: { /* ... */ },
  fr: {  // NEW
    subtitle: "Nous serions heureux...",
    rsvp: "RSVP",
    info: "Informations pratiques",
  }
};
```

3. **Edit `thankyou.html`** - If using it, add translations.

4. **Update language buttons** in HTML if needed.

---

## Page Structure

### overview.html (Landing Page)

- Title and subtitle
- **Language switch buttons** (user selects language here)
- Navigation buttons (RSVP, Practical Info)

### index.html (RSVP Form)

- Form fields:
  - Guest name (required)
  - Attending status (Yes/No)
  - Plus One name (optional)
  - Number of children (optional)
  - Meal preference (optional)
- Shows/hides fields based on user responses
- Submits to Google Forms
- Redirects to thankyou.html on success

### thankyou.html (Confirmation Page)

- Simple thank you message
- Back button to form

---

## How Translations Work

1. User selects a language in **overview.html**
2. Selection is stored in browser's `localStorage`
3. User clicks "RSVP" link to **index.html**
4. index.html reads the saved language from localStorage
5. Form displays in the selected language

The language choice persists across browser sessions!

---

## Form Submission

The form submits to Google Forms. To change the submission URL:

1. Create a new Google Form
2. Copy the form submission URL
3. In `index.html`, find this line:

```html
<form id="rsvpForm" action="https://docs.google.com/forms/d/..." method="POST">
```

Replace the `action` URL with your new Google Forms URL.

---

## CSS Classes Reference

```css
.container         /* Main card container */
.language-switch   /* Language button group */
.btn              /* Base button style */
.btn-primary      /* Call-to-action button */
.btn-secondary    /* Secondary button */
.subtitle         /* Subtitle text */
.hidden           /* Hide element */
.text-center      /* Center text */
.text-muted       /* Light gray text */
```

---

## Code Organization

### index.html Structure

- **Meta tags & font imports** (head)
- **Shared CSS link** (head)
- **Inline styles** (optional overrides)
- **HTML form** (body)
- **Translation script** (bottom)
- **Form logic script** (bottom)

### Script Sections

1. **TRANSLATIONS & LOCALIZATION** - Language strings
2. **FORM LOGIC** - Toggle fields, handle submission

Each section has detailed comments explaining the code.

---

## Tips for Less Experienced Developers

### ✅ DO:
- Edit `styles.css` for styling changes
- Add comments when making changes
- Test locally with Python server
- Keep translations in sync across pages
- Use browser console to debug (F12)

### ❌ DON'T:
- Don't edit styles inside HTML `<style>` tags (use styles.css instead)
- Don't change field IDs or form field names without updating translations
- Don't test with `file://` URLs (use Python server instead)

### Debugging

Open browser Developer Tools (F12) and check:

- **Console tab** - JavaScript errors
- **Network tab** - Form submission status
- **Application tab** - localStorage values

---

## Responsive Design

The site is mobile-friendly. Breakpoints are in `styles.css`:

```css
@media (max-width: 768px) {
  /* Tablet styles */
}

@media (max-width: 480px) {
  /* Mobile styles */
}
```

---

## Future Enhancements

Ideas for expansion:

- Add a gallery/photos page
- Add wedding details/timeline page
- Send confirmation emails
- Admin dashboard to view responses
- Add guest filtering/seating arrangements
- Add dietary restrictions field
- Add RSVP deadline countdown

---

## Support

For questions, refer to:

1. **Code comments** - Every section has detailed comments
2. **Browser console** - Check for JavaScript errors
3. **HTML structure** - Semantic, self-documenting tags
4. **CSS variables** - All customizable at the top of styles.css

---

**Happy coding! 💍**
