# Northrop Grumman Design System Brand Spec

Extracted from provided reference specs and design system.

## Color Tokens (OKLch & Hex)

- `--bg`: `oklch(100% 0 0)` (`#ffffff`) — Primary light content canvas
- `--surface`: `oklch(12% 0.01 260)` (`#090a0f`) — Hero banner and navigation bar background
- `--fg`: `oklch(12% 0 0)` (`#111111`) — Primary body text
- `--muted`: `oklch(50% 0 0)` (`#666666`) — Secondary labels, metadata, and breadcrumbs
- `--border`: `oklch(88% 0 0)` (`#d9dee7`) — Divider lines and hairline input borders
- `--accent`: `oklch(42% 0.22 264)` (`#1677ff`) — Primary action buttons, active tabs, link highlights

## Typography Stacks

- **Display & Headings**: `'Inter', 'Helvetica Neue', Arial, sans-serif` — Heavy weight (700/800), tight letter-spacing (-0.02em), geometric posture.
- **Body & UI**: `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif` — Normal/medium weight (400/500), line-height 1.5.
- **Mono / Meta**: `ui-monospace, 'JetBrains Mono', 'IBM Plex Mono', monospace` — Capitalized metadata, read time indicators, search labels.

## Layout & Posture Rules

1. **8px Corner Radius**: Buttons, cards, and containers feature crisp 8px radii.
2. **High Contrast Header**: Top app bar and classification bar feature clean dark surface (`#090a0f`) with white text.
3. **Restrained Accent Budget**: High-signal blue (`#1677ff`) used for primary CTAs and active states.
