#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


# ====================================================================
# 1) 생성 규칙 (productions)  -  규칙 번호는 reduce 동작이 참조한다.
# ====================================================================
productions = {
     0: ("CODE'", ["CODE"]),
     1: ("CODE", ["VDECL", "CODE"]),
     2: ("CODE", ["FDECL", "CODE"]),
     3: ("CODE", ["CDECL", "CODE"]),
     4: ("CODE", []),
     5: ("VDECL", ["vtype", "id", "semi"]),
     6: ("VDECL", ["vtype", "ASSIGN", "semi"]),
     7: ("ASSIGN", ["id", "assign", "RHS"]),
     8: ("RHS", ["EXPR"]),
     9: ("RHS", ["literal"]),
    10: ("RHS", ["character"]),
    11: ("RHS", ["boolstr"]),
    12: ("EXPR", ["EXPR", "addsub", "TERM"]),
    13: ("EXPR", ["TERM"]),
    14: ("TERM", ["TERM", "multdiv", "FACTOR"]),
    15: ("TERM", ["FACTOR"]),
    16: ("FACTOR", ["lparen", "EXPR", "rparen"]),
    17: ("FACTOR", ["id"]),
    18: ("FACTOR", ["num"]),
    19: ("FDECL", ["vtype", "id", "lparen", "ARG", "rparen", "lbrace", "BLOCK", "RETURN", "rbrace"]),
    20: ("ARG", ["vtype", "id", "MOREARGS"]),
    21: ("ARG", []),
    22: ("MOREARGS", ["comma", "vtype", "id", "MOREARGS"]),
    23: ("MOREARGS", []),
    24: ("BLOCK", ["STMT", "BLOCK"]),
    25: ("BLOCK", []),
    26: ("STMT", ["VDECL"]),
    27: ("STMT", ["ASSIGN", "semi"]),
    28: ("STMT", ["if", "lparen", "COND", "rparen", "lbrace", "BLOCK", "rbrace", "ELSE"]),
    29: ("STMT", ["while", "lparen", "COND", "rparen", "lbrace", "BLOCK", "rbrace"]),
    30: ("COND", ["COND", "comp", "boolstr"]),
    31: ("COND", ["boolstr"]),
    32: ("ELSE", ["else", "lbrace", "BLOCK", "rbrace"]),
    33: ("ELSE", []),
    34: ("RETURN", ["return", "RHS", "semi"]),
    35: ("CDECL", ["class", "id", "lbrace", "ODECL", "rbrace"]),
    36: ("ODECL", ["VDECL", "ODECL"]),
    37: ("ODECL", ["FDECL", "ODECL"]),
    38: ("ODECL", []),
}


