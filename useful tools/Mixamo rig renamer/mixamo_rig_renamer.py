import bpy, re

arm = bpy.context.object
assert arm and arm.type == 'ARMATURE', "Select the armature first."

# Find all mesh objects skinned (deformed) by this armature
def skinned_meshes(arm_obj):
    out = []
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            for mod in obj.modifiers:
                if mod.type == 'ARMATURE' and mod.object == arm_obj:
                    out.append(obj)
                    break
    return out

meshes = skinned_meshes(arm)

# Build the renaming mapping:
# Example: mixamorig:LeftForeArm -> mixamorig:ForeArm.L
old2new = {}
pattern = re.compile(r'^(?P<prefix>.*?:)?(?P<side>Left|Right)(?P<base>.+)$')

for b in arm.data.bones:
    m = pattern.match(b.name)
    if m:
        prefix = m.group('prefix') or ''
        side = m.group('side')
        base = m.group('base')
        new = f"{prefix}{base}.{ 'L' if side == 'Left' else 'R' }"
        old2new[b.name] = new

# Rename the bones (this will also update FCurves/poses automatically)
for old, new in old2new.items():
    if old != new and new not in arm.data.bones:
        arm.data.bones[old].name = new

# Rename the corresponding vertex groups on every skinned mesh
for obj in meshes:
    for vg in obj.vertex_groups:
        if vg.name in old2new:
            vg.name = old2new[vg.name]

print("Renaming finished. Examples:", list(old2new.items())[:8])
