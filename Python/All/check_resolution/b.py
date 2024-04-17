import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
Width = user32.GetSystemMetrics(0)
Height = user32.GetSystemMetrics(1)

print(Width, Height)