// godCode web app. No build step: plain script, state in localStorage.
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const XP = { lesson: 5, drill: 10, problem: 30 };
  const XP_PER_LEVEL = 150;
  const KEY = "godcode:v1";
  const codeKey = (id) => "godcode:code:" + id;

  let modules = [];
  let flat = [];
  const byId = {};
  const moduleOf = {};
  let editor = null;
  let busy = false;

  // ---------------------------------------------------------------- state
  const blank = () => ({ done: {}, peeked: {}, xp: 0, days: [] });
  let state = blank();
  function load() {
    try {
      state = Object.assign(blank(), JSON.parse(localStorage.getItem(KEY) || "{}"));
    } catch (e) {
      state = blank();
    }
  }
  function save() {
    try {
      localStorage.setItem(KEY, JSON.stringify(state));
    } catch (e) {}
  }
  function savedCode(id) {
    try {
      return localStorage.getItem(codeKey(id));
    } catch (e) {
      return null;
    }
  }
  function saveCode(id, code) {
    try {
      localStorage.setItem(codeKey(id), code);
    } catch (e) {}
  }
  const today = () => {
    const d = new Date();
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  };
  function streak() {
    const days = new Set(state.days);
    const d = new Date();
    const key = (x) => x.getFullYear() + "-" + String(x.getMonth() + 1).padStart(2, "0") + "-" + String(x.getDate()).padStart(2, "0");
    if (!days.has(key(d))) d.setDate(d.getDate() - 1); // today not done yet does not break it
    let n = 0;
    while (days.has(key(d))) {
      n++;
      d.setDate(d.getDate() - 1);
    }
    return n;
  }
  const isDone = (id) => !!state.done[id];
  function complete(item, opts = {}) {
    if (isDone(item.id)) return 0;
    let xp = XP[item.kind];
    if (state.peeked[item.id]) xp = Math.floor(xp / 2);
    state.done[item.id] = { at: Date.now(), xp };
    state.xp += xp;
    if (!opts.imported && !state.days.includes(today())) state.days.push(today());
    save();
    return xp;
  }

  // ---------------------------------------------------------------- helpers
  const label = (item) => (item.kind === "lesson" ? "Lesson" : item.kind === "drill" ? "Drill " + item.n : "Problem " + item.n);
  const href = (item) => "#/" + item.id;
  function nextUndone(list) {
    return list.find((i) => !isDone(i.id));
  }
  function highlight(root) {
    root.querySelectorAll("pre code").forEach((el) => {
      const lang = (el.className.match(/language-(\w+)/) || [])[1];
      if (lang && lang !== "python" && lang !== "py") return;
      const text = el.textContent;
      CodeMirror.runMode(text, "python", el);
    });
  }
  const codeBlock = (code) => '<pre class="block"><code>' + esc(code.replace(/\s+$/, "")) + "</code></pre>";

  // Drill prompts come from code comments: keep indented lines as code, join
  // wrapped prose back into paragraphs, and honour `backticks`.
  function renderPrompt(text) {
    const inline = (s) => esc(s).replace(/`([^`]+)`/g, "<code>$1</code>");
    const out = [];
    text.split(/\n\s*\n/).forEach((para) => {
      let prose = [];
      let pre = [];
      const flushProse = () => {
        if (prose.length) out.push("<p>" + prose.join("<br>") + "</p>");
        prose = [];
      };
      const flushPre = () => {
        if (pre.length) out.push("<pre>" + esc(pre.join("\n")) + "</pre>");
        pre = [];
      };
      para.split("\n").forEach((line) => {
        if (/^\s{2,}\S/.test(line)) {
          flushProse();
          pre.push(line.replace(/^\s+/, ""));
          return;
        }
        flushPre();
        // "Sentence.  fn(x) -> y" : the trailing example gets its own code line
        const ex = line.match(/^(.*?\S)\s{2,}(\S.*->.*)$/);
        if (ex) {
          prose.push(inline(ex[1].trim()));
          flushProse();
          out.push("<pre>" + esc(ex[2].trim()) + "</pre>");
          return;
        }
        const prev = prose[prose.length - 1];
        // a wrapped sentence continues the previous line; a finished one starts a new line
        if (prev !== undefined && !/[.?!:)\]]$|-&gt;/.test(prev.trim())) prose[prose.length - 1] = prev + " " + inline(line.trim());
        else prose.push(inline(line.trim()));
      });
      flushProse();
      flushPre();
    });
    return out.join("");
  }

  function toast(msg) {
    const t = $("#toast");
    t.textContent = msg;
    t.hidden = false;
    clearTimeout(toast.timer);
    toast.timer = setTimeout(() => (t.hidden = true), 2600);
  }

  // ---------------------------------------------------------------- top bar
  function renderTop(item) {
    const level = Math.floor(state.xp / XP_PER_LEVEL) + 1;
    const into = state.xp % XP_PER_LEVEL;
    $("#level").innerHTML =
      "<span>Level <b>" + level + "</b></span><div class='bar'><i style='width:" + (into / XP_PER_LEVEL) * 100 + "%'></i></div><span>" + state.xp + " XP</span>";
    const s = streak();
    const el = $("#streak");
    el.textContent = s + " day streak";
    el.classList.toggle("cold", s === 0);
    const crumb = $("#crumb");
    if (!item) {
      crumb.hidden = true;
      return;
    }
    const mod = moduleOf[item.id];
    const idx = mod.items.indexOf(item) + 1;
    crumb.hidden = false;
    crumb.innerHTML = "<b>" + mod.num + " " + esc(mod.title) + "</b> &nbsp;·&nbsp; " + idx + " of " + mod.items.length + " &nbsp;▾";
  }

  // ---------------------------------------------------------------- dashboard
  function renderDash() {
    destroyEditor();
    renderTop(null);
    const total = flat.length;
    const done = flat.filter((i) => isDone(i.id)).length;
    const next = nextUndone(flat);
    const drills = flat.filter((i) => i.kind === "drill");
    const probs = flat.filter((i) => i.kind === "problem");
    const cnt = (list) => list.filter((i) => isDone(i.id)).length;

    const mods = modules
      .map((m) => {
        const d = m.items.filter((i) => i.kind === "drill");
        const p = m.items.filter((i) => i.kind === "problem");
        const dn = cnt(m.items);
        const all = dn === m.items.length;
        const target = nextUndone(m.items) || m.items[0];
        return (
          '<a class="mod' + (all ? " done" : "") + '" href="' + href(target) + '">' +
          '<div class="num">' + (all ? "✓" : m.num) + "</div>" +
          "<div><h3>" + esc(m.title) + "</h3>" +
          '<div class="bar green"><i style="width:' + (dn / m.items.length) * 100 + '%"></i></div>' +
          '<div class="meta"><span>' + cnt(d) + "/" + d.length + " drills</span>" +
          (p.length ? "<span>" + cnt(p) + "/" + p.length + " problems</span>" : "") + "</div></div>" +
          '<div class="go">' + (all ? "Review" : dn ? "Continue" : "Start") + " →</div></a>"
        );
      })
      .join("");

    $("#main").innerHTML =
      '<div class="dash"><div class="dash-inner">' +
      '<div class="hero"><div class="next">' +
      (next
        ? '<div class="label">Up next</div><h1>' + esc(next.title) + "</h1><p>" +
          moduleOf[next.id].num + " " + esc(moduleOf[next.id].title) + " · " + label(next) + "</p>"
        : '<div class="label">Course complete</div><h1>Every item is done</h1><p>Redo drills from a blank editor to keep them sharp.</p>') +
      "</div>" +
      (next ? '<a class="btn primary" href="' + href(next) + '">' + (done ? "Continue" : "Start learning") + "</a>" : "") +
      "</div>" +
      '<div class="tiles">' +
      "<div class='tile'><small>Completed</small><b>" + done + "</b> <span class='note'>/ " + total + "</span></div>" +
      "<div class='tile'><small>Drills</small><b>" + cnt(drills) + "</b> <span class='note'>/ " + drills.length + "</span></div>" +
      "<div class='tile'><small>Problems</small><b>" + cnt(probs) + "</b> <span class='note'>/ " + probs.length + "</span></div>" +
      "<div class='tile'><small>Streak</small><b>" + streak() + "</b> <span class='note'>days</span></div>" +
      "</div>" +
      '<h2 class="sec">Python for DSA, NeetCode order</h2><div class="mods">' + mods + "</div>" +
      '<div class="foot"><span>Progress is saved in this browser.</span>' +
      '<button class="btn ghost" id="export">Export progress</button>' +
      '<button class="btn ghost" id="import">Import</button>' +
      '<button class="btn ghost" id="reset">Reset</button>' +
      '<input type="file" id="import-file" accept="application/json" hidden></div>' +
      "</div></div>";

    $("#export").onclick = exportProgress;
    $("#import").onclick = () => $("#import-file").click();
    $("#import-file").onchange = importProgress;
    $("#reset").onclick = () => {
      if (!confirm("Erase all progress, XP, and saved code in this browser? This cannot be undone.")) return;
      Object.keys(localStorage).filter((k) => k.startsWith("godcode:")).forEach((k) => localStorage.removeItem(k));
      load();
      importRepoWork(true);
      renderDash();
    };
  }

  function exportProgress() {
    const dump = {};
    Object.keys(localStorage).filter((k) => k.startsWith("godcode:")).forEach((k) => (dump[k] = localStorage.getItem(k)));
    const a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([JSON.stringify(dump, null, 1)], { type: "application/json" }));
    a.download = "godcode-progress-" + today() + ".json";
    a.click();
    URL.revokeObjectURL(a.href);
  }
  async function importProgress(e) {
    const file = e.target.files[0];
    if (!file) return;
    try {
      const dump = JSON.parse(await file.text());
      Object.keys(dump).filter((k) => k.startsWith("godcode:")).forEach((k) => localStorage.setItem(k, dump[k]));
      load();
      renderDash();
      toast("Progress imported");
    } catch (err) {
      toast("That file is not a godCode export");
    }
  }

  // ---------------------------------------------------------------- lesson
  function bottomBar(item, middle) {
    const i = flat.indexOf(item);
    const prev = flat[i - 1];
    const next = flat[i + 1];
    return (
      '<div class="bottom">' +
      (prev ? '<a class="btn ghost" href="' + href(prev) + '">← Previous</a>' : "") +
      '<div class="grow"></div>' + middle +
      (next
        ? '<a class="btn ' + (isDone(item.id) ? "good" : "ghost") + '" id="next" href="' + href(next) + '">Next →</a>'
        : '<a class="btn ghost" id="next" href="#/">Finish</a>') +
      "</div>"
    );
  }

  function renderLesson(item) {
    destroyEditor();
    renderTop(item);
    const done = isDone(item.id);
    $("#main").innerHTML =
      '<div class="reading"><div class="md">' + marked.parse(item.md) + "</div></div>" +
      bottomBar(item, done ? "" : '<button class="btn primary" id="read">Mark as read  +' + XP.lesson + " XP</button>");
    highlight($(".md"));
    const btn = $("#read");
    if (btn)
      btn.onclick = () => {
        const xp = complete(item);
        toast("+" + xp + " XP");
        const next = flat[flat.indexOf(item) + 1];
        location.hash = next ? href(next) : "#/";
      };
  }

  // ---------------------------------------------------------------- exercise
  function destroyEditor() {
    if (editor) editor.toTextArea && editor.getWrapperElement().remove();
    editor = null;
  }

  function leftPane(item) {
    const done = isDone(item.id);
    let h = '<div class="kicker">';
    h += item.kind === "drill"
      ? '<span class="tag drill">Drill ' + item.n + "</span><span>" + esc(item.section) + "</span>"
      : '<span class="tag problem">' + esc(item.level) + " problem</span><span>" + esc(item.topic) + "</span>";
    h += '<span class="tag done" id="done-tag"' + (done ? "" : " hidden") + ">Completed</span></div>";
    h += '<h1 class="' + (item.kind === "drill" ? "fn" : "") + '">' + esc(item.title) + "</h1>";
    h += '<div class="prompt">' + renderPrompt(item.prompt) + "</div>";
    const examples = item.examples || item.tests.slice(0, 3).map((t) => t.call + "  ->  " + t.expected).join("\n");
    h += "<h4>Examples</h4>" + codeBlock(examples);
    if (item.hint) h += "<details><summary>Hint (only peek if you are stuck)</summary><div class='prompt'>" + renderPrompt(item.hint) + "</div></details>";
    h += '<details id="sol"><summary>Reference solution</summary><div id="sol-body"></div></details>';
    h += '<p class="note" style="margin-top:18px">' + item.tests.length + " test cases. <b>Run</b> tries the first one and shows anything you print. <b>Submit</b> checks them all.</p>";
    return h;
  }

  function showSolution(item) {
    const body = $("#sol-body");
    body.innerHTML =
      (item.solutionNote ? '<p class="note">' + esc(item.solutionNote) + "</p>" : "") + codeBlock(item.solution);
    highlight(body);
  }

  function renderExercise(item) {
    destroyEditor();
    renderTop(item);
    const mac = /Mac/.test(navigator.platform);
    const mod = mac ? "⌘" : "Ctrl ";
    $("#main").innerHTML =
      '<div class="ws" id="ws">' +
      '<section class="left">' + leftPane(item) + "</section>" +
      '<div class="divider" id="divider"></div>' +
      '<section class="right">' +
      '<div class="pane-head"><span>solution.py</span><div class="grow"></div><button class="link" id="reset-code">Reset to starter</button></div>' +
      '<div class="editor" id="editor"></div>' +
      '<div class="pane-head"><span>Results</span></div>' +
      '<div class="console" id="console"><div class="idle">Write your answer above, then Run or Submit.</div></div>' +
      "</section></div>" +
      bottomBar(
        item,
        '<button class="btn" id="run">Run<kbd>' + mod + '↵</kbd></button><button class="btn primary" id="submit">Submit<kbd>' + mod + "⇧↵</kbd></button>"
      );
    highlight($(".left"));

    const split = localStorage.getItem("godcode:split");
    if (split) $("#ws").style.setProperty("--split", split);

    const initial = savedCode(item.id) ?? item.existing ?? item.draft ?? item.starter;
    editor = CodeMirror($("#editor"), {
      value: initial,
      mode: "python",
      lineNumbers: true,
      indentUnit: 4,
      tabSize: 4,
      matchBrackets: true,
      autoCloseBrackets: true,
      extraKeys: {
        Tab: (cm) => (cm.somethingSelected() ? cm.indentSelection("add") : cm.replaceSelection("    ", "end")),
        "Shift-Tab": (cm) => cm.indentSelection("subtract"),
        "Cmd-/": "toggleComment",
        "Ctrl-/": "toggleComment",
        "Cmd-Enter": () => run(item, false),
        "Ctrl-Enter": () => run(item, false),
        "Shift-Cmd-Enter": () => run(item, true),
        "Shift-Ctrl-Enter": () => run(item, true),
      },
    });
    editor.on("change", () => saveCode(item.id, editor.getValue()));
    setTimeout(() => editor && editor.refresh(), 0);

    $("#run").onclick = () => run(item, false);
    $("#submit").onclick = () => run(item, true);
    $("#reset-code").onclick = () => {
      if (editor.getValue() !== item.starter && !confirm("Replace your code with the starter?")) return;
      editor.setValue(item.starter);
    };
    $("#sol").addEventListener("toggle", (e) => {
      const d = e.currentTarget;
      if (!d.open || $("#sol-body").innerHTML) return;
      if (!isDone(item.id) && !state.peeked[item.id]) {
        if (!confirm("Peeking before you solve it halves the XP for this one. A hint or one more attempt usually teaches more. Show it anyway?")) {
          d.open = false;
          return;
        }
        state.peeked[item.id] = true;
        save();
      }
      showSolution(item);
    });
    dragDivider();
  }

  function dragDivider() {
    const div = $("#divider");
    const ws = $("#ws");
    div.onpointerdown = (e) => {
      div.setPointerCapture(e.pointerId);
      div.classList.add("drag");
      div.onpointermove = (ev) => {
        const pct = Math.min(70, Math.max(25, (ev.clientX / ws.clientWidth) * 100)) + "%";
        ws.style.setProperty("--split", pct);
      };
      div.onpointerup = () => {
        div.classList.remove("drag");
        div.onpointermove = null;
        try {
          localStorage.setItem("godcode:split", ws.style.getPropertyValue("--split"));
        } catch (err) {}
        editor && editor.refresh();
      };
    };
  }

  function caseHtml(r) {
    const mark = { pass: "✓", fail: "✗", error: "✗", todo: "·" }[r.status];
    let h = '<div class="case ' + r.status + '">' + mark + " " + esc(r.call);
    if (r.status === "fail") h += '<div class="detail"><em>got</em>' + esc(r.got) + "\n<em>expected</em>" + esc(r.expected) + "</div>";
    if (r.status === "error") h += '<div class="detail">' + esc(r.error) + "</div>";
    return h + "</div>";
  }

  async function run(item, submit) {
    if (busy || !editor) return;
    busy = true;
    const out = $("#console");
    $("#run").disabled = $("#submit").disabled = true;
    out.innerHTML = '<div class="idle">' + ($("#py").classList.contains("ready") ? "Running…" : "Loading Python, first run takes a few seconds…") + "</div>";
    const report = await Runner.grade(item, editor.getValue(), submit ? {} : { limit: 1 });
    busy = false;
    if (!$("#console") || location.hash !== href(item)) return; // navigated away mid-run
    $("#run").disabled = $("#submit").disabled = false;

    let h = "";
    const passed = report.results.filter((r) => r.status === "pass").length;
    if (report.error) {
      h += '<div class="banner fail">Your code did not run</div><div class="case error">' + esc(report.error) + "</div>";
    } else if (report.status === "todo") {
      h += '<div class="banner info">Not started yet. Replace the placeholder body with your code.</div>';
    } else if (submit && report.status === "pass") {
      const xp = complete(item);
      h += '<div class="banner pass">All ' + passed + " tests passed" + (xp ? "  +" + xp + " XP" : "") + "</div>";
      if (xp) toast("+" + xp + " XP");
      $("#done-tag").hidden = false;
      const next = $("#next");
      next.classList.remove("ghost");
      next.classList.add("good");
      renderTop(item);
    } else if (submit) {
      h += '<div class="banner fail">' + passed + " of " + report.results.length + " tests passed</div>";
    } else {
      h += '<div class="banner ' + (report.status === "pass" ? "info" : "fail") + '">' +
        (report.status === "pass" ? "First test passes. Submit to check all " + item.tests.length + "." : "First test does not pass yet") + "</div>";
    }
    if (report.stdout) h += "<h5>Printed output</h5><div class='stdout'>" + esc(report.stdout) + "</div>";
    if (report.status !== "todo") h += report.results.map(caseHtml).join("");
    out.innerHTML = h;
    out.scrollTop = 0;
  }

  // ---------------------------------------------------------------- outline drawer
  function openDrawer(mod, current) {
    const sel = $("#drawer-module");
    sel.innerHTML = modules.map((m) => '<option value="' + m.id + '"' + (m === mod ? " selected" : "") + ">" + m.num + " " + esc(m.title) + "</option>").join("");
    let h = "";
    let section = null;
    mod.items.forEach((i) => {
      const sec = i.kind === "lesson" ? "Start here" : i.kind === "drill" ? i.section : "Problems";
      if (sec !== section) {
        section = sec;
        h += "<h6>" + esc(sec) + "</h6>";
      }
      h +=
        '<a class="row' + (isDone(i.id) ? " done" : "") + (i === current ? " on" : "") + '" href="' + href(i) + '">' +
        '<span class="mark">' + (isDone(i.id) ? "✓" : "○") + '</span><span class="n">' + (i.kind === "lesson" ? "" : i.n) +
        '</span><span class="t">' + esc(i.title) + "</span></a>";
    });
    $("#drawer-list").innerHTML = h;
    $("#drawer").hidden = false;
    const on = $("#drawer-list .on");
    if (on) on.scrollIntoView({ block: "center" });
  }
  function closeDrawer() {
    $("#drawer").hidden = true;
  }

  // ---------------------------------------------------------------- routing
  function currentItem() {
    return byId[decodeURIComponent(location.hash.replace(/^#\//, ""))];
  }
  function route() {
    closeDrawer();
    const item = currentItem();
    if (!item) return renderDash();
    if (item.kind === "lesson") renderLesson(item);
    else renderExercise(item);
  }

  // Work already done in the repo files counts: build.py flags it as "existing".
  function importRepoWork(quiet) {
    let n = 0;
    flat.forEach((i) => {
      if (i.existing && !isDone(i.id)) {
        if (savedCode(i.id) === null) saveCode(i.id, i.existing);
        complete(i, { imported: true });
        n++;
      }
    });
    if (n && !quiet) toast("Imported " + n + " exercises you already solved in the repo");
  }

  async function init() {
    load();
    const data = await (await fetch("content.json", { cache: "no-cache" })).json();
    modules = data.modules;
    modules.forEach((m) =>
      m.items.forEach((i) => {
        flat.push(i);
        byId[i.id] = i;
        moduleOf[i.id] = m;
      })
    );
    importRepoWork(false);

    Runner.onStatus((s) => {
      const el = $("#py");
      el.className = "py " + s;
      el.querySelector("span").textContent = s === "ready" ? "Python ready" : s === "error" ? "Python failed to load" : "Loading Python";
    });
    $("#crumb").onclick = () => {
      const item = currentItem();
      if (item) openDrawer(moduleOf[item.id], item);
    };
    $("#drawer").onclick = (e) => {
      if (e.target.id === "drawer") closeDrawer();
    };
    $("#drawer-close").onclick = closeDrawer;
    $("#drawer-module").onchange = (e) => openDrawer(modules.find((m) => m.id === e.target.value), currentItem());
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closeDrawer();
    });
    window.addEventListener("hashchange", route);
    route();
  }

  init().catch((err) => {
    $("#main").innerHTML = '<div class="boot">Could not load the course. Run <code>python web/build.py</code>, then reload. (' + esc(err.message) + ")</div>";
  });
})();
