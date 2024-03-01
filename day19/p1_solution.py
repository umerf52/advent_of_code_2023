import sys
from ast import literal_eval


def solve(inp, wf):
    while True:
        for items in wf:
            if (
                items[0] is None
                and items[1] is None
                and items[2] is None
                and items[3] is not None
            ):
                if items[3] == "A" or items[3] == "R":
                    return items[3]
                wf = workflows[items[3]]
                if wf == "A" or wf == "R":
                    return wf
                else:
                    wf = workflows[items[3]]
                    break

            compare = inp[items[0]]
            op = items[1]
            value = items[2]
            next_wf = items[3]

            if op == "<":
                if compare < value:
                    if next_wf == "A" or next_wf == "R":
                        return next_wf
                    wf = workflows[next_wf]
                    break
            elif op == ">":
                if compare > value:
                    if next_wf == "A" or next_wf == "R":
                        return next_wf
                    wf = workflows[next_wf]
                    break


file_name = sys.argv[1]

with open(file_name, "r") as file:
    lines = file.readlines()

total = 0
workflows = {}
lines = [line.strip() for line in lines]
for line in lines:
    if line and not line.startswith("{"):  # workflows
        line = line[:-1]  # remove last '}'
        # separate name and rest
        name, rest = line.split("{")
        for i, item in enumerate(rest.split(",")):
            # last item
            if i == len(rest.split(",")) - 1:
                workflows[name] = workflows.get(name, []) + [(None, None, None, item)]
            else:
                condition, next_item = item.split(":")
                operator = "<" if "<" in condition else ">"
                broken = condition.split(operator)
                workflows[name] = workflows.get(name, []) + [
                    (broken[0], operator, int(broken[1]), next_item)
                ]

    elif line and line.startswith("{"):  # inputs
        # add single quotes around keys
        line = (
            line.replace("{", "{'")
            .replace("=", "'=")
            .replace(",", ",'")
            .replace("=", ":")
        )
        evaluated_dict = literal_eval(line)

        if solve(evaluated_dict, workflows["in"]) == "A":
            for v in evaluated_dict.values():
                total += v

print(total)
