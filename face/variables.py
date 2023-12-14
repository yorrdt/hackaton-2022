import func


admin_path = "db/admin/"
user_path = "db/user/"

detectionEnabled = False
saveFrame = False
compareFrameAndFace = False
countOfAdmins = func.countFiles(admin_path)
countOfUsers = func.countFiles(user_path)