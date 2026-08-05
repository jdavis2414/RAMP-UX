# Northrop Grumman Design System Brand Spec

Extracted from provided reference screenshots (`mrw7o4r9-image.png`, `mrw7o4v5-image.png`).

## Color Tokens (OKLch & Hex)

- `--bg`: `oklch(100% 0 0)` (`#ffffff`) — Primary light content canvas
- `--surface`: `oklch(12% 0.01 260)` (`#090a0f`) — Hero banner and navigation bar background
- `--fg`: `oklch(12% 0 0)` (`#111111`) — Primary body text
- `--muted`: `oklch(50% 0 0)` (`#666666`) — Secondary labels, metadata, and breadcrumbs
- `--border`: `oklch(88% 0 0)` (`#e2e2e2`) — Divider lines and hairline input borders
- `--accent`: `oklch(42% 0.22 264)` (`#0033cc`) — Primary action buttons, active tabs, link highlights
- `--navy-banner`: `oklch(22% 0.12 260)` (`#00205b`) — Deep aerospace blue section backgrounds

## Typography Stacks

- **Display & Headings**: `'Inter', 'Helvetica Neue', Arial, sans-serif` — Heavy weight (700/800), tight letter-spacing (-0.02em), geometric posture.
- **Body & UI**: `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif` — Normal/medium weight (400/500), line-height 1.5.
- **Mono / Meta**: `ui-monospace, 'JetBrains Mono', 'IBM Plex Mono', monospace` — Capitalized metadata, read time indicators, search labels.

## Layout & Posture Rules

1. **Sharp Geometry (0px border-radius)**: Buttons, inputs, hero cards, and search boxes feature clean, unrounded 90-degree corners.
2. **Right-Angle Frame Motif**: Signature top-and-right angle bracket framing (`┌` / `┐`) used on logos, headlines, and callout sections.
3. **High Contrast Dark/Light Block Rhythm**: Top header & main hero feature deep black (`oklch(12% 0.01 260)`), transitioning into crisp white content sections.
4. **Restrained Accent Budget**: High-intensity electric blue (`#0033cc`) is used strictly for CTA button fills, active carousel/pagination indicators, and interactive links.
5. **Linear Navigation Dividers**: Vertical separators (`|`) for top utility navigation links and chevrons (`>`) for hierarchical breadcrumbs.