# ====================================================================
# 2) ACTION 표  (state, terminal) -> 동작   [jsmachines 로 구성 후 기록]
# ====================================================================
ACTION = {
    # state 0
    (0, "vtype"): ("shift", 5), (0, "class"): ("shift", 6), (0, "$"): ("reduce", 4),
    # state 1
    (1, "$"): ("accept",),
    # state 2
    (2, "vtype"): ("shift", 5), (2, "class"): ("shift", 6), (2, "$"): ("reduce", 4),
    # state 3
    (3, "vtype"): ("shift", 5), (3, "class"): ("shift", 6), (3, "$"): ("reduce", 4),
    # state 4
    (4, "vtype"): ("shift", 5), (4, "class"): ("shift", 6), (4, "$"): ("reduce", 4),
    # state 5
    (5, "id"): ("shift", 10),
    # state 6
    (6, "id"): ("shift", 12),
    # state 7
    (7, "$"): ("reduce", 1),
    # state 8
    (8, "$"): ("reduce", 2),
    # state 9
    (9, "$"): ("reduce", 3),
    # state 10
    (10, "assign"): ("shift", 14), (10, "semi"): ("shift", 13), (10, "lparen"): ("shift", 15),
    # state 11
    (11, "semi"): ("shift", 16),
    # state 12
    (12, "lbrace"): ("shift", 17),
    # state 13
    (13, "vtype"): ("reduce", 5), (13, "id"): ("reduce", 5), (13, "rbrace"): ("reduce", 5), (13, "if"): ("reduce", 5), (13, "while"): ("reduce", 5), (13, "return"): ("reduce", 5), (13, "class"): ("reduce", 5), (13, "$"): ("reduce", 5),
    # state 14
    (14, "id"): ("shift", 26), (14, "num"): ("shift", 27), (14, "literal"): ("shift", 20), (14, "character"): ("shift", 21), (14, "boolstr"): ("shift", 22), (14, "lparen"): ("shift", 25),
    # state 15
    (15, "vtype"): ("shift", 29), (15, "rparen"): ("reduce", 21),
    # state 16
    (16, "vtype"): ("reduce", 6), (16, "id"): ("reduce", 6), (16, "rbrace"): ("reduce", 6), (16, "if"): ("reduce", 6), (16, "while"): ("reduce", 6), (16, "return"): ("reduce", 6), (16, "class"): ("reduce", 6), (16, "$"): ("reduce", 6),
    # state 17
    (17, "vtype"): ("shift", 5), (17, "rbrace"): ("reduce", 38),
    # state 18
    (18, "semi"): ("reduce", 7),
    # state 19
    (19, "addsub"): ("shift", 33), (19, "semi"): ("reduce", 8),
    # state 20
    (20, "semi"): ("reduce", 9),
    # state 21
    (21, "semi"): ("reduce", 10),
    # state 22
    (22, "semi"): ("reduce", 11),
    # state 23
    (23, "addsub"): ("reduce", 13), (23, "multdiv"): ("shift", 34), (23, "semi"): ("reduce", 13), (23, "rparen"): ("reduce", 13),
    # state 24
    (24, "addsub"): ("reduce", 15), (24, "multdiv"): ("reduce", 15), (24, "semi"): ("reduce", 15), (24, "rparen"): ("reduce", 15),
    # state 25
    (25, "id"): ("shift", 26), (25, "num"): ("shift", 27), (25, "lparen"): ("shift", 25),
    # state 26
    (26, "addsub"): ("reduce", 17), (26, "multdiv"): ("reduce", 17), (26, "semi"): ("reduce", 17), (26, "rparen"): ("reduce", 17),
    # state 27
    (27, "addsub"): ("reduce", 18), (27, "multdiv"): ("reduce", 18), (27, "semi"): ("reduce", 18), (27, "rparen"): ("reduce", 18),
    # state 28
    (28, "rparen"): ("shift", 36),
    # state 29
    (29, "id"): ("shift", 37),
    # state 30
    (30, "rbrace"): ("shift", 38),
    # state 31
    (31, "vtype"): ("shift", 5), (31, "rbrace"): ("reduce", 38),
    # state 32
    (32, "vtype"): ("shift", 5), (32, "rbrace"): ("reduce", 38),
    # state 33
    (33, "id"): ("shift", 26), (33, "num"): ("shift", 27), (33, "lparen"): ("shift", 25),
    # state 34
    (34, "id"): ("shift", 26), (34, "num"): ("shift", 27), (34, "lparen"): ("shift", 25),
    # state 35
    (35, "addsub"): ("shift", 33), (35, "rparen"): ("shift", 43),
    # state 36
    (36, "lbrace"): ("shift", 44),
    # state 37
    (37, "comma"): ("shift", 46), (37, "rparen"): ("reduce", 23),
    # state 38
    (38, "vtype"): ("reduce", 35), (38, "class"): ("reduce", 35), (38, "$"): ("reduce", 35),
    # state 39
    (39, "rbrace"): ("reduce", 36),
    # state 40
    (40, "rbrace"): ("reduce", 37),
    # state 41
    (41, "addsub"): ("reduce", 12), (41, "multdiv"): ("shift", 34), (41, "semi"): ("reduce", 12), (41, "rparen"): ("reduce", 12),
    # state 42
    (42, "addsub"): ("reduce", 14), (42, "multdiv"): ("reduce", 14), (42, "semi"): ("reduce", 14), (42, "rparen"): ("reduce", 14),
    # state 43
    (43, "addsub"): ("reduce", 16), (43, "multdiv"): ("reduce", 16), (43, "semi"): ("reduce", 16), (43, "rparen"): ("reduce", 16),
    # state 44
    (44, "vtype"): ("shift", 47), (44, "id"): ("shift", 48), (44, "rbrace"): ("reduce", 25), (44, "if"): ("shift", 53), (44, "while"): ("shift", 54), (44, "return"): ("reduce", 25),
    # state 45
    (45, "rparen"): ("reduce", 20),
    # state 46
    (46, "vtype"): ("shift", 55),
    # state 47
    (47, "id"): ("shift", 56),
    # state 48
    (48, "assign"): ("shift", 14),
    # state 49
    (49, "return"): ("shift", 58),
    # state 50
    (50, "vtype"): ("shift", 47), (50, "id"): ("shift", 48), (50, "rbrace"): ("reduce", 25), (50, "if"): ("shift", 53), (50, "while"): ("shift", 54), (50, "return"): ("reduce", 25),
    # state 51
    (51, "vtype"): ("reduce", 26), (51, "id"): ("reduce", 26), (51, "rbrace"): ("reduce", 26), (51, "if"): ("reduce", 26), (51, "while"): ("reduce", 26), (51, "return"): ("reduce", 26),
    # state 52
    (52, "semi"): ("shift", 60),
    # state 53
    (53, "lparen"): ("shift", 61),
    # state 54
    (54, "lparen"): ("shift", 62),
    # state 55
    (55, "id"): ("shift", 63),
    # state 56
    (56, "assign"): ("shift", 14), (56, "semi"): ("shift", 13),
    # state 57
    (57, "rbrace"): ("shift", 64),
    # state 58
    (58, "id"): ("shift", 26), (58, "num"): ("shift", 27), (58, "literal"): ("shift", 20), (58, "character"): ("shift", 21), (58, "boolstr"): ("shift", 22), (58, "lparen"): ("shift", 25),
    # state 59
    (59, "rbrace"): ("reduce", 24), (59, "return"): ("reduce", 24),
    # state 60
    (60, "vtype"): ("reduce", 27), (60, "id"): ("reduce", 27), (60, "rbrace"): ("reduce", 27), (60, "if"): ("reduce", 27), (60, "while"): ("reduce", 27), (60, "return"): ("reduce", 27),
    # state 61
    (61, "boolstr"): ("shift", 67),
    # state 62
    (62, "boolstr"): ("shift", 67),
    # state 63
    (63, "comma"): ("shift", 46), (63, "rparen"): ("reduce", 23),
    # state 64
    (64, "vtype"): ("reduce", 19), (64, "rbrace"): ("reduce", 19), (64, "class"): ("reduce", 19), (64, "$"): ("reduce", 19),
    # state 65
    (65, "semi"): ("shift", 70),
    # state 66
    (66, "comp"): ("shift", 72), (66, "rparen"): ("shift", 71),
    # state 67
    (67, "comp"): ("reduce", 31), (67, "rparen"): ("reduce", 31),
    # state 68
    (68, "comp"): ("shift", 72), (68, "rparen"): ("shift", 73),
    # state 69
    (69, "rparen"): ("reduce", 22),
    # state 70
    (70, "rbrace"): ("reduce", 34),
    # state 71
    (71, "lbrace"): ("shift", 74),
    # state 72
    (72, "boolstr"): ("shift", 75),
    # state 73
    (73, "lbrace"): ("shift", 76),
    # state 74
    (74, "vtype"): ("shift", 47), (74, "id"): ("shift", 48), (74, "rbrace"): ("reduce", 25), (74, "if"): ("shift", 53), (74, "while"): ("shift", 54), (74, "return"): ("reduce", 25),
    # state 75
    (75, "comp"): ("reduce", 30), (75, "rparen"): ("reduce", 30),
    # state 76
    (76, "vtype"): ("shift", 47), (76, "id"): ("shift", 48), (76, "rbrace"): ("reduce", 25), (76, "if"): ("shift", 53), (76, "while"): ("shift", 54), (76, "return"): ("reduce", 25),
    # state 77
    (77, "rbrace"): ("shift", 79),
    # state 78
    (78, "rbrace"): ("shift", 80),
    # state 79
    (79, "vtype"): ("reduce", 33), (79, "id"): ("reduce", 33), (79, "rbrace"): ("reduce", 33), (79, "if"): ("reduce", 33), (79, "else"): ("shift", 82), (79, "while"): ("reduce", 33), (79, "return"): ("reduce", 33),
    # state 80
    (80, "vtype"): ("reduce", 29), (80, "id"): ("reduce", 29), (80, "rbrace"): ("reduce", 29), (80, "if"): ("reduce", 29), (80, "while"): ("reduce", 29), (80, "return"): ("reduce", 29),
    # state 81
    (81, "vtype"): ("reduce", 28), (81, "id"): ("reduce", 28), (81, "rbrace"): ("reduce", 28), (81, "if"): ("reduce", 28), (81, "while"): ("reduce", 28), (81, "return"): ("reduce", 28),
    # state 82
    (82, "lbrace"): ("shift", 83),
    # state 83
    (83, "vtype"): ("shift", 47), (83, "id"): ("shift", 48), (83, "rbrace"): ("reduce", 25), (83, "if"): ("shift", 53), (83, "while"): ("shift", 54), (83, "return"): ("reduce", 25),
    # state 84
    (84, "rbrace"): ("shift", 85),
    # state 85
    (85, "vtype"): ("reduce", 32), (85, "id"): ("reduce", 32), (85, "rbrace"): ("reduce", 32), (85, "if"): ("reduce", 32), (85, "while"): ("reduce", 32), (85, "return"): ("reduce", 32),
}


