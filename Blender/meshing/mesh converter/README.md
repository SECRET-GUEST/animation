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

This Blender Python script is designed to automatically convert non-Mesh objects, specifically Curve, Metaball, Surface, and Text objects, into Mesh objects in your Blender scene. This conversion is particularly useful when preparing these objects for rigging, skinning, or weight painting, as Blender's armature modifier, automatic weights, and other rigging tools are optimized for Mesh objects.

To utilize the script, copy and paste the provided code into Blender's Text Editor. Once the code is in place, click the "Run Script" button or press Alt + P to execute the script. As the script runs, it will iterate through all objects present in the Blender scene. If an object is identified as a Curve, Metaball, Surface, or Text type, it will be converted to a Mesh object. Following the conversion, you can proceed with linking the new Mesh objects to an armature using your preferred rigging method, such as parent with automatic weights or manual weight painting.
