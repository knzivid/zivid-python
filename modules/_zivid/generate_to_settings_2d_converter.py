"""This file imports used classes, modules and packages."""
"""This file imports used classes, modules and packages."""
import inspect
from collections import namedtuple
from dataclasses import dataclass
from typing import Tuple
import subprocess
from _zivid.common import (
    _create_class,
    _imports,
    _recursion,
)
import tempfile
from pathlib import Path
import inflection


def start_traverse():
    from _zivid._zivid import Settings2D as InternalSettings
    from zivid import Settings

    data_model = _recursion(InternalSettings, indentation_level=0)
    with tempfile.NamedTemporaryFile(suffix=".py") as temp_file:
        temp_file = Path(temp_file.name)
        raw_text = _imports(internal=False, settings=True)
        raw_text += _create_to_settings_converter(
            data_model, settings_type="Settings2D"
        )

        new_lines = []
        for line in raw_text.splitlines():
            new_lines.append(line[4:])

        temp_file.write_text("\n".join(new_lines))
        print(temp_file.read_text())
        subprocess.check_output((f"black {temp_file}"), shell=True)
        print(temp_file.read_text())
        path_to_settings = (
            Path(__file__).resolve() / ".." / ".." / "zivid" / "settings__3d.py"
        ).resolve()
        path_to_settings.write_text(temp_file.read_text())


def _create_to_settings_converter(node_data, settings_type: str):
    temp_internal_name = "internal_{name}".format(
        name=inflection.underscore(node_data.name)
    )
    nested_converters = [
        _create_to_settings_converter(element, settings_type=settings_type)
        for element in node_data.children
    ]
    nested_converters_string = "\n".join(nested_converters)
    return_class = "zivid.Settings2D{path}".format(
        temp_internal_name=temp_internal_name,
        path=".{path}".format(path=node_data.path,) if node_data.path else "",
    )
    member_convert_logic = ""
    for member in node_data.member_variables:
        member_convert_logic += "{member} = {temp_internal_name}.{member_not_snake_case}.value,".format(
            member=inflection.underscore(member),
            member_not_snake_case=member.lower(),
            temp_internal_name=temp_internal_name,
        )

    child_convert_logic = ""
    for child in node_data.children:
        child_convert_logic += "{child}=_to_{child}({temp_internal_name}.{child_not_snake_case}),".format(
            child=inflection.underscore(child.name),
            child_not_snake_case=child.name.lower(),
            temp_internal_name=temp_internal_name,
        )

    base_class = """
def _to_{target_name}(internal_{target_name}):
    {nested_converters}
    return {return_class}({child_convert_logic} {member_convert_logic})
    
    
""".format(
        target_name=inflection.underscore(node_data.name),
        nested_converters=nested_converters_string,
        return_class=return_class,
        member_convert_logic=member_convert_logic,
        child_convert_logic=child_convert_logic,
    )
    indented_lines = list()
    for line in base_class.splitlines():
        indented_lines.append("    " + line)
    return "\n".join(indented_lines)
