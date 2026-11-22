"""Headless check: run every code cell of every notebook with scripted input.

Usage:  python tests/check_notebooks.py [notebooks_dir] [--show]

* `input()` is replaced by a function that answers from the prompt text (see ANSWERS).
* Each notebook runs in its own temporary working directory so file-handling labs leave nothing behind.
* A notebook passes when every code cell runs without an uncaught exception within the time limit.
"""
import builtins, contextlib, glob, io, json, os, signal, sys, tempfile, traceback

ANSWERS = [  # (substring of lower-cased prompt, answer) — first match wins
    ("password", "admin"), ("option", "3"), ("sentence", "Data science rocks"),
    ("matric", "CMP/PGD/001"), ("name", "Aisha"), ("income", "60000"), ("salary", "45000"),
    ("age", "30"), ("(0-100)", "75"), ("add another", "n"),
]
DEFAULT = "5"
TIME_LIMIT = 10


def fake_input(prompt=""):
    p = str(prompt).lower()
    for key, ans in ANSWERS:
        if key in p:
            return ans
    return DEFAULT


class Timeout(Exception):
    pass


def _alarm(signum, frame):
    raise Timeout("cell exceeded time limit")


def run_notebook(path, show=False):
    nb = json.load(open(path, encoding="utf-8"))
    ns = {"__name__": "__main__"}
    cwd = os.getcwd()
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)
        real_input = builtins.input
        builtins.input = fake_input
        try:
            for idx, cell in enumerate(nb["cells"]):
                if cell["cell_type"] != "code":
                    continue
                src = "".join(cell["source"])
                buf = io.StringIO()
                signal.signal(signal.SIGALRM, _alarm)
                signal.alarm(TIME_LIMIT)
                try:
                    with contextlib.redirect_stdout(buf):
                        exec(compile(src, f"{os.path.basename(path)}[cell {idx}]", "exec"), ns)
                except BaseException as exc:  # noqa: BLE001
                    failures.append((idx, f"{type(exc).__name__}: {exc}"))
                finally:
                    signal.alarm(0)
                if show:
                    print(f"--- cell {idx} ---\n{buf.getvalue()}")
        finally:
            builtins.input = real_input
            os.chdir(cwd)
    return failures


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    show = "--show" in sys.argv
    folder = args[0] if args else os.path.join(os.path.dirname(__file__), "..", "notebooks")
    paths = sorted(glob.glob(os.path.join(folder, "*.ipynb")))
    bad = 0
    for p in paths:
        fails = run_notebook(p, show)
        status = "PASS" if not fails else "FAIL"
        print(f"{status}  {os.path.basename(p)}")
        for idx, msg in fails:
            bad += 1
            print(f"      cell {idx}: {msg}")
    print(f"\n{len(paths)} notebooks checked, {bad} failing cell(s)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
