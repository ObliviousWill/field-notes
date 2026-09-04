# MN Landscapes — concept site

A single-page, lead-generation concept build for MN Landscapes (Norfolk garden
design & build, est. 1997). Self-contained: one HTML file, no build step, no
dependencies beyond Google Fonts.

Open `index.html` in a browser, or publish it anywhere static.

## Design direction

Warm and planted, photography-led: sage grounds, forest-green ink and solid
green buttons, with marigold reserved for star ratings and the headline
highlight. Petrona for headings, Source Sans 3 for everything else, 19px
body, soft radii and low shadows.

An earlier pass used monospace annotations, hard offset shadows and a survey
grid. It stood out, but it read as developer tooling rather than horticulture,
and letterspaced monospace at 11px is the wrong choice for an audience mostly
in their 50s and 60s. That version is kept in git history only.

The one technical flourish that survived is the canvas-drawn CAD garden plan
in the design section, because in-house drawings are a real differentiator
against a man-with-a-van, and no competitor in the area shows them.

## Where the real content came from

The company's own copy, project write-ups, accreditations, reviews and contact
details were reconstructed from public sources (mnlandscapes.co.uk, Companies
House, Pavestone, Facebook). The live site could not be fetched directly from
the build environment, so anything price-related was deliberately left out
rather than invented.

Note that much of the public material predates the change of ownership: the
founders sold the business to Chris. MN Horticulture is not his, and the
business does not do garden maintenance — design and build only. All copy here is deliberately written as
a claim about the business rather than about any individual, so nothing on the
page depends on who is on the tools. Two things still need checking against
the current company (see below).

## What still needs the client

- **Photography.** Every image slot is a textured "material plate" tagged with
  what belongs there (`Photo 01` … `Photo 09`). Swap each `<div class="plate …">`
  for an `<img>`; the aspect ratios are already set.
- **Confirm the accreditations still stand** in the current company's name.
  APL, BALI and TrustMark all police their marks, and the limited company
  behind the business was only registered in 2023. The claims come from the
  live site, but they predate the sale.
- **Confirm** the review attributions, the phone number and the email address
  (`chris@mnlandscapes.com` is on a different domain to the website — worth
  moving to `.co.uk` for trust).
- **Two proposed promises need his agreement.** The page says he hands over
  the planting plan at the end, and that he'll suggest a local gardener if
  asked. Both are cheap for a design-and-build outfit that already draws
  planting plans, and both are good differentiators — but they are proposals,
  not things he has said he does.
- **Form handling.** The submit handler is a client-side demo. Point it at an
  email/CRM endpoint and keep the thank-you state.

## Site architecture this page assumes

This file is the **home page** of a hub-and-spoke site, not the whole site.
It is deliberately a selection: four projects, six services, five questions.
Measured at 1,600 words — 12 screenfuls on desktop, 20 on a phone, with a
persistent call/quote bar so the form is always one tap away.

The full build should be:

| Page | Job |
|---|---|
| Home | This page. Establish trust, show the work, capture the easy enquiries. |
| 6 service pages | Garden design, patios & paving, driveways, walls & steps, decking & fencing, planting & lawns. Each with its own title, H1, URL, projects, FAQs and form. These are what rank. |
| One page per project | The highest-value SEO asset, and what prospects actually want to see. He already has these indexed under `/site/norwich-gardening-projects/`. |
| Areas we cover | The full town list, off the home page. |
| 3–4 town pages | Only where there are real projects to show. Never one per village — thin location pages are a penalty risk. |
| Ad landing page | No navigation, one action, for paid traffic. Should not be the home page. |

**Migration risk:** the existing `.asp` project URLs are indexed. Any rebuild
needs a 301 redirect map, or it throws away rankings the business already has.
This is the largest technical risk in the project.
