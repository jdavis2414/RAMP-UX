# Ramp Design System Specification

**Project:** CIDO Ramp — Compute Environment Management System  
**Version:** 1.0.0  
**Target:** High-Performance Compute Systems Engineering & Operations Portal

---

## 1. Visual Direction & Brand Posture

The Ramp design system delivers a high-density, authoritative defense-grade application interface for managing compute environments and cost estimates.

### Posture Cues & Principles
- **Dark Top Chrome / Light Content Canvas**: Dark black appbar (`#111111`) and dark green classification banner (`#006622`) ground the interface, transitioning into a clean, uncluttered white (`#ffffff`) and light gray (`#f7f8fa`) workspace.
- **8px Geometric Radius**: Standardized 8px corner radii across buttons, cards, progress bars, input fields, and modal containers.
- **High-Signal Accent Discipline**: Primary blue accent (`#1677ff`) is reserved strictly for primary CTA buttons, active progress indicators, and active selection highlights.
- **Header Alignment**: Equal height (`72px`) for the left Home section box and top Environment Request header bar to enforce a continuous horizontal baseline.

---

## 2. Color Tokens

All CSS color literals across the application adhere strictly to the registered Ramp palette:

| Token Name | Hex | OKLch Value | Role / Usage |
| :--- | :--- | :--- | :--- |
| `--bg` | `#ffffff` | `oklch(100% 0 0)` | Primary content canvas |
| `--fg` | `#111111` | `oklch(12% 0 0)` | Primary text, dark appbar background, completed fills |
| `--accent` | `#1677ff` | `oklch(56% 0.22 255)` | Primary CTAs, active progress bars, outline button strokes |
| `--surface` | `#f7f8fa` | `oklch(98% 0.004 240)` | Neutral card backgrounds, hero headers, hover states |
| `--muted` | `#6b7280` | `oklch(52% 0.018 240)` | Secondary labels, descriptions, and breadcrumbs |
| `--border` | `#d9dee7` | `oklch(89% 0.006 240)` | Dividers, input outlines, card boundaries |
| `--unclassified` | `#006622` | `oklch(40% 0.16 142)` | Top and bottom UNCLASSIFIED banner background |

---

## 3. Typography & Hierarchy

- **Display & Headings**: `Inter, system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif`  
  Heavy/Bold weights (700/800) with tight letter-spacing (`-0.01em` to `-0.02em`).
- **Body & Controls**: `Inter, system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif`  
  Normal/Medium weights (400/500/600) for UI labels, card descriptions, and button copy.
- **Monospace & Metadata**: `ui-monospace, 'JetBrains Mono', 'IBM Plex Mono', monospace`  
  Used for IDs (`ENV-2026-8941`), price tags (`$5,400.00`), and classification banner text (`UNCLASSIFIED`).

---

## 4. Key Component Specifications

### Classification Banners
- **Height**: `28px`, fixed at top (`top: 0`) and bottom (`bottom: 0`) of the screen.
- **Style**: Dark green (`#006622`), white bold monospace text (`11px`), centered with `0.12em` uppercase tracking.
- **Label**: `UNCLASSIFIED`.

### Header App Bar (`.appbar`)
- **Height**: `56px` / `64px`, sticky top beneath classification banner.
- **Background**: Solid black (`#111111`).
- **Brand Elements**:
  - Ramp logo mark (white `R` icon box + white `Ramp` title).
  - Northrop Grumman wordmark (`NORTHROP GRUMMAN`) with signature top-right angle bracket motif (`.ng-brand-bracket`) in crisp white, placed directly to the left of the User Profile button.
  - User Profile icon button (`40px × 40px`, `#111111` background, `#d9dee7` border, white profile icon SVG) triggering the User Profile modal.

### Left Vertical Navigation (`.vertical-nav`)
- **Width**: `240px` fixed sidebar.
- **Home Box**: `72px` height, matching the right content header height to align bottom border lines seamlessly across the layout.
- **Active Workflow Section**: Left indicator border (`3px solid #1677ff`) with bold workflow title.
- **Sub-Task Items**: Clean list with inline status badges (`✓` checkmark badge for completed, `!` alert badge for in-progress/error).

### Task Workflow Organism (`workflow.html`) & Dedicated Task Pages (`ProgramDetails.html`, `FinancialDetails.html`)
- **Cost Data Bar**: Borderless and background-transparent summary displaying `Base Fee`, `Compliance Levels`, and `TOTAL` in `sans-serif` Inter typography.
- **Phase Progress Component**: Row of horizontal progress bar segments for each task phase (`100%` filled for complete, `50%` filled for in-progress, `0%` for unstarted).
- **Breadcrumb**: Positioned directly underneath the phase progress bars.
- **`workflow.html` Layout**: Primary Task Workflow organism displaying the task list overview, progress headers, and task step cards with placeholder routing.
- **`ProgramDetails.html` Layout**: Dedicated task page for the "Enter Program Details" workflow step, housing the full form card (Program Name, Sector, Division, Approver, Co-Owners, Description) and navigation buttons (`Back` and `Save & Continue`).
- **`FinancialDetails.html` Layout**: Dedicated task page created from wireframe `image-1.png` for the "Enter Financial Details" workflow step, featuring form fields for `Cost Code`, `Job Number (JN)`, `Organizational Code`, and `IWO Number`, with `Back` and `Save & Continue` action buttons.
- **Task Cards & Action Buttons**:
  - Card list with titles and descriptions.
  - **Uniform Fixed Button Width**: `120px` fixed width with centered text alignment for all task buttons regardless of text length.
  - Button styling variants:
    - `EDIT`: Solid blue filled button (`btn-primary`).
    - `RESUME`: Solid blue filled button (`btn-primary`).
    - `START`: Blue outline stroke button (`btn-outline-blue`: `border: 1px solid #1677ff; color: #1677ff; background-color: #ffffff;`).

### Homepage Layout (`index.html`)
- **Hero Header**: High-level portal overview with quick launch actions (`Request Cost Estimate`, `Request New Environment`).
- **Section Order**:
  1. **Compute Environments** (displayed first): Active compute cards with ID, status badge, title, paragraph description, monthly rate, and RBAC action controls (`Edit`, `Archive`, `New Cost Est`, `Monitor`).
  2. **Cost Estimates** (displayed second): Draft estimate cards with ID, status badge, title, paragraph description, monthly rate, and action controls (`Edit`, `Delete`, `Clone`).

---

## 5. Workflows & RBAC Rules

1. **Request Cost Estimate**: Creates and recalculates cost estimates for new environments.
2. **Request New Environment**: Complete provisioning workflow including program details, financial details, cloud setup, on-prem setup, user/location configuration, and toolset selection.
3. **Edit Environment**: Modify active instance allocations and specs.
4. **Archive Environment**: Deprovision and snapshot persistent storage.
5. **Monitor Environments**: View live telemetry, CPU/GPU utilization, and burn rate.

**RBAC Roles:**
- **Owner**: Granted full execution, edit, archive, and monitoring rights across all environments and estimates.
- **Reviewer**: Restricted to view-only monitoring and reference cost estimate cloning.
