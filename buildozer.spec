[app]
title = dosecalculator
package.name = dosecalculator
package.domain = org.dosecalculator
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,qml,js,db
version = 0.25
requirements = python3,shiboken6,PySide6
orientation = portrait,landscape
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false
android.ndk_path = /home/user/.pyside6_android_deploy/android-ndk/android-ndk-r26b
android.sdk_path = /home/user/.pyside6_android_deploy/android-sdk
p4a.bootstrap = qt
p4a.local_recipes = /home/user/DoseCalculatorModern/deployment/recipes
p4a.branch = develop
android.permissions = android.permission.WRITE_EXTERNAL_STORAGE, android.permission.ACCESS_NETWORK_STATE, android.permission.INTERNET
android.add_jars = /home/user/DoseCalculatorModern/deployment/jar/PySide6/jar/Qt6AndroidNetworkInformationBackend.jar,/home/user/DoseCalculatorModern/deployment/jar/PySide6/jar/Qt6AndroidQuick.jar,/home/user/DoseCalculatorModern/deployment/jar/PySide6/jar/Qt6AndroidBindings.jar,/home/user/DoseCalculatorModern/deployment/jar/PySide6/jar/Qt6AndroidNetwork.jar,/home/user/DoseCalculatorModern/deployment/jar/PySide6/jar/Qt6Android.jar
p4a.extra_args = --qt-libs=Gui,Qml,Core,Network,QuickControls2,OpenGL,Quick --load-local-libs=plugins_platforms_qtforandroid --init-classes=
icon.filename = /home/user/Downloads/sign.jpg
presplash.filename = /home/user/Downloads/sign.jpg

[buildozer]
log_level = 2
warn_on_root = 1
bin_dir = /home/user/DoseCalculatorModern

