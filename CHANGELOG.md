# Changelog

## 2.0 – 21 November 2026

Revision following a full review of the original course pack.

**New**
- Week 13 (error handling and debugging) and Week 14 (OOP and mini-project) notebooks.
- Mini-project workbook now requires a class, validated input, CSV read **and** write, `assert` tests and an AI-assistance declaration.
- `tests/check_notebooks.py` and a GitHub Actions workflow that run every notebook headlessly.
- Colab badges, `docs/COURSE_ALIGNMENT.md`.

**Corrected**
- Week 8: the memory-view example now matches the code; added step slicing, `sort`/`reverse`/`extend`/`count`/`index`, aliasing versus copying, tuple unpacking.
- Week 9: dictionaries are insertion-ordered (Python ≥ 3.7), not "unordered"; added frequency counting with a dictionary and `Counter`; sets can no longer be mistaken for counters; empty-set pitfall.
- Week 12: `encoding="utf-8"`, the `csv` module, safe parsing, Colab temporary-storage warning, file-mode table.
- Week 4: precedence table fixed (`not` > `and` > `or`), `**` associativity, chained comparisons.
- Week 5: electricity tariff stated unambiguously (flat and marginal versions); Grade D removed from the exercise to match the A/B/C/F scale used in the course.
- Week 10: base case of `factorial` fixed, mutable-default pitfall, `global`, docstrings, default and keyword arguments.
- Weeks 1, 2, 3, 6, 7, 11: bytecode demonstration, flowchart, f-strings and identifiers, complete dry-run table, input-validation loop, reproducible simulation (`seed(42)`), string formatting and a Unicode (Yorùbá) example.
- Removed the leftover "Wait for confirmation before proceeding…" lines.
- Saved outputs cleared so students see clean notebooks.
