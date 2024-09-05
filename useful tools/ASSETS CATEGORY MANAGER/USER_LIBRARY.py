import bpy
import uuid
from pathlib import Path

categories = {
    "GEOMETRY NODES": {
        "Overlays/Grid": [],
        "Overlays/Axes": [],
        "Overlays/Annotations": [],

        "Surface/Subdivision": [],
        "Surface/Displacement": [],
        "Surface/Noise": [],

        "Deformation/Bend": [],
        "Deformation/Twist": [],
        "Deformation/Lattice": [],

        "Attributes/Attribute Transfer": [],
        "Attributes/Attribute Mix": [],
        "Attributes/Attribute Sample": [],

        "Instances/Instance on Points": [],
        "Instances/Instance on Faces": [],
        "Instances/Instance Scale": [],

        "Proximity/Geometry Proximity": [],
        "Proximity/Object Proximity": [],
        "Proximity/Surface Proximity": [],

        "Utilities/Modifiers": [],
        "Utilities/Operations": [],
        "Utilities/Transform": []
    },

    "MATERIALS": {
        "Metals": [],
        "Plastics": [],
        "Woods": [],
        "Fabrics": [],
        "Liquids": []
    },

    "TEXTURES": {
        "Diffuse": [],
        "Normal Maps": [],
        "Displacement": [],
        "Specular": []
    },

    "MODELS": {


        "Characters/Humans/Male": [],
        "Characters/Humans/Female": [],
        "Characters/Humans/Low poly": [],

        "Characters/Monsters/Soulslike": [],
        "Characters/Monsters/Backrooms": [],
        "Characters/Monsters/Yokais": [],
        "Characters/Monsters/Entities": [],
        "Characters/Monsters/Ghosts": [],

        "Characters/Animals/Farm": [],
        "Characters/Animals/Zoo": [],
        "Characters/Animals/Pets": [],
        "Characters/Animals/Birds": [],
        "Characters/Animals/Reptiles": [],
        "Characters/Animals/Fish": [],
        "Characters/Animals/Marine Mammals": [],
        "Characters/Animals/Insects": [],
        "Characters/Animals/Wildlife": [],
        "Characters/Animals/Extinct": [],
        "Characters/Animals/Mythical Creatures": [],
        "Characters/Animals/Fantasy": [],

        "Characters/Clothes/Suits/Armor/Female Top": [],
        "Characters/Clothes/Suits/Armor/Female Bottom": [],
        "Characters/Clothes/Suits/Armor/Female Sides": [],
        "Characters/Clothes/Suits/Armor/Female Helmet": [],
        "Characters/Clothes/Suits/Armor/Female Gloves": [],

        "Characters/Clothes/Suits/Armor/Male Top": [],
        "Characters/Clothes/Suits/Armor/Male Bottom": [],
        "Characters/Clothes/Suits/Armor/Male Sides": [],
        "Characters/Clothes/Suits/Armor/Male Helmet": [],
        "Characters/Clothes/Suits/Armor/Male Gloves": [],

        "Characters/Clothes/Suits/Costumes/Halloween": [],
        "Characters/Clothes/Suits/Costumes/Cosplay": [],
        "Characters/Clothes/Suits/Costumes/Fantasy": [],
        "Characters/Clothes/Suits/Costumes/Historical": [],
        "Characters/Clothes/Suits/Costumes/Sci-Fi": [],

        "Characters/Clothes/Suits/Swimwear/Bikinis": [],
        "Characters/Clothes/Suits/Swimwear/Swim Shorts": [],
        "Characters/Clothes/Suits/Swimwear/One-Piece": [],
        "Characters/Clothes/Suits/Swimwear/Swim Trunks": [],
        "Characters/Clothes/Suits/Swimwear/Rash Guards": [],

        "Characters/Clothes/Suits/Sportswear/Gym Wear": [],
        "Characters/Clothes/Suits/Sportswear/Running Wear": [],
        "Characters/Clothes/Suits/Sportswear/Yoga Wear": [],
        "Characters/Clothes/Suits/Sportswear/Swimwear": [],
        "Characters/Clothes/Suits/Sportswear/Team Sports": [],

        "Characters/Clothes/Suits/Uniforms/School": [],
        "Characters/Clothes/Suits/Uniforms/Military": [],
        "Characters/Clothes/Suits/Uniforms/Work": [],
        "Characters/Clothes/Suits/Uniforms/Medical": [],
        "Characters/Clothes/Suits/Uniforms/Service": [],

        "Characters/Clothes/Suits/Fantasy Wear/Elven": [],
        "Characters/Clothes/Suits/Fantasy Wear/Warrior": [],
        "Characters/Clothes/Suits/Fantasy Wear/Mage": [],
        "Characters/Clothes/Suits/Fantasy Wear/Rogue": [],
        "Characters/Clothes/Suits/Fantasy Wear/Steampunk": [],
        "Characters/Clothes/Suits/Fantasy Wear/Mecha": [],


        "Characters/Clothes/Tops/T-Shirts": [],
        "Characters/Clothes/Tops/Shirts": [],
        "Characters/Clothes/Tops/Blouses": [],
        "Characters/Clothes/Tops/Sweaters": [],
        "Characters/Clothes/Tops/Jackets": [],

        "Characters/Clothes/Bottoms/Pants": [],
        "Characters/Clothes/Bottoms/Shorts": [],
        "Characters/Clothes/Bottoms/Skirts": [],
        "Characters/Clothes/Bottoms/Jeans": [],
        "Characters/Clothes/Bottoms/Leggings": [],

        "Characters/Clothes/Footwear/Shoes": [],
        "Characters/Clothes/Footwear/Boots": [],
        "Characters/Clothes/Footwear/Sneakers": [],
        "Characters/Clothes/Footwear/Sandals": [],
        "Characters/Clothes/Footwear/Heels": [],

        "Characters/Clothes/Headwear/Hats": [],
        "Characters/Clothes/Headwear/Caps": [],
        "Characters/Clothes/Headwear/Helmets": [],
        "Characters/Clothes/Headwear/Scarves": [],
        "Characters/Clothes/Headwear/Bandanas": [],

        "Characters/Clothes/Accessories/Bags": [],
        "Characters/Clothes/Accessories/Belts": [],
        "Characters/Clothes/Accessories/Gloves": [],

        "Characters/Clothes/Accessories/Jewelry/Necklaces": [],
        "Characters/Clothes/Accessories/Jewelry/Earrings": [],
        "Characters/Clothes/Accessories/Jewelry/Rings": [],
        "Characters/Clothes/Accessories/Jewelry/Bracelets": [],
        "Characters/Clothes/Accessories/Jewelry/Watches": [],

        "Characters/Clothes/Underwear/Bras": [],
        "Characters/Clothes/Underwear/Panties": [],
        "Characters/Clothes/Underwear/Boxers": [],
        "Characters/Clothes/Underwear/Briefs": [],
        "Characters/Clothes/Underwear/Lingerie": [],


        "Furnitures/Chairs/Dining Chairs": [],
        "Furnitures/Chairs/Office Chairs": [],
        "Furnitures/Chairs/Armchairs": [],
        "Furnitures/Chairs/Stools": [],
        "Furnitures/Chairs/Recliners": [],
        "Furnitures/Chairs/Rocking Chairs": [],

        "Furnitures/Tables/Dining Tables": [],
        "Furnitures/Tables/Coffee Tables": [],
        "Furnitures/Tables/Desks": [],
        "Furnitures/Tables/Side Tables": [],
        "Furnitures/Tables/Consoles": [],
        "Furnitures/Tables/Outdoor Tables": [],

        "Furnitures/Beds/Single Beds": [],
        "Furnitures/Beds/Double Beds": [],
        "Furnitures/Beds/Queen Beds": [],
        "Furnitures/Beds/King Beds": [],
        "Furnitures/Beds/Bunk Beds": [],
        "Furnitures/Beds/Sofa Beds": [],

        "Furnitures/Cabinets/Wardrobes": [],
        "Furnitures/Cabinets/Dressers": [],
        "Furnitures/Cabinets/Nightstands": [],
        "Furnitures/Cabinets/Bookshelves": [],
        "Furnitures/Cabinets/Display Cabinets": [],
        "Furnitures/Cabinets/Pantry Cabinets": [],

        "Furnitures/Sofas/Sectional Sofas": [],
        "Furnitures/Sofas/Loveseats": [],
        "Furnitures/Sofas/Sleeper Sofas": [],
        "Furnitures/Sofas/Reclining Sofas": [],
        "Furnitures/Sofas/Futons": [],

        "Furnitures/Storage/Shelves": [],
        "Furnitures/Storage/Chest of Drawers": [],
        "Furnitures/Storage/Storage Bins": [],
        "Furnitures/Storage/Storage Ottomans": [],
        "Furnitures/Storage/Toy Boxes": [],

        "Furnitures/Outdoor/Chairs": [],
        "Furnitures/Outdoor/Tables": [],
        "Furnitures/Outdoor/Sofas": [],
        "Furnitures/Outdoor/Benches": [],
        "Furnitures/Outdoor/Patio Sets": [],

        "Furnitures/Office/Desks": [],
        "Furnitures/Office/Chairs": [],
        "Furnitures/Office/File Cabinets": [],
        "Furnitures/Office/Conference Tables": [],
        "Furnitures/Office/Cubicles": [],

        "Furnitures/Kids/Beds": [],
        "Furnitures/Kids/Chairs": [],
        "Furnitures/Kids/Tables": [],
        "Furnitures/Kids/Storage": [],
        "Furnitures/Kids/Desks": [],

        "Furnitures/Kitchen/Islands": [],
        "Furnitures/Kitchen/Cabinets": [],
        "Furnitures/Kitchen/Pantries": [],
        "Furnitures/Kitchen/Breakfast Nooks": [],

        "Furnitures/Restaurant/Dining Tables": [],
        "Furnitures/Restaurant/Dining Chairs": [],
        "Furnitures/Restaurant/Booths": [],
        "Furnitures/Restaurant/Serving Trolleys": [],
        "Furnitures/Restaurant/Menu Stands": [],
        "Furnitures/Restaurant/Host/Hostess Stands": [],
        "Furnitures/Restaurant/Decorative Elements": [],

        "Furnitures/Restaurant/Bar/Bar Counters": [],
        "Furnitures/Restaurant/Bar/Bar Stools": [],
        "Furnitures/Restaurant/Bar/High Tables": [],
        "Furnitures/Restaurant/Bar/Bottle Racks": [],
        "Furnitures/Restaurant/Bar/Glasses Storage": [],
        "Furnitures/Restaurant/Bar/Wine Cabinets": [],

        "Furnitures/Rave Party/DJ Booths": [],
        "Furnitures/Rave Party/Speakers": [],
        "Furnitures/Rave Party/Lighting Rigs": [],
        "Furnitures/Rave Party/Dance Floors": [],
        "Furnitures/Rave Party/Lounge Areas": [],
        "Furnitures/Rave Party/Bar Counters": [],
        "Furnitures/Rave Party/Crowd Control Barriers": [],
        "Furnitures/Rave Party/Smoke Machines": [],
        "Furnitures/Rave Party/Outdoor Tents": [],
        "Furnitures/Rave Party/Chill-out Areas": [],
        "Furnitures/Rave Party/Portable Toilets": [],

        "Furnitures/City Objects/Benches": [],
        "Furnitures/City Objects/Street Lights": [],
        "Furnitures/City Objects/Trash Bins": [],
        "Furnitures/City Objects/Fountains": [],
        "Furnitures/City Objects/Public Toilets": [],

        "Furnitures/Construction/Barriers": [],
        "Furnitures/Construction/Cones": [],
        "Furnitures/Construction/Scaffolding": [],
        "Furnitures/Construction/Cranes": [],
        "Furnitures/Construction/Portable Toilets": [],

        "Furnitures/Professional Equipment/Firefighting Equipment": [],
        "Furnitures/Professional Equipment/Police Equipment": [],
        "Furnitures/Professional Equipment/Medical Equipment": [],
        "Furnitures/Professional Equipment/Traffic Cones": [],
        "Furnitures/Professional Equipment/Barricade Tape": [],


        "World/Planets": [],
        "World/Universe": [],
        "World/Galaxy": [],


        "Vehicles/Cars/SUV": [],
        "Vehicles/Cars/Truck": [],
        "Vehicles/Cars/Sports Car": [],
        "Vehicles/Cars/Classic Car": [],
        "Vehicles/Cars/Low poly": [],

        "Vehicles/Planes/Private Jet": [],
        "Vehicles/Planes/Fighter Jet": [],
        "Vehicles/Planes/Helicopter": [],
        "Vehicles/Planes/Glider": [],
        "Vehicles/Planes/Cargo Plane": [],

        "Vehicles/Boats/Yacht": [],
        "Vehicles/Boats/Fishing Boat": [],
        "Vehicles/Boats/Commercial": [],
        "Vehicles/Boats/Submarine": [],
        "Vehicles/Boats/Cargo Ship": [],

        "Vehicles/Motorcycles/Cruiser": [],
        "Vehicles/Motorcycles/Sportbike": [],
        "Vehicles/Motorcycles/Touring": [],
        "Vehicles/Motorcycles/Dirt Bike": [],
        "Vehicles/Motorcycles/Scooter": [],

        "Vehicles/Bicycles": [],

        "Vehicles/Trains/Train": [],
        "Vehicles/Trains/Metro": [],
        "Vehicles/Trains/Tram": [],

        "Vehicles/Spacecraft/Space Shuttle": [],
        "Vehicles/Spacecraft/Rocket": [],
        "Vehicles/Spacecraft/Satellite": [],
        "Vehicles/Spacecraft/Space Probe": [],

        "Vehicles/Heavy Machinery/Bulldozer": [],
        "Vehicles/Heavy Machinery/Crane": [],
        "Vehicles/Heavy Machinery/Excavator": [],
        "Vehicles/Heavy Machinery/Forklift": [],
        "Vehicles/Heavy Machinery/Dump Truck": [],

        "Vehicles/Emergency Vehicles/Ambulance": [],
        "Vehicles/Emergency Vehicles/Fire Truck": [],
        "Vehicles/Emergency Vehicles/Police Car": [],
        "Vehicles/Emergency Vehicles/Rescue Helicopter": [],


        "Cities/Buildings": [],
        "Cities/Streets": [],
        "Cities/Parks": [],
        "Cities/House": [],
        "Cities/Low poly": []
    },


    "Lights": {
        "Types/Point Lights": [],
        "Types/Spot Lights": [],
        "Types/Area Lights": [],
        "Types/Sun Lights": [],
        "Animations/Flicker": [],
        "Animations/Pulse": [],
        "Animations/Fade In/Out": []
    },
    "Cameras": {
        "Static Cameras": [],
        "Moving Cameras": [],
        "360 Cameras": [],
        "Depth of Field": [],
        "Camera Rigs": [],
        "Tracking": [],
        "Lenses/Wide Angle": [],
        "Lenses/Telephoto": [],
        "Lenses/Macro": [],
        "Lenses/Standard": [],
        "Camera Effects/Blur": [],
        "Camera Effects/Bokeh": [],
        "Camera Effects/Vignette": []
    },
    "Animations": {
        "Character Animations": [],
        "Object Animations": [],
        "Environment Animations": []
    }
}


