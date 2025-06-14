import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure
fig, ax = plt.subplots(figsize=(14, 10))

# Helper function to add a room
def add_room(x, y, width, height, label, color="lightgray"):
    rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor="black", facecolor=color)
    ax.add_patch(rect)
    ax.text(x + width / 2, y + height / 2, label, ha="center", va="center", fontsize=8, wrap=True)

# Define rooms with coordinates and sizes (simple proportional layout)
rooms = [
    # Arena
    (20, 20, 30, 30, "Main Arena", "lightcoral"),
    
    # Fighter Facilities
    (2, 50, 10, 10, "Tier 3 Locker Room\n(Gauntlet Survivors)", "lightblue"),
    (2, 38, 10, 10, "Tier 2 Locker Room\n(Sponsored Fighters)", "lightblue"),
    (2, 26, 10, 10, "Tier 1 Locker Room\n(Proven Fighters)", "lightblue"),
    (2, 14, 10, 10, "Training Room", "wheat"),
    (2, 2, 10, 10, "Rec Room", "wheat"),

    # Central connecting corridor
    (12, 2, 4, 58, "Corridor", "white"),

    # Staff/Admin Wing
    (35, 55, 8, 6, "Grudmore's Office", "thistle"),
    (27, 55, 8, 6, "Elara's Office", "plum"),
    (19, 55, 8, 6, "Champions Locker", "lightsteelblue"),

    # Extra rooms
    (35, 45, 8, 6, "Admin Records", "honeydew"),
    (27, 45, 8, 6, "Security Office", "lightgray"),
    (19, 45, 8, 6, "Medical Bay", "mistyrose"),

    # Staff-only section
    (42, 2, 12, 12, "Maintenance Access", "khaki"),
    (42, 16, 12, 14, "Staff Quarters\n(Former Vault)", "burlywood")
]

# Add rooms to the map
for room in rooms:
    add_room(*room)

# Configure plot
ax.set_xlim(0, 60)
ax.set_ylim(0, 65)
ax.set_aspect('equal')
ax.axis('off')
plt.title("Apexum Ground Floor Layout (Simplified Map)", fontsize=14)
plt.show()
