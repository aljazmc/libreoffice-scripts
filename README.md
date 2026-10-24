# libreoffice-scripts

Python scripts that build documents as flat OpenDocument XML and convert
them with LibreOffice into PDF, Word, images and about thirty other formats.
Every document is a small project of its own in `scripts/`, and one shell
script builds any project into any format.

## Requirements

- LibreOffice (`soffice` on the `PATH`), run headless
- Python 3 (standard library only)
- The fonts the projects use, e.g. Lato, Liberation, DejaVu, TeX Gyre and
  Quicksand; LibreOffice falls back to other fonts when one is missing, but
  then page counts may change

## Usage

```sh
./project.sh <project> <format>        # build one format
./project.sh <project> all             # build every format
./project.sh all <format>              # build every project
./project.sh <project> <format> clean  # remove one output
./project.sh <project> clean           # remove all outputs of a project
./project.sh clean                     # remove build/ and odf/
```

For example:

```sh
./project.sh job-hunting-nika-creative-technologist-cv-onepage pdf
```

Outputs go to `build/<project>.<format>`, and `odf` builds go to
`odf/<project>.odt`. Existing outputs are skipped; clean them to rebuild.
Running `./project.sh` without arguments lists the formats and projects.

### Formats

`apng bmp doc docbook docm docx dot dotx emf emz eps epub fodg fodt gif
html jpg odg otg ott pdf png rtf svg svgz tif txt uot webp wmf wmz wordxml
xhtml` and `odf`.

Text documents convert best to the Writer formats (`pdf`, `odf`, `docx`,
`doc`, `rtf`, `html`, `txt`, `epub`, ...). The image and drawing formats
(`png`, `svg`, `gif`, `eps`, `odg`, ...) go through LibreOffice Draw and
only keep shapes placed on the page, so flowing text comes out blank.

## How it works

```
project.sh ──> scripts/export<format>.py ──> scripts/common.py
                                               │ load_project()
                                               ▼
                         scripts/<project>/<name>.py: <name>() -> flat ODT
                                               │ export()
                                               ▼
                          soffice --headless --convert-to <format>
```

- `project.sh` checks the arguments and runs `scripts/export<format>.py`
  (or `scripts/saveodf.py`) with `PROJECT=<project>`.
- `scripts/common.py` imports the project and calls its function, then
  runs LibreOffice with a throwaway user profile, so it never touches a
  running LibreOffice and conversions can run in parallel.
- Each `scripts/export<format>.py` names the LibreOffice filter and its
  options for one format.

## Projects

A project is a folder `scripts/<theme>-<name>/` with a module `<name>.py`
that defines a function `<name>()` returning a flat ODT document as a
string. The part of the folder name after the last hyphen is the module
and function name, so it must be a valid Python name.

```
scripts/job-hunting-nika-creative-technologist-cv-onepage/
├── onepage.py       # def onepage(): the document's design and entry point
├── content.py       # PERSONA and DOCUMENT: who and what
└── typesetting.py   # turns them into a flat ODT of exactly N pages
```

Projects are self-contained: everything a project needs lives in its
folder, and other files in `scripts/` are only the exporters and
`common.py`.

### Job hunting

The `job-hunting-*` projects are CVs, cover letters and portfolio
documents of fictional people, named

```
job-hunting-<persona>-<job>-<document>-<onepage|twopages|fourpages>
```

There are ten personas from the digital industries, each with three
documents in three lengths:

| Persona | Applying as | Extra document | Look |
|---|---|---|---|
| felix | information designer | process-book | Swiss brutalist |
| ines | UI artist | devlog | arcade |
| kai | visualisation artist | showreel-breakdown | blueprint |
| leo | junior frontend developer | learning-log | till receipt |
| maks | XR lead | prototype-log | neon |
| nika | creative technologist | code-sketchbook | terminal |
| otto | principal engineer | open-source-portfolio | Markdown |
| ruth | art director | artist-statement | zine |
| yuki | sound designer | sound-portfolio | printed score |
| zara | medical animator | animation-treatment | cinema |

Every persona has a `cv`, a `cover-letter` and the extra document, each in
one, two and four pages.

**Exact page counts.** `typesetting.py` does not shrink fonts to fit.
Every paragraph, entry and bullet in `content.py` has a priority, and the
typesetter keeps the most important ones that fit into the estimated
height of the pages, in the order of the document. Line heights are fixed
and line wrapping is estimated from the average character width of each
font, so a one-page CV, a two-page CV and a four-page CV are the same
content, cut differently.

**Content.** `content.py` holds `PERSONA` (name, headline, contact) and
`DOCUMENT` (title and sections). A section has a `kind` (`text`,
`entries`, `bullets`, `tags`, `motto`) and priorities:

- `weight`: the priority of its first item; lower is more important
- `step`: how much less important each next item is
- `inner`: the same for the lines inside an entry
- `min_pages` / `max_pages`: the lengths the section appears in

Entries can have `items` (bullets), `fields` (label and text), `text`
paragraphs and a low-priority `story` that only appears when there is
room. `**bold**` and `*italic*` work in all text.

**Design.** The `DESIGN` dict in the project module chooses the colors
(`accent`, `ink`, `muted`, `page`), fonts (`font`, `heading_font`),
`density`, `margin`, header and heading styles, `heading_format` (e.g.
`"$ cat ~/{slug}.txt"` or `"Movement {roman} · {title}"`), `bullet`,
`divider` and `footer`. See `stylesheet()` in `typesetting.py` for every
option.

## License

MIT, see [LICENSE](LICENSE).
