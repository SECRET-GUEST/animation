import bpy, os
from pathlib import Path

def img_exists(p):
    """Check if a path exists on disk (handles Blender's // relative paths)."""
    try:
        return Path(bpy.path.abspath(p)).exists()
    except:
        return False

report = []
missing_imgs = []

# Collect all images that are missing on disk
for img in bpy.data.images:
    path = img.filepath or img.filepath_raw
    ok = img_exists(path) if path else False
    if not ok:
        missing_imgs.append(img)

def find_users(image):
    """Find all nodes (Materials, World, Compositor) that use a given image datablock."""
    users = []
    # Materials
    for mat in bpy.data.materials:
        if not mat.node_tree:
            continue
        for n in mat.node_tree.nodes:
            if n.type == 'TEX_IMAGE' and n.image == image:
                users.append(("MATERIAL", mat.name, n.name))
    # World
    for world in bpy.data.worlds:
        nt = world.node_tree
        if not nt:
            continue
        for n in nt.nodes:
            if n.type == 'TEX_IMAGE' and n.image == image:
                users.append(("WORLD", world.name, n.name))
    # Compositor
    for sc in bpy.data.scenes:
        nt = sc.node_tree
        if not nt:
            continue
        for n in nt.nodes:
            if n.type == 'IMAGE' and getattr(n, "image", None) == image:
                users.append(("COMPOSITOR", sc.name, n.name))
    return users

# Build the report
for img in missing_imgs:
    p = img.filepath or img.filepath_raw
    users = find_users(img)
    report.append(f"\n[MISSING] {img.name} -> {p}")
    if not users:
        report.append("  (no user found — probably harmless)")
    else:
        for kind, owner, node in users:
            report.append(f"  - {kind}: {owner}  | node: {node}")

# Write the report next to the .blend file
out = Path(bpy.path.abspath("//")) / "missing_image_users.txt"
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print(f"Done. Report written to: {out}")
