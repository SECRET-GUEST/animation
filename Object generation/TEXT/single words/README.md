![Blender](https://img.shields.io/badge/Blender-orange)
![Python 3.10.13](https://img.shields.io/badge/Python-3.10.13-blue)
```
██╗    ██╗ ██████╗ ██████╗ ██████╗ ███████╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║ █╗ ██║██║   ██║██████╔╝██║  ██║███████╗    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║███╗██║██║   ██║██╔══██╗██║  ██║╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████║    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
```
# Dynamic Text Generator

This Blender script automates the creation of text objects based on a list of words, allowing for customization of font size and font type. Each generated text object is named after the corresponding word and organized into a collection named "texts".

## Features

- **Automated Text Object Creation**: Generates text objects for each word in a provided list.
- **Custom Font Size**: Allows setting the font size for all text objects.
- **Font Type Customization**: Option to specify a custom font type, with fallback to Blender's default font.
- **Organized Collection**: Places all generated text objects in a collection named "texts".
- **Named Text Objects**: Each text object is named after its corresponding word for easy identification.

## Installation

1. **Blender Setup**:
   Ensure Blender 3.6 is installed on your system.

2. **Script Download**:
   Download the `dynamic_text_generator.py` script from this repository.

## Usage

1. **Open Blender**:
   Start Blender and open a new or existing project.

2. **Run the Script**:
   - Open the Text Editor view in Blender.
   - Load the `dynamic_text_generator.py` script.
   - Press `Run Script` to execute the script.

3. **Customize Parameters**:
   - `words`: A tuple of words to create as text objects (e.g., `("Hello", "World", "Blender")`).
   - `font_size`: The desired size of the text.
   - `font_path`: The path to your custom font file (optional). Leave as `None` for the default font.

##### Note : To use a custom font, provide the path to the font file in `font_path`. For example:

```python
font_path = "/path/to/your/font.ttf"
```

## Example

To create text objects for the words 'Apple', 'Banana', and 'Cherry' with a font size of 1.0 and the default font, set the parameters as follows:

```python
words = ("Apple", "Banana", "Cherry")
font_size = 1.0
font_path = None  # Use default font
```

