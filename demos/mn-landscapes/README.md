# MN Landscapes — concept site

A single-page, lead-generation concept build for MN Landscapes (Norfolk garden
design & build, est. 1997). Self-contained: one HTML file, no build step, no
dependencies beyond Google Fonts.

Open `index.html` in a browser, or publish it anywhere static.

## Where the real content came from

The company's own copy, project write-ups, accreditations, reviews and contact
details were reconstructed from public sources (mnlandscapes.co.uk,
mnhorticulture.com, Companies House, Pavestone, Facebook). The live site could
not be fetched directly from the build environment, so anything price-related
was deliberately left out rather than invented.

## What still needs the client

- **Photography.** Every image slot is a textured "material plate" tagged with
  what belongs there (`Photo 01` … `Photo 09`). Swap each `<div class="plate …">`
  for an `<img>`; the aspect ratios are already set.
- **Confirm** the review attributions, the phone number and the email address
  (`chris@mnlandscapes.com` is on a different domain to the website — worth
  moving to `.co.uk` for trust).
- **Form handling.** The submit handler is a client-side demo. Point it at an
  email/CRM endpoint and keep the thank-you state.
