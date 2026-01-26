# 🎨 Visual Design System

This file documents the current design so future developers can maintain consistency.

## 🎯 Design Philosophy

- **Clean & Minimal** - Focus on the couple and RSVP
- **Elegant** - Warm, inviting colors for a wedding
- **Accessible** - Easy to read, high contrast
- **Mobile-Friendly** - Works on all devices

---

## 🎨 Color Palette

All colors can be customized in `styles.css`:

```css
:root {
  --color-primary: #b89b5e;          /* Warm gold - accent color */
  --color-text: #1f1f1f;             /* Dark text - excellent readability */
  --color-text-light: #777;          /* Light gray - secondary text */
  --color-background: #faf9f6;       /* Off-white - clean background */
}
```

### Color Usage

| Color | Used For | Change If |
|-------|----------|-----------|
| `#b89b5e` (Gold) | Buttons, accents, card shadow | Want different theme color |
| `#1f1f1f` (Dark) | Main text, primary button | Want lighter/darker text |
| `#777` (Gray) | Labels, secondary text | Want different secondary color |
| `#faf9f6` (Off-white) | Background, inputs | Want lighter/darker background |

### Color Combinations

- **Gold + White**: High contrast, elegant
- **Dark + Off-white**: Professional, easy to read
- **Gold accent on white**: Modern and clean

---

## 🔤 Typography

```css
--font-primary: "Roboto", sans-serif;  /* Clean, modern sans-serif */

--font-size-h1: 36px;       /* Large titles */
--font-size-base: 14px;     /* Body text */

--font-weight-normal: 400;   /* Regular text */
--font-weight-medium: 500;   /* Slightly bolder (labels) */
--font-weight-bold: 600;     /* Headers, active states */
```

### Typography Hierarchy

1. **H1 (36px, bold)** - "Babette & Felix"
2. **P.subtitle (14px, uppercase)** - "We would love to celebrate..."
3. **Label (14px, medium)** - "Guest Name", "Will you attend?"
4. **Input (14px)** - Form fields and options
5. **Button (15px, medium)** - "Send RSVP", "RSVP"

---

## 📐 Spacing System

A consistent spacing scale makes the design cohesive:

```css
--spacing-small: 6px;         /* Small gaps */
--spacing-medium: 12px;       /* Medium spacing */
--spacing-large: 20px;        /* Large spacing */
--spacing-xl: 32px;           /* Extra large (form fields) */
--spacing-2xl: 48px;          /* Padding inside container */
```

### Spacing Usage

- **6px**: Padding inside small elements
- **12px**: Gap between form fields
- **20px**: Margin below language buttons
- **32px**: Space above submit button
- **48px**: Padding inside main container

---

## 🔘 Button Styles

### Primary Button (CTA)
```css
.btn-primary {
  background: #1f1f1f;       /* Dark background */
  color: #faf9f6;            /* Light text */
  padding: 14px;
  border-radius: 10px;
}

.btn-primary:hover {
  background: #000;          /* Even darker on hover */
}
```

**Used for**: "Send RSVP", "RSVP"
**Purpose**: Draw attention to main action

### Secondary Button
```css
.btn-secondary {
  background: transparent;
  border: 2px solid #b89b5e; /* Gold border */
  color: #b89b5e;            /* Gold text */
}

.btn-secondary:hover {
  background: rgba(246, 230, 166, 0.3); /* Subtle gold bg */
}
```

**Used for**: "Practical Information"
**Purpose**: Offer alternatives without overwhelming

---

## 📱 Layout & Spacing

### Container
- **Max width**: 520px (fits on all screens)
- **Padding**: 48px 36px (breathing room on sides)
- **Margin**: 80px auto (centered with top space)
- **Border radius**: 6px (subtle rounded corners)
- **Shadow**: `0 18px 40px rgba(0, 0, 0, 0.12)` (depth)

### Card Gradient Background
```css
background: linear-gradient(
  135deg,
  rgba(246, 230, 166, 0.95),  /* Light gold (top-left) */
  rgba(226, 180, 44, 0.95)    /* Darker gold (bottom-right) */
);
```

Creates a warm, inviting feeling.

---

## 🌍 Responsive Design

### Desktop (> 768px)
- Full 520px container width
- Plenty of padding
- Large font sizes

### Tablet (481px - 768px)
```css
--container-padding: 32px 24px;  /* Reduced padding */
--font-size-h1: 28px;            /* Slightly smaller */
```

### Mobile (< 480px)
```css
--container-padding: 24px 16px;  /* Minimal padding */
--font-size-h1: 24px;            /* Smaller to fit */
```

---

## 🎯 Visual Hierarchy

```
Large, Bold (H1)
"Babette & Felix"

Small, Uppercase
"We would love to celebrate with you"

Language Buttons
EN | DE | DK

Form Labels
Guest Name

Input Fields
[____________________]

Buttons
[    Send RSVP    ]
```

---

## 🎨 Design Tokens Reference

Copy these if you're adding components:

```css
/* Buttons */
padding: 14px;
border-radius: 10px;
font-size: 15px;
font-weight: 500;

/* Form Inputs */
padding: 12px;
border-radius: 8px;
border: 1px solid #ddd;
font-size: 14px;

/* Labels */
margin-top: 22px;
margin-bottom: 6px;
font-size: 14px;
font-weight: 500;

/* Transitions */
transition: 0.3s ease;
```

---

## 🌟 Special Effects

### Card Shadow (Depth)
```css
box-shadow: 0 18px 40px rgba(0, 0, 0, 0.12);
```
Creates subtle depth without looking harsh.

### Focus States
```css
input:focus {
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba(184, 155, 94, 0.1);
}
```
Golden glow indicates interactive elements.

### Hover Effects
```css
transition: background-color var(--transition), 
            transform var(--transition);

button:active {
  transform: translateY(1px);  /* Subtle press effect */
}
```

---

## 📋 Accessibility Features

- **High contrast text**: #1f1f1f on #faf9f6 (WCAG AAA)
- **Large tap targets**: Buttons 44px+ tall (mobile-friendly)
- **Clear labels**: All inputs have associated labels
- **Readable fonts**: Roboto 14px+ is easy to read
- **Focus indicators**: Visible when tabbing through form

---

## 🎭 Dark Mode Consideration

If you want to add dark mode, adjust these colors:

```css
/* Light mode (current) */
--color-text: #1f1f1f;
--color-background: #faf9f6;

/* Dark mode */
--color-text: #f5f5f5;
--color-background: #1a1a1a;
--color-card-bg: linear-gradient(135deg, #2a2a2a, #1a1a1a);
```

---

## 🚀 Adding New Visual Components

When adding new elements, follow these principles:

1. **Use existing colors** - Don't introduce new colors
2. **Maintain spacing** - Use the spacing scale
3. **Follow typography** - Use font sizes from the scale
4. **Add transitions** - Use `--transition: 0.3s ease`
5. **Test contrast** - Ensure readable text
6. **Keep it minimal** - Stay true to the clean aesthetic

---

## 📸 Visual Checklist

- [ ] Colors match the palette
- [ ] Text is readable (good contrast)
- [ ] Spacing is consistent
- [ ] Buttons look clickable
- [ ] Mobile version looks good
- [ ] No harsh shadows or effects
- [ ] Typography is clear and organized
- [ ] Focus states are visible
- [ ] Hover effects are subtle

---

**This design system ensures consistency and makes future changes easier!** ✨
