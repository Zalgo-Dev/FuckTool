pyinstaller --onefile `
  --name FuckTool `
  --version-file version_file.txt `
  --icon=resources\fucktool.ico `
  --hidden-import=prompt_toolkit `
  --hidden-import=getpass `
  --hidden-import=platform `
  --hidden-import=json `
  --hidden-import=requests `
  --hidden-import=dns `
  --hidden-import=dns.resolver `
  --hidden-import=bs4 `
  --hidden-import=toml `
  --add-data "resources\hgsdk;resources\hgsdk" `
  --add-data "bungee;bungee" `
  --add-data "commands;commands" `
  --add-data "core;core" `
  --add-data "FakeProxy;FakeProxy" `
  --add-data "config.py;." `
  main.py