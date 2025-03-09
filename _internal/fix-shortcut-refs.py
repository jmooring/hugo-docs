#!/usr/bin/env python3
"""
fix-shortcut-refs.py

Finds Markdown shortcut reference links and converts them to collapsed
reference links.

  Shortcut:   [label]
  Collapsed:  [label][]

Shortcut reference links are only valid per the CommonMark spec if they are
defined in the same Markdown rendering context. Hugo splits content at
shortcode boundaries, so shortcut links on one side of a shortcode may not
resolve to definitions on the other side.

Usage:
  # Dry run (report only):
  python3 fix-shortcut-refs.py

  # Apply changes:
  python3 fix-shortcut-refs.py --fix

  # Scan a specific directory:
  python3 fix-shortcut-refs.py --dir content/en/docs

Skips:
  - Footnote references ([^label])
  - Image links (![label])
  - Full reference links ([text][label])
  - Double-bracket constructs ([[label]])
  - Content inside fenced code blocks
  - Content inside paired {{< shortcode >}} ... {{< /shortcode >}} blocks
"""

import argparse
import glob
import re
import sys

REF_DEF       = re.compile(r'^\[([^\]]+)\]:', re.MULTILINE)
CODE_FENCE    = re.compile(r'^(`{3,}|~{3,})')
SC_OPEN       = re.compile(r'^\s*{{<\s*([\w][\w-]*)[^>]*>}}\s*$')
SC_CLOSE      = re.compile(r'^\s*{{<\s*/([\w][\w-]*)\s*>}}\s*$')


def get_skip_lines(lines):
    """Return a set of line indices that should not be modified.

    Skips lines inside fenced code blocks and paired block shortcodes.
    """
    # Only skip shortcodes that have a matching close tag (i.e. paired blocks).
    open_names  = {m.group(1) for l in lines for m in [SC_OPEN.match(l)]  if m}
    close_names = {m.group(1) for l in lines for m in [SC_CLOSE.match(l)] if m}
    paired = open_names & close_names

    skip = set()
    stack = []
    in_code = False
    fence_char = None
    fence_len = 0

    for i, line in enumerate(lines):
        if not in_code:
            fm = CODE_FENCE.match(line)
            if fm:
                in_code = True
                fence_char = fm.group(1)[0]
                fence_len = len(fm.group(1))
                skip.add(i)
                continue
        else:
            skip.add(i)
            if re.match(r'^' + re.escape(fence_char) + r'{' + str(fence_len) + r',}\s*$', line):
                in_code = False
            continue

        cm = SC_CLOSE.match(line)
        if cm and stack and stack[-1] == cm.group(1):
            skip.add(i)
            stack.pop()
            continue

        om = SC_OPEN.match(line)
        if om and om.group(1) in paired:
            skip.add(i)
            stack.append(om.group(1))
            continue

        if stack:
            skip.add(i)

    return skip


def process_file(filepath, fix=False):
    """Find (and optionally fix) shortcut reference links in a file.

    Returns a list of (line_number, original_line, new_line) tuples for each
    changed line.
    """
    with open(filepath) as f:
        content = f.read()

    # Collect reference labels, excluding footnotes.
    labels = [l for l in REF_DEF.findall(content) if not l.startswith('^')]
    if not labels:
        return []

    lines = content.split('\n')
    skip = get_skip_lines(lines)
    results = []
    modified_lines = list(lines)

    for i, line in enumerate(lines):
        # Skip protected regions and reference definition lines.
        if i in skip or re.match(r'^\[[^\]]+\]:', line):
            continue

        modified = line
        for label in labels:
            # Negative lookbehind: exclude !, [, ] before the opening bracket.
            #   !  → image links (![label])
            #   [  → double-bracket constructs ([[label]])
            #   ]  → full reference links ([text][label])
            pattern = re.compile(
                r'(?<![!\[\]])\[' + re.escape(label) + r'\](?!\[|\()'
            )
            modified = pattern.sub(f'[{label}][]', modified)

        if modified != line:
            results.append((i + 1, line, modified))
            modified_lines[i] = modified

    if fix and results:
        with open(filepath, 'w') as f:
            f.write('\n'.join(modified_lines))

    return results


def main():
    parser = argparse.ArgumentParser(
        description='Find or fix shortcut reference links in Markdown files.'
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Apply changes in place. Without this flag, only report findings.',
    )
    parser.add_argument(
        '--dir',
        default='content',
        help='Directory to scan (default: content).',
    )
    args = parser.parse_args()

    pattern = f'{args.dir.rstrip("/")}/**/*.md'
    files = sorted(glob.glob(pattern, recursive=True))

    if not files:
        print(f'No .md files found matching: {pattern}', file=sys.stderr)
        sys.exit(1)

    total_files = 0
    total_changes = 0

    for filepath in files:
        changes = process_file(filepath, fix=args.fix)
        if changes:
            total_files += 1
            total_changes += len(changes)
            print(f'\n{filepath}')
            for lineno, original, new in changes:
                print(f'  line {lineno}:')
                print(f'    - {original.strip()}')
                print(f'    + {new.strip()}')

    action = 'Fixed' if args.fix else 'Found'
    print(f'\n{action} {total_changes} shortcut reference link(s) in {total_files} file(s).')
    if not args.fix and total_changes:
        print('Run with --fix to apply changes.')


if __name__ == '__main__':
    main()
