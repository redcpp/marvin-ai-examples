import ast
import math
import operator
import random

from simpleeval import SimpleEval, safe_power

from marvin.plugins import Plugin

math_functions = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "sqrt": math.sqrt,
    "ln": math.log,
    "log": math.log10,
    "abs": operator.abs,
    "e": math.e,
    "pi": math.pi,
    "π": math.pi,
    "random": lambda a=0, b=1: a + (b - a) * random.random(),
    "randint": random.randint,
    "min": min,
    "max": max,
    "len": len,
}

_calculator = SimpleEval(functions=math_functions)
_calculator.operators[ast.BitXor] = safe_power

class MyCalculator(Plugin):
    name: str = "mycalculator"
    description: str = (
        "Compute arithmetic expressions. Expressions can ONLY include operators,"
        f" numbers, and the functions {', '.join(math_functions)}; not strings or"
        " units."
    )

    async def run(self, expression: str) -> str:
        return eval(expression)