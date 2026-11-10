# godCode web

The practice repo as a browser learning tool: lesson on the left, editor on the right,
Python running in the page, XP and a streak for finishing things.

It covers the Python modules that have a `drills.py` (currently 00 to 06): 7 lessons,
240 drills, 39 problems. `20_react_ts` and `30_cpp` are not included, because they cannot
be graded in a browser the way Python can.

## Run it

```bash
python3 -m http.server 5180 --directory web/site
```

Then open http://localhost:5180. It has to be served over http; opening `index.html`
straight from disk will not load the course.

## Rebuild after changing the repo

The site reads `web/site/content.json`, which is generated from the module folders:

```bash
python3 web/build.py
```

Run it whenever a lesson, drill, problem, or solution changes, or when a new module is
added. The build:

- reads every `NN_topic/` folder that has a `drills.py`, without modifying any of them
- runs every reference solution through the grader and fails if one does not pass
- flags drills and problems already solved in the repo files, so the site imports them
  as completed
- carries a half-written attempt across as the starting code in the editor

## How it fits together

```
web/
  build.py           repo files  ->  site/content.json
  site/
    index.html       page shell
    styles.css
    app.js           dashboard, workspace, progress, XP, streak
    runner.js        talks to the Python worker, kills it on a timeout
    pyworker.js      web worker that loads Pyodide
    grader.py        the grader, shared by the browser and build.py
    content.json     generated
    art/             engravings and icons, with CREDITS.md
```

- **Python** runs in the browser through Pyodide, in a web worker. A run that takes longer
  than 6 seconds is treated as an infinite loop and stopped.
- **Run** tries the first test and shows anything printed. **Submit** checks every test
  and awards XP.
- **Progress** (XP, streak, completed items, your code) lives in the browser's
  localStorage. Use Export on the dashboard to back it up or move it to another browser.
- **Solutions** are behind a confirm. Opening one before solving halves the XP for that
  item.
- The editor, Markdown renderer, and Pyodide load from public CDNs, so the first visit
  needs a connection.

## Putting it online

`web/site` is a plain static folder with no server code. Any static host works (GitHub
Pages, Netlify, Vercel, Cloudflare Pages): point it at `web/site` as the publish
directory, with no build command.

## Theme and art

The site is dressed as a fantasy quest log: chapters, ranks, boss fights. The names and
ranks are original; nothing is taken from a named fantasy franchise. All artwork is
freely licensed and listed in `web/site/art/CREDITS.md`. The icon set is CC BY 3.0, so
the credit line at the bottom of the dashboard has to stay.
