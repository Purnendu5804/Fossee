bl_info = {
    "name": "FOSSEE Task 2: Complete Suite",
    "author": "Purnendu Tiwari",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Task 2",
    "description": "Distributes, Deletes, and Merges cubes",
    "category": "Object",
}

import bpy
import math


class Task2Properties(bpy.types.PropertyGroup):
    num_cubes: bpy.props.IntProperty(
        name="Number of Cubes",
        description="Enter a natural number < 20",
        default=1,
        min=1,
        soft_max=20
    )



class MESH_OT_distribute_cubes(bpy.types.Operator):
    """Distribute N cubes in a grid"""
    bl_idname = "mesh.distribute_cubes"
    bl_label = "Distribute Cubes"
    
    def execute(self, context):
        scene = context.scene
        N = scene.task2_props.num_cubes
        
        if N > 20:
            self.report({'ERROR'}, "Number out of range (>20)")
            return {'CANCELLED'}
        
        # Create/Get Collection
        col_name = "Task2_Cubes"
        if col_name not in bpy.data.collections:
            collection = bpy.data.collections.new(col_name)
            context.scene.collection.children.link(collection)
        else:
            collection = bpy.data.collections[col_name]
        
        
        cols = math.ceil(math.sqrt(N))
        
       
        for i in range(N):
            x = (i % cols) * 1.0 
            y = (i // cols) * 1.0
            
            bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, 0))
            
            obj = context.active_object

            for old_col in obj.users_collection:
                old_col.objects.unlink(obj)
            collection.objects.link(obj)
            
        self.report({'INFO'}, f"Distributed {N} cubes.")
        return {'FINISHED'}

class MESH_OT_delete_cubes(bpy.types.Operator):
    """Delete selected cubes"""
    bl_idname = "mesh.delete_cubes"
    bl_label = "Delete Selected"
    
    def execute(self, context):
        # Delete only selected objects
        bpy.ops.object.delete()
        self.report({'INFO'}, "Deleted selected objects.")
        return {'FINISHED'}

class MESH_OT_merge_cubes(bpy.types.Operator):
    """Merge selected cubes and remove internal faces"""
    bl_idname = "mesh.merge_cubes"
    bl_label = "Compose Mesh"
    
    def execute(self, context):
        selected = context.selected_objects
        if len(selected) < 2:
            self.report({'WARNING'}, "Select at least 2 objects to merge")
            return {'CANCELLED'}
            

        bpy.ops.object.join()
        

        bpy.ops.object.mode_set(mode='EDIT')
        

        bpy.ops.mesh.select_all(action='SELECT')
        
        # 4. Merge vertices (Remove Doubles)

        bpy.ops.mesh.remove_doubles(threshold=0.001)
        
        # 5. Remove Internal Faces (The "Common Face" requirement)
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_interior_faces()
        bpy.ops.mesh.delete(type='FACE')
        

        bpy.ops.object.mode_set(mode='OBJECT')
        
        self.report({'INFO'}, "Merged cubes and removed internal faces.")
        return {'FINISHED'}

# UI
class VIEW3D_PT_task2_panel(bpy.types.Panel):
    bl_label = "Task 2 Controls"
    bl_idname = "VIEW3D_PT_task2_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Task 2'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        props = scene.task2_props

        layout.prop(props, "num_cubes")
        layout.separator()
        

        layout.operator("mesh.distribute_cubes")
        

        layout.operator("mesh.delete_cubes")
        
        layout.separator()
        layout.label(text="Feature Set 2:")
        

        layout.operator("mesh.merge_cubes")


classes = [
    Task2Properties, 
    MESH_OT_distribute_cubes, 
    MESH_OT_delete_cubes,
    MESH_OT_merge_cubes,
    VIEW3D_PT_task2_panel
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.task2_props = bpy.props.PointerProperty(type=Task2Properties)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.task2_props

if __name__ == "__main__":
    register()