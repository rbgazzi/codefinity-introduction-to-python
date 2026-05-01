# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update_tuple = ("tomatoes", "celery", "cilantro")
shelf1_concat = shelf1 + shelf1_update_tuple
celery_count = shelf1_concat.count("celery")
celery_index = shelf1_concat.index("celery")
print(f"Updated Shelf #1: {shelf1_concat}")
print(f"Number of celery: {celery_count}")
print(f"Celery Index: {celery_index}")