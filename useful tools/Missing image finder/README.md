
[![STATUS](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()
[![Blender](https://img.shields.io/badge/Blender-4.5-orange.svg)](https://www.blender.org/download/releases/4-5/)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)]()

```
███╗   ███╗██╗███████╗███████╗██╗███╗   ██╗ ██████╗     ██╗███╗   ███╗ █████╗  ██████╗ ███████╗     █████╗ ██╗   ██╗██████╗ ██╗████████╗
████╗ ████║██║██╔════╝██╔════╝██║████╗  ██║██╔════╝     ██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝    ██╔══██╗██║   ██║██╔══██╗██║╚══██╔══╝
██╔████╔██║██║███████╗███████╗██║██╔██╗ ██║██║  ███╗    ██║██╔████╔██║███████║██║  ███╗█████╗      ███████║██║   ██║██║  ██║██║   ██║   
██║╚██╔╝██║██║╚════██║╚════██║██║██║╚██╗██║██║   ██║    ██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝      ██╔══██║██║   ██║██║  ██║██║   ██║   
██║ ╚═╝ ██║██║███████║███████║██║██║ ╚████║╚██████╔╝    ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗    ██║  ██║╚██████╔╝██████╔╝██║   ██║   
╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝   
                                                                                                                                        
```

# Missing Image Audit 🖼️🔍

---

## ✨ Features

* Scan all **images** in a `.blend` project.
* Detect which images are **missing on disk**.
* Report exactly **where** those images are used (Material, World, Compositor).
* Export the results to a file `missing_image_users.txt` next to your blend.
* Saves time hunting broken textures in complex Blender projects.

---

## ⚙️ Prerequisites

* **Blender 4.5+** (script tested on recent versions).
* Python **built into Blender** (no external dependencies).


---

## 📋 TODO

* [ ] Add auto-relink option (search for missing textures in project folders).
* [ ] Add support for **UDIM tile sets**.
* [ ] CLI mode for batch scanning multiple `.blend` files.

---

## 🚀 Usage

1. Open your project in **Blender**.
2. Go to **Scripting → Text Editor**.
3. Load the script `audit_missing_images.py`.
4. Press **Run Script**.
5. Check the generated `missing_image_users.txt` in the same folder as your `.blend`.

Example output:

```
[MISSING] BackRoomsWallpaper.png -> 
  - MATERIAL: Mur jaune.001  | node: Image Texture
```

---

## 💻 Installation

Clone the repository or copy the script directly, then in Blender:

* `Scripting → Open` → select `audit_missing_images.py`.

---

## 📜 License

This project is released under the **MIT License**.
You are free to use, modify, and distribute with attribution.
