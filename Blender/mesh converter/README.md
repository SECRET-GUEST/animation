BLENDER 3.4 | Python 10.8
```
███╗   ███╗███████╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗     ██╗   ██╗██████╗ 
████╗ ████║██╔════╝██╔════╝██║  ██║██║████╗  ██║██╔════╝     ██║   ██║██╔══██╗
██╔████╔██║█████╗  ███████╗███████║██║██╔██╗ ██║██║  ███╗    ██║   ██║██████╔╝
██║╚██╔╝██║██╔══╝  ╚════██║██╔══██║██║██║╚██╗██║██║   ██║    ██║   ██║██╔═══╝ 
██║ ╚═╝ ██║███████╗███████║██║  ██║██║██║ ╚████║╚██████╔╝    ╚██████╔╝██║     
╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝ ╚═╝                                                                                                                                                                        
```
![1](https://user-images.githubusercontent.com/92639080/228399775-3ae3894b-3112-40a1-8a6b-45f8660d1557.gif)


# Description 

This Blender Python script automatically converts Curve, Metaball, Surface, and Text objects in the scene to Mesh objects. 
This conversion can be helpful when preparing objects for rigging, as Blender's armature modifier and weight painting tools work best with Mesh objects.

To use the script, simply copy and paste it into Blender's Text Editor, and click "Run Script" or press Alt + P. The script will iterate through all objects in the scene, and if an object is of type Curve, Metaball, Surface, or Text, it will be converted to a Mesh object. After the conversion, you can proceed to link the objects to an armature using your preferred method.
