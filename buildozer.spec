[app]

# (str) Title of your application
title = PdfSearch

# (str) Package name
package.name = pdfsearch

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (str) The version of your application
version = 1.0

# (list) Application requirements
requirements = kivy,pillow

# (str) Custom source folders for requirements
# Sets custom folder for kivy requirements because the defaults are too big
source.include_exts = py,png,jpg,kv,atlas
source.kivy = kivy

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (list) Services
android.services = 

# (str) Android API to use
android.api = 29

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 1

# (list) List of service to declare
services = 

# (str) The orientation to start with
orientation = portrait

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (list) List of features to declare
android.features = android.hardware.usb.host

# (list) List of Java classes to add to the android project
android.add_jars = 

# (list) List of Java *.jar files to add to the android project (can be absolute or relative to the spec file)
android.add_jars_app = 

# (list) Android AAR archives to add (currently works only with sdl2_gradle)
#android.add_aars = 

# (list) Gradle dependencies to add (currently works only with sdl2_gradle)
#android.gradle_dependencies = 

# (list) application meta-data to set (key=value format)
#android.meta_data = 

# (list) Activity attributes to declare
#android.manifest_additions = 

# (list) xml files to include
#android.add_xml = 

# (list) Java files to add (can be java or a referenced jar files)
#android.add_src = 

# (str) Path to a custom toolchain to be used
#android.toolchain = /opt/android-sdk/

# (str) Path to a custom ndk to be used (if empty, it will be automatically downloaded.)
#android.ndk_path = 

# (bool) Use a black overlay to hide the contents of the screen. This is useful for
# taking screenshots of the application without having to modify any of the UI.
#android.screenshot = False

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
#android.orientation = portrait

# (bool) Indicate whether the application should be resizable (Android only)
#resizable = 0

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (str) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
