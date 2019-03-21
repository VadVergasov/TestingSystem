# -*- mode: python -*-

from kivy.deps import sdl2, glew

a = Analysis(['main.py'],
            pathex=[''],
            binaries=None,
            datas=[('locale', 'locale'),
            ('data', 'data')],
            hiddenimports=["unicodedata", "idna"],
            hookspath=None,
            runtime_hooks=None,
            excludes=None,
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=None)
pyz = PYZ(a.pure, a.zipped_data,
            cipher=None)
exe = EXE(pyz,
        a.scripts,
        exclude_binaries=True,
        name='MakeTest',
        debug=False,
        strip=False,
        upx=True,
        console=False)
coll = COLLECT(exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
        strip=False,
        upx=True,
        name='MakeTest')
