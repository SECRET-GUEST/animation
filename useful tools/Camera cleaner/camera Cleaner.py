import bpy

"""
⚠️ IMPORTANT:
- This does NOT touch animation keyframes (camera motion paths remain intact).
- Safe to run after motion tracking to clean up unwanted video overlays.
"""

# 1) Remove background images from all cameras
for cam_obj in [o for o in bpy.data.objects if o.type == 'CAMERA']:
    cam_data = cam_obj.data
    if hasattr(cam_data, "show_background_images"):
        cam_data.show_background_images = False
    if hasattr(cam_data, "background_images"):
        cam_data.background_images.clear()

# 2) Clear the Active Clip (motion tracking video) from all scenes
for sc in bpy.data.scenes:
    if hasattr(sc, "active_clip"):
        sc.active_clip = None

# 3) Disable Sequencer and Compositing (they can also force video overlays)
for sc in bpy.data.scenes:
    sc.render.use_sequencer = False
    sc.use_nodes = False

# 4) Hide objects parented to cameras (movie planes created by "Setup Tracking Scene")
for obj in bpy.data.objects:
    if obj.parent and obj.parent.type == 'CAMERA':
        obj.hide_viewport = True
        obj.hide_render = True

print("Camera cleanup complete: backgrounds cleared, active_clip removed, child movie planes hidden.")
