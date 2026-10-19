# cms-core

A minimal, fast CMS written in Python that beats Drupal's complexity.

- Markdown content files (no DB required)
- Jinja2 templates
- Static site generation + dynamic serve
- Plugin architecture for content types
- CLI: `cms init`, `cms build`, `cms serve`
- One dependency: Jinja2 + Python-Markdown

## Install

```bash
pip install git+https://github.com/JovianOps/cms-core.git
```

## Usage

```bash
cms init       # Create new project
cms build      # Generate static site to dist/
cms serve      # Start local dev server on :8000
```

## License

MIT
