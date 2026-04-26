# design.md - Eqar UI Guidance

Use this file before creating, redesigning, or polishing frontend UI for Eqar.

Eqar is a buyer-facing Canadian real estate search and market intelligence product. It should feel fast, serious, trustworthy, and useful on a phone outside a property. It is not a generic SaaS dashboard and not a marketing landing page.

## Core Rule
Design like the user is making a high-stakes housing decision, not browsing a lead funnel.

Every screen should help the buyer answer:
- What is this home?
- What changed?
- What did nearby homes actually sell for?
- Is the price credible?
- What do I do next if I choose to?

## Product Feel
Aim for:
- Clean, data-rich, and calm.
- Fast and concrete.
- Serious enough for a large transaction.
- Friendly enough for non-experts.
- Mobile-first without making desktop feel stretched.

Avoid:
- Lead-gen landing-page energy.
- Generic AI dashboard patterns.
- Decorative metric cards.
- Oversized hero sections.
- Fake market insight panels.
- Dark, glossy control-room UI.
- Signup-wall pressure.

## Key Surfaces
### Search
- Map/list is the primary product surface.
- Desktop should use a split map/list layout.
- Mobile should use a map with a bottom sheet result list.
- Filters should be real controls, not decorative chips.
- The map should stay responsive while filters change.
- Listing cards should be compact, image-led, and scannable.
- Do not overload cards with every fact. Save depth for listing detail.

### Listing Detail
- Photos matter. The gallery should feel smooth, stable, and premium.
- Property facts should be easy to scan.
- Price, status, address, and key facts should be visible without hunting.
- Listing history should be a first-class timeline.
- Price changes, relists, terminations, and sold events should be legible.
- Comparable sales should be table/map friendly, not buried in prose.
- Source timestamp and data provenance should be visible but not loud.

### Sold And Comparables
- Sold prices should feel like market evidence, not a teaser.
- Tables should support comparison: sale date, distance, property type, beds/baths, size, list price, sold price, DOM, and similarity.
- Maps should visually distinguish active, sold, and subject properties.
- Estimate ranges should be shown as ranges, not single magic numbers.

### Neighborhood Pages
- SEO pages should still feel useful to humans.
- Use actual listings, sold trends, price bands, market stats, schools, and neighborhood boundaries.
- Avoid generic city-guide filler.
- Keep the search/listing pathway obvious.

### Contact And Tour Flows
- Contact actions must be explicit.
- Consent language should be plain.
- Do not make agent contact feel like a trap.
- Saving, viewing, or comparing must not look like it will contact an agent.

## Layout Standards
- Use stable map/list dimensions to prevent layout shift.
- Keep toolbars compact and predictable.
- Keep filters reachable on mobile.
- Use tables for comparison-heavy data.
- Use timelines for listing history.
- Use split panels for map/list and detail/comps workflows.
- Use cards only for repeated items like listing cards or saved searches.
- Avoid cards inside cards.
- Avoid decorative section containers.

## Interaction Standards
- Filters: checkboxes, toggles, segmented controls, sliders, selects, and numeric inputs as appropriate.
- Map controls: icons with tooltips.
- Saved state: clear heart/bookmark behavior.
- Alerts: explicit cadence and criteria.
- Contact: explicit button, explicit modal, explicit consent.
- Gallery: swipe, keyboard, thumbnails on desktop, stable aspect ratios.
- Loading: skeletons or reserved space to avoid layout jump.

## Visual Standards
- Border radius: 6-8px for most UI, 10-12px only for large gallery/listing surfaces if needed.
- Shadows: minimal and functional.
- Borders: subtle 1px lines.
- Typography: readable, restrained, no decorative headline tricks.
- Body text: 14-16px.
- Data labels: compact but accessible.
- Icons: use a consistent icon library such as lucide if the app includes one.
- Colors: neutral base with a small number of functional accents.

## Color Direction
Prefer a light, serious product palette unless the user chooses a brand:
- Background: `#f7f7f5`
- Surface: `#ffffff`
- Text: `#1f2933`
- Muted text: `#64707d`
- Border: `#d9dedc`
- Primary: `#0f766e`
- Primary hover: `#115e59`
- Accent: `#c2410c`
- Success/sold: `#047857`
- Warning/price change: `#b45309`
- Map active: `#0f766e`
- Map sold: `#7c3aed`

Do not let the app become a one-note teal theme. Use accent colors only for meaning.

## Hard Bans
- No unsolicited-contact prompts disguised as normal browsing.
- No full-screen signup wall for basic search.
- No dashboard hero blocks.
- No decorative gradient blobs.
- No glassmorphism.
- No floating ornamental sidebars.
- No fake charts or invented statistics.
- No huge rounded pills everywhere.
- No overpadded listing cards.
- No text that explains obvious UI mechanics.
- No generic copy like "unlock your real estate journey."
- No dark premium theme unless deliberately designed and tested.
- No mobile layout that becomes a long stack of disconnected panels.

## Mobile Requirements
- Search must be usable one-handed.
- Filter controls must not cover the whole product without an easy path back.
- Bottom sheet states should be predictable: collapsed, half, full.
- Listing cards need stable image aspect ratios.
- Text must not overlap photos, map controls, or sticky bars.
- The primary listing facts must fit without horizontal scrolling.
- Gallery should avoid jank on mid-range phones.

## Performance Design Rules
- Reserve image and map container dimensions.
- Lazy-load heavy panels.
- Avoid shipping giant filter payloads to the client.
- Prefer compact listing summary payloads in search.
- Use responsive images and thumbnails.
- Do not animate layout-critical elements.
- Avoid scroll-linked effects.

## Accessibility
- Search and listing detail should be keyboard navigable.
- Map-only information needs list/table equivalents.
- Color cannot be the only status indicator.
- Buttons and controls need accessible labels.
- Form errors must be explicit.
- Contrast should pass WCAG AA for normal text.

## Review Checklist
Before finishing UI work:
- The first screen is the actual search product, not a landing page.
- Map/list interaction works on desktop and mobile.
- Listing cards are compact and stable.
- Listing detail has a serious, high-quality photo/gallery treatment.
- Sold/comps data is easy to compare.
- Listing history is visible and understandable.
- Contact actions are explicit and consent-based.
- No fake data visualizations were added for decoration.
- No text overlaps at common mobile and desktop widths.
- Performance budgets were considered, especially images and map payloads.