# Define the catalog file location
asset_library_path = bpy.context.preferences.filepaths.asset_libraries[0].path
catalog_file_path = Path(asset_library_path) / "blender_assets.cats.txt"

# Load existing catalogs or create a new list if empty
if catalog_file_path.exists() and catalog_file_path.stat().st_size > 0:
    with open(catalog_file_path, 'r') as file:
        lines = file.readlines()
else:
    lines = ["VERSION 1\n"]

# Function to add catalogs and subcatalogs
def add_catalog(catalogs, parent_uuid, parent_path, subcategories):
    for subcategory in subcategories:
        if isinstance(subcategory, dict):
            for sub, subsubcategories in subcategory.items():
                sub_path = f"{parent_path}/{sub}"
                if not any(sub_path in line for line in catalogs):
                    sub_uuid = uuid.uuid4()
                    catalogs.append(f"{sub_uuid}:{sub_path}:{sub}\n")
                catalogs = add_catalog(catalogs, sub_uuid, sub_path, subsubcategories)
        else:
            sub_path = f"{parent_path}/{subcategory}"
            if not any(sub_path in line for line in catalogs):
                sub_uuid = uuid.uuid4()
                catalogs.append(f"{sub_uuid}:{sub_path}:{subcategory}\n")
    return catalogs

# Add categories and subcategories
for category, subcategories in categories.items():
    cat_path = category
    if not any(cat_path in line for line in lines):
        cat_uuid = uuid.uuid4()
        lines.append(f"{cat_uuid}:{cat_path}:{category}\n")
    else:
        for line in lines:
            if cat_path in line:
                cat_uuid = line.split(":")[0]
                break
    lines = add_catalog(lines, cat_uuid, cat_path, subcategories)

# Save the updated catalogs
with open(catalog_file_path, 'w') as file:
    file.writelines(lines)

