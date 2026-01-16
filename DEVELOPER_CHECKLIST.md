# Developer Modification Checklist

Use this checklist whenever you make changes to the wedding site.

## Before You Start

- [ ] Read the relevant code section's comments
- [ ] Make one change at a time
- [ ] Test after each change

## Making Style Changes

- [ ] Edit `styles.css` (NOT inline `<style>` tags)
- [ ] Use CSS variables at top of `styles.css` when possible
- [ ] Test on mobile (resize browser or use mobile simulator)
- [ ] Check all three pages (overview, index, thankyou)

## Adding/Changing Text

- [ ] Update HTML content
- [ ] If text appears in multiple languages, update translations in `translations` object
- [ ] Update all related pages (check which pages have that text)
- [ ] Test the language switcher (overview page)

## Modifying Form Fields

- [ ] Add/edit HTML in the form
- [ ] Add `id` and `name` attributes
- [ ] If adding translations, update `applyLanguage()` function
- [ ] Update all language translations if user-facing
- [ ] Don't change `name="entry.XXXXX"` (Google Forms field IDs)

## Adding a New Language

- [ ] Add language object to `translations` in index.html
- [ ] Add language object to `translations` in overview.html
- [ ] Add language button in overview.html if needed
- [ ] Update language detection code in init functions
- [ ] Test all pages in the new language

## Making Layout Changes

- [ ] Update `styles.css` container/layout properties
- [ ] Check responsive breakpoints (mobile/tablet)
- [ ] Update spacing if needed (`--spacing-*` variables)
- [ ] Verify all pages look correct

## Changing Colors

- [ ] Update relevant variables in `styles.css` `:root`
- [ ] Test contrast (text should be readable)
- [ ] Check on dark and light backgrounds
- [ ] Verify links and buttons are visible

## Testing Checklist

After making changes:

- [ ] Run local server (`python3 -m http.server 8000`)
- [ ] Test on `http://localhost:8000/overview.html`
- [ ] Click through all pages (overview → RSVP → thank you)
- [ ] Test language switcher
- [ ] Test form functionality
- [ ] Check browser console for errors (F12)
- [ ] Test on mobile (DevTools responsive mode)
- [ ] Verify localStorage persists language choice

## Code Quality

- [ ] Code is readable and understandable
- [ ] Complex sections have comments
- [ ] No console errors or warnings
- [ ] Consistent formatting with existing code

## Performance

- [ ] Page loads quickly (< 2 seconds)
- [ ] Images are optimized (< 1MB each)
- [ ] No console warnings about performance

## Accessibility

- [ ] Form labels are associated with inputs (`for` attribute)
- [ ] Buttons have clear labels
- [ ] Color alone doesn't convey information
- [ ] Mobile-friendly and touch-friendly

## Before Deployment

- [ ] Test all features one final time
- [ ] Check all pages load correctly
- [ ] Verify form submission works
- [ ] Test on different browsers
- [ ] Create backup of working version
- [ ] Update `README.md` if you made significant changes

## Rollback Plan

If something breaks:

1. Open `index.html`, `overview.html`, or `styles.css`
2. Undo your recent changes
3. Test again
4. If still broken, check browser console for errors
5. Refer to `README.md` for proper structure

## File Edit Summary

Copy this after making changes (for documentation):

```
Files modified:
- [x] styles.css (lines X-Y: description)
- [x] index.html (lines X-Y: description)
- [x] overview.html (lines X-Y: description)

Changes made:
- Description of change 1
- Description of change 2

Testing completed:
- [x] Overview page
- [x] RSVP form
- [x] Thank you page
- [x] Language switcher
- [x] Mobile responsiveness
- [x] Form submission
```

---

**Remember: Test early, test often! 🧪**
