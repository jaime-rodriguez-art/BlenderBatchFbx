import bpy
import os

script_directory = os.path.dirname(bpy.data.filepath)

output_directory = os.path.join(script_directory, "exported_fbxs")

os.makedirs(output_directory, exist_ok=True)

for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        
        output_file = os.path.join(output_directory, obj.name + ".fbx")
        
        bpy.ops.export_scene.fbx(
            filepath=output_file,
            use_selection=True,
            add_leaf_bones=False,  
        )
        
        obj.select_set(False)

print("Exported all objects as .fbx files to", output_directory)
