# Lifeng's Academic Homepage

This repository now builds an academic homepage with the [al-folio](https://github.com/alshedivat/al-folio) template and deploys it to GitHub Pages at <https://lifeng10.github.io/>.

## How this repo works

- `_config.yml` contains site-level al-folio overrides.
- `_pages/` contains top-level pages such as About, Publications, Projects, and CV.
- `_bibliography/papers.bib` contains publications rendered by al-folio.
- `_news/` contains announcements shown on the homepage.
- `_projects/` contains project cards.
- `.github/workflows/publish.yaml` downloads the official al-folio template, applies these files, builds the site, and deploys it with GitHub Pages.

Edit the content files above to personalize the site.
