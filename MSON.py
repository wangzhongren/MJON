import json
from typing import Any, List, Tuple, Union


class MJONParser:
    def __init__(self):
        self.lines: List[str] = []
        self.pos = 0

    def parse(self, text: str) -> Any:
        self.lines = [line.rstrip() for line in text.splitlines() if line.strip()]
        self.pos = 0
        return self._parse_block(0)

    def _parse_block(self, indent_level: int) -> Union[dict, list]:
        result = {}
        current_key = None
        array_mode = False
        array_items = []

        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            stripped = line.lstrip()
            indent = len(line) - len(stripped)

            if indent < indent_level:
                break  # End of current block

            if stripped.startswith('@'):
                if array_mode:
                    result[current_key] = array_items
                    array_items = []
                    array_mode = False

                if ':' in stripped:
                    key, val = map(str.strip, stripped[1:].split(':', 1))
                    self.pos += 1
                    if self._peek_indent() > indent:
                        nested = self._parse_block(self._peek_indent())
                        result[key] = nested
                    else:
                        result[key] = self._auto_convert(val)

                    current_key = key
                else:
                    raise ValueError(f"Invalid line format: {line}")

            elif stripped.startswith('*'):
                if not array_mode:
                    array_items = []
                    array_mode = True

                self.pos += 1
                if self._peek_indent() > indent:
                    item = self._parse_block(self._peek_indent())
                    array_items.append(item)
                else:
                    val = stripped[1:].strip()
                    array_items.append(self._auto_convert(val))

            else:
                self.pos += 1  # Skip unknown line format

        if array_mode and current_key:
            result[current_key] = array_items

        return result

    def _peek_indent(self) -> int:
        if self.pos >= len(self.lines):
            return -1
        next_line = self.lines[self.pos]
        return len(next_line) - len(next_line.lstrip())

    def _auto_convert(self, val: str) -> Any:
        if val.lower() in ['true', 'false']:
            return val.lower() == 'true'
        try:
            return int(val)
        except ValueError:
            pass
        try:
            return float(val)
        except ValueError:
            pass
        return val


class MJONGenerator:
    def __init__(self):
        self.lines = []

    def generate(self, obj: Any, indent: int = 0) -> str:
        self.lines = []
        self._write(obj, indent)
        return "\n".join(self.lines)

    def _write(self, obj: Any, indent: int, prefix: str = ''):
        indent_str = '  ' * indent

        if isinstance(obj, dict):
            for key, val in obj.items():
                if isinstance(val, (dict, list)):
                    self.lines.append(f"{indent_str}@{key}:")
                    self._write(val, indent + 1)
                else:
                    self.lines.append(f"{indent_str}@{key}: {val}")
        elif isinstance(obj, list):
            for item in obj:
                if isinstance(item, (dict, list)):
                    self.lines.append(f"{indent_str}*")
                    self._write(item, indent + 1)
                else:
                    self.lines.append(f"{indent_str}* {item}")
        else:
            self.lines.append(f"{indent_str}{prefix}{obj}")


# Example usage (will be excluded in final open-source module):
example_mjon = """
@summary: 用户希望建立简洁的类 JSON 格式
@meta:
  @version: 1.0
  @timestamp: 1716361440
@tags:
  * 压缩
  * 多维结构
  * token优化
@steps:
  *
    @order: 1
    @action: 构建结构化格式
  *
    @order: 2
    @action: 使用 gzip + base64
  *
    @order: 3
    @action: 定义轻量语义协议
"""

parser = MJONParser()
parsed = parser.parse(example_mjon)

generator = MJONGenerator()
generated = generator.generate(parsed)

parsed, generated  # Output both parsed and generated version to confirm correctness
