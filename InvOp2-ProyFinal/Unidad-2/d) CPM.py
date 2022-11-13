from criticalpath import Node
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

r = Node('rutacritica')

tareas = [("A", {"duracion": 3}), 
          ("B", {"duracion": 2}), 
          ("C", {"duracion": 4}), 
          ("D", {"duracion": 3}), 
          ("E", {"duracion": 2}), 
          ("F", {"duracion": 4}), 
          ("G", {"duracion": 2}), 
          ("H", {"duracion": 1}), 
          ("I", {"duracion": 2}), 
          ("J", {"duracion": 4})]

dependencias = [("A", "E"), 
                ("B", "E"), 
                ("E", "F"),
                ("F", "G"), 
                ("G", "I"), 
                ("I", "J"),
                ("C", "J"), 
                ("H", "I"), 
                ("D", "H")]

for i in tareas:
    r.add(Node(i[0], duration=i[1]["duracion"]))

for j in dependencias:
    r.link(j[0],j[1])

r.update_all()
r.get_critical_path()
print(p.duration)