xujignya
hahaha
def joiner_badge_traffic(input_files):
    outputs = dict()
    assert "/traffic/badge/raw" in input_files, "Must have /traffic/badge/raw folder in inputs"
    for input_file in input_files["/traffic/badge/raw"]:
        last_dot_index = input_file.name.rfind('.')
        file_extension = input_file.name[last_dot_index:]
        if file_extension not in ('.json', '.bz2'):
            continue
        output_file = "/traffic/badge/enhanced/{}".format(input_file.name)
        outputs[output_file] = ManifestHandler.SingleRun(output_file, {"/traffic/badge/raw": [input_file]})
    return outputs.values()

