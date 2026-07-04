#define MyAppName "GUI Music Extractor + Ringtone Maker"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "CyberAttackStop"
#define MyAppExeName "GUI Music Extractor.exe"

[Setup]
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=installer
OutputBaseFilename=GUI_Music_Extractor_Setup_v1.0.0
Compression=lzma
SolidCompression=yes
WizardStyle=modern
SetupIconFile=assets\icons\icon_1.ico

[Files]
Source: "dist\GUI Music Extractor.exe"; DestDir: "{app}"; Flags: ignoreversion

Source: "assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs createallsubdirs
Source: "core\*"; DestDir: "{app}\core"; Flags: recursesubdirs createallsubdirs

; OPTIONAL (if you use ffmpeg locally)
Source: "ffmpeg\*"; DestDir: "{app}\ffmpeg"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\GUI Music Extractor"; Filename: "{app}\GUI Music Extractor.exe"
Name: "{commondesktop}\GUI Music Extractor"; Filename: "{app}\GUI Music Extractor.exe"

[Run]
Filename: "{app}\GUI Music Extractor.exe"; Description: "Launch App"; Flags: nowait postinstall skipifsilent