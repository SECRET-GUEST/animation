
# Asset Catalog Organizer

This script is designed to help Blender users create and organize asset catalogs using text-based Large Language Models (LLMs). It simplifies the creation of nested categories within Blender's asset library, allowing for better organization and management of assets.

## Features

- Automatically create nested categories and subcategories in Blender's asset library.
- Uses a hierarchical structure with slashes ("/") to define subcategories.
- Supports a wide range of asset types including geometry nodes, materials, textures, models, furnitures, world, vehicles, cities, lights, cameras, and animations.
- Easy to customize and extend for different asset organization needs.

## Installation

1. Ensure you have Blender 4.2 or later installed.
2. Download the script and save it to your Blender project directory.
3. Open Blender and load your project.
4. Open the script in Blender's text editor.

## Usage

1. Update the `categories` dictionary in the script to match your desired asset hierarchy.
2. Run the script in Blender's text editor to automatically create the specified categories and subcategories.

## Main Categories and Subcategories

The script includes predefined categories and subcategories for various asset types. Here is a brief overview of what is included:

### Geometry Nodes

- **Overlays**: Grid, Axes, Annotations
- **Surface**: Subdivision, Displacement, Noise
- **Deformation**: Bend, Twist, Lattice
- **Attributes**: Attribute Transfer, Attribute Mix, Attribute Sample
- **Instances**: Instance on Points, Instance on Faces, Instance Scale
- **Proximity**: Geometry Proximity, Object Proximity, Surface Proximity
- **Utilities**: Modifiers, Operations, Transform

### Materials

- **Types**: Metals, Plastics, Woods, Fabrics, Liquids

### Textures

- **Types**: Diffuse, Normal Maps, Displacement, Specular

### Models

- **Characters**:
  - **Humans**: Male, Female, Low poly
  - **Monsters**: Soulslike, Backrooms, Yokais, Entities, Ghosts
  - **Clothes**:
    - **Suits**: Armor (Female Top, Female Bottom, Female Sides, Female Helmet, Female Gloves, Male Top, Male Bottom, Male Sides, Male Helmet, Male Gloves), Costumes (Halloween, Cosplay, Fantasy, Historical, Sci-Fi), Swimwear (Bikinis, Swim Shorts, One-Piece, Swim Trunks, Rash Guards), Sportswear (Gym Wear, Running Wear, Yoga Wear, Swimwear, Team Sports), Uniforms (School, Military, Work, Medical, Service), Fantasy Wear (Elven, Warrior, Mage, Rogue, Steampunk, Mecha)
    - **Tops**: T-Shirts, Shirts, Blouses, Sweaters, Jackets
    - **Bottoms**: Pants, Shorts, Skirts, Jeans, Leggings
    - **Footwear**: Shoes, Boots, Sneakers, Sandals, Heels
    - **Headwear**: Hats, Caps, Helmets, Scarves, Bandanas
    - **Accessories**: Bags, Belts, Gloves, Jewelry (Necklaces, Earrings, Rings, Bracelets, Watches)
    - **Underwear**: Bras, Panties, Boxers, Briefs, Lingerie

### Furnitures

- **Chairs**: Dining Chairs, Office Chairs, Armchairs, Stools, Recliners, Rocking Chairs
- **Tables**: Dining Tables, Coffee Tables, Desks, Side Tables, Consoles, Outdoor Tables
- **Beds**: Single Beds, Double Beds, Queen Beds, King Beds, Bunk Beds, Sofa Beds
- **Cabinets**: Wardrobes, Dressers, Nightstands, Bookshelves, Display Cabinets, Pantry Cabinets
- **Sofas**: Sectional Sofas, Loveseats, Sleeper Sofas, Reclining Sofas, Futons
- **Storage**: Shelves, Chest of Drawers, Storage Bins, Storage Ottomans, Toy Boxes
- **Outdoor**: Chairs, Tables, Sofas, Benches, Patio Sets
- **Office**: Desks, Chairs, File Cabinets, Conference Tables, Cubicles
- **Kids**: Beds, Chairs, Tables, Storage, Desks
- **Kitchen**: Islands, Cabinets, Pantries, Breakfast Nooks
- **Restaurant**: Dining Tables, Dining Chairs, Booths, Bar Counters, Serving Trolleys, Menu Stands, Host/Hostess Stands, Decorative Elements
- **Bar**: Bar Counters, Bar Stools, High Tables, Bottle Racks, Glasses Storage, Wine Cabinets
- **Rave Party**: DJ Booths, Speakers, Lighting Rigs, Dance Floors, Lounge Areas, Bar Counters, Crowd Control Barriers, Smoke Machines, Outdoor Tents, Chill-out Areas, Portable Toilets
- **City Objects**: Benches, Street Lights, Trash Bins, Fountains, Public Toilets
- **Construction**: Barriers, Cones, Scaffolding, Cranes, Portable Toilets
- **Professional Equipment**: Firefighting Equipment, Police Equipment, Medical Equipment, Traffic Cones, Barricade Tape



