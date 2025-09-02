
[![STATUS](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()
[![Blender](https://img.shields.io/badge/Blender-4.5-orange.svg)](https://www.blender.org/download/releases/4-5/)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)]()


```
 ██████╗ █████╗ ███╗   ███╗███████╗██████╗  █████╗      ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗ 
██╔════╝██╔══██╗████╗ ████║██╔════╝██╔══██╗██╔══██╗    ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
██║     ███████║██╔████╔██║█████╗  ██████╔╝███████║    ██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝
██║     ██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗██╔══██║    ██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║██║ ╚═╝ ██║███████╗██║  ██║██║  ██║    ╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                                 
```

# Blender Camera Background Cleaner 📷🧹

## ✨ Features

* Remove all **Background Images** (Movie Clips, images) from every camera.
* Clear the **Active Clip** in Scene properties (used by motion tracking).
* Disable **Sequencer** and **Compositing** to avoid unwanted overlays.
* Hide any objects parented to cameras (often movie planes added by *Setup Tracking Scene*).
* Keeps all **animation keyframes** and motion paths intact.


---

## ⚙️ Prerequisites

* **Blender 4.5+**.
* No external Python dependencies required.



---

## 📋 TODO

* [ ] Add option to selectively clean only certain cameras.
* [ ] Add command-line flag for batch cleanup.
* [ ] Auto-detect unused movie planes and delete them permanently.


---

## 🚀 Usage

1. Open your `.blend` in **Blender**.
2. Go to **Scripting → Text Editor**.
3. Load the script `clean_camera_backgrounds.py`.
4. Press **Run Script**.
5. All cameras are now clean:

   * No video/image background.
   * No active tracking clip.
   * No Sequencer/Compositor overlay.
   * Any movie planes parented to cameras are hidden.

Example console output:

```
Camera cleanup complete: backgrounds cleared, active_clip removed, child movie planes hidden.
```

---

## 💻 Installation

Clone the repository or copy the script directly:

```bash
git clone https://github.com/YOUR_USERNAME/blender-camera-background-cleaner.git
```

Then in Blender:

* `Scripting → Open` → select `clean_camera_backgrounds.py`.


---

## 📜 License

Released under the **MIT License**.

