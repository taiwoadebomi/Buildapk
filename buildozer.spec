[app]

# (str) Title of your application
title = Registration App

# (str) Package name
package.name = registrationapp

# (str) Package domain (use anything like org.test)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,kv,png,jpg

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3==3.7.6,hostpython3==3.7.6,kivy,pillow




osx.python_version = 3.7.6



osx.kivy_version = 1.9.1
# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0


# (str) Icon (optional)
# icon.filename = icon.png


# (list) Permissions (only if needed)
# android.permissions = INTERNET


# (str) Android API to use
android.api = 33

# (str) Minimum API your app supports
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Skip update
android.skip_update = False


# (str) Entry point
entrypoint = main.py


[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

