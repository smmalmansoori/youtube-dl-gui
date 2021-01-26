# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['youtube_dl_gui/__main__.py'],
             binaries=[],
             datas=[
                 ('youtube_dl_gui/data', 'data')
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Youtube-DLG',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Youtube-DLG')
app = BUNDLE(coll,
             name='Youtube-DLG.app',
             icon='youtube_dl_gui/data/pixmaps/youtube-dl-gui.icns',
             bundle_identifier=None,
             info_plist={
                'NSPrincipalClass': 'NSApplication',
                'NSAppleScriptEnabled': False,
             },
            )