# ====================================================================
# 3) GOTO 표  (state, nonterminal) -> 다음 상태
# ====================================================================
GOTO = {
    # state 0
    (0, "CODE"): 1, (0, "VDECL"): 2, (0, "FDECL"): 3, (0, "CDECL"): 4,
    # state 2
    (2, "CODE"): 7, (2, "VDECL"): 2, (2, "FDECL"): 3, (2, "CDECL"): 4,
    # state 3
    (3, "CODE"): 8, (3, "VDECL"): 2, (3, "FDECL"): 3, (3, "CDECL"): 4,
    # state 4
    (4, "CODE"): 9, (4, "VDECL"): 2, (4, "FDECL"): 3, (4, "CDECL"): 4,
    # state 5
    (5, "ASSIGN"): 11,
    # state 14
    (14, "RHS"): 18, (14, "EXPR"): 19, (14, "TERM"): 23, (14, "FACTOR"): 24,
    # state 15
    (15, "ARG"): 28,
    # state 17
    (17, "VDECL"): 31, (17, "FDECL"): 32, (17, "ODECL"): 30,
    # state 25
    (25, "EXPR"): 35, (25, "TERM"): 23, (25, "FACTOR"): 24,
    # state 31
    (31, "VDECL"): 31, (31, "FDECL"): 32, (31, "ODECL"): 39,
    # state 32
    (32, "VDECL"): 31, (32, "FDECL"): 32, (32, "ODECL"): 40,
    # state 33
    (33, "TERM"): 41, (33, "FACTOR"): 24,
    # state 34
    (34, "FACTOR"): 42,
    # state 37
    (37, "MOREARGS"): 45,
    # state 44
    (44, "VDECL"): 51, (44, "ASSIGN"): 52, (44, "BLOCK"): 49, (44, "STMT"): 50,
    # state 47
    (47, "ASSIGN"): 11,
    # state 49
    (49, "RETURN"): 57,
    # state 50
    (50, "VDECL"): 51, (50, "ASSIGN"): 52, (50, "BLOCK"): 59, (50, "STMT"): 50,
    # state 58
    (58, "RHS"): 65, (58, "EXPR"): 19, (58, "TERM"): 23, (58, "FACTOR"): 24,
    # state 61
    (61, "COND"): 66,
    # state 62
    (62, "COND"): 68,
    # state 63
    (63, "MOREARGS"): 69,
    # state 74
    (74, "VDECL"): 51, (74, "ASSIGN"): 52, (74, "BLOCK"): 77, (74, "STMT"): 50,
    # state 76
    (76, "VDECL"): 51, (76, "ASSIGN"): 52, (76, "BLOCK"): 78, (76, "STMT"): 50,
    # state 79
    (79, "ELSE"): 81,
    # state 83
    (83, "VDECL"): 51, (83, "ASSIGN"): 52, (83, "BLOCK"): 84, (83, "STMT"): 50,
}

