import os
import subprocess
import anndata as ad

input_path = meta["resources_dir"] + "/pancreas/unintegrated.h5ad"
output_path = "integrated.h5ad"
cmd = [
    meta['executable'],
    "--input", input_path,
    "--output", output_path
]

print(">> Checking whether input file exists", flush=True)
assert os.path.exists(input_path)

print(">> Running script as test", flush=True)
out = subprocess.run(cmd, stderr=subprocess.STDOUT).stdout
print(out)

print(">> Checking whether file exists", flush=True)
assert os.path.exists(output_path)

print(">> Reading h5ad files", flush=True)
input = ad.read_h5ad(input_path)
output = ad.read_h5ad(output_path)
print(f"input: {input}", flush=True)
print(f"output: {output}", flush=True)

print(">> Checking whether predictions were added", flush=True)
# TODO: use helper function to check whether the required fields are defined
assert output.layers['corrected_counts'] is not None

print(">> Check values", flush=True)
assert meta['functionality_name'] == output.uns['method_id']
assert input.uns["dataset_id"] == output.uns["dataset_id"]

print(">> All tests passed successfully")
