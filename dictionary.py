student = {"name": "Abhishek", "age": 18, "course": "FYBSc"}
print("Original Dictionary:", student)
print("Name:", student["name"])
student["age"] = 19
student["city"] = "Pune"
print("After Update:", student)
student.pop("course")
print("After Removing course:", student)
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Is 'name' present?", "name" in student)
print("Length:", len(student))

git reset --hard HEAD~1
git push origin main --force