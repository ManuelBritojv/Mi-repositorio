from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
cubo = Entity(model='cube', collider='box')
cubo.color=color.random_color()
cubo = Entity(position=Vec3(1,1,1))

player = FirstPersonController()
app.run()