![Blender](https://img.shields.io/badge/Blender-4.5-orange?\&logo=blender)

```markdown
██████╗ ██╗ ██████╗     ██████╗ ███████╗███╗   ██╗ █████╗ ███╗   ███╗███████╗██████╗ 
██╔══██╗██║██╔════╝     ██╔══██╗██╔════╝████╗  ██║██╔══██╗████╗ ████║██╔════╝██╔══██╗
██████╔╝██║██║  ███╗    ██████╔╝█████╗  ██╔██╗ ██║███████║██╔████╔██║█████╗  ██████╔╝
██╔══██╗██║██║   ██║    ██╔══██╗██╔══╝  ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██║  ██║██║╚██████╔╝    ██║  ██║███████╗██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═╝  ╚═╝╚═╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
```

## Mixamo rig renamer

![1](https://github.com/user-attachments/assets/e4999c9c-d36e-42af-937c-8200084ecebb)

This script automatically renames **Mixamo rigs** inside Blender to use the standard
`.L / .R` naming convention.

Why? Because Blender’s mirror tools (`Ctrl+Shift+V` for mirrored pose paste,
X-Axis Mirror in Pose Mode, animation mirroring, etc.) **only work** when bones
are properly suffixed `.L` and `.R`.

Mixamo rigs use names like `mixamorig:LeftArm` / `mixamorig:RightArm`, which Blender
does not recognize as symmetrical pairs.

This script fixes that in **one click** (bones + vertex groups).

---

## ✨ Features

* Renames **all bones** from `LeftArm` → `Arm.L`, `RightArm` → `Arm.R`
* Updates **vertex groups** automatically to match the new bone names
* Keeps the `mixamorig:` prefix intact for compatibility
* Works with **any Mixamo skeleton** imported into Blender
* Compatible with Blender **4.5+**

---

## 📦 Prerequisites

* **Blender 4.5** or later 
* Basic knowledge of running scripts in Blender’s **Text Editor** or **Scripting tab**
* A Mixamo rig imported into Blender

---

## ⚙️ Installation

1. Open Blender.
2. Import your Mixamo character (FBX).
3. Switch to the **Scripting** workspace.
4. Create a new text block and paste the script.
5. Press **Run Script**.

---

## 🚀 Usage

* Select your **Armature** in the viewport.
* Run the script.
* All bones + vertex groups will be renamed in seconds.
* Now you can use Blender’s **mirroring tools**:

  * `Ctrl+C` → Copy pose
  * `Ctrl+Shift+V` → Paste mirrored pose
  * Works in **animation keyframes** as well.

