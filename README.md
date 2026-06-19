# SLR Parser

A small command-line SLR syntax analyzer written in Python. The parser reads a
whitespace-separated stream of lexical token names, checks the stream against a
hardcoded SLR parsing table, and prints either an `accept` parse tree or a
descriptive `[reject]` error.


## Requirements

- Python 3
- No third-party packages

## Input Format

Input files contain token names separated by whitespace. The parser does not
read raw source code; it expects source code to have already been tokenized.

Example:

```text
vtype id assign num addsub num semi
```

The parser appends the end-of-input marker `$` internally, so input files should
not include `$`.

Supported terminals include:

```text
vtype id num literal character boolstr
assign addsub multdiv comp
semi comma lparen rparen lbrace rbrace
if else while return class
```

## Usage

Run the parser on a token stream:

```bash
python syntax_analyzer.py test/test_accept_1.txt
```

On Windows PowerShell, the same command is:

```powershell
python .\syntax_analyzer.py .\test\test_accept_1.txt
```

Print the SLR ACTION/GOTO table:

```bash
python syntax_analyzer.py --table
```

## Output

For accepted input, the parser prints `accept` followed by an indented parse
tree:

```text
accept
CODE
  VDECL
    vtype  (line 1)
    id  (line 1)
    semi  (line 1)
  CODE
    epsilon
```

For rejected input, it prints the line number, unexpected token, and expected
tokens for the current parser state:

```text
[reject] line 1: unexpected token 'semi'. expected one of: id, lparen, num
```

Unknown tokens are rejected before parsing:

```text
[reject] line 1: unknown token '...' (not a terminal of the grammar)
```

## Grammar Summary

The parser recognizes a compact language grammar with:

- Top-level variable declarations, function declarations, and class declarations
- Variable declarations with optional assignment
- Arithmetic expressions using `addsub`, `multdiv`, parentheses, identifiers,
  and numbers
- Literal, character, and boolean right-hand side values
- Function declarations with optional typed arguments
- Statement blocks containing declarations, assignments, `if`/`else`, and
  `while`
- Required `return` statements in function bodies
- Class bodies containing variable and function declarations

The grammar and parse tables are defined directly in `syntax_analyzer.py` in the
`productions`, `ACTION`, and `GOTO` dictionaries.

## Examples

Accepted variable declaration:

```text
vtype id semi
```

Accepted function declaration:

```text
vtype id lparen rparen lbrace
  vtype id assign literal semi
  vtype id assign character semi
  vtype id assign boolstr semi
  while lparen boolstr comp boolstr rparen lbrace
    id assign lparen num addsub num rparen multdiv id semi
  rbrace
  return id semi
rbrace
```

Rejected expression with a missing operand:

```text
vtype id assign num addsub semi
```

## Running Sample Tests

Run an individual sample:

```bash
python syntax_analyzer.py test/test_accept_1.txt
python syntax_analyzer.py test/test_reject_1.txt
```

Compare output manually with the files in `output/`.

PowerShell loop for all samples:

```powershell
Get-ChildItem .\test\*.txt | ForEach-Object {
    Write-Host "== $($_.Name) =="
    python .\syntax_analyzer.py $_.FullName
}
```

## Notes

- The parse tree uses an epsilon marker to display empty productions.
- Line numbers in errors and parse trees come from the input token stream file.
- The current implementation is table-driven and educational: changing the
  grammar requires updating the productions and SLR ACTION/GOTO tables together.
