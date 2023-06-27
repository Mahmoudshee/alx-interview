import importlib.util

# Dynamically import the pascal_triangle module
module_name = "0-pascal_triangle"
module_spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)
pascal_triangle = module.pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)

