# design.md - Eqar UI Skill

This is the shared UI design skill for Codex and Claude Code on Eqar. Use it before creating, redesigning, or polishing any frontend UI.

The goal is to avoid default AI-generated dashboard aesthetics and produce interfaces that feel practical, composed, and human-designed.

## Core Rule
If a UI choice feels like a default AI move, reject it and choose the cleaner, more ordinary option.

Eqar should feel closer to Linear, Raycast, Stripe, or GitHub than to a generic AI dashboard.

## Mandatory Workflow
1. Read existing UI files before changing design.
2. Reuse project colors, spacing, and component patterns when they exist.
3. If no palette exists, pick from the palettes in this file instead of inventing random colors.
4. Before editing, identify likely "AI UI" defaults for the task and avoid them.
5. Prefer designer-like components: predictable layout, clear hierarchy, restrained styling, and functional controls.
6. Keep dashboard UI dense enough for repeated professional use.
7. Do not add decorative content just to fill space.

## Normal UI Standard
- Sidebars: 240-260px fixed width, solid background, simple border-right, no floating shell.
- Headers: plain text hierarchy, no eyebrow labels, no gradient text, no decorative explainer copy.
- Sections: standard 20-30px padding, no hero blocks inside dashboards.
- Navigation: simple links, subtle hover states, no transform animations, no fake badges.
- Buttons: solid fills or simple borders, 8-10px radius max, no pill overload, no gradients.
- Cards: simple containers, 8-12px radius max, subtle borders, minimal shadow.
- Forms: labels above fields, standard inputs, simple focus rings.
- Inputs: solid borders, no animated underlines or morphing shapes.
- Modals: centered overlay, simple backdrop, straightforward close button.
- Dropdowns: simple list, subtle shadow, clear selected state.
- Tables: clean rows, simple borders, subtle hover, left-aligned text.
- Lists: simple items, consistent spacing, no decorative bullets.
- Tabs: underline or border indicator, no pill backgrounds or sliding animations.
- Badges: small, functional only, simple border/background, 6-8px radius.
- Avatars: simple circle or rounded square, no decorative rings unless status is functional.
- Icons: consistent 16-20px size, no decorative icon backgrounds.
- Typography: readable 14-16px body text, clear hierarchy, no mixed serif/sans shortcut.
- Spacing: use a consistent 4/8/12/16/24/32px scale.
- Borders: 1px solid, subtle colors, no gradient borders.
- Shadows: max `0 2px 8px rgba(0,0,0,0.1)`.
- Transitions: 100-200ms color/opacity only; avoid transform effects.
- Layouts: standard grid/flex, predictable structure, no creative asymmetry.
- Containers: max-width 1200-1400px when needed, standard padding.
- Panels: simple background differentiation and borders, no glass effects.
- Toolbars: 48-56px height, clear actions, no decorative elements.
- Breadcrumbs: simple text with separators.

## Hard Bans
- No oversized rounded corners.
- No pill overload.
- No floating glassmorphism shells.
- No soft corporate gradients used to fake taste.
- No generic dark SaaS composition.
- No decorative sidebar blobs.
- No control-room cosplay unless explicitly requested.
- No serif headline plus sans body shortcut to "premium."
- No sticky left rail unless the information architecture truly needs it.
- No metric-card grid as the first instinct.
- No fake charts that exist only to fill space.
- No glows, blur haze, frosted panels, conic gradients, or decorative donuts.
- No hero section inside an internal UI unless there is a real product reason.
- No alignment that creates dead space just to look expensive.
- No overpadded layouts.
- No mobile collapse that turns the app into a long stacked sandwich.
- No ornamental labels like "live pulse", "night shift", or "operator checklist" unless they are product vocabulary.
- No generic startup copy.
- No style decisions made only because they are easy to generate.
- No `<small>` headers.
- No rounded `span` decorations.
- No colors drifting toward blue unless already established by the project.
- No big "headline" blocks inside dashboard surfaces.