# ====================================================================
# 4) 파서 본체 (위 표만 참조)
# ====================================================================

# 문법에서 터미널/논터미널만 추출. 
nonterminals = {lhs for (lhs, _rhs) in productions.values()}
terminals = {s for (_lhs, rhs) in productions.values() for s in rhs if s not in nonterminals}


class Node:
    """파스 트리 노드 하나."""
    def __init__(self, symbol, line=None):
        self.symbol = symbol          # 터미널 또는 논터미널 이름
        self.children = []            # 자식 노드 리스트
        self.line = line              # 잎(터미널)일 때의 줄 번호

    def __repr__(self):
        return f"Node({self.symbol})"


def read_tokens(path):
    # 입력 파일을 (토큰, 줄번호) 리스트로 읽는다. (끝 표식 '$' 는 여기서 붙이지 않는다.)
    tokens = []
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            for tok in line.split():
                tokens.append((tok, lineno))
    return tokens


def check_unknown_tokens(tokens):
    # 문법에 없는 토큰을 찾는다. 끝 표식 '$' 도 terminals 에 없으므로,
    # 입력 안에 '$' 가 들어 있으면 여기서 함께 걸러진다(조용히 무시되는 것 방지).
    return [(t, ln) for (t, ln) in tokens if t not in terminals]


