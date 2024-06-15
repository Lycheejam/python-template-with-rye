# Python template with rye

ryeで管理するPythonプロジェクトテンプレートです。  
「Use this repository」から使用します。

```sh
python-template-with-rye (main)$ rye --version
rye 0.34.0
commit: 0.34.0 (d31340178 2024-05-20)
platform: linux (x86_64)
self-python: cpython@3.12.3
symlink support: true
uv enabled: true
python-template-with-rye (main)$ rye sync
Reusing already existing virtualenv
Generating production lockfile: /home/xxx/work/python-template-with-rye/requirements.lock
Generating dev lockfile: /home/xxx/work/python-template-with-rye/requirements-dev.lock
Installing dependencies
Audited 19 packages in 1ms
Done!
```

## TODO

* DependabotがRyeに対応してないのでパッケージの自動アップデートが組めてない。