## Specifically Avoided Patterns
- 20-32px border radii across everything.
- Repeating the same rounded rectangle treatment on sidebar, cards, buttons, and panels.
- 280px sidebars with large brand blocks and decorative nav.
- Floating detached sidebars with rounded outer shells.
- Glass cards containing charts without product-specific reason.
- Donut charts with hand-wavy percentages.
- Hierarchy created with glows instead of spacing, text, and borders.
- Mixed alignment where some content hugs edges and other content floats center-ish.
- Muted gray-blue text that weakens contrast.
- Blue-black gradient "premium dark mode."
- Eyebrow labels, uppercase labels, and letter-spacing as a default pattern.
- Decorative copy such as "operational clarity without the clutter."
- Section notes explaining obvious UI.
- Hover transforms such as `translateX(2px)`.
- Dramatic shadows such as `0 24px 60px rgba(0,0,0,0.35)`.
- Status dots created with pseudo-elements unless status is genuinely needed.
- Gradient pipeline/progress bars.
- KPI grids as the default dashboard opening.
- Decorative "team focus" or "recent activity" panels.
- Tag badges on every table cell/status.
- Workspace blocks in the sidebar with CTA buttons.
- Gradient brand marks.
- Nav badges showing fake counts or "Live".
- Quota or usage panels with decorative progress bars.
- Footer meta lines.
- Trend indicators that exist only for color.
- Right rails full of filler schedules.
- Multiple nested panel types.

## Color Selection
Priority order:
1. Use the existing project palette if one exists.
2. If there is no palette, choose one palette below.
3. Do not invent random color combinations.

Prefer calm, dark, muted colors for Eqar unless the user asks otherwise.

### Preferred Dark Palettes
| Palette | Background | Surface | Primary | Secondary | Accent | Text |
|---|---|---|---|---|---|---|
| Obsidian Depth | `#0f0f0f` | `#1a1a1a` | `#00d4aa` | `#00a3cc` | `#ff6b9d` | `#f5f5f5` |
| Carbon Elegance | `#121212` | `#1e1e1e` | `#bb86fc` | `#03dac6` | `#cf6679` | `#e1e1e1` |
| Graphite Pro | `#18181b` | `#27272a` | `#a855f7` | `#ec4899` | `#14b8a6` | `#fafafa` |
| Onyx Matrix | `#0e0e10` | `#1c1c21` | `#00ff9f` | `#00e0ff` | `#ff0080` | `#f0f0f0` |

Avoid blue-heavy palettes unless the user explicitly asks for them.

### Acceptable Light Palettes
| Palette | Background | Surface | Primary | Secondary | Accent | Text |
|---|---|---|---|---|---|---|
| Pearl Minimal | `#f8f9fa` | `#ffffff` | `#0066cc` | `#6610f2` | `#ff6b35` | `#212529` |
| Ivory Studio | `#f5f5f4` | `#fafaf9` | `#0891b2` | `#06b6d4` | `#f59e0b` | `#1c1917` |
| Sand Warm | `#faf8f5` | `#ffffff` | `#b45309` | `#d97706` | `#059669` | `#451a03` |
| Frost Bright | `#f1f5f9` | `#f8fafc` | `#0f766e` | `#14b8a6` | `#e11d48` | `#0f172a` |

## Eqar-Specific Guidance
- Eqar is a real-estate agent work tool, not a marketing page.
- Build internal dashboard screens as operational software: direct, scannable, and repeat-use friendly.
- Use real workflows as layout drivers: clients, conversations, documents, analyses, calculations, exports.
- Avoid fake metrics until the backend can provide meaningful data.
- Prefer lists, tables, split panes, forms, and toolbars over decorative cards.
- Keep client-share/export states visibly stricter than draft states.

## Review Checklist
Before finishing UI work, verify:
- No dashboard hero block.
- No decorative eyebrow labels.
- No unnecessary metric-card grid.
- No glass, glow, blur, or gradient decoration.
- No over-large radius.
- No fake chart or fake trend.
- Text hierarchy is plain and useful.
- Layout works for a busy agent returning to the app daily.
- Mobile layout remains structured and usable.
