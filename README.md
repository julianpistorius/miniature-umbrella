# Hugo Conversion

This repository contains the original Jetstream2 HTML files and a new `site/` directory with a Hugo implementation.

## Building the site

1. Ensure [Hugo](https://gohugo.io) is installed.
2. Run:

```bash
cd site
hugo --minify
```

The generated site will appear in `site/public`.

## Editing content with Decap CMS

This repo includes [Decap CMS](https://decapcms.org/) under `site/static/admin`.
After building or running `hugo server`, open `/admin/` in your browser
(`http://localhost:1313/admin/` when using `hugo server`).
The default configuration uses the Git Gateway backend; adjust `config.yml`
in that directory for your hosting setup.
