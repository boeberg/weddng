# 📖 Documentation Index

Welcome! This is your guide to the wedding RSVP website codebase.

## 🚀 Quick Start

**Want to make a change?** Pick your task:

### "I want to change colors"
→ Read: **CUSTOMIZATION_GUIDE.md** (Colors section)
→ Edit: `styles.css` (`:root` section)

### "I want to change fonts or layout"
→ Read: **CUSTOMIZATION_GUIDE.md**
→ Edit: `styles.css`

### "I want to add images or change text"
→ Read: **CUSTOMIZATION_GUIDE.md** (Change Text, Add Images)
→ Edit: `index.html`, `overview.html`, or `thankyou.html`

### "I want to add a new language"
→ Read: **README.md** (How to Customize section)
→ Edit: `index.html`, `overview.html`

### "I'm making a big change and want to be careful"
→ Read: **DEVELOPER_CHECKLIST.md**
→ Follow the checklist step by step

### "I'm new and want to understand everything"
→ Read: **README.md**
→ Then read: **CUSTOMIZATION_GUIDE.md**

### "I want to understand what was improved"
→ Read: **REFACTORING_SUMMARY.md**

---

## 📁 File Guide

### Core Files (What the User Sees)

| File | Purpose | Edit When |
|------|---------|-----------|
| `index.html` | RSVP form page | Adding/changing form fields or translations |
| `overview.html` | Landing & language selection | Changing main text or adding languages |
| `thankyou.html` | Confirmation page | Changing thank you message |
| `styles.css` | All styling | Changing colors, fonts, spacing, layout |

### Documentation (What YOU Read)

| File | Purpose | Read When |
|------|---------|-----------|
| `README.md` | Complete developer guide | You need detailed explanations |
| `CUSTOMIZATION_GUIDE.md` | Quick reference | You want fast answers |
| `DEVELOPER_CHECKLIST.md` | QA & testing guide | Making changes, before deployment |
| `REFACTORING_SUMMARY.md` | What was improved | Understanding the codebase improvements |

### Configuration

| File | Purpose |
|------|---------|
| `config.yaml` | Site configuration |
| `.git/` | Version control |

---

## 🎯 Common Tasks

### Change the header color
1. Open `styles.css`
2. Find `:root { --color-primary: ...`
3. Change `#b89b5e` to your color
4. Save and refresh browser

### Add a wedding hashtag to the form
1. Open `index.html`
2. Find the `<form id="rsvp-form">` section
3. Add new input field:
```html
<label for="hashtag">Hashtag (optional)</label>
<input id="hashtag" name="entry.XXXXX" type="text" />
```
4. Get the field ID from Google Forms (replace XXXXX)

### Change "Please choose..." text
1. Open `index.html`
2. Find `const translations = {`
3. Edit `select: "Please choose..."` in each language

### Add a header image
1. Open `overview.html`
2. Add before the `<h1>`:
```html
<img src="your-photo.jpg" alt="Couple" style="max-width: 100%; border-radius: 10px; margin-bottom: 20px;">
```

### Make text bigger
1. Open `styles.css`
2. Find `:root {`
3. Change `--font-size-h1: 36px;` to a bigger number

---

## 📚 How to Read the Code

### HTML Files
```html
<!-- Comments like this explain what follows -->
<div class="container">
  <!-- Each section is clearly labeled -->
  <!-- Look for HTML comments as your guide -->
</div>
```

### JavaScript
```javascript
/**
 * Comments like this explain the function
 * They tell you what it does and why
 */
function applyLanguage(lang) {
  // Individual lines have comments too
}
```

### CSS
```css
:root {
  /* CSS Variables at the top = easy customization */
  --color-primary: #b89b5e;
}

/* Clear class names show what they do */
.container { /* Main card */ }
.btn-primary { /* Main button */ }
```

---

## ⚡ Most Important Tips

1. **Always edit `styles.css` for styling changes** (not HTML `<style>` tags)
2. **Test after each change** (`python3 -m http.server 8000`)
3. **Make one change at a time** (easier to debug)
4. **Check the comments in the code** (they explain things!)
5. **Use localhost** (localStorage doesn't work with `file://` URLs)

---

## 🧪 Testing Checklist

After making changes:

- [ ] Open `http://localhost:8000/overview.html`
- [ ] Click through all pages
- [ ] Test language switcher
- [ ] Fill out form and submit
- [ ] Check browser console for errors (F12)
- [ ] Test on mobile (DevTools responsive mode)

---

## 🤔 Stuck?

1. **Check the code comments first** - They often explain things
2. **Read CUSTOMIZATION_GUIDE.md** - Covers 90% of common needs
3. **Search the code** - Use Ctrl+F to find what you're looking for
4. **Check browser console** - Press F12, go to Console tab
5. **Read README.md** - More detailed explanations

---

## 🎓 Learning Path for New Developers

**Day 1:**
- [ ] Read this file (you're here!)
- [ ] Skim `CUSTOMIZATION_GUIDE.md`
- [ ] Look at `styles.css` (just the `:root` section)

**Day 2:**
- [ ] Read `README.md`
- [ ] Make a small styling change (color or font)
- [ ] Test and verify it works

**Day 3:**
- [ ] Change some text content in the HTML
- [ ] Add a new language to the translations
- [ ] Review `DEVELOPER_CHECKLIST.md`

**Day 4+:**
- [ ] Make bigger changes with confidence!
- [ ] Use the checklist for quality assurance

---

## 📞 Quick Reference

### File Locations
- **Styling**: `styles.css`
- **Language 1**: `index.html` (translations object)
- **Language 2**: `overview.html` (translations object)
- **Form**: `index.html` (form section)
- **Landing**: `overview.html`

### Key Sections in Code

**In index.html:**
- Lines ~1-20: Head and CSS links
- Lines ~220-250: HTML form
- Lines ~285+: Translation and form logic

**In overview.html:**
- Lines ~1-20: Head and CSS links
- Lines ~40-60: Header and language buttons
- Lines ~70+: Translation and language logic

**In styles.css:**
- Lines ~1-30: CSS variables (customize here!)
- Lines ~40-100: Global styles
- Lines ~100-200: Component styles
- Lines ~200+: Responsive design

---

## 🎉 You're Ready!

Now you have everything you need to:
- ✅ Understand the codebase
- ✅ Make changes confidently
- ✅ Test properly
- ✅ Help the next developer

**Start with CUSTOMIZATION_GUIDE.md for your first change!**

---

**Happy coding! 💍**
