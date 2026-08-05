# Module 20: React & TypeScript

Built for the OverClocked Services assessment (React Basic + TypeScript Basic sections),
but it is a general React and TypeScript foundation.

## Setup (once)

```bash
cd 20_react_ts
npm install
```

## Grade yourself

Same idea as the Python modules, except vitest is the runner instead of a `TESTS` block at
the bottom of the file.

```bash
npm test              # everything
npm run ts            # TypeScript problems only
npm run react         # React problems only
npm run watch         # re-run on save, the best way to work
```

One problem at a time:

```bash
npx vitest run problems/react/03_form
```

## See it running

```bash
npm run dev
```

Uncomment whichever problem you are on in `src/App.tsx`. The tests grade correctness, the
browser shows you what you actually built. Use both.

## Layout

```
20_react_ts/
  LESSON_TYPESCRIPT.md      read first for the ts/ problems
  LESSON_REACT.md           read first for the react/ problems
  problems/react/00_drills.tsx   23 micro-exercises, start here
  problems/ts/*.ts          5 stubs you fill in  (+ .test.ts graders)
  problems/react/*.tsx      7 stubs you fill in  (+ .test.tsx graders)
  solutions/                reference answers, all verified passing
  src/                      playground app for npm run dev
```

## Start here if React is new

`problems/react/00_drills.tsx`. 23 micro-exercises, one idea each, most a single line, with
the explanation directly above each blank. Roughly an hour. Everything else in the React
half assumes these.

```bash
npx vitest problems/react/00_drills
```

Read `LESSON_REACT.md` **after** the drills are green, not before. It lands as review then
instead of as a wall of new terms.

## Suggested order

`react/00_drills` → `ts/01` → `ts/02` → `ts/03` → `react/01` → `react/02` → `react/03`
→ `react/05` → `react/04` → `ts/04` → `ts/05` → `react/06` → `react/07`

TypeScript 01 to 03 first because React problems are written in TypeScript and you will
fight the types otherwise. Then React 05 (searchable list) before 04 (to-do) because 05
teaches derived state, which makes 04 much easier.

If you only have one day, do **react/01, 02, 03, 05, 04** in that order and skip everything
else. That is the core.

## Rules that make this work

- **Write from memory.** Reading a solution and moving on teaches nothing.
- **Never edit a `.test.ts` or `.test.tsx` file.** They are the grader.
- Stuck 10+ minutes? Read the `Hint` block at the top of the problem file. Still stuck? Read
  the solution, then **close it and rewrite from an empty file.**
- Redo 04 and 05 cold a few days later. Spacing is what makes it stick.

## The habit that matters most

Every React problem lists its required `data-testid` values at the top. **Put all of them
into your JSX before writing any logic.** Graders select by test id, so a perfect component
with a misspelled test id scores zero. Building that habit here is worth more than any
individual pattern in this module.
