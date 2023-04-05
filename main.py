from SearchRoom import RoomCatalog

room = RoomCatalog()
name,description = room.user_select("Suites")
name, description, size, bed_type, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights = room.select_room("Oriental 2-Bedroom Suite")
print(f"{name}\n{description}\n{size}\n{bed_type}\n{toilet_type}\n{complimentary}\n{speaker}\n{bathrobes}\n{details}\n{highlights}")