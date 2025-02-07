#      |               |                                 |
                
#                  |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#           |                                  |                                     |
                
#                  |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#   |                          |                       |                    |
#           |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                                                        |
#      |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                       |                    |
                
#                      |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#           |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                |                                        |
                
#                  |                     |
#   |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |     |                                |                       |                              |                                |
#           |                               |                                         |                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#   |         |                                   PRESENTATION                                                |                                |                    |   |                                |                    |   |                                |                    |        |                                |                    |
#                                                                                                                               |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#                |                             /                 \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#        |                               This script allows Blender to  
                
#                                 wash your project from all unused things in          |                                           |               |                                           |               |                                           |                    |                                           |
                
#                           /                      |    v    |                    \
#               You can set whatever you want to remove  in settings but proceed with caution  !
#                                   |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |
#                                                                                                    |                                                                 |                      |                     |                       |                      |                     |                       |                      |                     |                            |
#           
#      |                  !      |                                   |     |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
#                                |                                   |     |                  
#                   |            |                   Anyway          !                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |
                
#              |                      |                 have                                                 |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                                           |
                

#                 |                                  FUN         |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                                                      |
                
#                                                         =)
                
#
#                                |                      or                                       |                                                            |                    |                |                       |                    |                |                       |                    |                    |                                           |
                

#              |                              |       DIE ! ! !        |                       |                            |                |                       |                    |                |                       |                    |                    |                                           |#      |                        |                                         |                                |
                
#
#                                                     !                                       |                                |                    |  |                                |                    |  |                                |                    |       |                                |                    |
                
#      |               |                                 !
                
#                  |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#           |                                  !                                     |
                
#                  |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#   |                          |                       |                    !
#           |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                    |                                    |
              
#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|
import bpy

#____ ____ ___ ___ _ _  _ ____ ____ 
#[__  |___  |   |  | |\ | | __ [__  
#___] |___  |   |  | | \| |__] ___] 
                                   
#OPENING | https://www.youtube.com/watch?v=qmk3Rri0jsQ&ab_channel=SECRETGUEST

# Set these variables to 'y' for yes or whatever else for no to choose what to clear
clear_caches = 'y'  
clear_keyframes = 'y' 
clear_unused_materials = 'y'  
clear_unused_textures = 'y'  
clear_unused_meshes = 'y'  
clear_unused_images = 'y'  
clear_unused_collections = 'y'  
clear_orphan_data = 'y'
clear_unused_uv_maps = 'y'
clear_unused_node_groups = 'y'


#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                

def clear_simulation_caches():
    """Efface les caches des simulations (fluides, particules, rigid body, etc.)."""
    for obj in bpy.data.objects:
        for modifier in obj.modifiers:
            if modifier.type in {'PARTICLE_SYSTEM', 'CLOTH', 'SOFT_BODY'}:
                modifier.point_cache.frame_start = bpy.context.scene.frame_start

            if modifier.type == 'FLUID' and modifier.fluid_type == 'DOMAIN':
                modifier.domain_settings.cache_frame_start = bpy.context.scene.frame_start

    # Effacer le cache de la simulation de rigidité
    if bpy.context.scene.rigidbody_world:
        bpy.ops.ptcache.free_bake_all()


def clear_all_keyframes():
    """Supprime toutes les keyframes des objets, matériaux, courbes, caméras et lumières."""
    for data_block in [bpy.data.objects, bpy.data.materials, bpy.data.curves, bpy.data.cameras, bpy.data.lights]:
        for item in data_block:
            if item.animation_data:
                item.animation_data_clear()


def clear_unused_data_block(data_block):
    """Supprime les blocs de données inutilisés."""
    for item in list(data_block):  # Utilisation de `list()` pour éviter des erreurs de suppression
        if item.users == 0:
            data_block.remove(item)


def clear_orphaned_data():
    """Supprime les éléments orphelins sans utilisateurs."""
    orphan_blocks = [bpy.data.meshes, bpy.data.materials, bpy.data.textures, bpy.data.images, bpy.data.node_groups]
    for block_type in orphan_blocks:
        clear_unused_data_block(block_type)


def clear_uv_maps():
    """Supprime les UV maps inutilisées dans tous les objets MESH."""
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.uv_layers:
            used_uv_maps = set()

            # Récupérer les noms d'UV utilisés dans les matériaux
            for mat_slot in obj.material_slots:
                if mat_slot.material and mat_slot.material.use_nodes:
                    for node in mat_slot.material.node_tree.nodes:
                        if node.type == 'UVMAP' and hasattr(node, "uv_map") and node.uv_map:
                            uv_name = node.uv_map
                            if isinstance(uv_name, bytes):  # Vérifie si c'est en bytes
                                uv_name = uv_name.decode('utf-8')
                            used_uv_maps.add(uv_name)

            # Supprimer les UV non utilisées
            for uv_map in list(obj.data.uv_layers):  # Sécuriser l'itération
                if uv_map.name not in used_uv_maps:
                    if uv_map.name in obj.data.uv_layers:  # Vérifier si elle existe encore
                        obj.data.uv_layers.remove(uv_map)



def clear_unused_nodes():
    """Supprime les groupes de nœuds inutilisés."""
    for group in list(bpy.data.node_groups):  # Sécuriser la suppression
        if group.users == 0:
            bpy.data.node_groups.remove(group)


# Exécuter les fonctions de nettoyage en fonction des paramètres définis
if clear_unused_materials == 'y':
    clear_unused_data_block(bpy.data.materials)
    
if clear_unused_textures == 'y':
    clear_unused_data_block(bpy.data.textures)
    
if clear_unused_meshes == 'y':
    clear_unused_data_block(bpy.data.meshes)
    
if clear_unused_images == 'y':
    clear_unused_data_block(bpy.data.images)
    
if clear_unused_collections == 'y':
    clear_unused_data_block(bpy.data.collections)
    
if clear_orphan_data == 'y':
    clear_orphaned_data()
    
if clear_unused_uv_maps == 'y':
    clear_uv_maps()
    
if clear_unused_node_groups == 'y':
    clear_unused_nodes()

if clear_caches == 'y':
    clear_simulation_caches()

if clear_keyframes == 'y':
    clear_all_keyframes()

