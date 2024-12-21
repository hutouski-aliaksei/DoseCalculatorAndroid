[app]

# title of your application
title = dosecalculator

# project directory. the general assumption is that project_dir is the parent directory
# of input_file
project_dir = /home/user/DoseCalculatorModern

# source file path
input_file = /home/user/DoseCalculatorModern/main.py

# directory where exec is stored
exec_directory = .

# path to .pyproject project file
project_file = DoseCalculator.pyproject

# application icon
icon = /home/user/ve/venv/lib/python3.11/site-packages/PySide6/scripts/deploy_lib/pyside_icon.jpg

[python]

# python path
python_path = /home/user/ve/venv/bin/python3.11

# python packages to install
packages = Nuitka==2.4.8

# buildozer = for deploying Android application
android_packages = buildozer==1.5.0,cython==0.29.33

[qt]

# comma separated path to qml files required
# normally all the qml files required by the project are added automatically
qml_files = main.qml,der.qml,coefficients.qml,dynamic.qml

# excluded qml plugin binaries
excluded_qml_plugins = QtQuick3D,QtSensors,QtTest,QtWebEngine

# qt modules used. comma separated
modules = Gui,Qml,Core,QuickControls2,Quick,OpenGL,Network

# qt plugins used by the application
plugins = 

[android]

# path to pyside wheel
wheel_pyside = /home/user/whl/PySide6-6.8.0a1-6.8.1-cp311-cp311-android_aarch64.whl

# path to shiboken wheel
wheel_shiboken = /home/user/whl/shiboken6-6.8.0a1-6.8.1-cp311-cp311-android_aarch64.whl

# plugins to be copied to libs folder of the packaged application. comma separated
plugins = platforms_qtforandroid

[nuitka]

# usage description for permissions requested by the app as found in the info.plist file
# of the app bundle
# eg = extra_args = --show-modules --follow-stdlib
macos.permissions = 

# mode of using nuitka. accepts standalone or onefile. default is onefile.
mode = onefile

# (str) specify any extra nuitka arguments
extra_args = --quiet --noinclude-qt-translations

[buildozer]

# build mode
# possible options = [release, debug]
# release creates an aab, while debug creates an apk
mode = debug

# contrains path to pyside6 and shiboken6 recipe dir
recipe_dir = /home/user/DoseCalculatorModern/deployment/recipes

# path to extra qt android jars to be loaded by the application
jars_dir = /home/user/DoseCalculatorModern/deployment/jar/PySide6/jar

# if empty uses default ndk path downloaded by buildozer
ndk_path = /home/user/.pyside6_android_deploy/android-ndk/android-ndk-r26b

# if empty uses default sdk path downloaded by buildozer
sdk_path = /home/user/.pyside6_android_deploy/android-sdk

# other libraries to be loaded. comma separated.
# loaded at app startup
local_libs = plugins_platforms_qtforandroid

# architecture of deployed platform
# possible values = ["aarch64", "armv7a", "i686", "x86_64"]
arch = aarch64

