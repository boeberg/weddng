# Quick Customization Guide

**Made for developers who want to change things fast without reading documentation.**

## Change Colors (Most Common)

Open `styles.css` and edit the `:root` section at the top:

```css
:root {
  --color-primary: #b89b5e;        /* Gold - change this */
  --color-text: #1f1f1f;           /* Dark text */
  --color-background: #faf9f6;     /* Light background */
}
```

**That's it!** The entire site updates.

---

## Change Font

In `styles.css`:

```css
:root {
  --font-primary: "Roboto", sans-serif;  /* Change to "Arial", "Georgia", etc */
}
```

Or add a Google Font:

```html
<!-- In the <head> of index.html and overview.html -->
<link href="https://fonts.googleapis.com/css2?family=FONT-NAME:wght@400;700&display=swap" rel="stylesheet">
```

---

## Change Text

- **"We would love to celebrate with you"** → Edit in `index.html` line ~227
- **"We're so happy to celebrate..."** → Edit in `overview.html` line ~46
- **"Thank you! 💕"** → Edit in `index.html` translations object
- **Button text** → Edit in translations objects

---

## Add a Logo/Image

In `index.html` or `overview.html`, add before the `<h1>`:

```html
<img src="your-logo.png" alt="Logo" style="max-width: 150px; margin-bottom: 20px;">
```

---

## Change Button Style

In `styles.css`, find `.btn-primary`:

```css
.btn-primary {
  background-color: var(--color-text);
  color: var(--color-background);
}

.btn-primary:hover {
  background-color: #000;  /* Change hover color here */
}
```

---

## Add More Form Fields

1. Add to HTML form in `index.html`:
```html
<label for="allergies">Dietary Restrictions</label>
<input id="allergies" name="entry.XXXXX" type="text">
```

2. Add to translations (if needs translation):
```javascript
const translations = {
  en: { allergies: "Dietary Restrictions", ... },
  de: { allergies: "Diätetische Einschränkungen", ... }
};
```

3. Add to `applyLanguage()` function:
```javascript
const allergiesLabel = document.querySelector('label[for="allergies"]');
if (allergiesLabel) allergiesLabel.textContent = t.allergies;
```

---

## Change Spacing/Padding

In `styles.css`:

```css
:root {
  --spacing-large: 20px;      /* Change these values */
  --container-padding: 48px 36px;  /* Top/bottom Left/right */
}
```

---

## Make Text Bigger

In `styles.css`:

```css
:root {
  --font-size-h1: 48px;  /* Was 36px, now 48px */
  --font-size-base: 16px; /* Was 14px, now 16px */
}
```

---

## Add a Favicon

In `<head>` of index.html, overview.html, thankyou.html:

```html
<link rel="icon" href="favicon.ico">
```

---

## Hide Language Switch

In `overview.html`, add to `<style>`:

```css
.language-switch {
  display: none;
}
```

---

## Change Thank You Page

Edit `thankyou.html` - simple HTML, no JavaScript complications.

---

## Test Your Changes

```bash
python3 -m http.server 8000
```

Then visit: `http://localhost:8000/overview.html`

**Remember**: Use HTTP server, not `file://` URLs!

---

## Most Important Files

1. **styles.css** - ALL visual styling
2. **index.html** - RSVP form (and translations)
3. **overview.html** - Landing page (and language switcher)
4. **thankyou.html** - Thank you page

---

## Need Help?

- Check the comment above each code section
- Browser F12 → Console tab shows errors
- Search for your text in the files to find where to change it
- Read `README.md` for detailed info

---

**Tip: Make ONE small change, test it, then make the next one!** ✅