def parse(tokens):
    # ACTION/GOTO 표를 따라가는 표준 LR 파싱 루프. 성공하면 파스 트리의 뿌리를 돌려준다.
    state_stack = [0]
    node_stack = []
    i = 0
    while True:
        s = state_stack[-1]
        tok, line = tokens[i]
        act = ACTION.get((s, tok))

        if act is None:                                   # 갈 곳이 없으면 reject
            expected = sorted({t for (st, t) in ACTION if st == s})
            exp = ", ".join(expected) if expected else "(none)"
            raise SyntaxError(
                f"[reject] line {line}: unexpected token '{tok}'. expected one of: {exp}")

        kind = act[0]
        if kind == "shift":                               # 토큰을 잎으로 push 하고 상태 이동
            node_stack.append(Node(tok, line))
            state_stack.append(act[1])
            i += 1

        elif kind == "reduce":                            # A -> alpha 로 줄이기
            lhs, rhs = productions[act[1]]
            children = []
            for _ in range(len(rhs)):
                state_stack.pop()
                children.append(node_stack.pop())
            children.reverse()
            parent = Node(lhs)
            parent.children = children if children else [Node("ε")]   # ε 규칙
            node_stack.append(parent)
            g = GOTO.get((state_stack[-1], lhs))
            if g is None:
                raise SyntaxError(
                    f"[reject] line {line}: missing GOTO (state {state_stack[-1]}, {lhs})")
            state_stack.append(g)

        elif kind == "accept":                            # 성공
            return node_stack[-1]


def print_tree(node, depth=0):
    # 파스 트리를 들여쓰기로 출력. 잎(터미널)에는 줄 번호도 같이 보여 준다.
    if node.line is not None:
        print("  " * depth + f"{node.symbol}  (line {node.line})")
    else:
        print("  " * depth + node.symbol)
    for c in node.children:
        print_tree(c, depth + 1)


def dump_table():
    # 파일에 내장된 SLR 표를 사람이 읽기 좋게 출력 (확인용).
    terms = ["vtype", "id", "num", "literal", "character", "boolstr", "assign", "addsub", "multdiv", "comp", "semi", "comma", "lparen", "rparen", "lbrace", "rbrace", "if", "else", "while", "return", "class", "$"]
    nts = ["CODE", "VDECL", "ASSIGN", "RHS", "EXPR", "TERM", "FACTOR", "FDECL",  "ARG", "MOREARGS", "BLOCK", "STMT", "COND", "ELSE", "RETURN", "CDECL", "ODECL"]
    nstates = 1 + max(s for (s, _t) in ACTION)
    for i in range(nstates):
        acts = []
        for t in terms:
            a = ACTION.get((i, t))
            if not a:
                continue
            tag = ("s%d" % a[1]) if a[0] == "shift" else ("r%d" % a[1]) if a[0] == "reduce" else "acc"
            acts.append("%s=%s" % (t, tag))
        gs = ["%s=%d" % (A, GOTO[(i, A)]) for A in nts if (i, A) in GOTO]
        line = "State %3d | ACTION: %s" % (i, "  ".join(acts) if acts else "-")
        if gs:
            line += "   || GOTO: " + "  ".join(gs)
        print(line)


def main():
    # 'ε' 같은 비ASCII 문자를 어떤 환경에서도 출력하도록 표준 출력을 UTF-8 로 맞춘다.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass

    args = sys.argv[1:]
    if args == ["--table"]:
        dump_table()
        return
    if len(args) != 1 or args[0].startswith("--"):
        print("Usage:")
        print("    python3 syntax_analyzer.py <input_file>")
        print("    python3 syntax_analyzer.py --table")
        sys.exit(1)

    # 입력 파일 읽기 — 없는 파일 등은 트레이스백 대신 깔끔한 메시지로 처리
    try:
        raw = read_tokens(args[0])
    except OSError as e:
        print(f"[error] cannot read input file '{args[0]}': {e}")
        sys.exit(1)

    # 문법에 없는 토큰을 먼저 거른다 (입력에 '$' 가 있으면 여기서 걸림)
    bad = check_unknown_tokens(raw)
    if bad:
        t, ln = bad[0]
        print(f"[reject] line {ln}: unknown token '{t}' (not a terminal of the grammar)")
        return

    # 끝 표식 '$' 를 붙여 파싱한다.
    last = raw[-1][1] if raw else 1
    tokens = raw + [("$", last)]
    try:
        root = parse(tokens)
        print("accept")
        print_tree(root)
    except SyntaxError as e:
        print(str(e))


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        # 출력을 head 등으로 자를 때 나는 BrokenPipeError 는 조용히 처리.
        try:
            sys.stdout.close()
        except Exception:
            pass
