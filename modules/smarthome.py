def control(cmd):
    if "light" in cmd:
        return "Smart light toggled"
    if "fan" in cmd:
        return "Smart fan toggled"
    return "Device not recognized"