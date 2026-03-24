# Design System Document: Institutional Virtual Yearbook

## 1. Overview & Creative North Star: "The Ethereal Archive"

This design system moves beyond the traditional, rigid institutional aesthetic to create **"The Ethereal Archive."** The goal is to transform data and historical records into a living, breathing digital experience. We are not building a static document; we are building a sophisticated, translucent ecosystem.

The "North Star" of this system is **Luminous Depth**. By utilizing glassmorphism, intentional asymmetry, and a refusal of hard structural lines, we create an environment that feels both authoritative (Institutional) and cutting-edge (Tech-forward). We break the "template" look by overlapping glass layers, using extreme typographic contrast, and letting background gradients bleed through UI elements to create a sense of cohesion and "soul."

---

### 2. Colors: Tonal Depth & Luminous Accents

Our palette is rooted in the heritage of `primary` (#00396b) and `secondary` (#bc0004), but it is executed through a lens of transparency and light.

*   **The "No-Line" Rule:** Under no circumstances should 1px solid borders be used for sectioning. Boundaries are defined by color shifts. For example, a `surface-container-low` (#eff4ff) section sits directly against a `background` (#f8f9ff) to create a soft, sophisticated transition.
*   **The "Glass & Gradient" Rule:** Primary CTAs and Hero sections should utilize a linear gradient from `primary` (#00396b) to `primary_container` (#005092) at a 135° angle. This adds a "weighted" professional polish that flat color lacks.
*   **Surface Hierarchy:**
    *   **Lowest Layer:** `surface` (#f8f9ff) - The base canvas.
    *   **Mid Layer:** `surface_container` (#e5eeff) - Grouping related content blocks.
    *   **Floating Layer:** Glassmorphic containers using `surface_container_lowest` (#ffffff) at **70% opacity** with a `backdrop-blur` of 12px-20px.

---

### 3. Typography: The Editorial Scale

We pair the geometric authority of **Manrope** for display with the high-utility legibility of **Inter**.

*   **Display & Headlines (Manrope):** These are our "anchors." Use `display-lg` (3.5rem) with tight letter-spacing (-0.02em) for hero titles. This creates a high-end editorial feel that demands attention.
*   **Titles & Body (Inter):** `title-lg` (1.375rem) serves as the bridge between narrative and data. `body-md` (0.875rem) is our workhorse, ensuring high density of information remains readable.
*   **The Hierarchy Intent:** Massive display type represents the "Institutional Weight," while clean, smaller body text represents "Modern Precision."

---

### 4. Elevation & Depth: Tonal Layering

Traditional shadows and borders are replaced by **Ambient Layering**.

*   **The Layering Principle:** To lift a card, do not reach for a shadow first. Place a `surface_container_lowest` (#ffffff) card on a `surface_container_high` (#dce9ff) background. The delta in lightness creates the "lift."
*   **Ambient Shadows:** For floating elements like modals or dropdowns, use an ultra-diffused shadow: `box-shadow: 0 20px 40px rgba(11, 28, 48, 0.06);`. Note the color: we use a tinted version of `on_surface` (#0b1c30) rather than pure black.
*   **The "Ghost Border" Fallback:** If a container requires a border for accessibility, use `outline_variant` (#c2c6d2) at **15% opacity**. It should be felt, not seen.
*   **Glassmorphism Specifics:** Apply a 1px inner stroke using `on_surface_variant` (#424750) at **10% opacity** to the top and left edges of glass cards to simulate a light-catching "beveled" edge.

---

### 5. Components

#### Buttons
*   **Primary:** Gradient fill (`primary` to `primary_container`), `rounded-md` (0.75rem). No shadow.
*   **Secondary (Glass):** `surface_container_lowest` at 20% opacity, `backdrop-blur: 8px`, with a `Ghost Border`.
*   **Tertiary:** Text only using `primary` (#00396b), bold weight, with a `2px` underline that only appears on hover.

#### Glassmorphic Cards (The Signature Element)
*   **Styling:** `background: rgba(255, 255, 255, 0.7)`, `backdrop-filter: blur(16px)`, `border-radius: xl` (1.5rem).
*   **Usage:** Use these for data visualization placeholders and "Yearbook" profile snapshots.
*   **Spacing:** Use `spacing-6` (1.5rem) for internal padding to ensure content "breathes" within the glass.

#### Inputs & Fields
*   **Style:** `surface_container_lowest` fill. On focus, transition the "Ghost Border" to 50% opacity of the `primary` color.
*   **Error State:** Use `error` (#ba1a1a) for the label text and a soft `error_container` (#ffdad6) for the input background.

#### Data Visualization (Placeholders)
*   Instead of standard bar charts, use rounded-pill shapes (`rounded-full`) and subtle gradients from `tertiary` (#003d4e) to `tertiary_fixed_dim` (#59d5fe) to maintain the tech-forward, "liquid" feel.

---

### 6. Do’s and Don'ts

#### Do:
*   **Do** overlap elements. Let a glass card partially sit over a section transition to create depth.
*   **Do** use `monospace` (15% weight) for metadata, such as dates, figure numbers, or "SCIA-2024" tags.
*   **Do** use large amounts of white space (e.g., `spacing-20`) between major institutional sections.

#### Don't:
*   **Don't** use 100% opaque, high-contrast borders. It breaks the "Ethereal" illusion.
*   **Don't** use standard "Material Design" shadows. They are too heavy for this professional, light-filled UI.
*   **Don't** use divider lines to separate list items. Use a `spacing-2` gap and a subtle background shift on hover.
*   **Don't** use "pure black" (#000000). Always use `on_surface` (#0b1c30) to maintain tonal harmony with the blues.