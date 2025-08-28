[app]

# Название приложения
title = Calculator

# Имя пакета (уникальное)
package.name = calculator
package.domain = org.test

# Главный файл
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Версия приложения
version = 0.1

# Требования (kivy + python)
requirements = python3,kivy

# Ориентация экрана
orientation = portrait

# Иконка (можно потом заменить)
#icon.filename = %(source.dir)s/icon.png

# Версия Android API
android.api = 31
android.minapi = 21
android.sdk = 20
android.ndk = 23b
android.ndk_api = 21

# Архитектуры
android.archs = arm64-v8a, armeabi-v7a

# Формат сборки
android.release_artifact = apk
android.debug_artifact = apk


[buildozer]

log_level = 2
warn_on_root = 1
